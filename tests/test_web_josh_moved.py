def test_web_josh(page):
    print("Abriendo la página de Joshua Garcia...")
    page.goto("https://joshuagarciia.myportfolio.com/work", wait_until="domcontentloaded")
    title = page.title()
    print(f"Título de la página: {title}")
    page.wait_for_timeout(500)
    assert "Joshua Garcia" in title or "Portfolio" in title
    print("✓ Test Passed!")
