# Introducción

Esta guía está dirigida a personas que están empezando en QA Automation y quieren aprender Playwright con Python y Pytest.

## Qué es Playwright
Playwright es una herramienta de automatización de navegadores que permite controlar Chromium, Firefox y WebKit. Se usa para crear tests end-to-end que interactúan con páginas web.

## Qué es Pytest
Pytest es un framework de testing para Python que facilita descubrir y ejecutar tests, manejar aserciones y soporta fixtures para setup/teardown.

## Por qué se usan juntos
Playwright provee las APIs para automatizar navegadores, y Pytest proporciona la estructura para organizar y ejecutar tests de forma reproducible y escalable.

# Cómo ejecutar este proyecto

1. Clonar el repositorio:

```bash
git clone <repo-url>
cd playwright-python-report
```

2. Crear y activar un entorno virtual:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
pip install playwright
playwright install
```

4. Ejecutar los tests:

```bash
pytest -q
```

# Estructura del proyecto

- `tests/`: carpeta donde están todos los tests. Facilita descubrimiento y organización.
- `conftest.py`: archivo donde se definen fixtures reutilizables (por ejemplo `page`).
- `README.md`: documentación del proyecto.
- `.gitignore`: lista de archivos/dir que no deben subirse a Git.

# Buenas prácticas implementadas

- Fixtures: se centraliza la creación y cierre de navegadores/contextos/páginas.
- Reutilización de código: evitar duplicar setup/teardown en cada test.
- Snake case: nombres de archivos y funciones siguen la convención Python.
- Organización de carpetas: separar tests en `tests/` y mantener código adicional fuera.
- Uso de Pytest: tests descubiertos automáticamente, fáciles de ejecutar y ampliar.

# Cómo mejorar este proyecto

## Próximos pasos para seguir aprendiendo

- Page Object Model (POM): separar selectores y acciones en clases para mejorar mantenimiento.
- Data Driven Testing: parametrizar tests con múltiples conjuntos de datos.
- CI/CD con GitHub Actions: ejecutar tests automáticamente en cada push/PR.
- Reportes avanzados: integrar Allure u otros reportes HTML.
- Testing cross-browser: ejecutar la suite en Chromium, Firefox y WebKit.

# Cómo usar IA para aprender QA Automation

Los asistentes de IA (por ejemplo GitHub Copilot o ChatGPT) pueden ayudarte a:

- Entender código: pedir explicaciones de funciones y fixtures.
- Refactorizar tests: sugerir mejoras y aplicar patrones como POM.
- Aprender Playwright: generar ejemplos y snippets para acciones comunes.
- Aprender Pytest: ejemplos de fixtures, parametrización y hooks.
- Generar ejemplos: pedir tests de ejemplo para páginas concretas.
- Revisar buenas prácticas: solicitar checklist de revisión técnica.

Ejemplos de prompts útiles:

- "Explícame qué hace este test y cómo mejorarlo: <pega código>"
- "Genera un Page Object para esta página que tenga métodos para login y logout."
- "Refactoriza este test para usar fixtures y POM."
- "Dame una pipeline de GitHub Actions para ejecutar pytest y publicar reportes Allure."

# Aprendizajes obtenidos durante este proyecto

- Una revisión técnica ayuda a estandarizar nombres, estructura y prácticas.
- El feedback iterativo mejora la legibilidad y el valor educativo del repositorio.
- Implementar fixtures y organizar tests facilita el aprendizaje para quienes entran al proyecto.

---

Gracias por usar esta guía. ¡Sigue practicando y mejorando tus tests!
