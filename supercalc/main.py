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


simple.add_command(main_group, name="si")
simple.add_command(sci_grp, name="sc")


def main():
    # main_group()
    simple()


if __name__ == "__main__":
    simple()
