import click
from click_aliases import ClickAliasedGroup
from supercalc.simple.simple_calc import main_group
from supercalc.scientific.scientific_calc import sci_grp
from pathlib import Path


@click.group()
@click.help_option("-h", "--help", "--h")
def simple(scls=ClickAliasedGroup):
    pass


def read_number_from_file(filepath):
    """Reads the first line of a file and returns it as a string."""
    with open(filepath, "r") as file:
        return file.readline().strip()


@simple.command()
@click.help_option("--h", "-h", "--help")
@click.option("--long_argument_name_01", type=int, help="First number")
@click.option("--long_argument_name_02", type=int, help="Second number")
def test_bash_completion_command(long_argument_name_01, long_argument_name_02):
    """Test command for bash completion."""
    click.echo(f"Arguments: {long_argument_name_01}, {long_argument_name_02}")
    # click.echo("Test command for bash completion.")
    # z = long_argument_name_01 + long_argument_name_02
    # click.echo(f"Sum: {z}")
    print("Hi")


simple.add_command(main_group, name="si")
simple.add_command(sci_grp, name="sc")


def main():
    # main_group()
    simple()


if __name__ == "__main__":
    simple()
