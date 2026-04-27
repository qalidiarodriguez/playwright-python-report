# 🎭 Playwright Python Report

Repositorio de pruebas automatizadas con Playwright y Python para sitios web de PamSTEM.

## 📋 Descripción

Este proyecto contiene tests automatizados para verificar el funcionamiento de los sitios web de **Lidia Pamela Rodríguez Vigueras** (QA Queen & Fundadora de PamSTEM).

## 🧪 Tests Incluidos

### 1. test-web-pamstem.py
Test de 4 pasos que verifica:
1. ✅ Abrir la web principal
2. ✅ Navegar al menú → QA Queen → ver primer video
3. ✅ Navegar al menú → PamSTEM → ver primer video
4. ✅ Cerrar navegador

### 2. test-python.py
Ejemplo básico de Playwright para aprender la estructura.

## 🚀 Cómo ejecutar los tests

### Prerrequisitos
```bash
# Instalar Playwright
pip install playwright

# Instalar navegadores
playwright install
```

### Ejecutar un test
```bash
python test-web-pamstem.py
```

### Ejecutar en modo headless (sin navegador visible)
```python
# Cambiar en el código:
browser = p.chromium.launch(headless=True)
```

## 📂 Estructura del proyecto

```
playwright-python-report/
├── test-web-pamstem.py    # Test principal de 4 pasos
├── test-python.py         # Ejemplo básico
└── README.md              # Este archivo
```

## 🔧 Tecnologías usadas

| Tecnología | Versión |
|------------|---------|
| Python | 3.12.4 |
| Playwright | 1.58.0 |
| Chromium | 145.0.7632.6 |
| Firefox | 146.0.1 |
| WebKit | 26.0 |

## 🌐 Sitios probados

- **Web principal**: [qalidiarodriguez.github.io/lidipamelarodriguezvigueras.github.io](https://qalidiarodriguez.github.io/lidipamelarodriguezvigueras.github.io/)
- **Sección PamSTEM**: [pamstem/index.html](https://qalidiarodriguez.github.io/lidipamelarodriguezvigueras.github.io/pamstem/index.html)

## 👩‍💻 Autora

**Lidia Pamela Rodríguez Vigueras**
- QA Engineer certificada
- Fundadora de PamSTEM
- QA Queen 👑

> "El cuidado también crea tecnología"

## 📝 Licencia

MIT License - Feel free to use and learn from this project!

---

⭐️ Si este proyecto te ayuda, dale una estrella en GitHub