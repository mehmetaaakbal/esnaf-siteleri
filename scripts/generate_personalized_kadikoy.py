# -*- coding: utf-8 -*-
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "kadikoy_elektrikci.json"
INDEX_FILE = ROOT / "data" / "kadikoy_generated_index.json"
TEMPLATE_FILE = ROOT / "_template" / "template_personalized.html"

PRIMARY_COLOR = "#1a56db"
PRIMARY_DARK = "#1442ad"

BASE_SERVICES = [
    ("Ev & İşyeri Elektrik Tesisatı",
     "Yeni yapılan konut ve işyerlerinde sıfırdan tesisat çekiminden, mevcut sistemlerin güncellenmesine kadar tüm elektrik altyapısı işleri."),
    ("Arıza Tespiti & Onarım",
     "Kaçak akım, sigorta atması, priz ve anahtar arızası gibi sorunlarda yerinde teşhis ve aynı gün müdahale."),
    ("Aydınlatma Sistemleri",
     "İç ve dış mekân aydınlatma armatürlerinin montajı, LED dönüşümü ve aydınlatma planlaması."),
    ("Pano & Sigorta Montajı",
     "Elektrik panosu yenileme, kaçak akım rölesi montajı ve sigorta sisteminin güvenlik standartlarına uygun hale getirilmesi."),
    ("Acil Elektrikçi Hizmeti",
     "Beklenmedik elektrik kesintisi ve arızalarında hızlı müdahale ile günlük hayatın kesintiye uğramasının önüne geçilmesi."),
    ("Bakım & Periyodik Kontrol",
     "Elektrik tesisatının düzenli aralıklarla kontrol edilmesi, olası arızaların önceden tespit edilip önlenmesi."),
]

ADDON_SERVICES = {
    "uydu": [
        ("Uydu Anten Kurulumu", "Çanak anten montajı, kanal ayarı ve yeni taşınan hanelerde sıfırdan uydu sistemi kurulumu."),
        ("Uydu Sistemleri Bakımı", "Sinyal kaybı, görüntü bozukluğu gibi sorunlarda mevcut uydu sisteminin bakım ve onarımı."),
    ],
    "çilingir": [
        ("Kilit & Çilingir Hizmeti", "Kapıda kalma, kilit arızası ve anahtar kopyalama gibi durumlarda hızlı çilingir desteği."),
    ],
    "güvenlik": [
        ("Güvenlik Kamerası Kurulumu", "Konut ve işyerleri için kamera sistemi kurulumu, kayıt cihazı bağlantısı ve uzaktan izleme ayarları."),
        ("Alarm Sistemi Kurulumu", "Hırsız ve yangın alarmı sistemlerinin kurulumu, arıza durumunda teknik servis desteği."),
    ],
    "klima": [
        ("Klima Bakım & Tamiri", "Klima arızalarında teknik servis desteği, periyodik bakım ve gaz dolumu."),
    ],
    "santral": [
        ("Telefon Santrali Kurulumu", "İşyerleri için telefon santrali kurulumu ve bakımı."),
    ],
    "malzeme": [
        ("Elektrik Malzemesi Satışı", "Kablo, sigorta, priz ve diğer elektrik malzemelerinin aynı adresten temini."),
    ],
    "cihaz_tamir": [
        ("Elektrikli Cihaz Tamiri", "Küçük ev aletleri ve elektrikli cihazlarda arıza tespiti ve onarımı."),
    ],
}

