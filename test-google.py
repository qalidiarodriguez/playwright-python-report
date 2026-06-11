from playwright.sync_api import sync_playwright
import os
from datetime import datetime

def test_google():
    # Crear directorios para videos y screenshots
    os.makedirs("./videos", exist_ok=True)
    os.makedirs("./screenshots/google", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with sync_playwright() as p:
        # headless=False para ver el navegador
        # Agregar grabación de video
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(record_video_dir="./videos")
        page = context.new_page()
        
        print("\n🎬 Grabando video... (Google Test)")
        print("Abriendo Google...")
        page.goto("https://www.google.com")
        
        # Captura 1: Página cargada
        screenshot_path_1 = f"./screenshots/google/01_pagina_cargada_{timestamp}.png"
        page.screenshot(path=screenshot_path_1)
        print(f"📸 Captura 1 guardada: {screenshot_path_1}")
        
        title = page.title()
        print(f"Título de la página: {title}")
        
        # Esperar un poco para que puedas ver la página
        page.wait_for_timeout(3000)
        
        # Captura 2: Antes de cerrar
        screenshot_path_2 = f"./screenshots/google/02_antes_cerrar_{timestamp}.png"
        page.screenshot(path=screenshot_path_2)
        print(f"📸 Captura 2 guardada: {screenshot_path_2}")
        
        assert "Google" in title
        print("✓ Test Passed!")
        
        context.close()
        browser.close()
        print("Navegador cerrado.")
        print(f"🎥 Video guardado en: ./videos/")

# Eliminado `if __name__ == "__main__"` para permitir descubrimiento por pytest.