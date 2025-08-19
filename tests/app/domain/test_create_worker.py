from service_bonus.domain.worker import Worker


def test_create_worker():
    worker = Worker(name="Alice", years_of_service=10, base_salary=3000)
    assert worker.name == "Alice"
    assert worker.years_of_service == 10
    assert worker.base_salary == 3000