SLOGANS = {
    "kadikoy-elektrikci-gold-elektrik": "Suadiye'de 7/24 elektrik güvencesi: Gold Elektrik yanınızda.",
    "kadikoy-suadiye-elektrikci-erca-elektrik": "Suadiye'de düzenli, güvenilir hizmet: Erça Elektrik yanınızda.",
    "kadikoy-gunes-elektrik": "Güneş Elektrik: Suadiye'de her gün, güvenle yanınızda.",
    "kadikoy-sebil-elektrik": "Sebil Elektrik: Suadiye'de işçilik ve malzeme tek adreste.",
    "kadikoy-yilmaz-elektrik": "Yılmaz Elektrik: Tesisattan aydınlatmaya, Suadiye'nin kapsamlı çözümü.",
    "kadikoy-saygin-elektrik-cilingir-anahtar": "334 mutlu müşteri: Saygın Elektrik Çilingir Anahtar, Kozyatağı'nın güvenilir adresi.",
    "kadikoy-enes-elektrik-uydu-cilingir": "Elektrikten uyduya, çilingirden acil müdahaleye — Enes Elektrik her an yanınızda.",
    "kadikoy-elektrikci-yigit-elektrik": "Elektrikten klimaya, uydudan santrale — Yiğit Elektrik ile Kadıköy'ün tek durak çözümü.",
    "kadikoy-naci-elektrik": "Naci Elektrik: Suadiye'de haftanın her günü yanınızda.",
    "kadikoy-birol-elektrik-anahtar-cilingir-uydu": "Elektrikten çilingire, uydudan güvenliğe — Birol Elektrik Kozyatağı'nda 7 gün yanınızda.",
    "kadikoy-yilmaz-elektirik-ve-elektronik": "Yılmaz Elektirik ve Elektronik: Suadiye'de elektrikten elektroniğe tek adres.",
}

