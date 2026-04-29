from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        # headless=False para ver el navegador
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        
        print("Abriendo Google...")
        page.goto("https://www.google.com")
        
        title = page.title()
        print(f"Título de la página: {title}")
        
        # Esperar un poco para que puedas ver la página
        page.wait_for_timeout(3000)
        
        assert "Google" in title
        print("✓ Test Passed!")
        
        browser.close()
        print("Navegador cerrado.")

if __name__ == "__main__":
    test_google()        