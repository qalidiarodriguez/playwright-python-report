import os
from datetime import datetime


def test_google(page):
    # Crear directorios para screenshots (no grabamos video desde pytest fixture)
    os.makedirs("./screenshots/google", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    print("\nAbriendo Google...")
    page.goto("https://www.google.com", wait_until="domcontentloaded")

    # Captura 1: Página cargada
    screenshot_path_1 = f"./screenshots/google/01_pagina_cargada_{timestamp}.png"
    page.screenshot(path=screenshot_path_1)
    print(f"📸 Captura 1 guardada: {screenshot_path_1}")

    title = page.title()
    print(f"Título de la página: {title}")

    # Esperar un poco para que puedas ver la página (si corres en modo no-headless)
    page.wait_for_timeout(1000)

    # Captura 2: Antes de cerrar
    screenshot_path_2 = f"./screenshots/google/02_antes_cerrar_{timestamp}.png"
    page.screenshot(path=screenshot_path_2)
    print(f"📸 Captura 2 guardada: {screenshot_path_2}")

    assert "Google" in title
    print("✓ Test Passed!")
