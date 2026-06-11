"""
Ejemplo básico de Playwright con Python
Este archivo contiene un test de ejemplo para comenzar a usar Playwright
"""

from playwright.sync_api import sync_playwright

def test_ejemplo():
    """Test de ejemplo que abre un navegador y navega a una página"""
    with sync_playwright() as p:
        # Lanzar navegador (puede ser chromium, firefox o webkit)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navegar a una URL
        page.goto("https://example.com")
        
        # Obtener el título de la página
        titulo = page.title()
        print(f"Título de la página: {titulo}")
        
        # Cerrar navegador
        browser.close()

# Eliminado `if __name__ == "__main__"` para permitir descubrimiento por pytest.