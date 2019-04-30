import json, os
from os import path
import click
from click import command
from thingsboard_cli.version import __version__
from thingsboard_cli.rest_api import (
  authenticate,
  create_api_client
)
import thingsboard_client as tb

class CliContext(object):
    def __init__(self, tb_client):
      self.client = tb_client
pass_cli_context = click.make_pass_decorator(CliContext)


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
  is_authenticated, token = authenticate(url, username, password)
  if is_authenticated:
    click.echo(click.style("Authenticated!", fg='green'))
    tb_client = create_api_client(url, username, password, token)

  else:
    click.echo(click.style("Could not authenticate with given credentials", fg='red'))
    print(response.json())
    exit(1)

  ctx.obj = CliContext(tb_client)


def create_output(output):
  if not path.exists(output):
    click.echo(click.style("Creating output directory: {}".format(output), fg='green'))
    os.makedirs(output)

  def save_to_file(content, name):
    filename = '{}.json'.format(name)
    with open(path.join(output, filename), 'w') as outfile:
      click.echo(click.style("Saving: {}".format(name), fg='green'))
      json.dump(content.to_dict(), outfile, indent=2, sort_keys=True, separators=(',', ':'))

  return save_to_file


@cli.command()
@pass_cli_context
@click.option('--output', '-o', default='dashboards', type=click.Path(exists=False, writable=True, dir_okay=True))
@click.option('--include', '-i', default='.*', type=str)
@click.option('--exclude', '-e', default='', type=str)
@click.option('--write', '-w', default=True, type=bool)
def dashboard_list(repo, output, include, exclude, write):
  click.echo('- Dashboards')
  def print_dashboards(dashboards):
    [click.echo("{} {}".format(d.id.id, d.name)) for d in dashboards]

  controller = tb.DashboardControllerApi(repo.client)
  dashboards = controller.get_tenant_dashboards_using_get(limit=100).data
  print_dashboards(dashboards)

  def fetch_dashboard_metatada(id):
    response = controller.get_dashboard_by_id_using_get(id)
    return response

  save_to_file = create_output(output)

  def export_dashboard_metatada(id, name):
    metadata = fetch_dashboard_metatada(id)
    save_to_file(metadata, name)

  [export_dashboard_metatada(d.id.id, d.name) for d in dashboards]


@cli.command()
@pass_cli_context
@click.option('--output', '-o', default='rule-chains', type=click.Path(exists=False, writable=True, dir_okay=True))
@click.option('--include', '-i', default='.*', type=str)
@click.option('--exclude', '-e', default='', type=str)
@click.option('--write', '-w', default=True, type=bool)
def rule_chains_list(repo, output, include, exclude, write):
  click.echo('- Rule Chains')
  def print_items(items):
    [click.echo("{} {}".format(d.id.id, d.name)) for d in items]

  controller = tb.RuleChainControllerApi(repo.client)
  items = controller.get_rule_chains_using_get(limit=100).data
  print_items(items)

  def fetch_item(id):
    response = controller.get_rule_chain_meta_data_using_get(id)
    return response

  save_to_file = create_output(output)

  def export_item(id, name):
    content = fetch_item(id)
    save_to_file(content, name)

  [export_item(d.id.id, d.name) for d in items]


def main(**kwargs):
  cli(auto_envvar_prefix='TB_CLI')

if __name__ == '__main__':
  main()
