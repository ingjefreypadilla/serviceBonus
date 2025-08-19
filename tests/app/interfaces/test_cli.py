import subprocess
import sys
import json
from pathlib import Path

import pytest


def run_cli_with_json(json_data):
    temp_file = Path("temp_worker.json")
    temp_file.write_text(json.dumps(json_data), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "main.py", "--json", str(temp_file)],
        capture_output=True,
        text=True
    )

    temp_file.unlink()
    return json.loads(result.stdout)

def test_cli_example():
    json_data = {
        "nombre": "Jefrey Padilla",
        "fecha_ingreso": "2023-03-15",
        "salarios_mensuales": {
            "enero": 3000000, "febrero": 3000000, "marzo": 3000000,
            "abril": 3200000, "mayo": 3200000, "junio": 3200000
        },
        "periodo_calculo": "primer_semestre",
        "metodo_calculo_salario": "promedio",
        "ausencias_no_remuneradas": ["2024-04-12"]
    }

    output = run_cli_with_json(json_data)

    assert output["empleado"] == "Jefrey Padilla"
    assert output["periodo_calculo"] == "primer_semestre"
    assert output["dias_trabajados_semestre"] == 0
    assert pytest.approx(output["renta_exenta_25_por_ciento"]) == 0
    assert pytest.approx(output["prima_bruta"]) == 0
    assert pytest.approx(output["base_gravable_impuesto"]) == 0
    assert output["impuesto_retenido"] == 0
    assert pytest.approx(output["prima_neta"]) == 0