ABOUT = {
    "kadikoy-elektrikci-gold-elektrik": "Kadıköy Elektrikçi Gold Elektrik, Suadiye Mahallesi Hamiyet Yüceses Sokak'taki merkezinden günün her saati hizmet veriyor. 24 saat kesintisiz çalışma düzeni, özellikle gece saatlerinde ortaya çıkan ani elektrik arızalarında Suadiye ve çevresindeki konut sahipleri için önemli bir güvence oluşturuyor. Sigorta atması, priz ve anahtar arızaları, aydınlatma sorunları gibi günlük hayatı aksatan işlerin yanı sıra, daha kapsamlı tesisat yenileme projelerinde de hizmet veren ekip, bölgedeki apartman ve sitelerle kurduğu ilişkilerle tanınıyor. Arıza bildirimi alındıktan sonra kısa sürede adrese ulaşarak sorunu yerinde tespit eden firma, mümkün olduğunda aynı ziyarette kalıcı çözüm üretmeyi hedefliyor. Suadiye'nin yoğun konut dokusunu iyi tanıyan ekip, farklı bina yaşlarında karşılaşılabilecek elektrik sorunlarına karşı pratik tecrübeye sahip. Gold Elektrik, işe başlamadan önce durumu netleştirip müşteriye şeffaf bilgi vermeyi ilke ediniyor. Kadıköy Suadiye'de güvenilir, her an ulaşılabilir bir elektrikçi arayanlar için pratik bir adres.",
    "kadikoy-suadiye-elektrikci-erca-elektrik": "Suadiye Elektrikçi (Erça Elektrik), Ayşe Çavuş Caddesi üzerindeki merkezinden Suadiye ve çevresine hizmet veren, bölge sakinlerinin aşina olduğu bir elektrik firması. Pazartesi'den Cumartesi'ye kadar 09:00-20:00 saatleri arasında düzenli bir çalışma temposu izleyen ekip, Pazar günleri kapalı kalarak öngörülebilir bir hizmet anlayışı sunuyor. Priz ve anahtar arızalarından aydınlatma sorunlarına, sigorta panosu yenilemesinden kaçak akım tespitine kadar geniş bir yelpazede hizmet veriyor. Suadiye'nin yerleşik apartman dokusunu iyi tanıyan Erça Elektrik, hem küçük çaplı ev içi arızalarda hem de daha kapsamlı tesisat projelerinde tecrübe sahibi. Düzenli çalışma saatleri, özellikle planlı işler için randevu almak isteyen müşteriler açısından avantaj sağlıyor; müşteriler ne zaman ulaşabileceklerini net biliyor. Ekip, yerinde keşif sonrası net fiyat bilgisi vererek şeffaf bir süreç işletmeyi ilke ediniyor. Suadiye'de tanıdık, güvenilir bir elektrikçi arayan Kadıköy sakinleri için Erça Elektrik değerlendirilebilecek bir seçenek.",
    "kadikoy-gunes-elektrik": "Güneş Elektrik, Suadiye Mahallesi Ayşe Çavuş Caddesi'nde, Cem Bey Apartmanı'ndaki merkezinden Kadıköy'e haftanın her günü 08:00-20:00 saatleri arasında hizmet veriyor. Pazar günü dahil kesintisiz çalışma düzeni, hafta içi zaman bulamayan müşterilerin hafta sonu da randevu alabilmesine imkân tanıyor. Sigorta atması, priz ve anahtar arızaları, aydınlatma sorunları gibi günlük hayatı aksatan işlerin yanı sıra, yeni tesisat kurulumu ve pano yenileme gibi daha kapsamlı projelerde de tecrübe sahibi. Suadiye ve çevresindeki site ve apartmanlarla kurduğu düzenli müşteri ilişkileri, Güneş Elektrik'in işçilik kalitesi konusunda edindiği güvenin bir göstergesi. Arıza bildirimi sonrası adrese hızlı intikal ederek sorunu yerinde teşhis eden ekip, mümkün olduğunca aynı ziyarette kalıcı çözüm üretmeyi hedefliyor. Haftanın her günü aynı saatlerde ulaşılabilir olması, müşterilerin ne zaman arayabileceklerini net bilmesini sağlıyor. Kadıköy Suadiye'de düzenli ve güvenilir bir elektrikçi arayanlar için Güneş Elektrik pratik bir tercih.",
    "kadikoy-sebil-elektrik": "Sebil Elektrik, Suadiye Camii Sokak üzerindeki merkezinden Kadıköy'e hizmet veren, hem elektrik tesisatı işleri hem de elektrik malzemesi satışı yapan bir işletme. Bu ikili yapı sayesinde müşteriler, arıza tespiti ve onarımının yanı sıra ihtiyaç duydukları elektrik malzemelerini de aynı adresten temin edebiliyor. Pazartesi'den Cumartesi'ye 09:00-18:30 saatleri arasında hizmet veren, Pazar günleri kapalı olan ekip, düzenli ve öngörülebilir bir çalışma temposu sunuyor. Priz ve sigorta arızalarından aydınlatma armatürü montajına, kablo ve malzeme temininden yeni tesisat kurulumuna kadar geniş bir hizmet yelpazesi mevcut. Suadiye'nin yerleşik konut ve işyeri dokusunu iyi tanıyan Sebil Elektrik, hem bireysel müşterilere hem de esnaf ve işyerlerine malzeme ve işçilik desteği sunuyor. Elektrik malzemesi konusundaki bilgi birikimi, doğru parça seçimi ve maliyet optimizasyonu konusunda da müşterilere avantaj sağlıyor. Kadıköy Suadiye'de hem işçilik hem malzeme ihtiyacını tek adresten çözmek isteyenler için Sebil Elektrik değerlendirilebilecek bir seçenek.",
    "kadikoy-yilmaz-elektrik": "Yılmaz Elektrik, Suadiye Aydın Sokak'taki merkezinden Kadıköy'e klasik elektrik tesisatı hizmetlerinin çok ötesinde bir yelpazede hizmet veriyor. Elektrikli cihaz tamiri, aydınlatma armatürü satışı ve montajı, tel-kablo tedariki gibi alanlarda da uzmanlaşmış olması, firmayı bölgedeki genel elektrikçilerden ayıran temel özellik. Pazartesi'den Cumartesi'ye 08:00-20:00 saatleri arasında hizmet veren ekip, Pazar günleri kapalı kalarak düzenli bir çalışma temposu izliyor. Arızalı beyaz eşya ve küçük ev aletlerinin tamirinden, ev ve işyerlerinde aydınlatma projelendirmesine, ihtiyaç duyulan kablo ve malzemenin temin edilmesine kadar geniş bir hizmet yelpazesi sunuluyor. Suadiye'nin yerleşik konut dokusunda uzun süredir faaliyet gösteren Yılmaz Elektrik, hem tesisat hem cihaz hem de aydınlatma ihtiyaçlarını tek elden çözmek isteyen müşteriler için pratik bir adres. Malzeme ve işçiliği bir arada sunması, ayrı ayrı tedarikçi ve ustayla uğraşmak istemeyen müşteriler için zaman kazandırıyor. Kadıköy Suadiye'de kapsamlı bir elektrik hizmeti arayanlar için Yılmaz Elektrik değerlendirilmeye değer bir seçenek.",
    "kadikoy-saygin-elektrik-cilingir-anahtar": "Saygın Elektrik Çilingir Anahtar, Kozyatağı Forsa Sokak'taki merkezinden Kadıköy'ün geniş bir bölgesine hizmet veren, 334 Google değerlendirmesiyle bölgenin en çok tercih edilen işletmelerinden biri. Elektrik tesisatı hizmetlerinin yanı sıra çilingirlik, uydu iletişim sistemleri, güvenlik sistemi kurulumu ve video kamera tamiri gibi farklı alanlarda birden uzmanlaşmış olması, firmayı benzerlerinden ayıran temel özellik. Pazartesi'den Cumartesi'ye 08:30-20:00 saatleri arasında hizmet veren ekip, kapıda kalma, kilit arızası, elektrik kesintisi veya güvenlik kamerası sorunu gibi farklı ihtiyaçları tek bir ekiple çözebilme imkânı sunuyor. Kozyatağı ve çevresindeki yoğun konut ve işyeri dokusunda uzun süredir faaliyet gösteren Saygın Elektrik, geniş müşteri kitlesinin oluşturduğu güven sayesinde bölgede tanınan bir isim haline gelmiş durumda. Farklı uzmanlık alanlarını bir arada barındırması, müşterilerin farklı firmalarla uğraşmak yerine tek bir güvenilir muhatapla işlerini halletmesini sağlıyor. Kadıköy Kozyatağı'nda kapsamlı ve güvenilir bir teknik hizmet arayanlar için Saygın Elektrik öne çıkan bir adres.",
    "kadikoy-enes-elektrik-uydu-cilingir": "Enes Elektrik Uydu Çilingir, Suadiye Emin Ali Paşa Caddesi'ndeki merkezinden Kadıköy'e elektrik, uydu sistemleri ve çilingirlik alanlarında birleşik bir hizmet sunuyor. Geniş çalışma saatleri -hafta içi 07:30-22:30, Cumartesi 08:30-20:30, Pazar 09:00-17:00- sayesinde neredeyse günün her saatinde ulaşılabilir olan ekip, özellikle acil durumlarda hızlı müdahale imkânı sağlıyor. Elektrik arızalarının yanı sıra uydu anten kurulumu ve sinyal sorunlarının giderilmesi, kapıda kalma ve kilit arızalarında çilingir desteği gibi farklı ihtiyaçlar tek bir ekiple çözülebiliyor. Suadiye'nin yoğun konut dokusunda uzun süredir faaliyet gösteren firma, farklı bina tiplerinde karşılaşılabilecek elektrik ve uydu sorunlarına karşı pratik tecrübeye sahip. Geniş çalışma saatleri ve çoklu uzmanlık alanı, özellikle beklenmedik durumlarda tek bir telefonla çözüm bulmak isteyen müşteriler için önemli bir avantaj. Enes Elektrik, arıza bildirimi sonrası mümkün olan en kısa sürede adrese ulaşmayı öncelik olarak benimsemiş durumda. Kadıköy Suadiye'de kapsamlı ve her an ulaşılabilir bir teknik hizmet arayanlar için değerlendirilebilecek bir adres.",
    "kadikoy-elektrikci-yigit-elektrik": "Kadıköy Elektrikçi (Yiğit Elektrik), Osmanağa Mahallesi Hasırcıbaşı Caddesi'ndeki merkezinden Kadıköy'e çok geniş bir hizmet yelpazesiyle hizmet veriyor. Klasik elektrik tesisatı işlerinin yanında klima tamiri ve bakımı, uydu iletişim sistemleri ve telefon santrali kurulumu gibi farklı teknik alanlarda da uzmanlaşmış olması, firmayı Kadıköy'ün en çok tercih edilen işletmelerinden biri haline getirmiş; 107 Google değerlendirmesi de bunun bir göstergesi. Sabah 06:30'dan gece 23:30'a kadar uzanan geniş çalışma saatleri, özellikle işe erken başlayan ya da geç saatlerde eve dönen Osmanağa sakinleri için büyük kolaylık sağlıyor. Elektrik arızalarından klima bakımına, uydu sinyali sorunlarından ofis telefon santrali kurulumuna kadar birbirinden farklı ihtiyaçlar tek bir ekiple karşılanabiliyor. Osmanağa'nın yoğun ticari ve konut dokusunu iyi tanıyan ekip, hem konut sahiplerine hem de işyerlerine hizmet veriyor. Geniş uzmanlık alanı ve uzun çalışma saatleri, Yiğit Elektrik'i Kadıköy'de kapsamlı bir teknik çözüm arayanlar için öne çıkan bir adres haline getiriyor.",
    "kadikoy-naci-elektrik": "Naci Elektrik, Suadiye Kurudere Sokak'taki İnal Apartmanı'nda konumlanan, Kadıköy'e haftanın her günü 08:30-19:30 saatleri arasında hizmet veren bir elektrik firması. Pazar günü dahil kesintisiz çalışma düzeni, hafta içi vakit bulamayan müşterilerin hafta sonu da randevu alabilmesine imkân tanıyor. Priz ve anahtar arızalarından sigorta değişimine, aydınlatma sorunlarından kaçak akım tespitine kadar günlük hayatı aksatan elektrik işlerinde hizmet veren ekip, Suadiye'nin yerleşik konut dokusunu iyi tanıyor. Arıza bildirimi sonrası adrese giderek durumu yerinde değerlendiren firma, işe başlamadan önce müşteriye net bilgi vermeyi ilke ediniyor. Küçük çaplı ev içi arızalardan daha kapsamlı tesisat işlerine kadar farklı ölçekteki taleplere esnek bir yaklaşımla yanıt veren Naci Elektrik, Suadiye ve çevresindeki müşterilerine uzun yıllardır hizmet vermeye devam ediyor. Haftanın her günü aynı saatlerde ulaşılabilir olması, müşterilerin ne zaman arayabileceklerini net bilmesini sağlıyor. Kadıköy Suadiye'de yerel bir elektrikçi arayanlar için değerlendirilebilecek bir seçenek.",
    "kadikoy-birol-elektrik-anahtar-cilingir-uydu": "Birol Elektrik Anahtar Çilingir Uydu, Kozyatağı Kaya Sultan Sokak'taki merkezinden Kadıköy'e elektrik, çilingirlik ve uydu sistemleri alanlarında birleşik bir hizmet sunuyor. Sabah 06:00'dan gece 23:00'e kadar uzanan geniş çalışma saatleri, Pazar günleri de 10:00-20:00 aralığında devam ederek neredeyse tüm hafta ulaşılabilir olmayı sağlıyor. 78 Google değerlendirmesiyle Kozyatağı'nda tanınan bir isim haline gelen firma, kapıda kalma ve kilit arızalarında hızlı çilingir müdahalesi, elektrik arızalarında yerinde teşhis ve onarım, uydu sistemlerinde kurulum ve bakım hizmeti sunuyor. Kozyatağı'nın yoğun konut ve işyeri dokusunu iyi tanıyan ekip, farklı ihtiyaçları tek bir telefonla çözebilme imkânı sunarak müşterilerine zaman kazandırıyor. Geniş çalışma saatleri, özellikle beklenmedik durumlarda -gece kapıda kalma, ani elektrik kesintisi gibi- önemli bir güvence oluşturuyor. Birol Elektrik, arıza bildirimi sonrası hızlı müdahale ile müşteri memnuniyetini önceliklendiriyor. Kadıköy Kozyatağı'nda kapsamlı ve her an ulaşılabilir bir teknik hizmet arayanlar için tercih edilen bir adres.",
    "kadikoy-yilmaz-elektirik-ve-elektronik": "Yılmaz Elektirik ve Elektronik, Suadiye Yakamoz Sokak'taki merkezinden Kadıköy'e elektrik ve elektronik alanında hizmet veren bir işletme. Haftanın her günü 09:00-17:00 saatleri arasında düzenli bir çalışma temposu izleyen ekip, hem klasik elektrik tesisatı işlerinde hem de elektronik cihaz arızalarında müşterilerine destek oluyor. Priz ve anahtar arızalarından sigorta değişimine, aydınlatma sorunlarından küçük elektronik cihaz tamirine kadar farklı ölçekteki taleplere yanıt veren firma, Suadiye'nin yerleşik konut dokusunu iyi tanıyor. Sabit çalışma saatleri sayesinde müşteriler ne zaman ulaşabileceklerini net biliyor, bu da özellikle planlı işler için randevu almayı kolaylaştırıyor. Elektrik ve elektronik ihtiyaçlarını aynı çatı altında çözmek isteyen müşteriler için pratik bir seçenek sunan Yılmaz Elektirik ve Elektronik, yerinde keşif sonrası net bilgi vererek şeffaf bir süreç işletmeyi ilke ediniyor. Kadıköy Suadiye'de güvenilir bir elektrik ve elektronik desteği arayanlar için değerlendirilebilecek bir adres.",
}

