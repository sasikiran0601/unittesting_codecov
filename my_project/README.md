# My Project

## Setup

Create and activate a local virtual environment before installing dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the tests with:

```powershell
pytest -v
pytest --cov=app --cov-report=term
```
