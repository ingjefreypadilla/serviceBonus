import pytest

from service_bonus.use_cases.calculate_bonus import BonusCalculator


@pytest.fixture
def calculator():
    return BonusCalculator()

def test_bonus_within_cap(calculator):
    bonus = calculator.calculate(name="Alice", years=10, salary=3000)
    assert bonus == 1500

def test_bonus_at_cap(calculator):
    bonus = calculator.calculate(name="Bob", years=20, salary=4000)
    assert bonus == 4000

def test_bonus_exceeding_cap(calculator):
    bonus = calculator.calculate(name="Carol", years=25, salary=4000)
    assert bonus == 4000