# Web de instalación

La [landing bilingüe](https://palaciomemoriacodigo.github.io/english-character-immersion/) es la entrada recomendada. Ofrece seis pasos ilustrados, copia directa, descarga de una fuente, progreso local y ayuda. No conecta con la cuenta de ChatGPT.

## Probar cambios

Desde la raíz del repositorio:

```bash
python scripts/privacy_check.py
python scripts/build.py
python scripts/privacy_check.py --generated
```

Abre `dist/start/index.html` o `en.html`. La copia tiene alternativa manual. Las ejecuciones de Validate para PR y main conservan una vista previa `landing-preview` y capturas `landing-browser-review` durante tres días. En un repositorio público estos artefactos no son privados. No subas datos reales. Las pruebas Chromium comprueban la instalación web, no la recuperación de fuentes o las conversaciones dentro de ChatGPT.

## Publicar una actualización

1. Completar la [lista de revisión](../../MAINTAINER_CHECKLIST.md), incluidos derechos y privacidad; no confundir visibilidad pública con autorización.
2. Confirmar que Settings > Pages usa GitHub Actions. Mantener PUBLIC_RELEASE_APPROVED=true únicamente si la revisión de distribución está aprobada.
3. Ejecutar Publish approved landing en main con la confirmación PUBLISH. El workflow valida y analiza los archivos antes de publicar únicamente dist/start/.
4. Comprobar build y deploy, abrir la URL desde una ventana privada y probar descargas y copia en HTTPS.

No hay publicación automática por push. El usuario actualiza su proyecto manualmente. La [guía oficial de Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) explica la configuración.
