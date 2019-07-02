import api.calculator as calc
import pytest


@pytest.mark.parametrize("n1,n2,func", [(8, 0, "division")])
def test_division_error(n1, n2, func):
    resp = calc.Calculator(n1, n2, func)
    msg, status_code = resp.call_calc()
    exp = {"error": "Zero division error"}
    assert msg == exp
    assert status_code == 500


@pytest.mark.parametrize("n1,n2,exp,func", [
    (1, 2, 3, "addition"),
    (5, 15, 75,  "multiplication"),
    (80, 3, 26.67, "division"),
    (100, 73, 27, "subtraction")
])
def test_unit_calculator(n1, n2, exp, func):
    resp = calc.Calculator(n1, n2, func)
    msg, status_code = resp.call_calc()
    exp = {"result": exp}
    assert msg == exp
    assert status_code == 200
