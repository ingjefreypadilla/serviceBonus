# service_bonus/use_cases/interfaces/calculate_base_salary.py
from abc import ABC, abstractmethod
from datetime import date

class ICalculateBaseSalary(ABC):

    @abstractmethod
    def calculate(self, worker, calculated_period, calculated_period_method, filtered_months):
        pass

class CalculateBaseSalary(ICalculateBaseSalary):

    def calculate(self, worker, period_to_calculate, calculated_period_method, filtered_months):
        salaries = [worker.monthly_salaries[m] for m in filtered_months if m in worker.monthly_salaries]

        if calculated_period_method == "promedio":
            return sum(salaries) / len(salaries)

        return salaries[-1]