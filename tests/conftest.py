# tests/conftest.py — pytest config
def pytest_configure(config):
    config.option.htmlpath = "report.html"
