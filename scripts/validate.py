"""Validate configuration, schemas and empty public state templates."""
from pathlib import Path
import csv, hashlib, json, re
ROOT = Path(__file__).resolve().parents[1]
MODULES = ['00_Character_Immersion_Protocol.md','01_Lelouch_Character_Profile.md','02_Sunny_Character_Profile.md','03_Nephis_Character_Profile.md','04_Izaya_Character_Profile.md','05_Roxas_Character_Profile.md','06_Character_Relationships.md','07_English_Learning_Progress.md','08_English_Error_Tracking.md','09_Shadow_Slave_RPG_Campaign.md']
TEMPLATES = ['Session_Review_TEMPLATE.md','Session_Errors_TEMPLATE.csv','Campaign_Checkpoint_TEMPLATE.md']
FIELDS = 'session_id,date,character,activity,feedback_mode,source,record_type,category,rule_id,original,corrected,explanation_es,occurrences,priority,confidence,practice_prompt'.split(',')
def validate():
    prompt = (ROOT/'config/PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
    assert len(prompt)<=8000, 'Prompt exceeds project design budget'
    for name in MODULES:
        assert (ROOT/'modules'/name).is_file() and name in prompt, name
    for name in TEMPLATES: assert (ROOT/'templates'/name).is_file(), name
    with (ROOT/'templates/Session_Errors_TEMPLATE.csv').open(encoding='utf-8-sig',newline='') as f:
        assert list(csv.reader(f)) == [FIELDS], 'CSV template must have only the exact header'
    for name, digest in json.loads((ROOT/'scripts/public_state_hashes.json').read_text()).items():
        assert hashlib.sha256((ROOT/'modules'/name).read_bytes()).hexdigest()==digest, f'Public state template changed: {name}. Review and reset before updating hash.'
    assert re.fullmatch(r'\d+\.\d+\.\d+(?:-[\w.-]+)?', (ROOT/'VERSION').read_text().strip())
    print(f'Validation passed; instruction length: {len(prompt)} characters.')
if __name__ == '__main__': validate()
