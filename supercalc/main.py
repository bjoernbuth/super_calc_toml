import click
from click_aliases import ClickAliasedGroup
from supercalc.calc.calc import calc
from supercalc.dumphelp_to_file import dumphelp_to_file
from pathlib import Path


@click.group()
@click.help_option("-h", "--help", "--h")
def suca(scls=ClickAliasedGroup):
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


suca.add_command(calc, name="calc")


suca.add_command(dumphelp_to_file, name="dh")


def main():
    # main_group()
    suca()


if __name__ == "__main__":
    suca()
