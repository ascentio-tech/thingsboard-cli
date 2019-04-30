import json, os
from os import path
import click
from click import command
from thingsboard_cli.version import __version__
import thingsboard_client as tb
import requests

class Repo(object):
    def __init__(self, tb_client):
      self.client = tb_client
pass_repo = click.make_pass_decorator(Repo)


@click.group()
@click.version_option(version=__version__)
@click.option('--username', '-u', required=True)
@click.option('--url', required=True)
@click.password_option(confirmation_prompt=False)
@click.pass_context
def cli(ctx, username, url, password):
  """
  Thinsboard CLI
  """
  def authenticate(url, username, password):
    path = "{}/api/auth/login".format(url)
    response = requests.post(url=path, json={'username':username, 'password':password})
    if response.status_code == requests.codes.ok:
      return True, response.json()['token']
    else:
      return False, ''

  def create_api_client(url, username, password, token):
    configuration = tb.Configuration()
    configuration.username = username
    configuration.password = password
    configuration.host = url
    configuration.verify_ssl = False
    configuration.api_key['X-Authorization'] = token
    configuration.api_key_prefix['X-Authorization'] = 'Bearer'
    return tb.ApiClient(configuration=configuration)

  is_authenticated, token = authenticate(url, username, password)
  if is_authenticated:
    click.echo(click.style("Authenticated!", fg='green'))
    tb_client = create_api_client(url, username, password, token)

  else:
    click.echo(click.style("Could not authenticate with given credentials", fg='red'))
    print(response.json())
    exit(1)

  ctx.obj = Repo(tb_client)


@cli.command()
@pass_repo
def dashboard_list(repo):
  click.echo('- Listing all dashboards')
  def print_dashboards(dashboards):
    [click.echo("{} {}".format(d.id.id, d.name)) for d in dashboards]

  controller = tb.DashboardControllerApi(repo.client)
  dashboards = controller.get_tenant_dashboards_using_get(limit=100).data
  print_dashboards(dashboards)

  def fetch_dashboard_metatada(id):
    # conf = repo.client.configuration
    # auth = conf.auth_settings
    # path = '{}/api/dashboard/{}'.format(conf.host, id)
    # api_key = conf.get_api_key_with_prefix('X-Authorization')
    # response = requests.get(url=path,headers={'X-Authorization': api_key})
    response = controller.get_dashboard_by_id_using_get(id)
    return response


  output = 'dashboards'
  def create_output(output):
    if not path.exists(output):
      click.echo(click.style("Creating output directory", fg='green'))
      os.makedirs(output)

  create_output(output)

  def export_dashboard_metatada(id, name):
    metadata = fetch_dashboard_metatada(id)

    filename = '{}.json'.format(name)
    with open(path.join(output, filename), 'w') as outfile:
      click.echo(click.style("Saving dashboard: {}".format(name), fg='green'))
      json.dump(metadata.to_dict(), outfile, indent=2, sort_keys=True, separators=(',', ':'))


  [export_dashboard_metatada(d.id.id, d.name) for d in dashboards]


def main(**kwargs):
  cli(auto_envvar_prefix='TB_CLI')

if __name__ == '__main__':
  main()
