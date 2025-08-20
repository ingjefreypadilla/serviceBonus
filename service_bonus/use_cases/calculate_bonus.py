# service_bonus/use_cases/calculate_bonus.py
from service_bonus.domain.worker import Worker
from service_bonus.use_cases.interfaces.calculate_base_salary import CalculateBaseSalary
from service_bonus.use_cases.interfaces.calculate_bonus_interface import ICalculateBonus
from service_bonus.use_cases.interfaces.calculate_worked_months import CalculateWorkedMonths


class BonusCalculator(ICalculateBonus):

    def __init__(self):
        self.calculate_base_salary = CalculateBaseSalary()
        self.calculate_worked_months = CalculateWorkedMonths()

    def calculate(self, worker: Worker, period_to_calculate: str = "primer_semestre", method_to_calculate_period: str = "promedio") -> dict:

        worked_months = self.calculate_worked_months.calculate(period_to_calculate, worker)
        base_salary = self.calculate_base_salary.calculate(worker, period_to_calculate, method_to_calculate_period, worked_months)

        total_days_of_semester = len(worked_months) * 30
        unpaid_absences = len(worker.unpaid_absences)
        worked_days = total_days_of_semester - unpaid_absences

        return {
            "empleado": worker.name,
            "periodo_calculo": period_to_calculate,
            "salario_base_prima": round(base_salary, 2),
            "dias_trabajados_semestre": worked_days,
            "prima_bruta": 0,
            "renta_exenta_25_por_ciento": 0,
            "base_gravable_impuesto": 0,
            "impuesto_retenido": 0,
            "prima_neta": 0
        }
