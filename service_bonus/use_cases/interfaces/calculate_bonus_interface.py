# service_bonus/use_cases/interfaces/calculate_bonus_interface.py
from abc import ABC, abstractmethod

from service_bonus.domain.worker import Worker


class ICalculateBonus(ABC):

    @abstractmethod
    def calculate(self, worker: Worker, calculated_period, calculated_period_method) -> float:
        pass
