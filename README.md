# Playwright-Python-tests - Automated Testing with Playwright & Python

![GitHub stars](https://img.shields.io/github/stars/hbkandhi12/playwright-python-tests?style=social)
![GitHub forks](https://img.shields.io/github/forks/hbkandhi12/playwright-python-tests?style=social)
![GitHub issues](https://img.shields.io/github/issues/hbkandhi12/playwright-python-tests)

Automate your web testing using **Playwright** and **Python**. This project provides end-to-end testing capabilities with **pytest** and **Playwright** for modern web applications.

---

## 🚀 Features
- ✅ **Fast & Reliable Browser Automation** with Playwright
- ✅ **Headless Mode** for running tests in the background
- ✅ **Cross-Browser Support** (Chromium, Firefox, WebKit)
- ✅ **Easy Configuration** using `pytest`
- ✅ **Parallel Test Execution**
- ✅ **Allure Reports for Test Insights**

---

## 📌 Prerequisites
Make sure you have the following installed:
- Python 3.7+
- Node.js (for Playwright CLI)
- `poetry` package manager

---

## ⚙️ Installation
Clone the repository and install dependencies:
```bash
# Clone the repository
git clone https://github.com/hbkandhi12/playwright-python-tests.git
cd playwright-python-tests

# Install dependencies using Poetry
poetry install

# Install Playwright browsers
poetry run playwright install
```

---

## 🚀 Running Tests
Run Playwright tests using `pytest`:
```bash
poetry run pytest --headed  # Runs tests with a visible browser
poetry run pytest --headless  # Runs tests in headless mode (faster)
```

Run tests in parallel:
```bash
poetry run pytest -n auto  # Runs tests in parallel using multiple CPU cores
```

Generate an **Allure Report**:
```bash
poetry run pytest --alluredir=allure-results
poetry run allure generate allure-results -o allure-report --clean
```
You can view the latest test results in the [Allure Test Report]
```bash
## Build Status

![Build Status](https://img.shields.io/github/workflow/status/hbkandhi12/playwright-python-tests/Playwright%20-%20Pytest%20automation%20suite)

## Allure Test Report

You can view the latest test results in the [Allure Test Report](https://hbkandhi12.github.io/playwright-python-tests/allure-report/).

```
---

## 📁 Project Structure
```
playwright-python-tests/
│── tests/
│   ├── test_login.py       # Login page test cases
│   ├── test_checkout.py    # Checkout workflow tests
│
│── pages/
│   ├── login_page.py       # Page Object Model for login page
│   ├── inventory_page.py   # Page Object Model for inventory
│
│── conftest.py             # Pytest fixtures
│── pyproject.toml          # Poetry configuration file
│── README.md               # Project documentation
```

---

## 🛠️ GitHub Actions for Allure Reports
To automatically generate and deploy **Allure Reports** on GitHub Pages, add the following **GitHub Actions workflow**:

Create `.github/workflows/allure-report.yml` and add:
```yaml
name: Playwright Tests & Allure Report

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Poetry
        run: pip install poetry

      - name: Install dependencies
        run: poetry install

      - name: Install Playwright browsers
        run: poetry run playwright install

      - name: Run tests and generate Allure results
        run: poetry run pytest --alluredir=allure-results

      - name: Generate Allure Report
        run: |
          poetry run allure generate allure-results -o allure-report --clean

      - name: Deploy Allure Report to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./allure-report
```

Make sure GitHub Pages is enabled in your repo settings under **Settings > Pages** and set it to deploy from `gh-pages` branch.

---

## 🛠️ Contributing
Want to improve this project? Contributions are welcome! 🚀

### Steps to Contribute:
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a **Pull Request**

---

## 📢 Community & Support
Have a question or feature request? **Create an issue** or start a **GitHub discussion**!

- 📌 **Issues**: [Submit here](https://github.com/hbkandhi12/playwright-python-tests/issues)
- 💬 **Discussions**: [Join here](https://github.com/hbkandhi12/playwright-python-tests/discussions)

---

## 📜 License
This project is licensed under the **MIT License**.

---

### ⭐ If you find this project helpful, please give it a **star** to support development! ⭐

