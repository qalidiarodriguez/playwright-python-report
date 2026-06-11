"""
Prueba de ejemplo demostrando buenas prácticas para Playwright + Pytest.

- Usa `snake_case` para el nombre del archivo y PEP8.
- Usa el fixture `page` para el manejo del navegador.
- No usa `if __name__ == "__main__"` — pytest descubre tests automáticamente.

Comentarios breves:
- Pytest Fixtures: permiten centralizar setup/teardown y compartir recursos entre tests.
- No usar `__main__`: los tests deben ser descubiertos y ejecutados por `pytest`.
- Beneficios: claridad, reutilización, menos código repetido y apto para portafolio.
"""

import re
from playwright.sync_api import expect


def test_ejemplo(page):
    """Navega a la web de Playwright y verifica el título contiene 'Playwright'."""
    # `page` es un fixture: evita crear manualmente browser/context/page en cada test.
    page.goto("https://playwright.dev/", wait_until="domcontentloaded", timeout=60000)

    # Usamos el título de la página para una comprobación rápida y estable.
    # `expect(page).to_have_title` es más fiable que el locator "title" en algunas páginas.
    expect(page).to_have_title(re.compile(r"Playwright"), timeout=10000)
