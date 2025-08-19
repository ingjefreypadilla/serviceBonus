from datetime import date
from service_bonus.domain.worker import Worker

def test_create_worker():
    worker = Worker(
        name="Jefrey Padilla",
        start_date=date(2023, 3, 15),
        monthly_salaries={"enero": 3000000, "febrero": 3000000},
        unpaid_absences=[date(2024, 4, 12)]
    )

    assert worker.name == "Jefrey Padilla"
    assert worker.start_date == date(2023, 3, 15)
    assert worker.monthly_salaries["enero"] == 3000000
    assert len(worker.unpaid_absences) == 1