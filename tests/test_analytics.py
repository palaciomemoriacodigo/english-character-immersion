import csv, tempfile, unittest
from pathlib import Path
from analytics.analizar_errores import analyze,FIELDS
class AnalyticsTests(unittest.TestCase):
    def test_counts_and_duplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); inp=root/'input'; inp.mkdir(); out=root/'output'
            row=dict.fromkeys(FIELDS,'example'); row.update(session_id='synthetic-1',record_type='error',category='prepositions',rule_id='PREP_DEPEND_ON',occurrences='2',confidence='high')
            other=dict(row,record_type='naturalness',occurrences='1')
            with (inp/'Session_Errors_demo.csv').open('w',newline='',encoding='utf-8') as f:
                w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows([row,row,other])
            self.assertEqual(analyze(inp,out),(2,1))
            self.assertTrue((out/'Patrones_por_regla.csv').exists())
    def test_invalid_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'Session_Errors_invalid.csv').write_text('bad\n')
            with self.assertRaises(ValueError): analyze(root,root/'out')
