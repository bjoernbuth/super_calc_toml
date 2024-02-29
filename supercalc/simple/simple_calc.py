"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    - module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.
    - another var (custom type): laber bla bla

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html

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