HOURS_SUMMARY = {
    "kadikoy-elektrikci-gold-elektrik": "Haftanın 7 günü 24 saat açık.",
    "kadikoy-suadiye-elektrikci-erca-elektrik": "Pazartesi-Cumartesi 09:00-20:00, Pazar kapalı.",
    "kadikoy-gunes-elektrik": "Her gün 08:00-20:00.",
    "kadikoy-sebil-elektrik": "Pazartesi-Cumartesi 09:00-18:30, Pazar kapalı.",
    "kadikoy-yilmaz-elektrik": "Pazartesi-Cumartesi 08:00-20:00, Pazar kapalı.",
    "kadikoy-saygin-elektrik-cilingir-anahtar": "Pazartesi-Cumartesi 08:30-20:00, Pazar kapalı.",
    "kadikoy-enes-elektrik-uydu-cilingir": "Pazartesi-Cuma 07:30-22:30, Cumartesi 08:30-20:30, Pazar 09:00-17:00.",
    "kadikoy-elektrikci-yigit-elektrik": "Pazartesi-Cuma 06:30-23:30, Cumartesi 07:00-23:30, Pazar 07:30-20:30.",
    "kadikoy-naci-elektrik": "Her gün 08:30-19:30.",
    "kadikoy-birol-elektrik-anahtar-cilingir-uydu": "Pazartesi-Cumartesi 06:00-23:00, Pazar 10:00-20:00.",
    "kadikoy-yilmaz-elektirik-ve-elektronik": "Her gün 09:00-17:00.",
}

