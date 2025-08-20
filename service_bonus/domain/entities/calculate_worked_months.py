from abc import ABC, abstractmethod
from typing import Any

from service_bonus.domain.entities.utils.date_util import (
    MONTHS_FIRST_SEMESTER,
    MONTHS_SECOND_SEMESTER,
    month_name_to_number,
)
from service_bonus.domain.worker import Worker


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
            if worker.start_date.month <= mes_num:
                worked_months.append(m)

        return worked_months
