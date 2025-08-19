# service_bonus/use_cases/calculate_bonus.py
from service_bonus.domain.worker import Worker
from service_bonus.use_cases.interfaces.calculate_bonus_interface import ICalculateBonus


class BonusCalculator(ICalculateBonus):

    def calculate(self, worker: Worker, calculated_period: str = "primer_semestre", calculated_period_method: str = "promedio") -> dict:
        return {
            "empleado": worker.name,
            "periodo_calculo": calculated_period,
            "salario_base_prima": 0,
            "dias_trabajados_semestre": 0,
            "prima_bruta": 0,
            "renta_exenta_25_por_ciento": 0,
            "base_gravable_impuesto": 0,
            "impuesto_retenido": 0,
            "prima_neta": 0
        }
