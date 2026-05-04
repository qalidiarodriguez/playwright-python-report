from playwright.sync_api import sync_playwright


def test_web_josh():
    with sync_playwright() as p:
        # headless=False para ver el navegador
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        
        print("Abriendo la página de Joshua Garcia...")
        page.goto("https://joshuagarciia.myportfolio.com/work")
        
        title = page.title()
        print(f"Título de la página: {title}")
        
        # Esperar un poco para poder ver la página cargada
        page.wait_for_timeout(3000)
        
        assert "Joshua Garcia" in title or "Portfolio" in title
        print("✓ Test Passed!")
        
        browser.close()
        print("Navegador cerrado.")


if __name__ == "__main__":
    test_web_josh()
