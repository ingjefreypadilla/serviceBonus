from datetime import datetime

import pytest

from service_bonus.domain.worker import Worker
from service_bonus.use_cases.calculate_bonus import BonusCalculator


@pytest.fixture
def calculator():
    return BonusCalculator()

@pytest.fixture
def worker():
    ausencias_no_remuneradas = [
        "2024-04-12",
        "2024-04-15"
    ]

    worker = Worker(
        name="Jefrey Padilla",
        start_date=datetime.strptime("2023-03-15", "%Y-%m-%d").date(),
        monthly_salaries={
            "enero": 3000000,
            "febrero": 3000000,
            "marzo": 3000000,
            "abril": 3200000,
            "mayo": 3200000,
            "junio": 3200000,
            "julio": 3200000,
            "agosto": 3200000,
            "septiembre": 3500000,
            "octubre": 3500000,
            "noviembre": 3500000,
            "diciembre": 3500000
          },
        unpaid_absences=[datetime.strptime(d, "%Y-%m-%d").date() for d in ausencias_no_remuneradas],
    )

    return worker

@pytest.fixture
def expected_bonus():

    return {
            "empleado": "Jefrey Padilla",
            "periodo_calculo": "primer_semestre",
            "salario_base_prima": 0,
            "dias_trabajados_semestre": 0,
            "prima_bruta": 0,
            "renta_exenta_25_por_ciento": 0,
            "base_gravable_impuesto": 0,
            "impuesto_retenido": 0,
            "prima_neta": 0
        }

def test_should_calculate_bonus(calculator, worker, expected_bonus):
    calculated_period = "primer_semestre"
    calculated_period_method = "promedio"

    bonus = calculator.calculate( worker, calculated_period, calculated_period_method)

    assert bonus == expected_bonus
