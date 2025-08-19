# app/domain/cli.py
from dataclasses import dataclass

@dataclass
class Worker:
    name: str
    years_of_service: int
    base_salary: float