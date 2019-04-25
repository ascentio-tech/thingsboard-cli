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
  path = "{}/api/auth/login".format(url)

  response = requests.post(url=path,json={'username':username, 'password':password})
  if response.status_code == requests.codes.ok:
    configuration = tb.Configuration()
    configuration.username = username
    configuration.password = password
    configuration.host = url
    configuration.api_key['X-Authorization'] = response.json()['token']
    configuration.api_key_prefix['X-Authorization'] = 'Bearer'
    tb_client = tb.ApiClient()

  else:
    click.echo("Could not authenticate with given credentials")
    print response.json()
    exit(1)

  ctx.obj = Repo(tb_client)

@cli.command()
@pass_repo
def dashboard_list(repo):
  click.echo('- Listing all dashboards')
  dashboards = tb.DashboardcontrollerApi(repo.client).get_tenant_dashboards_using_get(limit=100).data
  [click.echo("{} {}".format(d.id.id, d.name)) for d in dashboards]


def main(**kwargs):
  cli(auto_envvar_prefix='TB_CLI')

if __name__ == '__main__':
  main()
