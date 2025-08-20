# 🧮 Service Bonus CLI

A simple **Python CLI** project built with **Clean Architecture** principles to calculate **service bonuses for workers**.

---

## 📂 Project Structure

```
serviceBonus/
│── pyproject.toml
│── .gitignore.toml
│── docker-compose.toml
│── Dockerfile.toml
│── requirements.txt
│── README.md
│── service_bonus/
│   ├── domain/           # Core business logic (Entities, Models)
│   │   ├── entities
│   │   │   ├──utils
│   │   │   │   ├──date_util.py
│   │   │   ├──calculate_base_salary.py
│   │   │   ├──calculate_worked_days.py
│   │   │   └──calculate_worked_days.py
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
│       ├──dto
│       │   └──worker_input.py
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

## ▶️ How to run

#### Prior to Execution
If you wish to modify the file, you should replace the file located at /input/jefrey.json with another file that aligns with your preferences.

### Via Local

Run the CLI with:

```bash
python main.py --json input/jefrey.json
```

### Via Dockerfile

```bash
# Build image
docker build -t worker_cli_app .

# Run container
docker run --rm worker_cli_app --json input/jefrey.json
```

#### Via DockerCompose
```bash
# Build image
docker-compose build

# Run container
docker-compose run --rm worker_cli --json input/jefrey.json
```


---

## ▶️ Usage

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
    "2023-04-12",
    "2023-04-15"
  ]
}
```


### Example Output

```json
{
        "empleado": "Jefrey Padilla",
        "periodo_calculo": "primer_semestre",
        "salario_base_prima": 3100000,
        "dias_trabajados_semestre": 118,
        "prima_bruta": 863013.70,
        "renta_exenta_25_por_ciento": 215753.42,
        "base_gravable_impuesto": 647260.28,
        "impuesto_retenido": 0,
        "prima_neta": 863013.70
    }
```

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

## ⚙️ Dependencies
This application was developed using Python version 3.9.

---

## Metadata
/docs: This directory contains an ADR to validate each technical decision.

---

## 🚀 Additional (for developers)

### Check code style
```bash
flake8 service_bonus/
```

### Auto-format code
```bash
black service_bonus/
```

### Sort imports
```bash
isort service_bonus/
```

---

## 🚀 Future Improvements

- Add persistence (e.g., save/load workers from DB or JSON file).  
- Add multiple bonus calculation strategies.  
- Add a REST API (FastAPI) or GUI interface.  
- Package as a Python library with `pip install`. 
- Improving all business logic

---

## Take a look
For further information, please refer to the GitHub repository at https://github.com/ingjefreypadilla/serviceBonus. 
This repository meticulously separates each commit and conducts thorough testing.