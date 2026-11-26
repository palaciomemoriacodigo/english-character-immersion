# Local English learning analytics

Optional; not required to use ChatGPT. Python 3.12 is used by CI, and the script uses only the standard library.

1. Export your session CSVs using `Feedback now` or confirm a report after a farewell.
2. Save them in a private folder **outside the Git repository**, with filenames `Session_Errors_*.csv`.
3. From the extracted installation package or repository root, run:

```bash
python analytics/analizar_errores.py --input "/path/to/private/reports" --output "/path/to/private/results"
```

On Windows, replace the example paths with your own quoted paths.

Outputs: `Historico_errores.csv` (observations), `Resumen_por_categoria.csv` (counts by category), `Patrones_por_regla.csv` (rules and distinct sessions), and `Resumen_historico.md` (summary).

Errors and naturalness suggestions are separate. Identical rows are deduplicated. Invalid schema or values raise an error. Counts alone do not measure CEFR or improvement because the amount of language practised is not recorded. Empty exports cannot identify a session. Keep all inputs and results private; this tool does not upload data.
