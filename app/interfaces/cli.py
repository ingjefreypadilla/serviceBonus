# app/interfaces/cli.py
import argparse

from app.use_cases.calculate_bonus import BonusCalculator
from app.use_cases.interfaces.calculate_bonus_interface import ICalculateBonus


def run():
    parser = argparse.ArgumentParser(description="Service Bonus Calculator CLI")
    parser.add_argument("--name", type=str, required=True)
    parser.add_argument("--years", type=int, required=True)
    parser.add_argument("--salary", type=float, required=True)

    args = parser.parse_args()

    name, years, salary = args.name, args.years, args.salary

    calculator: ICalculateBonus = BonusCalculator()
    bonus = calculator.calculate(name, years, salary)

    print(f"Worker: {name}")
    print(f"Years of service: {years}")
    print(f"Base salary: ${salary:.2f}")
    print(f"Service bonus: ${bonus:.2f}")
