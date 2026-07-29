# bdd-pytest-python

[![CI](https://github.com/selvamjstester/bdd-pytest-python/actions/workflows/ci.yml/badge.svg)](https://github.com/selvamjstester/bdd-pytest-python/actions/workflows/ci.yml)

**Behaviour-Driven Development** framework using **pytest-bdd** with **Gherkin** feature files. Covers both **Web UI** (Playwright, against [SauceDemo](https://www.saucedemo.com)) and **API** (requests, against [JSONPlaceholder](https://jsonplaceholder.typicode.com)).

> 🧑‍🎓 **New to coding or BDD?** Read **[LEARN.md](LEARN.md)** — a from-scratch guide to Gherkin, step definitions, and writing your own scenario.

## Highlights

- 🥒 **Gherkin** `.feature` files (`Scenario`, `Background`, `Scenario Outline` + `Examples`)
- 🔗 **Step definitions** with `parsers.parse` typed params
- 🌐 **Web** steps via Playwright + 🔌 **API** steps via requests — one BDD stack, two layers
- 🧺 **Shared `context`** fixture to pass state between steps
- 📊 **HTML report** + **GitHub Actions CI**

## Project structure

```
features/
├── login.feature        # Web UI scenarios
└── users_api.feature     # API scenarios
tests/
├── test_login_steps.py
└── test_users_api_steps.py
pytest.ini
```

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
```

## Running tests

```bash
pytest --browser chromium        # all scenarios
pytest tests/test_users_api_steps.py   # API scenarios only (no browser)
```

---
Part of my SDET portfolio. Demonstrates readable, business-facing BDD across UI and API.
