# 🧮 Service Bonus CLI

A simple **Python CLI** project built with **Clean Architecture** principles to calculate **service bonuses for workers**.

---

## 📂 Project Structure

```
service_bonus_cli/
│── pyproject.toml        # or requirements.txt
│── README.md
│── app/
│   ├── domain/           # Core business logic (Entities, Models)
│   │   └── worker.py
│   │
│   ├── use_cases/        # Application rules (Interactors)
│   │   ├── interfaces.py       # Use case interfaces (ports)
│   │   └── calculate_bonus.py  # Implementation of bonus calculation
│   │
│   ├── infrastructure/   # External adapters (repos, persistence, etc.)
│   │   └── repositories.py
│   │
│   └── interfaces/       # Delivery layer (CLI)
│       └── cli.py
│
└── main.py               # CLI entry point
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ingjefreypadilla/serviceBonus.git
cd serviceBonus
```

(Optionally, create a virtual environment:)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

Install dependencies (if you add any later):

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the CLI with:

```bash
python main.py --json input/jefrey.json
```
### Example Input
```json
{
  "nombre": "Jefrey Padilla",
  "fecha_ingreso": "2023-03-15",
  "salarios_mensuales": {
    "enero": 3000000,
    "febrero": 3000000,
    "marzo": 3000000,
    "abril": 3200000,
    "mayo": 3200000,
    "junio": 3200000,
    "julio": 3200000,
    "agosto": 3200000,
    "septiembre": 3500000,
    "octubre": 3500000,
    "noviembre": 3500000,
    "diciembre": 3500000
  },
  "periodo_calculo": "primer_semestre",
  "metodo_calculo_salario": "promedio",
  "ausencias_no_remuneradas": [
    "2024-04-12",
    "2024-04-15"
  ]
}
```


### Example Output

```json
{
        "empleado": "Jefrey Padilla",
        "periodo_calculo": "primer_semestre",
        "salario_base_prima": 3100000,
        "dias_trabajados_semestre": 105,
        "prima_bruta": 863013.70,
        "renta_exenta_25_por_ciento": 215753.42,
        "base_gravable_impuesto": 647260.28,
        "impuesto_retenido": 0,
        "prima_neta": 863013.70
    }
```

---

## 📖 Bonus Calculation Rule

- **5% of base salary per year of service**
- **Capped at 20 years**

Example:  
- Base salary = `$3000`  
- Years of service = `12`  
- Bonus = `3000 * 0.05 * 12 = $1800`

---

## ✅ More Examples

### Example 1 – Worker with 5 years
```bash
python main.py --name Bob --years 5 --salary 2000
```

Output:
```
Worker: Bob
Years of service: 5
Base salary: $2000.00
Service bonus: $500.00
```

---

### Example 2 – Worker with 25 years (capped at 20)
```bash
python main.py --name Carol --years 25 --salary 4000
```

Output:
```
Worker: Carol
Years of service: 25
Base salary: $4000.00
Service bonus: $4000.00
```

---

## 🏛 Clean Architecture Principles

- **Domain Layer (`domain/`)**  
  Contains pure business entities (`Worker`).

- **Use Cases Layer (`use_cases/`)**  
  Application-specific rules. Defines **interfaces (ports)** and implementations (e.g., `BonusCalculator`).

- **Interfaces Layer (`interfaces/`)**  
  Entry points like CLI (`cli.py`). It depends on **use case interfaces**, not implementations.

- **Infrastructure Layer (`infrastructure/`)**  
  Adapters for persistence or external services. Currently minimal.

This separation makes the project **modular, testable, and future-proof**.  
You could easily replace the CLI with a REST API or a database without changing core logic.

---

## 🧪 Tests (Optional)

Create a `tests/` folder for unit tests:

```
tests/
├── app/
├────── domain/test_worker.py
├────── interfaces/test_cli.py
└────── use_cases/calculate_bonus.py
```

Run tests with:

```bash
pytest
```

---

## 🚀 Future Improvements

- Add persistence (e.g., save/load workers from DB or JSON file).  
- Add multiple bonus calculation strategies.  
- Add a REST API (FastAPI) or GUI interface.  
- Package as a Python library with `pip install`.  

---
