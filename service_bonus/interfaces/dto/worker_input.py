from datetime import date
from typing import Dict, List, Literal

from pydantic import BaseModel, field_validator


class WorkerInput(BaseModel):
    nombre: str
    fecha_ingreso: date
    salarios_mensuales: Dict[
        Literal[
            "enero",
            "febrero",
            "marzo",
            "abril",
            "mayo",
            "junio",
            "julio",
            "agosto",
            "septiembre",
            "octubre",
            "noviembre",
            "diciembre",
        ],
        float,
    ]
    periodo_calculo: Literal["primer_semestre", "segundo_semestre", "actual"]
    metodo_calculo_salario: Literal["promedio", "actual"]
    ausencias_no_remuneradas: List[date]

    @field_validator("ausencias_no_remuneradas", mode="before")
    def parse_dates(cls, v):
        return [date.fromisoformat(d) if isinstance(d, str) else d for d in v]
