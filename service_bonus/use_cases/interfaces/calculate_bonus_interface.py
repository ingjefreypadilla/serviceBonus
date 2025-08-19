# service_bonus/use_cases/interfaces/calculate_bonus_interface.py
from abc import ABC, abstractmethod

class ICalculateBonus(ABC):

    @abstractmethod
    def calculate(self, name: str, years: int, salary: float) -> float:
        pass
