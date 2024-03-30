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


class CustomGroup(click.Group):
    def get_help(self, ctx):
        original_help = super().get_help(ctx)
        return f"==== Running newcalc (nc) ====\n\n{original_help}"


@click.command(cls=CustomGroup)
def cli():
    pass


# quick hack for testing to have undecorated version of the function
def add_orig(numbers):
    """Add numbers together"""
    total = sum(numbers)
    click.echo(f"Sum: {total}")


@cli.command()
@click.argument("numbers", nargs=-1, type=int)
def add(numbers):
    """Add numbers together"""
    total = sum(numbers)
    click.echo(f"Sum: {total}")


@cli.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def subtract(x, y):
    """Subtract numbers"""
    res = x - y
    click.echo(f"Difference: {res}")


@cli.command()
@click.argument("numbers", nargs=-1, type=int)
def mult(numbers):
    """Multiply numbers"""
    result = 1
    for num in numbers:
        result *= num
    click.echo(f"Product: {result}")


@cli.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def div(x, y):
    """Divide two numbers"""
    try:
        result = x / y
        click.echo(f"Division: {result}")
    except ZeroDivisionError:
        click.echo("Error: Cannot divide by zero")


@cli.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def exp(x, y):
    """Exponentiation"""
    result = x**y
    click.echo(f"Exponentiation: {result}")


@cli.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def mod(x, y):
    """Modulo operation"""
    try:
        result = x % y
        click.echo(f"Modulo: {result}")
    except ZeroDivisionError:
        click.echo("Error: Cannot perform modulo operation with zero divisor")


if __name__ == "__main__":
    cli()
