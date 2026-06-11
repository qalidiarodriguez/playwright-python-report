"""
Conftest para Pytest que proporciona el fixture `page` usando Playwright.

Usamos fixtures para centralizar setup/teardown y facilitar la reutilización
entre tests. Esto evita duplicación y hace los tests más fáciles de mantener.
"""

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def _playwright():
    """Inicializa Playwright una vez por sesión de tests."""
    pw = sync_playwright().start()
    yield pw
    pw.stop()


@pytest.fixture(scope="session")
def browser(_playwright):
    """Lanza el navegador Chromium en modo headless (una vez por sesión)."""
    browser = _playwright.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    """Crea un contexto y una nueva página por cada test y la limpia al final.

    Usar este fixture evita instanciar manualmente browser/context/page en cada test.
    """
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
