# -*- coding: utf-8 -*-
import hashlib
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "atasehir_elektrikci.json"
INDEX_FILE = ROOT / "data" / "generated_index.json"
TEMPLATE_FILE = ROOT / "_template" / "template_personalized.html"

# Firms that already have their own website — left untouched.
EXCLUDE_SLUGS = {
    "atasehir-elektrikci-devran",
    "art-of-elektrik",
    "atasehir-elektrikci-ustasi",
    "atasehir-cozum-elektrik-elektronik-uydu-servisi",
    "asir-elektrik",
    "altay-elektrik",
    "be-ha-teknik-elektrik-yapi-ve-insaat",
}

PALETTES = [
    ("#1a56db", "#1442ad"),  # Mavi
    ("#15803d", "#14532d"),  # Yeşil
    ("#c2410c", "#9a3412"),  # Turuncu
    ("#3730a3", "#1e1b4b"),  # Lacivert
]

BASE_SERVICES = [
    "Ev & İşyeri Elektrik Tesisatı",
    "Arıza Tespiti & Onarım",
    "Aydınlatma Sistemleri",
    "Pano & Sigorta Montajı",
    "Acil Elektrikçi Hizmeti",
    "Bakım & Periyodik Kontrol",
]

SLOGANS = {
    "satiroglu-elektrik": "Ataşehir'de dürüst fiyat, hızlı çözüm: Şatıroğlu Elektrik yanınızda.",
    "atasehir-uydu-ve-elektrik-servisi": "Elektrikten uydu anten kurulumuna, Ataşehir'in tek adres çözümü.",
    "elektrikci": "Ataşehir'de arızanız ne olursa olsun, tek telefonla yanınızdayız.",
    "celik-elektrik-elektrikci-atasehir-elektrik": "Sağlam işçilik, kalıcı çözüm — Çelik Elektrik güvencesiyle.",
    "acl-elektrik": "Ataşehir'de hızlı müdahale, güvenilir elektrik hizmeti: ACL Elektrik.",
    "atasehir-elektrikci-uydu-internet-apaydin-elektrik": "Elektrikten uyduya, çilingirden internete — Apaydın Elektrik ile tek durak çözüm.",
    "ozgur-elektrik": "Özgür Elektrik: Ataşehir'de yılların verdiği tecrübeyle 7/24 yanınızda.",
    "atasehir-esatpasa-umraniye-kadikoy-anadolu-yakasi-elektrikci-ozguven-elektrik": "Ataşehir'den Ümraniye'ye, Kadıköy'e — Anadolu Yakası'nın güvenilir elektrikçisi Özgüven Elektrik.",
    "arke-elektrik": "Elektrikten güvenlik sistemlerine, eviniz ve işyeriniz Arke Elektrik güvencesinde.",
    "elektrikci-atasehir": "Elektrik tesisatından güvenlik sistemine, Ataşehir'in güvenilir çözüm ortağı.",
    "alan-elektrik": "Alan Elektrik: Ataşehir'de kaliteli işçilik, uygun fiyat.",
    "alperdem-elektrik": "Alperdem Elektrik ile Ataşehir'de elektrik dertleriniz bitsin.",
    "fetih-elektrikci-gul-elektrik": "Fetih Elektrikçi Gül Elektrik: Ataşehir'de güler yüzlü, güvenilir hizmet.",
}


def pick_palette(name: str):
    h = int(hashlib.md5(name.encode("utf-8")).hexdigest(), 16)
    return PALETTES[h % len(PALETTES)]


def build_services(name: str, categories: list[str]) -> list[str]:
    services = list(BASE_SERVICES)
    name_l = name.lower()
    cats_l = " ".join(categories).lower()

    if "uydu" in name_l or "uydu" in cats_l:
        services += ["Uydu Anten Kurulumu", "Uydu Sistemleri Bakımı"]
    if "internet" in name_l:
        services += ["İnternet Altyapı Kurulumu"]
    if "çilingir" in cats_l:
        services += ["Kilit & Çilingir Hizmeti"]
    if any(k in cats_l for k in ["güvenlik", "alarm", "kamera"]):
        services += ["Güvenlik Kamerası Kurulumu", "Alarm Sistemi Kurulumu"]
    if "inşaat" in name_l or "yapı" in name_l:
        services += ["Bina Elektrik Tesisatı", "Yeni İnşaat Elektrik Projesi"]
    if "esatpaşa" in name_l or "ümraniye" in name_l or "kadıköy" in name_l:
        services += ["Anadolu Yakası Geniş Hizmet Ağı"]

    # de-duplicate while preserving order
    seen = set()
    unique = []
    for s in services:
        if s not in seen:
            seen.add(s)
            unique.append(s)
    return unique


def build_trust_line(score, reviews) -> str:
    if score:
        reviews = reviews or 0
        return f"{score}/5 puan — {reviews} Google değerlendirmesi ile doğrulanmış işletme"
    return "Ataşehir'de uzun yıllardır güvenilir hizmet veren yerel esnaf"


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    index_rows = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    year = str(datetime.now().year)

    name_to_slug = {r["name"]: r["slug"] for r in index_rows}

    updated = []
    for item in data:
        name = (item.get("title") or "İsimsiz Firma").strip()
        slug = name_to_slug.get(name)
        if not slug or slug in EXCLUDE_SLUGS:
            continue

        phone = (item.get("phone") or "").strip()
        phone_raw = (item.get("phoneUnformatted") or phone).strip()
        address = (item.get("address") or "").strip()
        category = (item.get("categoryName") or "Elektrikçi").strip()
        categories = item.get("categories") or []
        score = item.get("totalScore")
        reviews = item.get("reviewsCount")

        primary, primary_dark = pick_palette(name)
        services = build_services(name, categories)
        services_html = "\n".join(
            f'      <div class="service-item">{s}</div>' for s in services
        )
        trust_line = build_trust_line(score, reviews)
        slogan = SLOGANS.get(slug, f"{name}: Ataşehir'de güvenilir elektrik hizmeti.")

        html = template
        html = html.replace("{{FIRMA_ADI}}", name)
        html = html.replace("{{KATEGORI}}", category)
        html = html.replace("{{ADRES}}", address or "Adres bilgisi mevcut değil")
        html = html.replace("{{TELEFON_RAW}}", phone_raw or "")
        html = html.replace("{{TELEFON}}", phone or "Telefon bilgisi mevcut değil")
        html = html.replace("{{YIL}}", year)
        html = html.replace("{{PRIMARY_COLOR}}", primary)
        html = html.replace("{{PRIMARY_DARK}}", primary_dark)
        html = html.replace("{{SLOGAN}}", slogan)
        html = html.replace("{{SERVICES_HTML}}", services_html)
        html = html.replace("{{TRUST_LINE}}", trust_line)

        out_dir = ROOT / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        updated.append((slug, name, primary))

    print(f"Updated {len(updated)} personalized sites.")
    for slug, name, primary in updated:
        print(f"- {slug} ({primary})")


if __name__ == "__main__":
    main()
