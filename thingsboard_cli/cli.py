import click
import signal
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
    response = requests.post(url=path,json={'username':username, 'password':password})
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

  dashboards = tb.DashboardControllerApi(repo.client).get_tenant_dashboards_using_get(limit=100)
  print_dashboards(dashboards)


def main(**kwargs):
  cli(auto_envvar_prefix='TB_CLI')

if __name__ == '__main__':
  main()
