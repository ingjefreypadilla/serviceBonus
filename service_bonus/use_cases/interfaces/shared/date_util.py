MONTHS_FIRST_SEMESTER = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
MONTHS_SECOND_SEMESTER = ["julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def month_name_to_number(name: str) -> int:
    mapping = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
        "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    return mapping.get(name.lower(), 1)