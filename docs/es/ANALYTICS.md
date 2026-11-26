# Análisis local de aprendizaje

Es opcional: no necesitas Python para conversar en ChatGPT. La versión de Python utilizada en CI es 3.12 y el script solo utiliza la biblioteca estándar.

1. Exporta tus CSV con `Feedback now` o confirma el informe tras despedirte.
2. Guárdalos en una carpeta privada **fuera del repositorio Git**, con nombres `Session_Errors_*.csv`.
3. Desde la carpeta del repositorio o el ZIP descomprimido, ejecuta:

```powershell
python analytics/analizar_errores.py --input "C:\EnglishPrivate\reportes" --output "C:\EnglishPrivate\resultados"
```

Sustituye las rutas de ejemplo por tus rutas reales.

| Resultado | Contenido |
| --- | --- |
| Historico_errores.csv | Observaciones acumuladas |
| Resumen_por_categoria.csv | Frecuencias por categoría |
| Patrones_por_regla.csv | Reglas y número de sesiones distintas |
| Resumen_historico.md | Resumen de resultados |

Los errores y las mejoras de naturalidad se contabilizan por separado. Se eliminan filas exactamente duplicadas y se comprueba el esquema. Los recuentos no demuestran por sí mismos evolución ni nivel CEFR, porque no conocemos el volumen total de práctica. Un CSV vacío no identifica una sesión. El script no sube datos a Internet; conserva entradas y resultados en privado.
