# Desarrollo y mantenimiento

[Volver al README](../README.md) · [Web de instalación](https://palaciomemoriacodigo.github.io/english-character-immersion/) · [Guía de despliegue](es/LANDING.md)

La experiencia recomendada es la landing bilingüe y una sola fuente de ChatGPT. No se necesita Python para utilizar el proyecto. Los módulos separados se mantienen como fuentes de desarrollo y permiten mejorar o corregir personajes de forma independiente.

## Estructura

| Ruta | Finalidad |
| --- | --- |
| config/ | Instrucciones originales del proyecto |
| modules/ | Perfiles, protocolo, progreso, correcciones y RPG |
| templates/ | Plantillas vacías de informes y checkpoints |
| empezar/ | Dos archivos generados y disponibles como alternativa a la web |
| site/ | Plantilla HTML, tema CSS compartido, traducciones y página legal |
| docs/ | Guías, seis ilustraciones de instalación y portadas |
| scripts/ | Generación y validación |
| tests/ | Pruebas estructurales, conversacionales y de navegador |
| analytics/ | Herramienta Python opcional de análisis de errores |
| .github/ | Validación, publicación de versiones y Pages |

## Desarrollo local

Python 3.12, biblioteca estándar para generar los archivos:

```bash
python scripts/privacy_check.py
python scripts/validate.py
python -m unittest discover -s tests
python scripts/build.py
python scripts/privacy_check.py --generated
```

Abre `dist/start/index.html`. El comando genera únicamente el ZIP Empezar y la web. Tras cambiar instrucciones, módulos o plantillas, ejecuta `python scripts/sync_start.py` y confirma los dos archivos generados de `empezar/`. CI comprueba que son idénticos a los de la web. No los edites directamente.

La comprobación preventiva de privacidad no cubre todo el historial ni los píxeles de las imágenes; revisa también los datos personales manualmente. Los artefactos de Actions de un repositorio público no son privados.

La validación de navegador utiliza Playwright y Chromium; consulta `tests/browser_landing.py` y el workflow Validate. No demuestra el comportamiento conversacional de ChatGPT: consulta [pruebas manuales](../tests/CONVERSATIONAL_TESTS.md).

## Opciones avanzadas

Si necesitas diagnosticar la recuperación de fuentes por separado, ejecuta `python scripts/build.py --advanced`. Genera también los paquetes Full (13 fuentes) y Lite (5 fuentes). No mezcles ediciones. [Instalación avanzada ES](es/INSTALLATION.md) · [EN](en/INSTALLATION.md).

El análisis de CSV es opcional: [guía ES](es/ANALYTICS.md) · [EN](en/ANALYTICS.md). Guarda informes y resultados fuera de Git.

## Versionado y publicación

Consulta [lista de comprobación](../MAINTAINER_CHECKLIST.md), [changelog](../CHANGELOG.md), [roadmap](../ROADMAP.md) y [contribuciones](../CONTRIBUTING.md). La web se actualiza mediante Publish approved landing; las releases publican únicamente el ZIP Empezar. Para una nueva versión aprobada, actualiza VERSION y CHANGELOG, ejecuta sync_start y las pruebas, confirma los cambios y crea una etiqueta coincidente con VERSION (por ejemplo, v2.2.0). No publiques etiquetas sin resolver privacidad y derechos. Las versiones candidatas son prereleases. Los usuarios actualizan sus proyectos manualmente.

[Privacidad](../PRIVACY.md) · [Derechos de terceros](../NOTICE.md) · [Alcance de licencias MIT y CC BY-NC 4.0](../LICENSE). Solo se licencia el material original incluido en ese alcance; la visibilidad pública no concede permisos de terceros.
