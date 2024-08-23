import click

from pipcreator.writer import pip_creator
from pipcreator.convert import run_setup_command_convert
from pipcreator.upload import run_setup_command_upload
from pipcreator.guide import guide_learn
from pipcreator.constants import title

@click.group()
def cli():
    print(title)
    pass

@click.command()
@click.argument('directory')
def create(directory):
    directory = str(directory)
    pip_creator()

@click.command()
def convert():
    run_setup_command_convert()

@click.command()
def upload():
    run_setup_command_upload()

@click.command()
def guide():
    guide_learn()

cli.add_command(create)
cli.add_command(convert)
cli.add_command(upload)
cli.add_command(guide)