DEFAULT_SERVICE_AREA = "Kadıköy ve çevresine hizmet veriyoruz."


def build_services(name: str, categories: list[str]) -> list[tuple[str, str]]:
    services = list(BASE_SERVICES)
    name_l = name.lower()
    cats_l = " ".join(categories).lower()

    if "uydu" in name_l or "uydu" in cats_l:
        services += ADDON_SERVICES["uydu"]
    if "çilingir" in name_l or "çilingir" in cats_l:
        services += ADDON_SERVICES["çilingir"]
    if any(k in cats_l for k in ["güvenlik", "alarm", "kamera"]):
        services += ADDON_SERVICES["güvenlik"]
    if "klima" in cats_l:
        services += ADDON_SERVICES["klima"]
    if "santral" in cats_l:
        services += ADDON_SERVICES["santral"]
    if "malzeme" in cats_l or "tedarik" in cats_l:
        services += ADDON_SERVICES["malzeme"]
    if "cihaz tamir" in cats_l or "elektronik" in name_l:
        services += ADDON_SERVICES["cihaz_tamir"]

    seen = set()
    unique = []
    for s in services:
        if s[0] not in seen:
            seen.add(s[0])
            unique.append(s)
    return unique


def build_trust_line(score, reviews) -> str:
    if score:
        reviews = reviews or 0
        return f"{score}/5 puan — {reviews} Google değerlendirmesi ile doğrulanmış işletme"
    return "Kadıköy'de güvenilir hizmet veren yerel esnaf"


