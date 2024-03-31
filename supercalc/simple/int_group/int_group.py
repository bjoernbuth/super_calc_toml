"""Module for integer operations using click group."""

import click
from click_aliases import ClickAliasedGroup


@click.group(
    name="int",
    help="subcommand - Integer operations",
    cls=ClickAliasedGroup,
    # aliases=["i"],
)
def _int():
    pass


@_int.command(name="add", aliases=["a"])
@click.argument("numbers", nargs=-1, type=int)
def int_add(numbers):
    """Add 2 integers, (group int but also  main group)."""
    total = sum(numbers)
    click.echo(f"Sum: {total}")


@_int.command(name="sub")
@click.argument("x", type=int)
@click.argument("y", type=int)
def int_subtract(x, y):
    """Subtract 2 integers (group int but also  main group)"""
    res = x - y
    click.echo(f"Difference: {res}")


@_int.command(name="mult")
@click.argument("numbers", nargs=-1, type=int)
def int_mult(numbers):
    """Multiply integers, arbitrary number of args."""
    result = 1
    for num in numbers:
        result *= num
    click.echo(f"Product: {result}")


@_int.command(name="div")
@click.argument("x", type=int)
@click.argument("y", type=int)
def int_div(x, y):
    """Divide two numbers"""
    try:
        result = x / y
        click.echo(f"Division: {result}")
    except ZeroDivisionError:
        click.echo("Error: Cannot divide by zero")


@_int.command(name="exp")
@click.argument("x", type=int)
@click.argument("y", type=int)
def int_exp(x, y):
    """Exponentiation"""
    result = x**y
    click.echo(f"Exponentiation: {result}")


@_int.command(name="mod")
@click.argument("x", type=int)
@click.argument("y", type=int)
def int_mod(x, y):
    """Modulo operation"""
    try:
        result = x % y
        click.echo(f"Modulo: {result}")
    except ZeroDivisionError:
        click.echo("Error: Cannot perform modulo operation with zero divisor")


if __name__ == "__main__":
    _int()
