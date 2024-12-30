# upload-service

## How to run application
- pip install pipenv
- pipenv install
- pipenv shell
- pipenv install uvicorn --dev
- pipenv run uvicorn main:app --reload --port 4002

## Data migration
- Create migration script: `alembic revision --autogenerate -m "Your migration message"`
- Apply migration script: `alembic upgrade head`
- Revert migration script: `alembic downgrade -1`