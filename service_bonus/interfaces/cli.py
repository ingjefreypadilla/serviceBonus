# service_bonus/interfaces/cli.py
import argparse
import json
from datetime import datetime

from service_bonus.domain.worker import Worker
from service_bonus.interfaces.dto.worker_input import WorkerInput
from service_bonus.use_cases.calculate_bonus import BonusCalculator


def run():
    parser = argparse.ArgumentParser(description="Service Bonus Calculator CLI")
    parser.add_argument(
        "--json",
        type=str,
        required=True,
        help="JSON string or file path with worker data",
    )
    args = parser.parse_args()

    try:
        if args.json.endswith(".json"):
            with open(args.json, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = json.loads(args.json)

        WorkerInput.model_validate(data)
    except Exception as e:
        print(f"Error reading JSON or JSON Params Invalid: {e}")
        return

    start_date = datetime.strptime(data["fecha_ingreso"], "%Y-%m-%d").date()
    unpaid_absences = [
        datetime.strptime(d, "%Y-%m-%d").date()
        for d in data.get("ausencias_no_remuneradas", [])
    ]

    worker = Worker(
        name=data["nombre"],
        start_date=start_date,
        monthly_salaries=data["salarios_mensuales"],
        unpaid_absences=unpaid_absences,
    )

    calculator = BonusCalculator()
    result = calculator.calculate(
        worker,
        period_to_calculate=data.get("periodo_calculo", "primer_semestre"),
        method_to_calculate_period=data.get("metodo_calculo_salario", "promedio"),
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))
