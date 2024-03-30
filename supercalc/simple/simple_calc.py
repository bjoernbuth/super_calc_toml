"""Module for simple calculations.

Funtions:
    add: Add numbers together
    subtract: Subtract numbers
    mult: Multiply numbers
    div: Divide two numbers
    exp: Exponentiation
    mod: Modulo operation
"""

import click


# @click.group()


# class CustomGroup(click.Group):
#     def get_help(self, ctx):
#         original_help = super().get_help(ctx)
#         return f"==== Running newcalc (nc) ====\n\n{original_help}"


# @click.command(cls=CustomGroup)
@click.group()
def cli():
    """Click gropup for simple calculations."""
    pass


# for navigation purposes
CLI = None

# @click.command()


@cli.group(name="int", help="subcommand - Integer operations")
def _int():
    pass


# quick hack for testing to have undecorated version of the function
def add_orig(numbers):
    """Add numbers together"""
    total = sum(numbers)
    click.echo(f"Sum: {total}")


@_int.command(name="add")
@click.argument("numbers", nargs=-1, type=int)
def add(numbers):
    """Add numbers together"""
    total = sum(numbers)
    click.echo(f"Sum: {total}")


@_int.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def subtract(x, y):
    """Subtract numbers"""
    res = x - y
    click.echo(f"Difference: {res}")


@_int.command()
@click.argument("numbers", nargs=-1, type=int)
def mult(numbers):
    """Multiply numbers"""
    result = 1
    for num in numbers:
        result *= num
    click.echo(f"Product: {result}")


@_int.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def div(x, y):
    """Divide two numbers"""
    try:
        result = x / y
        click.echo(f"Division: {result}")
    except ZeroDivisionError:
        click.echo("Error: Cannot divide by zero")


@_int.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def exp(x, y):
    """Exponentiation"""
    result = x**y
    click.echo(f"Exponentiation: {result}")


@_int.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def mod(x, y):
    """Modulo operation"""
    try:
        result = x % y
        click.echo(f"Modulo: {result}")
    except ZeroDivisionError:
        click.echo("Error: Cannot perform modulo operation with zero divisor")


GROUP_FLOAT = None


# create a subgroup of the cli group
@cli.group(name="float", help="subcommand - Float operations")
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


@cli.group(name="fr", help="subcommand - fractions")
def _fr():
    pass


@_fr.command(name="add")
@click.argument("x", type=str)
@click.argument("y", type=str)
# @click.argument("c", type=str)
# @click.argument("d", type=str)
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


if __name__ == "__main__":
    cli()
    # pass
