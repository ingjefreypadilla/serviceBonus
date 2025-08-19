# service_bonus/use_cases/calculate_bonus.py
from datetime import date

from service_bonus.domain.worker import Worker
from service_bonus.use_cases.interfaces.calculate_bonus_interface import ICalculateBonus

MONTHS_FIRST_SEMESTER = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
MONTHS_SECOND_SEMESTER = ["julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def month_name_to_number(name: str) -> int:
    mapping = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
        "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    return mapping.get(name.lower(), 1)


def calculate_base_salary(worker: Worker, period_to_calculate: str, calculated_period_method: str) -> float:
    if period_to_calculate == "primer_semestre":
        months = MONTHS_FIRST_SEMESTER
    elif period_to_calculate == "segundo_semestre":
        months = MONTHS_SECOND_SEMESTER
    else:
        months = list(worker.monthly_salaries.keys())

    filtered_months = []
    for m in months:
        # Convertir nombre del mes a número
        mes_num = month_name_to_number(m)
        if worker.start_date.year < date.today().year or worker.start_date.month <= mes_num:
            filtered_months.append(m)

    salaries = [worker.monthly_salaries[m] for m in filtered_months if m in worker.monthly_salaries]

    if calculated_period_method == "promedio":
        return sum(salaries) / len(salaries)

    return salaries[-1]


class BonusCalculator(ICalculateBonus):

    def calculate(self, worker: Worker, period_to_calculate: str = "primer_semestre", method_to_calculate_period: str = "promedio") -> dict:

        base_salary = calculate_base_salary(worker, period_to_calculate, method_to_calculate_period)

        return {
            "empleado": worker.name,
            "periodo_calculo": period_to_calculate,
            "salario_base_prima": round(base_salary, 2),
            "dias_trabajados_semestre": 0,
            "prima_bruta": 0,
            "renta_exenta_25_por_ciento": 0,
            "base_gravable_impuesto": 0,
            "impuesto_retenido": 0,
            "prima_neta": 0
        }
