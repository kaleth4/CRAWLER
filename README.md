# 🕷️ WebCrawler — Recon Tool for Web Pentesting

```
 ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗
██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝
```

> **Web reconnaissance tool** — Crawling inteligente de aplicaciones web para pentesting autorizado.  
> Basado en buenas prácticas **OWASP** para reconocimiento y enumeración.

---

## ⚡ Uso rápido

```bash
python CRAWLER.py https://objetivo.com/
```

---

## 🚀 Instalación

```bash
pip install beautifulsoup4
pip install lxml
pip install html5lib
```

> Requisito base: `requests` (incluido en la mayoría de entornos Python estándar)

---

## 🔧 Características

| Feature | Descripción |
|---|---|
| 🔁 Crawling recursivo | Sigue todos los enlaces internos dentro del dominio objetivo |
| 🍪 Cookies & sesiones | Soporta crawling autenticado y flujos de sesión complejos |
| 📋 Detección de formularios | Enumera formularios GET y POST con sus campos |
| 🔍 Extracción de parámetros | Identifica parámetros en query strings |
| 🎯 Control de scope | Respeta estrictamente el dominio objetivo |
| 🧩 Headers personalizados | Configura headers y cookies para distintos roles |
| 📏 Control de profundidad | Define hasta dónde llega el crawling |

---

## 🏗️ Arquitectura

```
CRAWLER.py
├── Scope Validator       → Valida que cada URL pertenezca al dominio objetivo
├── URL Manager           → Set de URLs visitadas para evitar bucles infinitos
├── HTTP Engine           → requests — manejo de sesiones y cookies
├── HTML Parser           → BeautifulSoup — extracción de enlaces y formularios
├── Endpoint Analyzer     → Detecta parámetros, métodos HTTP y campos input
└── URL Normalizer        → Normalización para eliminar duplicados
```

---

## 🎯 Casos de uso en pentesting

```
✔  Descubrimiento de endpoints ocultos
✔  Mapeo completo de superficie de ataque
✔  Recolección de parámetros para fuzzing
✔  Identificación de formularios sensibles
✔  Base para automatizar pruebas OWASP Top 10
```

---

## 🛡️ Detección de vectores

El crawler identifica puntos de entrada potenciales para:

- **XSS** — Parámetros en query string y campos de formulario
- **SQL Injection** — Entradas sin sanitización visible
- **IDOR** — Parámetros de referencia a objetos
- **CSRF** — Formularios sin tokens visibles
- **Auth Bypass** — Rutas con restricción de acceso

---

## 📌 Roadmap

- [ ] JavaScript rendering (Playwright / Selenium)
- [ ] Exportación a JSON / formato compatible con Burp Suite
- [ ] Integración con wordlists
- [ ] Detección de tecnologías (stack fingerprinting)
- [ ] Rate limiting inteligente

---

## ⚠️ Disclaimer

> Esta herramienta es exclusivamente para uso en **entornos autorizados**.  
> El crawling sin autorización puede ser ilegal. Úsala únicamente contra sistemas que tengas permiso explícito de auditar.

---

## 📚 Referencias

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
