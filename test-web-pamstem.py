"""
Test para PamSTEM - 4 pasos
1. Abrir la web
2. Ir al botón QA Queen y ver el primer video
3. Ir al botón PamSTEM y ver el primer video
"""

from playwright.sync_api import sync_playwright

def test_pamstem_4_pasos():
    """Test de 4 pasos para PamSTEM"""
    
    with sync_playwright() as p:
        # Paso 1: Abrir la web
        print("Paso 1: Abriendo la web...")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://qalidiarodriguez.github.io/lidipamelarodriguezvigueras.github.io/")
        print("✅ Web abierta")
        
        # Esperar a que cargue la página
        page.wait_for_load_state("domcontentloaded")
        print(f"Título de la página: {page.title()}")
        
        # IMPORTANTE: El menú está oculto (hamburger), hay que abrirlo primero
        print("\n→ Abriendo menú hamburger...")
        menu_btn = page.locator('#menuBtn')
        menu_btn.click()
        page.wait_for_timeout(500)
        print("✅ Menú abierto")
        
        # Paso 2: Ir al botón QA Queen y ver el primer video
        print("\nPaso 2: Buscando botón QA Queen...")
        try:
            # Clic en el enlace QA Queen (va a #video-cv)
            qa_queen_button = page.locator('.menu-link').filter(has_text='QA Queen').first
            qa_queen_button.click()
            print("✅ Clic en QA Queen")
            
            # Esperar a que haga scroll hasta el video
            page.wait_for_timeout(1500)
            
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
            
            # Verificar que el video de PamSTEM está presente
            video_pam = page.locator('iframe[src*="youtube.com/embed/vDoEyMuZ8Eo"]').first
            if video_pam.is_visible():
                print("✅ Video de PamSTEM encontrado y visible")
            else:
                print("⚠️ Video de PamSTEM no encontrado directamente")
            
        except Exception as e:
            print(f"⚠️ Error en paso 3: {e}")
        
        # Paso 4: Cerrar el navegador
        print("\nPaso 4: Cerrando navegador...")
        browser.close()
        print("✅ Test completado")

if __name__ == "__main__":
    test_pamstem_4_pasos()