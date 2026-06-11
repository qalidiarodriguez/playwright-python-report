"""
Ejemplo básico de Playwright con Python
Este archivo contiene un test de ejemplo para comenzar a usar Playwright
"""

# Este test usa el fixture `page` definido en `conftest.py`.
# Evita usar `sync_playwright()` dentro de pytest para prevenir conflictos con el loop asincrónico.

def test_ejemplo(page):
    """Navega a example.com usando el fixture `page`."""
    page.goto("https://example.com")
    titulo = page.title()
    assert "Example Domain" in titulo
