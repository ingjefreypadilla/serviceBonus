# service_bonus/use_cases/interfaces/calculate_base_salary.py
from abc import ABC, abstractmethod
from datetime import date

MONTHS_FIRST_SEMESTER = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
MONTHS_SECOND_SEMESTER = ["julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def month_name_to_number(name: str) -> int:
    mapping = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
        "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    return mapping.get(name.lower(), 1)


class ICalculateBaseSalary(ABC):

    @abstractmethod
    def calculate(self, worker, calculated_period, calculated_period_method):
        pass

class CalculateBaseSalary(ICalculateBaseSalary):

    def calculate(self, worker, period_to_calculate, calculated_period_method):
        if period_to_calculate == "primer_semestre":
            months = MONTHS_FIRST_SEMESTER
        elif period_to_calculate == "segundo_semestre":
            months = MONTHS_SECOND_SEMESTER
        else:
            months = list(worker.monthly_salaries.keys())

        filtered_months = []
        for m in months:
            mes_num = month_name_to_number(m)
            if worker.start_date.year < date.today().year or worker.start_date.month <= mes_num:
                filtered_months.append(m)

        salaries = [worker.monthly_salaries[m] for m in filtered_months if m in worker.monthly_salaries]

        if calculated_period_method == "promedio":
            return sum(salaries) / len(salaries)

        return salaries[-1]