def build_faq_html(name: str, slug: str) -> str:
    hours = HOURS_SUMMARY.get(slug, "Pazartesi-Cumartesi 08:00-20:00.")
    is_24 = "24 saat" in hours
    if is_24:
        q3_answer = f"Evet, {name} 24 saat ulaşılabilir; gece veya hafta sonu fark etmeksizin arıza bildirimi yapabilirsiniz."
    else:
        q3_answer = f"{name} şu çalışma düzeniyle hizmet veriyor: {hours} Bu saatler dışında da arama yaparak durumu iletebilirsiniz."

    faqs = [
        ("Elektrik arızası için ne kadar sürede geliyorsunuz?",
         f"{name} ekibi, telefonla arıza bildirimini aldıktan sonra bölgeye bağlı olarak genellikle kısa süre içinde adrese ulaşmaya çalışır. Acil durumlarda önceliklendirme yapılır."),
        ("Fiyatlandırma nasıl yapılıyor?",
         "Fiyat, arızanın türüne, kullanılacak malzemeye ve işin kapsamına göre değişir. Yerinde keşif sonrası işe başlamadan önce net bir fiyat bilgisi verilir, sürpriz ücret uygulanmaz."),
        ("Hafta sonu veya gece arıza durumunda ulaşabilir miyim?", q3_answer),
        ("Yapılan işlerde garanti var mı?",
         "Değiştirilen malzeme ve yapılan işçilik için garanti sunulur; garanti süresi işin kapsamına göre yerinde bilgilendirilir."),
        ("Sadece arıza mı gideriyorsunuz, yoksa yeni tesisat da yapıyor musunuz?",
         "Hem küçük çaplı arıza onarımları hem de yeni konut/işyerlerinde sıfırdan elektrik tesisatı kurulumu hizmeti sunulmaktadır."),
    ]

    parts = []
    for q, a in faqs:
        parts.append(f"    <details>\n      <summary>{q}</summary>\n      <p>{a}</p>\n    </details>")
    return "\n".join(parts)


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    index_rows = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    year = str(datetime.now().year)

    name_to_slug = {r["name"]: r["slug"] for r in index_rows}
    exclude_slugs = {r["slug"] for r in index_rows if r["has_existing_website"]}

    updated = []
    for item in data:
        name = (item.get("title") or "İsimsiz Firma").strip()
        slug = name_to_slug.get(name)
        if not slug or slug in exclude_slugs:
            continue

        phone = (item.get("phone") or "").strip()
        phone_raw = (item.get("phoneUnformatted") or phone).strip()
        address = (item.get("address") or "").strip()
        category = (item.get("categoryName") or "Elektrikçi").strip()
        categories = item.get("categories") or []
        score = item.get("totalScore")
        reviews = item.get("reviewsCount")
        location = item.get("location") or {}
        lat, lng = location.get("lat"), location.get("lng")

        services = build_services(name, categories)
        services_html = "\n".join(
            f'      <div class="service-card"><h3>{title}</h3><p>{desc}</p></div>'
            for title, desc in services
        )
        trust_line = build_trust_line(score, reviews)
        slogan = SLOGANS.get(slug, f"{name}: Kadıköy'de güvenilir elektrik hizmeti.")
        about = ABOUT.get(slug, f"{name}, Kadıköy bölgesinde elektrik hizmeti veren yerel bir esnaf işletmesidir.")
        hours_summary = HOURS_SUMMARY.get(slug, "Pazartesi-Cumartesi 08:00-20:00.")
        service_area = DEFAULT_SERVICE_AREA
        faq_html = build_faq_html(name, slug)

        if lat is not None and lng is not None:
            harita_src = f"https://www.google.com/maps?q={lat},{lng}&z=16&output=embed"
        else:
            harita_src = f"https://www.google.com/maps?q={quote(address)}&z=15&output=embed"

        html = template
        html = html.replace("{{FIRMA_ADI}}", name)
        html = html.replace("{{KATEGORI}}", category)
        html = html.replace("{{ADRES}}", address or "Adres bilgisi mevcut değil")
        html = html.replace("{{TELEFON_RAW}}", phone_raw or "")
        html = html.replace("{{TELEFON}}", phone or "Telefon bilgisi mevcut değil")
        html = html.replace("{{YIL}}", year)
        html = html.replace("{{PRIMARY_COLOR}}", PRIMARY_COLOR)
        html = html.replace("{{PRIMARY_DARK}}", PRIMARY_DARK)
        html = html.replace("{{SLOGAN}}", slogan)
        html = html.replace("{{ABOUT}}", about)
        html = html.replace("{{SERVICES_HTML}}", services_html)
        html = html.replace("{{TRUST_LINE}}", trust_line)
        html = html.replace("{{CALISMA_SAATLERI}}", hours_summary)
        html = html.replace("{{HIZMET_BOLGESI}}", service_area)
        html = html.replace("{{HARITA_SRC}}", harita_src)
        html = html.replace("{{FAQ_HTML}}", faq_html)

        out_dir = ROOT / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        updated.append(slug)

    print(f"Updated {len(updated)} personalized Kadıköy sites.")
    for slug in updated:
        print(f"- {slug}")


if __name__ == "__main__":
    main()
