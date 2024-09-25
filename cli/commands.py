import click

@click.command()
@click.option('--name', default='World', help='Name to greet')
def hello(name):
    """Greet someone."""
    click.echo(f'Hello, {name}!')