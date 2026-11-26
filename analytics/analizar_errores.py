"""Local, standard-library-only analysis of session CSV exports."""
import argparse, csv
from collections import Counter, defaultdict
from pathlib import Path
FIELDS = 'session_id,date,character,activity,feedback_mode,source,record_type,category,rule_id,original,corrected,explanation_es,occurrences,priority,confidence,practice_prompt'.split(',')
def analyze(input_dir, output_dir):
    files = sorted(Path(input_dir).glob('Session_Errors_*.csv'))
    if not files: raise ValueError('No Session_Errors_*.csv files found')
    rows, seen = [], set()
    for path in files:
        with path.open(encoding='utf-8-sig',newline='') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != FIELDS: raise ValueError(f'{path.name}: invalid header')
            for row in reader:
                if None in row or any(v is None for v in row.values()): raise ValueError(f'{path.name}: malformed row')
                if row['record_type'] not in {'error','naturalness'} or row['confidence'] not in {'medium','high'}: raise ValueError(f'{path.name}: invalid record type/confidence')
                if not row['session_id'] or not row['rule_id'] or not row['category']: raise ValueError(f'{path.name}: missing identifiers')
                if int(row['occurrences']) < 1: raise ValueError(f'{path.name}: invalid occurrences')
                key=tuple(row[k] for k in FIELDS)
                if key not in seen: rows.append(row); seen.add(key)
    categories=Counter(); rules=Counter(); sessions=defaultdict(set)
    for row in rows:
        n=int(row['occurrences']); typ=row['record_type']; cat=row['category']; rule=row['rule_id']
        categories[typ,cat]+=n; rules[typ,rule]+=n; sessions[typ,rule].add(row['session_id'])
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    def write(name, header, data):
        with (out/name).open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.writer(f); w.writerow(header); w.writerows(data)
    write('Historico_errores.csv',FIELDS,([row[k] for k in FIELDS] for row in rows))
    write('Resumen_por_categoria.csv',['record_type','category','occurrences'],([t,c,n] for (t,c),n in categories.most_common()))
    write('Patrones_por_regla.csv',['record_type','rule_id','occurrences','distinct_sessions'],([t,r,n,len(sessions[t,r])] for (t,r),n in rules.most_common()))
    errors=sum(n for (t,c),n in categories.items() if t=='error'); natural=sum(n for (t,c),n in categories.items() if t=='naturalness')
    (out/'Resumen_historico.md').write_text(f'# Resumen histórico\n\n- Archivos leídos: {len(files)}\n- Sesiones con observaciones: {len({r["session_id"] for r in rows})}\n- Errores: {errors}\n- Mejoras de naturalidad: {natural}\n\nSolo se cuentan observaciones disponibles; se eliminan filas exactamente duplicadas. Los archivos sin observaciones no identifican una sesión. No hay denominador de palabras u oportunidades de uso: los recuentos no miden por sí solos evolución ni CEFR.\n',encoding='utf-8')
    return errors,natural
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--input',required=True); p.add_argument('--output',required=True); a=p.parse_args()
    try: print('Errors / naturalness:',analyze(a.input,a.output))
    except (ValueError,OSError) as e: p.exit(1,f'Error: {e}\n')
