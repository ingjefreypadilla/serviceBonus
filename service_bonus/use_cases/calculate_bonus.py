# service_bonus/use_cases/calculate_bonus.py
from service_bonus.domain.worker import Worker
from service_bonus.use_cases.interfaces.calculate_bonus_interface import ICalculateBonus


class BonusCalculator(ICalculateBonus):

    def calculate(self, name: str, years: int, salary: float) -> float:
        worker = Worker(name=name, years_of_service=years, base_salary=salary)
        years = min(worker.years_of_service, 20)
        return worker.base_salary * 0.05 * years
