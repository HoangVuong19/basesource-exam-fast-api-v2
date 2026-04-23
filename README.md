- Create python venv (macos)

> /opt/homebrew/bin/python3.12 -m venv .venv

- Use venv

> . .venv/bin/activate

- Install libs

> pip3 install -r requirements.txt

- Dev run

> uvicorn main:app --reload

- Show swagger api docs

> http://localhost:8000/docs

- Run pytest

> pytest -v

- Run recovery report

> create folder tests/coverage

> pytest --cov=. --cov-report=html:tests/coverage --cov-config=.coveragerc

> open index.html
