"""
Test combinado: Google + PamSTEM
Ejecuta ambos tests en un solo navegador
"""

def test_combinado(browser):
    """Ejecuta test-google y test-pamstem en secuencia usando el fixture `browser`."""
    # ===== TEST 1: GOOGLE =====
    print("=" * 50)
    print("TEST 1: GOOGLE")
    print("=" * 50)

    page = browser.new_page()

    # Abrir Google
    print("Abriendo Google...")
    page.goto("https://www.google.com", wait_until="domcontentloaded")
    page.wait_for_timeout(1000)

    title = page.title()
    print(f"Título: {title}")
    assert "Google" in title
    print("✅ Test Google Passed!")

    # Cerrar esta página pero mantener el navegador
    page.close()
    print("🔄 Cerrando pestaña de Google...\n")

    # ===== TEST 2: PAMSTEM =====
    print("=" * 50)
    print("TEST 2: PAMSTEM")
    print("=" * 50)

    # Crear nueva página en el mismo navegador
    page = browser.new_page()

    # Paso 1: Abrir la web
    print("Paso 1: Abriendo la web PamSTEM...")
    page.goto("https://qalidiarodriguez.github.io/lidipamelarodriguezvigueras.github.io/", wait_until="domcontentloaded")
    page.wait_for_timeout(500)
    print(f"Título: {page.title()}")
    print("✅ Web abierta")

    # Abrir menú hamburger
    print("\n→ Abriendo menú hamburger...")
    menu_btn = page.locator('#menuBtn')
    menu_btn.click()
    page.wait_for_timeout(500)
    print("✅ Menú abierto")

    # Paso 2: QA Queen
    print("\nPaso 2: Clic en QA Queen...")
    qa_queen_button = page.locator('.menu-link').filter(has_text='QA Queen').first
    qa_queen_button.click()
    page.wait_for_timeout(1500)
    print("✅ Clic en QA Queen")

    # Paso 3: PamSTEM
    print("\nPaso 3: Clic en PamSTEM...")
    # Volver a abrir el menú
    page.locator('#menuBtn').click()
    page.wait_for_timeout(500)

    pamstem_button = page.locator('.menu-link').filter(has_text='PamSTEM').first
    pamstem_button.click()
    page.wait_for_timeout(1500)
    print("✅ Clic en PamSTEM")

    print("\n" + "=" * 50)
    print("✅ TODOS LOS TESTS PASARON!")
    print("=" * 50)

    # Esperar un poco para ver el resultado
    page.wait_for_timeout(1000)

    print("\nFin de test combinado. (No cerramos el navegador; lo maneja el fixture)")
