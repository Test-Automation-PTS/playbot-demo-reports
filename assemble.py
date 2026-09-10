"""Present the public customer handoff under stable Allure/PDF URLs."""
import html
import json
import shutil
import sys
from pathlib import Path


def assemble(source, target):
    required = ('index.html', 'pdf/index.html', 'publication.json', 'history/history-trend.json')
    for name in required:
        if not (source/name).is_file():
            raise ValueError(f'Incomplete public report: {name}')
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    shutil.copytree(source, target/'allure', ignore=shutil.ignore_patterns('pdf', 'runs', 'publication.json'))
    shutil.copytree(source/'pdf', target/'pdf')
    if (source/'runs').is_dir():
        shutil.copytree(source/'runs', target/'runs')
    shutil.copyfile(source/'publication.json', target/'publication.json')
    (target/'.nojekyll').touch()
    publication=json.loads((source/'publication.json').read_text())
    number=publication['run_number']
    key=html.escape(publication['run_key'])
    commit=html.escape(publication['commit'])
    (target/'index.html').write_text(f'''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Playbot demo reports</title><style>
body{{font:16px system-ui;background:#f3f5fa;color:#20304b;margin:0}}main{{max-width:850px;margin:10vh auto;padding:30px}}h1{{font-size:38px}}p{{line-height:1.7;color:#5a6981}}nav{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:35px 0}}nav a{{padding:30px;background:white;border:1px solid #dbe2ec;border-radius:12px;text-decoration:none;color:#2455cc}}strong{{display:block;font-size:24px;margin-bottom:12px}}small{{overflow-wrap:anywhere}}@media(max-width:600px){{nav{{grid-template-columns:1fr}}}}
</style><main><p>PLAYBOT · PUBLIC DEMO RESULTS</p><h1>Test reports</h1><p>Two views of the same customer test run. Allure shows every module; the PDF dashboard adds document comparisons and redaction evidence.</p><nav><a href="allure/"><strong>Allure →</strong>All tests, steps, history and trends</a><a href="pdf/"><strong>PDF dashboard →</strong>PDF tests, steps, expected/actual and differences</a></nav><p>Latest published run: <b>#{number}</b> · {key}<br><small>Commit: {commit}</small></p><p><a href="https://github.com/Test-Automation-PTS/playbot-demo-customer/actions/runs/{key.split('-')[0]}">GitHub test run</a> · <a href="https://github.com/Test-Automation-PTS/playbot-demo-reports/tree/gh-pages">Published report files</a></p></main></html>''')


if __name__=='__main__':
    assemble(Path(sys.argv[1]),Path(sys.argv[2]))
