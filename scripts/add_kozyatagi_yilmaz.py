# -*- coding: utf-8 -*-
# Manually sourced (web search, not Apify) — user-confirmed phone number.
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_FILE = ROOT / "_template" / "template_personalized.html"
INDEX_FILE = ROOT / "data" / "kadikoy_generated_index.json"

SLUG = "kadikoy-kozyatagi-yilmaz-elektrik"
NAME = "Kozyatağı Elektrikçi Yılmaz Elektrik"
PHONE = "+90 536 200 84 82"
PHONE_RAW = "+905362008482"
ADDRESS = "Kozyatağı Mah. Hilmipaşa Cd. No:29 D:3, Kadıköy/İstanbul, Türkiye"
CATEGORY = "Elektrikçi"

SLOGAN = "Kozyatağı'nda elektrikten çilingire, hidrofordan beyaz eşyaya tek adres: Yılmaz Elektrik."

ABOUT = (
    "Kozyatağı Elektrikçi Yılmaz Elektrik, Hilmipaşa Caddesi üzerindeki merkezinden "
    "Kozyatağı ve çevresine geniş bir hizmet yelpazesiyle hizmet veriyor. Klasik "
    "elektrik arıza ve tadilat işlerinin yanı sıra beyaz eşya teknik servisi, çilingir "
    "hizmeti ve hidrofor bakım-onarımı gibi farklı alanlarda da destek sunması, "
    "firmayı bölgedeki genel elektrikçilerden ayıran temel özellik. Ev ve işyerlerinde "
    "karşılaşılan priz, sigorta ve aydınlatma arızalarının yanında, beyaz eşyalarda "
    "yaşanan teknik sorunlarda da yerinde müdahale imkânı sunuluyor. Kapıda kalma "
    "veya kilit arızası gibi acil durumlarda çilingir desteği vermesi, apartman ve "
    "sitelerin su basınç sistemlerinde karşılaşılan hidrofor arızalarına da bakması, "
    "Kozyatağı sakinlerinin farklı teknik ihtiyaçlarını tek bir telefonla çözebilmesini "
    "sağlıyor. Bölgedeki yoğun konut dokusunu iyi tanıyan ekip, arıza bildirimi sonrası "
    "adrese hızlı intikal ederek sorunu yerinde teşhis etmeyi hedefliyor. Kozyatağı'nda "
    "kapsamlı bir teknik hizmet arayan konut ve işyeri sahipleri için değerlendirilebilecek "
    "bir adres."
)

CALISMA_SAATLERI = "Pazartesi-Cumartesi 09:00-20:00 (kesin saatler için aramanızı öneririz)."
HIZMET_BOLGESI = "Kozyatağı ve Kadıköy çevresine hizmet veriyoruz."
TRUST_LINE = "Kozyatağı'nda elektrik, çilingir, hidrofor ve beyaz eşya teknik servisini bir arada sunan yerel esnaf"

SERVICES = [
    ("Ev & İşyeri Elektrik Tesisatı",
     "Yeni yapılan konut ve işyerlerinde sıfırdan tesisat çekiminden, mevcut sistemlerin güncellenmesine kadar tüm elektrik altyapısı işleri."),
    ("Arıza Tespiti & Onarım",
     "Kaçak akım, sigorta atması, priz ve anahtar arızası gibi sorunlarda yerinde teşhis ve aynı gün müdahale."),
    ("Aydınlatma Sistemleri",
     "İç ve dış mekân aydınlatma armatürlerinin montajı, LED dönüşümü ve aydınlatma planlaması."),
    ("Beyaz Eşya Teknik Servisi",
     "Elektrikli ev aletleri ve beyaz eşyalarda arıza tespiti, bakım ve onarım hizmeti."),
    ("Kilit & Çilingir Hizmeti",
     "Kapıda kalma, kilit arızası ve anahtar kopyalama gibi durumlarda hızlı çilingir desteği."),
    ("Hidrofor Bakım & Onarımı",
     "Apartman ve sitelerde su basınç sistemlerinin (hidrofor) bakımı ve arıza onarımı."),
]

FAQS = [
    ("Elektrik arızası için ne kadar sürede geliyorsunuz?",
     f"{NAME} ekibi, telefonla arıza bildirimini aldıktan sonra bölgeye bağlı olarak genellikle kısa süre içinde adrese ulaşmaya çalışır. Acil durumlarda önceliklendirme yapılır."),
    ("Fiyatlandırma nasıl yapılıyor?",
     "Fiyat, arızanın türüne, kullanılacak malzemeye ve işin kapsamına göre değişir. Yerinde keşif sonrası işe başlamadan önce net bir fiyat bilgisi verilir, sürpriz ücret uygulanmaz."),
    ("Hafta sonu veya gece arıza durumunda ulaşabilir miyim?",
     f"{NAME} şu çalışma düzeniyle hizmet veriyor: {CALISMA_SAATLERI} Bu saatler dışında da arama yaparak durumu iletebilirsiniz."),
    ("Yapılan işlerde garanti var mı?",
     "Değiştirilen malzeme ve yapılan işçilik için garanti sunulur; garanti süresi işin kapsamına göre yerinde bilgilendirilir."),
    ("Sadece elektrik mi, yoksa çilingir ve hidrofor işleri de yapıyor musunuz?",
     "Elektrik arıza ve tesisat işlerinin yanında çilingirlik, hidrofor bakım-onarımı ve beyaz eşya teknik servisi de sunulmaktadır."),
]


def main():
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    year = str(datetime.now().year)

    services_html = "\n".join(
        f'      <div class="service-card"><h3>{title}</h3><p>{desc}</p></div>'
        for title, desc in SERVICES
    )
    faq_html = "\n".join(
        f"    <details>\n      <summary>{q}</summary>\n      <p>{a}</p>\n    </details>"
        for q, a in FAQS
    )
    harita_src = f"https://www.google.com/maps?q={quote(ADDRESS)}&z=15&output=embed"

    html = template
    html = html.replace("{{FIRMA_ADI}}", NAME)
    html = html.replace("{{KATEGORI}}", CATEGORY)
    html = html.replace("{{ADRES}}", ADDRESS)
    html = html.replace("{{TELEFON_RAW}}", PHONE_RAW)
    html = html.replace("{{TELEFON}}", PHONE)
    html = html.replace("{{YIL}}", year)
    html = html.replace("{{PRIMARY_COLOR}}", "#1a56db")
    html = html.replace("{{PRIMARY_DARK}}", "#1442ad")
    html = html.replace("{{SLOGAN}}", SLOGAN)
    html = html.replace("{{ABOUT}}", ABOUT)
    html = html.replace("{{SERVICES_HTML}}", services_html)
    html = html.replace("{{TRUST_LINE}}", TRUST_LINE)
    html = html.replace("{{CALISMA_SAATLERI}}", CALISMA_SAATLERI)
    html = html.replace("{{HIZMET_BOLGESI}}", HIZMET_BOLGESI)
    html = html.replace("{{HARITA_SRC}}", harita_src)
    html = html.replace("{{FAQ_HTML}}", faq_html)

    out_dir = ROOT / SLUG
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html, encoding="utf-8")

    rows = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    rows = [r for r in rows if r["slug"] != SLUG]
    rows.append({
        "name": NAME,
        "phone": PHONE,
        "slug": SLUG,
        "has_existing_website": False,
        "existing_website": "",
        "source": "manual_web_search_user_confirmed",
    })
    INDEX_FILE.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {SLUG}/index.html and updated index.")


if __name__ == "__main__":
    main()
