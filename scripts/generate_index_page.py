# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

atasehir_rows = json.loads((ROOT / "data" / "generated_index.json").read_text(encoding="utf-8"))
kadikoy_rows = json.loads((ROOT / "data" / "kadikoy_generated_index.json").read_text(encoding="utf-8"))


def render_group(title, rows):
    items_html = []
    for r in rows:
        badge = ' <span class="badge">mevcut sitesi var</span>' if r["has_existing_website"] else ""
        items_html.append(f"""
      <li>
        <a href="./{r['slug']}/">{r['name']}</a>{badge}
        <span class="phone">{r['phone'] or '-'}</span>
      </li>""")
    return f"""
  <h2>{title}</h2>
  <ul>{''.join(items_html)}
  </ul>"""


groups_html = render_group("Ataşehir", atasehir_rows) + render_group("Kadıköy", kadikoy_rows)
total = len(atasehir_rows) + len(kadikoy_rows)

html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Esnaf Siteleri</title>
<style>
  body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;max-width:720px;margin:0 auto;padding:32px 20px;color:#111827;}}
  h1{{font-size:1.5rem;margin-bottom:8px;}}
  h2{{font-size:1.1rem;margin:28px 0 12px;color:#1442ad;}}
  p.sub{{color:#6b7280;margin-bottom:24px;}}
  ul{{list-style:none;padding:0;}}
  li{{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:12px 14px;border:1px solid #e5e7eb;border-radius:10px;margin-bottom:10px;}}
  a{{color:#1a56db;text-decoration:none;font-weight:600;}}
  a:hover{{text-decoration:underline;}}
  .phone{{color:#6b7280;font-size:.9rem;white-space:nowrap;}}
  .badge{{background:#fef3c7;color:#92400e;font-size:.72rem;padding:2px 8px;border-radius:999px;margin-left:6px;}}
</style>
</head>
<body>
  <h1>Esnaf Elektrikçi Siteleri</h1>
  <p class="sub">{total} firma için oluşturulmuş örnek tanıtım siteleri.</p>
  {groups_html}
</body>
</html>
"""

(ROOT / "index.html").write_text(html, encoding="utf-8")
print("index.html written")
