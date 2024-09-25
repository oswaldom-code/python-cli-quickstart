import click
from cli.commands import hello

@click.group()
def cli():
    pass

cli.add_command(hello)

if __name__ == "__main__":
    cli()
