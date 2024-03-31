"""Module for simple calculations.

Click groups:
    int: Integer operations (imported from int_group/int_group_click.py)
    float: Float operations
    fr: Fraction operations



Funtions:
    add: Add numbers together
    subtract: Subtract numbers
    mult: Multiply numbers
    div: Divide two numbers
    exp: Exponentiation
    mod: Modulo operation


"""

import click
from click_aliases import ClickAliasedGroup

from supercalc.simple.int_group import (  # pylint: disable=unused-import
    int_group,
    int_add,
    int_subtract,
    int_mult,
    int_div,
    int_exp,
    int_mod,
)


# @click.group()


# class CustomGroup(click.Group):
#     def get_help(self, ctx):
#         original_help = super().get_help(ctx)
#         return f"==== Running newcalc (nc) ====\n\n{original_help}"

MAIN_GROUP = None


# @click.command(cls=CustomGroup)
@click.group(cls=ClickAliasedGroup)
def main_group():
    """Click gropup for simple calculations."""
    pass


# for navigation purposes
CLI = None

# @click.command()

INT_GROUP = None


# # quick hack for testing to have undecorated version of the function
# def add_orig(numbers):
#     """Add numbers together"""
#     total = sum(numbers)
#     click.echo(f"Sum: {total}")


GROUP_FLOAT = None


# create a subgroup of the cli group
@main_group.group(
    name="float",
    help="subcommand - Float operations",
    cls=ClickAliasedGroup,
    aliases=[
        "fl",
    ],
)
@click.help_option("-h", "--help")
def _float():
    pass


@_float.command(name="add")
@click.argument("x", type=float)
@click.argument("y", type=float)
def float_add(x, y):
    """Add two numbers"""
    click.echo(f"Sum: {x + y}")


@_float.command(name="mult")
@click.argument("numbers", nargs=-1, type=float)
def float_mult(numbers):
    """Multiply numbers"""
    result = 1
    for num in numbers:
        result *= num
    click.echo(f"Product: {result}")


GROUP_FR = None


@main_group.group(
    name="fr",
    help="subcommand - fractions",
    cls=ClickAliasedGroup,
    aliases=["fr"],
)
@click.help_option("-h", "--help")
def _fr():
    pass


@_fr.command(name="add")
@click.argument("x", type=str)
@click.argument("y", type=str)
def fr_add(x, y):
    """Add two fractions"""

    # parse the input by splitting at the '/'
    a, b = x.split("/")
    c, d = y.split("/")

    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        result = (a * d + b * c), (b * d)

    except ZeroDivisionError:
        click.echo("Error: Cannot divide by zero")

    def simplify_fraction(numer, denom):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        common_divisor = gcd(numer, denom)
        return numer // common_divisor, denom // common_divisor

    result = simplify_fraction(*result)

    if result[1] == 1:
        click.echo(f"Sum: {result[0]}")
    else:
        click.echo(f"Sum: {result}")


# add some commands from the _int gropup to the main_group (a) for easier access
# (b) for testing purposes (keep the old way of calling the functions)
# main_group.add_command(int_add)
# main_group.add_command(int_subtract)
# main_group.add_command(int_mult)
# main_group.add_command(int_div)
# main_group.add_command(int_exp)
# main_group.add_command(int_mod)

main_group.add_command(int_group, aliases=["i"])


# cli = click.CommandCollection(sources=[int_group])

if __name__ == "__main__":
    main_group()
    # pass
