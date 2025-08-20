from abc import ABC, abstractmethod
from typing import Any

from service_bonus.domain.entities.calculate_worked_months import month_name_to_number
from service_bonus.domain.worker import Worker


class ICalculateWorkedDays(ABC):

    @abstractmethod
    def calculate(self, worked_months, worker: Worker) -> list[Any]:
        pass


class CalculateWorkedDays(ICalculateWorkedDays):

    def calculate(self, worked_months, worker) -> int:
        total_days_of_semester = len(worked_months) * 30

        month_numbers = {month_name_to_number(m) for m in worked_months}
        no_worked_days_semester = sum(
            1 for d in worker.unpaid_absences if d.month in month_numbers
        )
        worked_days = total_days_of_semester - no_worked_days_semester

        return worked_days
