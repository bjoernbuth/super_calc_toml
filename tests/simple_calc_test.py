from supercalc.calc import calc as calc
from supercalc.calc.int_group.int_group import int_group  # pylint: disable=unused-import

from click.testing import CliRunner

# # subtract, mult, div, exp, mod


def test_01():
    assert 1 + 1 == 2


# def test_add():
#     assert sc.add([1, 2, 3]) == 6


def test_simple_calc_add_cli():
    runner = CliRunner()
    result = runner.invoke(calc.int_group, ["add", "1", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "Sum: 6\n"


def test_simple_calc_mult():
    runner = CliRunner()
    result = runner.invoke(calc.int_group, ["mult", "1", "2", "3", "4"])
    assert result.exit_code == 0
    assert result.output == "Product: 24\n"


def test_simple_calc_mult_ten_numbers():
    runner = CliRunner()
    result = runner.invoke(calc.int_group, ["mult"] + [str(i) for i in range(1, 11)])
    assert result.exit_code == 0
    assert result.output == "Product: 3628800\n"


def test_invoke_calc_group():
    runner = CliRunner()
    result = runner.invoke(calc.calc)
    assert result.exit_code == 0
    assert "Usage: calc [OPTIONS] COMMAND [ARGS]..." in result.output

    assert False
