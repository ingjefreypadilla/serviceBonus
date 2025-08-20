# service_bonus/use_cases/calculate_bonus.py
from service_bonus.domain.worker import Worker
from service_bonus.use_cases.interfaces.calculate_base_salary import CalculateBaseSalary
from service_bonus.use_cases.interfaces.calculate_bonus_interface import ICalculateBonus

class BonusCalculator(ICalculateBonus):

    def __init__(self):
        self.calculate_base_salary = CalculateBaseSalary()

    def calculate(self, worker: Worker, period_to_calculate: str = "primer_semestre", method_to_calculate_period: str = "promedio") -> dict:

        base_salary = self.calculate_base_salary.calculate(worker, period_to_calculate, method_to_calculate_period)

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
