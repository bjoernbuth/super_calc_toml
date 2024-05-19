"""Module for integer operations using click group."""

import click
from click_aliases import ClickAliasedGroup


@click.group(
    name="int",
    help="subcommand - Integer operations",
    cls=ClickAliasedGroup,
    # aliases=["i"],
)
@click.help_option("-h", "--help")
def int_group():
    pass


@int_group.command(name='add')
@click.argument('files', type=click.Path(exists=True), nargs=-1)
def add_int(files):
    """Adds integers from given files."""
    total = 0
    for filepath in files:
        number_str = read_number_from_file(filepath)
        total += int(number_str)
    print(f"Integer sum: {total}")


@int_group.command(name="add", aliases=["a"])
@click.argument("numbers", nargs=-1, type=int)
def int_add(numbers):
    """Add 2 integers, (group int but also  main group)."""
    total = sum(numbers)
    click.echo(f"Sum: {total}")


@int_group.command(name="sub", aliases=["s"])
@click.argument("x", type=int)
@click.argument("y", type=int)
def int_subtract(x, y):
    """Subtract 2 integers (group int but also  main group)"""
    res = x - y
    click.echo(f"Difference: {res}")


@int_group.command(name="mult", aliases=["m"])
@click.argument("numbers", nargs=-1, type=int)
def int_mult(numbers):
    """Multiply integers, arbitrary number of args."""
    result = 1
    for num in numbers:
        result *= num
    click.echo(f"Product: {result}")


@int_group.command(name="div", aliases=["d"])
@click.argument("x", type=int)
@click.argument("y", type=int)
def int_div(x, y):
    """Divide two numbers"""
    try:
        result = x / y
        click.echo(f"Division: {result}")
    except ZeroDivisionError:
        click.echo("Error: Cannot divide by zero")


@int_group.command(name="exp", aliases=["e"])
@click.argument("x", type=int)
@click.argument("y", type=int)
def int_exp(x, y):
    """Exponentiation"""
    result = x**y
    click.echo(f"Exponentiation: {result}")


@int_group.command(name="mod")
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
    int_group()
