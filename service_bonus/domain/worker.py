# service_bonus/domain/worker.py
from dataclasses import dataclass
from datetime import date
from typing import Dict, List


@dataclass
class Worker:
    name: str
    start_date: date
    monthly_salaries: Dict[str, float]
    unpaid_absences: List[date]
