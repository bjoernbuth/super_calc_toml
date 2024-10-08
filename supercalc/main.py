from pathlib import Path

import click
from click_aliases import ClickAliasedGroup
from clickhelper.dumphelp_to_file import add_dump_help_to_file_command

from supercalc.calc.calc import calc


@click.group(cls=ClickAliasedGroup)
@click.help_option("-h", "--help", "--h")
def suca():
    pass


def read_number_from_file(filepath):
    """Reads the first line of a file and returns it as a string."""
    with open(filepath, "r") as file:
        return file.readline().strip()


@suca.command()
@click.help_option("--h", "-h", "--help")
@click.option("--long_argument_name_01", type=int, help="First number")
@click.option("--long_argument_name_02", type=int, help="Second number")
def bashcomp(long_argument_name_01, long_argument_name_02):
    """Test command for bash completion."""
    click.echo(f"Arguments: {long_argument_name_01}, {long_argument_name_02}")
    # click.echo("Test command for bash completion.")
    # z = long_argument_name_01 + long_argument_name_02
    # click.echo(f"Sum: {z}")
    print("Hi")


suca.add_command(calc, aliases=["c"])


def main():
    add_dump_help_to_file_command(suca, name_of_dump_help_command="dh")
    add_dump_help_to_file_command(calc)
    suca()


if __name__ == "__main__":
    suca()
