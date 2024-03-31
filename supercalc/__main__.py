import click
from click_aliases import ClickAliasedGroup


from supercalc.simple.simple_calc import main_group
from supercalc.scientific.scientific_calc import sci_grp


@click.group()
@click.help_option("-h", "--help", "--h")
def simple(scls=ClickAliasedGroup):
    pass


# @simple.command(name="nichts", aliases=["n"])
# def nichts():
#     click.echo("nichts")


# simple.add_command(main_group)
# simple.add_command(main_group, aliases=["sc"])


# @simple.group(
#     name="sc",
#     help="subcommand - scientific",
#     cls=ClickAliasedGroup,
# )
# def sc():
#     main_group()


simple.add_command(main_group, name="si")
simple.add_command(sci_grp, name="sc")


def main():
    # main_group()
    simple()


if __name__ == "__main__":
    simple()
