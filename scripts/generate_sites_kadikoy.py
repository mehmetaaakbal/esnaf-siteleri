# -*- coding: utf-8 -*-
import json
import re
import unicodedata
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "kadikoy_elektrikci.json"
TEMPLATE_FILE = ROOT / "_template" / "template.html"

TR_MAP = str.maketrans({
    "ç": "c", "Ç": "c", "ğ": "g", "Ğ": "g", "ı": "i", "İ": "i",
    "ö": "o", "Ö": "o", "ş": "s", "Ş": "s", "ü": "u", "Ü": "u",
})


def slugify(text: str) -> str:
    text = text.translate(TR_MAP)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "firma"


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    template = TEMPLATE_FILE.read_text(encoding="utf-8")

    year = str(datetime.now().year)
    rows = []
    seen_slugs = {}

    for item in data:
        name = (item.get("title") or "İsimsiz Firma").strip()
        phone = (item.get("phone") or "").strip()
        phone_raw = (item.get("phoneUnformatted") or phone).strip()
        address = (item.get("address") or "").strip()
        category = (item.get("categoryName") or "Elektrikçi").strip()
        score = item.get("totalScore")
        reviews = item.get("reviewsCount")
        website = (item.get("website") or "").strip()

        if score:
            puan = f"{score} / 5 ({reviews or 0} değerlendirme)"
        else:
            puan = "Henüz değerlendirme yok"

        base_slug = slugify(name)
        slug = base_slug if base_slug.startswith("kadikoy-") else f"kadikoy-{base_slug}"
        if slug in seen_slugs:
            seen_slugs[slug] += 1
            slug = f"{slug}-{seen_slugs[slug]}"
        else:
            seen_slugs[slug] = 1

        has_existing_website = bool(website)

        # baseline placeholder site for every firm (overwritten later
        # for no-website firms by generate_personalized_kadikoy.py)
        html = template
        html = html.replace("{{FIRMA_ADI}}", name)
        html = html.replace("{{KATEGORI}}", category)
        html = html.replace("{{ADRES}}", address or "Adres bilgisi mevcut değil")
        html = html.replace("{{TELEFON_RAW}}", phone_raw or "")
        html = html.replace("{{TELEFON}}", phone or "Telefon bilgisi mevcut değil")
        html = html.replace("{{PUAN}}", puan)
        html = html.replace("{{YIL}}", year)

        if not has_existing_website:
            out_dir = ROOT / slug
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / "index.html").write_text(html, encoding="utf-8")

        rows.append({
            "name": name,
            "phone": phone,
            "slug": slug,
            "has_existing_website": has_existing_website,
            "existing_website": website,
        })

    (ROOT / "data" / "kadikoy_generated_index.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Processed {len(rows)} firms.")
    for r in rows:
        flag = " [MEVCUT SITESI VAR]" if r["has_existing_website"] else ""
        print(f"- {r['slug']}: {r['name']} | {r['phone']}{flag}")


if __name__ == "__main__":
    main()
