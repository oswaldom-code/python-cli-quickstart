from click.testing import CliRunner
from cli.main import cli

def test_hello():
    runner = CliRunner()
    result = runner.invoke(cli, ['hello', '--name', 'Yoda'])
    assert result.exit_code == 0
    assert 'Hello, Yoda!' in result.output
