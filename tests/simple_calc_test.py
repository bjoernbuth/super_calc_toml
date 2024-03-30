from supercalc.simple import simple_calc as sc

from click.testing import CliRunner

# # subtract, mult, div, exp, mod


def test_01():
    assert 1 + 1 == 2


# def test_add():
#     assert sc.add([1, 2, 3]) == 6


def test_simple_calc_add_cli():
    runner = CliRunner()
    result = runner.invoke(sc.main_group, ["add", "1", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "Sum: 6\n"


def test_simple_calc_mult():
    runner = CliRunner()
    result = runner.invoke(sc.main_group, ["mult", "1", "2", "3", "4"])
    assert result.exit_code == 0
    assert result.output == "Product: 24\n"


def test_simple_calc_mult_ten_numbers():
    runner = CliRunner()
    result = runner.invoke(sc.main_group, ["mult"] + [str(i) for i in range(1, 11)])
    assert result.exit_code == 0
    assert result.output == "Product: 3628800\n"
