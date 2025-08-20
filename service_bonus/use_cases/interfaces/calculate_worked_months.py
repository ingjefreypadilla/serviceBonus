from abc import abstractmethod, ABC
from datetime import date
from typing import Any

from service_bonus.domain.worker import Worker

MONTHS_FIRST_SEMESTER = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
MONTHS_SECOND_SEMESTER = ["julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def month_name_to_number(name: str) -> int:
    mapping = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
        "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    return mapping.get(name.lower(), 1)


class ICalculateWorkedMonths(ABC):

    @abstractmethod
    def calculate(self, period_to_calculate, worker: Worker) -> list[Any]:
        pass


class CalculateWorkedMonths(ICalculateWorkedMonths):

    def calculate(self, period_to_calculate, worker) -> list[Any]:
        if period_to_calculate == "primer_semestre":
            months = MONTHS_FIRST_SEMESTER
        elif period_to_calculate == "segundo_semestre":
            months = MONTHS_SECOND_SEMESTER
        else:
            months = list(worker.monthly_salaries.keys())

        worked_months = []
        for m in months:
            mes_num = month_name_to_number(m)
            if worker.start_date.year < date.today().year or worker.start_date.month <= mes_num:
                worked_months.append(m)

        return worked_months
