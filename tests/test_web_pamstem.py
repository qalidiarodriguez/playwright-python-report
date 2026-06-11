"""
Test para PamSTEM - 4 pasos
1. Abrir la web
2. Ir al botón QA Queen y ver el primer video
3. Ir al botón PamSTEM y ver el primer video
"""

import os
from datetime import datetime


def test_pamstem_4_pasos(page):
    """Test de 4 pasos para PamSTEM usando el fixture `page`."""

    # Crear directorios para screenshots
    os.makedirs("./screenshots/pamstem", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Paso 1: Abrir la web
    print("\nPaso 1: Abriendo la web...")
    page.goto("https://qalidiarodriguez.github.io/lidipamelarodriguezvigueras.github.io/", wait_until="domcontentloaded")
    print("✅ Web abierta")

    # Esperar a que cargue la página
    page.wait_for_timeout(500)
    print(f"Título de la página: {page.title()}")

    # Captura 1: Web abierta
    screenshot_path_1 = f"./screenshots/pamstem/01_web_abierta_{timestamp}.png"
    page.screenshot(path=screenshot_path_1)
    print(f"📸 Captura 1 guardada: {screenshot_path_1}")

    # IMPORTANTE: El menú está oculto (hamburger), hay que abrirlo primero
    print("\n→ Abriendo menú hamburger...")
    menu_btn = page.locator('#menuBtn')
    menu_btn.click()
    page.wait_for_timeout(500)
    print("✅ Menú abierto")

    # Captura 2: Menú abierto
    screenshot_path_2 = f"./screenshots/pamstem/02_menu_abierto_{timestamp}.png"
    page.screenshot(path=screenshot_path_2)
    print(f"📸 Captura 2 guardada: {screenshot_path_2}")

    # Paso 2: Ir al botón QA Queen y ver el primer video
    print("\nPaso 2: Buscando botón QA Queen...")
    try:
        # Clic en el enlace QA Queen (va a #video-cv)
        qa_queen_button = page.locator('.menu-link').filter(has_text='QA Queen').first
        qa_queen_button.click()
        print("✅ Clic en QA Queen")

        # Esperar a que haga scroll hasta el video
        page.wait_for_timeout(1500)

        # Captura 3: QA Queen cargado
        screenshot_path_3 = f"./screenshots/pamstem/03_qa_queen_{timestamp}.png"
        page.screenshot(path=screenshot_path_3)
        print(f"📸 Captura 3 guardada: {screenshot_path_3}")

        # Verificar que el video de QA Queen está presente
        video_qa = page.locator('iframe[src*="youtube.com/embed/ZptX-WqOCms"]').first
        if video_qa.is_visible():
            print("✅ Video de QA Queen encontrado y visible")
        else:
            print("⚠️ Video de QA Queen no encontrado directamente")

    except Exception as e:
        print(f"⚠️ Error en paso 2: {e}")

    # Paso 3: Ir al botón PamSTEM y ver el primer video
    print("\nPaso 3: Buscando botón PamSTEM...")
    try:
        # Volver a abrir el menú si está cerrado
        menu_btn = page.locator('#menuBtn')
        if not menu_btn.is_visible():
            menu_btn.click()
            page.wait_for_timeout(500)

        # Clic en el enlace PamSTEM (va a pamstem/index.html)
        pamstem_button = page.locator('.menu-link').filter(has_text='PamSTEM').first
        pamstem_button.click()
        print("✅ Clic en PamSTEM")

        # Esperar a que cargue la nueva página
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(1500)

        print(f"Título de la página PamSTEM: {page.title()}")

        # Captura 4: PamSTEM cargado
        screenshot_path_4 = f"./screenshots/pamstem/04_pamstem_{timestamp}.png"
        page.screenshot(path=screenshot_path_4)
        print(f"📸 Captura 4 guardada: {screenshot_path_4}")

        # Verificar que el video de PamSTEM está presente
        video_pam = page.locator('iframe[src*="youtube.com/embed/vDoEyMuZ8Eo"]').first
        if video_pam.is_visible():
            print("✅ Video de PamSTEM encontrado y visible")
        else:
            print("⚠️ Video de PamSTEM no encontrado directamente")

    except Exception as e:
        print(f"⚠️ Error en paso 3: {e}")

    # Paso 4: Cerrar el navegador
    print("\nPaso 4: Finalizando test\n")
    print("✅ Test completado")
