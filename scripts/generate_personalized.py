# -*- coding: utf-8 -*-
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
    "internet": [
        ("İnternet Altyapı Kurulumu", "Ev ve işyerlerinde kablolu/kablosuz internet altyapısının kurulumu ve mevcut ağ sorunlarının giderilmesi."),
    ],
    "çilingir": [
        ("Kilit & Çilingir Hizmeti", "Kapıda kalma, kilit arızası ve anahtar kopyalama gibi durumlarda hızlı çilingir desteği."),
    ],
    "güvenlik": [
        ("Güvenlik Kamerası Kurulumu", "Konut ve işyerleri için kamera sistemi kurulumu, kayıt cihazı bağlantısı ve uzaktan izleme ayarları."),
        ("Alarm Sistemi Kurulumu", "Hırsız ve yangın alarmı sistemlerinin kurulumu, arıza durumunda teknik servis desteği."),
    ],
    "insaat": [
        ("Bina Elektrik Tesisatı", "Yeni inşaat projelerinde baştan sona elektrik tesisatı planlaması ve uygulaması."),
        ("Yeni İnşaat Elektrik Projesi", "İnşaat aşamasındaki binalarda proje bazlı elektrik altyapı çözümleri."),
    ],
    "genis_bolge": [
        ("Anadolu Yakası Geniş Hizmet Ağı", "Ataşehir'in yanı sıra Ümraniye ve Kadıköy'ü kapsayan geniş bir bölgede hizmet imkânı."),
    ],
}

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

ABOUT = {
    "satiroglu-elektrik": "Şatıroğlu Elektrik, Ataşehir'in Barbaros Mahallesi'nde faaliyet gösteren, günün her saati ulaşılabilir bir elektrik hizmeti sunuyor. Ev ve işyerlerinde karşılaşılan ani arızalardan planlı bakım işlerine kadar geniş bir yelpazede hizmet veren ekip, özellikle gece saatlerinde ortaya çıkan acil durumlarda hızlı çözüm üretmesiyle mahallede tanınıyor. Kaçak akım, sigorta atması, aydınlatma arızası gibi günlük hayatı aksatan sorunlarda yerinde teşhis yaparak kalıcı çözümler sunuyor. Barbaros ve çevresindeki apartman yönetimleri, işyerleri ve konutlarla uzun soluklu çalışma ilişkileri kurmuş olan Şatıroğlu Elektrik, işçilik kalitesinden ödün vermeden uygun fiyat politikasıyla da öne çıkıyor. 24 saat açık olması, özellikle iş saatleri dışında elektrik arızası yaşayan Ataşehir sakinleri için önemli bir güvence oluşturuyor. Telefonla ilk bilgi alışverişinin ardından adrese en kısa sürede intikal edilerek arıza yerinde tespit edilir ve mümkün olan durumlarda aynı ziyarette çözüme kavuşturulur. Şatıroğlu Elektrik, Ataşehir'de elektrikle ilgili her türlü ihtiyaç için güvenilir bir muhatap arayanlar için pratik bir çözüm ortağıdır.",
    "atasehir-uydu-ve-elektrik-servisi": "Ataşehir Uydu ve Elektrik Servisi, Atatürk Mahallesi Sedef Caddesi üzerindeki merkezinden hem klasik elektrik tesisatı hem de uydu/anten sistemleri alanında hizmet veriyor. Elektrik arızalarının yanı sıra çanak anten kurulumu, kanal ayarı ve uydu sistemlerinin bakımı konusunda da uzmanlaşmış olması, firmayı bölgedeki benzerlerinden ayıran temel özellik. Sabah 08:00'den gece 01:00'e kadar, hafta sonları dahil uzun çalışma saatleriyle hizmet veren ekip, özellikle akşam saatlerinde ortaya çıkan televizyon veya elektrik arızalarında bile ulaşılabilir olmasıyla dikkat çekiyor. Konut ve işyerlerinde priz, sigorta, aydınlatma gibi standart elektrik işlerinin yanında, yeni taşınan hanelerde uydu sistemi kurulumu, mevcut sistemlerde sinyal sorunlarının giderilmesi gibi işler de sıkça talep ediliyor. Atatürk Mahallesi ve çevresindeki site ve apartmanlarla kurduğu düzenli ilişkiler sayesinde bölgeyi iyi tanıyan firma, yerinde keşif sonrası net fiyatlandırma sunmasıyla da güven kazanıyor. Hem elektrik hem uydu ihtiyaçlarını tek elden çözmek isteyen Ataşehir sakinleri için pratik bir adres.",
    "elektrikci": "Barbaros Mahallesi Mimar Sinan Caddesi'nde hizmet veren bu elektrik atölyesi, Ataşehir'de yıllardır ev ve işyeri sahiplerinin ilk aradığı adreslerden biri. Hafta içi ve hafta sonu 08:30-20:00 saatleri arasında ulaşılabilir olan ekip, günlük hayatı aksatan küçük arızalardan kapsamlı tesisat yenilemelerine kadar geniş bir hizmet yelpazesi sunuyor. Priz ve anahtar değişiminden sigorta panosu yenilemeye, aydınlatma armatürü montajından kaçak akım tespitine kadar pek çok işi aynı gün içinde sonuçlandırabilen firma, özellikle hızlı müdahale konusunda bölgede iyi bir isim yapmış durumda. Yeni yapılan dairelerde sıfırdan elektrik tesisatı çekiminden, eski binalarda pano ve kablo yenilemesine kadar farklı ölçekteki projelerde de tecrübe sahibi. Barbaros ve komşu mahallelerdeki müşteri portföyü, işin büyüklüğüne bakılmaksızın aynı özenle yaklaşıldığının bir göstergesi. Telefonla iletilen arıza tarifine göre gerekli malzemeyi önceden hazırlayarak adrese giden ekip, gereksiz tekrar ziyaretleri önleyip zamandan tasarruf sağlamayı hedefliyor. Ataşehir'de güvenilir ve hızlı bir elektrikçi arayanlar için pratik bir seçenek.",
    "celik-elektrik-elektrikci-atasehir-elektrik": "Çelik Elektrik, Ataşehir çevresinde Aşıkveysel Mahallesi'nde konumlanan ve 24 saat kesintisiz hizmet veren bir elektrik firması. Gece yarısı yaşanan ani elektrik kesintilerinden, iş yerlerinde üretim sürecini aksatan pano arızalarına kadar farklı ölçekteki sorunlara hızlı müdahale edebilmesiyle tanınıyor. Ekip, sadece arıza gidermekle kalmayıp, elektrik tesisatının uzun vadeli güvenliğini de gözeterek periyodik kontrol ve bakım hizmeti sunuyor; bu sayede aynı arızanın tekrarlanmasının önüne geçilmesi hedefleniyor. Konutlarda kaçak akım rölesi montajından, işyerlerinde üç fazlı pano bakımına kadar geniş bir teknik bilgi birikimine sahip olan firma, hem bireysel hem ticari müşterilere hizmet veriyor. 24 saat erişilebilir olması, özellikle site yönetimleri ve işletmeler için önemli bir güven unsuru oluşturuyor; zira elektrik arızaları saat gözetmeksizin ortaya çıkabiliyor. Çelik Elektrik, yerinde keşif sonrası şeffaf fiyatlandırma ilkesiyle çalışarak, müşterisine işin kapsamını ve maliyetini işe başlamadan önce netleştiriyor. Ataşehir ve yakın çevresinde güvenilir, ulaşılabilir bir elektrik hizmeti arayanlar için değerlendirilebilecek bir adres.",
    "acl-elektrik": "ACL Elektrik, Ataşehir'in Küçükbakkalköy Mahallesi'nde, Şerifali Caddesi üzerindeki merkezinden günün her saati hizmet veriyor. Sanayi ve iş merkezlerinin yoğun olduğu bu bölgede, hem konutlara hem de işyerlerine yönelik elektrik çözümleri sunan firma, özellikle hızlı arıza tespiti ve müdahalesiyle biliniyor. Sigorta atması, kaçak akım, priz ve anahtar arızaları gibi günlük sorunların yanı sıra, yeni açılan işyerlerinde sıfırdan elektrik tesisatı kurulumu gibi daha kapsamlı projelerde de yer alıyor. Bölgedeki iş yoğunluğu göz önünde bulundurulduğunda, 24 saat ulaşılabilir olması, özellikle mesai saatleri dışında arıza yaşayan işletmeler için kritik bir avantaj sağlıyor. ACL Elektrik ekibi, arıza bildirimini aldıktan sonra mümkün olan en kısa sürede adrese ulaşmayı ve sorunu ilk ziyarette çözüme kavuşturmayı öncelik olarak benimsemiş durumda. Küçükbakkalköy ve çevresindeki tekrarlayan müşteri ilişkileri, firmanın işçilik kalitesi ve dürüst fiyatlandırma konusundaki itibarının bir göstergesi. Ataşehir'de güvenilir bir elektrik desteği arayan konut ve işyeri sahipleri için pratik bir tercih.",
    "atasehir-elektrikci-uydu-internet-apaydin-elektrik": "Apaydın Elektrik, İçerenköy Mahallesi Şafak Cami Sokak üzerindeki merkezinden Ataşehir'e üç farklı alanda birden hizmet sunan nadir işletmelerden biri: elektrik, uydu/internet altyapısı ve çilingirlik. Bu geniş hizmet yelpazesi sayesinde, bir eve taşınan ya da mevcut sistemini yenilemek isteyen müşteriler, elektrik tesisatından uydu anten kurulumuna, kilit değişiminden acil çilingir müdahalesine kadar birçok ihtiyacını tek bir ekiple çözebiliyor. Neredeyse tüm hafta 24 saat açık olan firma, sadece Pazar günü 10:00-19:00 saatleri arasında hizmet vererek de esnek bir çalışma düzeni sunuyor. İçerenköy ve çevresindeki apartman ve sitelerde hem bireysel taleplere hem de toplu bakım işlerine yanıt veren ekip, özellikle acil durumlarda -kapıda kalma, elektrik kesintisi, uydu sinyali kaybı gibi- hızlı çözüm üretmesiyle tanınıyor. Farklı uzmanlık alanlarını bir arada barındırması, müşterilerin farklı firmalarla uğraşmak yerine tek bir güvenilir muhatapla işlerini halletmesini sağlıyor. Ataşehir'de kapsamlı ve pratik bir teknik hizmet arayanlar için Apaydın Elektrik değerlendirilmeye değer bir adres.",
    "ozgur-elektrik": "Özgür Elektrik, Ataşehir'in Örnek Mahallesi'nde, İhtiyar Cahar Dudayev Caddesi üzerinde yıllardır hizmet veren, bölge sakinlerinin aşina olduğu bir elektrik firması. Pazartesi'den Cumartesi'ye kadar 08:00-20:00 saatleri arasında düzenli bir çalışma temposu izleyen ekip, Pazar günleri kapalı kalarak istikrarlı ve öngörülebilir bir hizmet anlayışı benimsiyor. Bu düzenli yapı, özellikle planlı işler -tesisat yenileme, aydınlatma projesi, pano montajı gibi- için randevu almak isteyen müşteriler açısından avantaj sağlıyor. Günlük arızalarda ise sigorta değişiminden priz tamirine, aydınlatma sorunlarından kaçak akım tespitine kadar hızlı ve pratik çözümler sunuluyor. Örnek Mahallesi ve çevresindeki uzun soluklu müşteri ilişkileri, Özgür Elektrik'in işçilik kalitesi konusunda edindiği güvenin bir göstergesi. Ekip, her işe başlamadan önce durumu yerinde inceleyip müşteriye net bilgi vererek şeffaf bir süreç işletmeyi ilke ediniyor. Ataşehir'de uzun yıllardır aynı bölgede faaliyet gösteren, tanıdık ve güvenilir bir elektrikçi arayanlar için Özgür Elektrik değerlendirilebilecek bir seçenek.",
    "atasehir-esatpasa-umraniye-kadikoy-anadolu-yakasi-elektrikci-ozguven-elektrik": "Özgüven Elektrik, Ataşehir'in Esatpaşa Mahallesi'nden hareketle Ümraniye ve Kadıköy'ü de kapsayan geniş bir bölgeye hizmet veren, Anadolu Yakası'nda tanınan bir elektrik firması. Haftanın her günü sabah 07:00'den gece 22:00'e kadar ulaşılabilir olması, geniş hizmet alanıyla birleşince, farklı ilçelerden gelen talepleri aynı gün içinde karşılayabilme esnekliği sağlıyor. Ziya Paşa Caddesi üzerindeki merkezinden hareket eden ekip, konut ve işyerlerinde karşılaşılan klasik elektrik arızalarının yanı sıra, birden fazla mahalleyi kapsayan site ve apartman yönetimleriyle de düzenli bakım anlaşmaları yürütüyor. Geniş coğrafyada faaliyet göstermenin getirdiği tecrübe, farklı bina tiplerinde ve farklı tesisat yaşlarında karşılaşılabilecek sorunlara karşı pratik çözümler üretebilme becerisini de beraberinde getiriyor. Esatpaşa, Ümraniye ve Kadıköy hattında yaşayan ve elektrik ihtiyaçları için bölgeyi iyi tanıyan bir ekiple çalışmak isteyenler için Özgüven Elektrik, uzun mesai saatleri ve geniş hizmet ağıyla pratik bir çözüm sunuyor.",
    "arke-elektrik": "Arke Elektrik, İçerenköy Mahallesi'nde, klasik elektrik hizmetlerinin ötesine geçerek güvenlik sistemleri alanında da uzmanlaşmış bir firma. Hırsız alarmı, yangın alarmı, güvenlik kamerası kurulumu ve video kamera tamiri gibi hizmetleri elektrik tesisatı işleriyle birlikte sunması, firmayı bölgedeki çoğu elektrikçiden ayıran temel özellik. Hafta içi ve Cumartesi günleri 07:30-19:00 saatleri arasında hizmet veren, Pazar günleri kapalı olan ekip, özellikle güvenlik sistemi kurmak isteyen konut ve işyeri sahipleri için planlı randevu düzeni sunuyor. Bir eve veya işyerine hem elektrik tesisatı hem de kamera/alarm sistemi kurmak isteyenler, tek bir firmayla çalışarak süreç yönetimini kolaylaştırabiliyor. Üsküdar-İçerenköy Yolu üzerindeki merkezinden bölgeye hizmet veren Arke Elektrik, güvenlik sistemlerinin kurulumunun yanı sıra arıza durumunda teknik servis desteği de sağlıyor. Evinin veya işyerinin hem elektrik altyapısını hem de güvenliğini aynı ekiple emanet etmek isteyen Ataşehir sakinleri için değerlendirilebilecek kapsamlı bir hizmet sunuyor.",
    "elektrikci-atasehir": "Elektrikçi Ataşehir, Ferhatpaşa Mahallesi'nde konumlanan ve haftanın her günü 10:00-19:00 saatleri arasında düzenli olarak hizmet veren bir elektrik firması. Klasik elektrik tesisatı hizmetlerinin yanında güvenlik sistemi kurulumu da sunması, özellikle yeni taşınan ya da güvenlik önlemlerini artırmak isteyen müşteriler için avantaj sağlıyor. Pazar günleri dahil kesintisiz çalışma düzeni, hafta içi zaman bulamayan müşterilerin hafta sonu randevu alabilmesine imkân tanıyor. Priz ve sigorta arızalarından aydınlatma sistemlerinin kurulumuna, pano yenilemeden güvenlik kamerası montajına kadar geniş bir yelpazede hizmet veren ekip, Ferhatpaşa ve çevresindeki konut ve işyerlerinde tanınan bir isim haline gelmiş durumda. Sabit çalışma saatleri sayesinde müşteriler ne zaman ulaşabileceklerini net biliyor, bu da özellikle planlı işler için randevu almayı kolaylaştırıyor. Elektrik ve güvenlik ihtiyaçlarını aynı çatı altında, düzenli ve öngörülebilir bir hizmet anlayışıyla çözmek isteyen Ataşehir sakinleri için Elektrikçi Ataşehir pratik bir tercih.",
    "alan-elektrik": "Alan Elektrik, İçerenköy Mahallesi İspirli Canip Sokak'taki merkezinden Ataşehir'e 24 saat kesintisiz hizmet sunan bir elektrik firması. Gece veya gündüz fark etmeksizin ulaşılabilir olması, özellikle beklenmedik elektrik arızalarıyla karşılaşan konut ve işyeri sahipleri için önemli bir güvence. Sigorta atması, priz ve anahtar arızaları, aydınlatma sorunları gibi günlük hayatı aksatan işlerin yanı sıra, daha kapsamlı tesisat yenileme ve pano montajı gibi projelerde de tecrübe sahibi. İçerenköy ve çevresindeki site ve apartmanlarla kurduğu düzenli çalışma ilişkileri, firmanın işçilik kalitesi konusunda edindiği güvenin bir göstergesi. Arıza bildirimi sonrası adrese hızlı intikal ederek sorunu yerinde teşhis eden ekip, mümkün olduğunca aynı ziyarette kalıcı çözüm üretmeyi hedefliyor. 24 saat açık olması, özellikle işyerlerinde vardiyalı çalışan ya da mesai saatleri dışında müdahale gerektiren müşteriler için pratik bir avantaj sağlıyor. Ataşehir'de güvenilir ve her an ulaşılabilir bir elektrikçi arayanlar için Alan Elektrik değerlendirilebilecek bir seçenek.",
    "alperdem-elektrik": "Alperdem Elektrik, Barbaros Mahallesi Mor Sümbül Sokak'taki merkezinden Ataşehir'e elektrik hizmeti sunan yerel bir işletme. Konut ve işyerlerinde karşılaşılan günlük elektrik arızalarına -priz ve anahtar sorunları, sigorta atması, aydınlatma arızaları gibi- pratik ve hızlı çözümler üretmeyi hedefleyen ekip, aynı zamanda yeni tesisat kurulumu ve mevcut sistemlerin bakımı konularında da hizmet veriyor. Barbaros Mahallesi'nin yerleşik yapısı ve yoğun konut dokusu göz önüne alındığında, bölgeyi iyi tanıyan bir ekiple çalışmanın avantajları öne çıkıyor; farklı bina yaşlarında ve tesisat tiplerinde karşılaşılabilecek sorunlara karşı pratik tecrübe bir arada bulunuyor. Alperdem Elektrik, işe başlamadan önce durumu yerinde değerlendirip müşteriye net bilgi vermeyi, gereksiz maliyetlerden kaçınmayı ilke ediniyor. Küçük çaplı ev içi arızalardan daha kapsamlı elektrik projelerine kadar farklı ölçekteki işlerde esnek çalışma anlayışı benimseyen firma, Ataşehir'de mahalle esnafı güveniyle hizmet vermeye devam ediyor.",
    "fetih-elektrikci-gul-elektrik": "Fetih Elektrikçi Gül Elektrik, Ataşehir'in Fetih Mahallesi'nde, Coşkunlar Sokak üzerindeki merkezinden günün her saati hizmet veren bir elektrik firması. 24 saat ulaşılabilir olması, özellikle gece saatlerinde ortaya çıkan ani elektrik kesintileri ve arızalarında Fetih Mahallesi ve çevresindeki sakinler için önemli bir güvence oluşturuyor. Sigorta atması, priz ve anahtar arızaları, aydınlatma sorunları gibi günlük hayatı aksatan işlerin yanı sıra, yeni yapılan konutlarda sıfırdan tesisat çekimi gibi daha kapsamlı projelerde de tecrübe sahibi. Mahalle esnafı olarak uzun yıllardır aynı bölgede hizmet veren ekip, güler yüzlü yaklaşımı ve dürüst fiyatlandırma anlayışıyla bölge sakinlerinin güvenini kazanmış durumda. Arıza bildirimi alındıktan sonra kısa sürede adrese ulaşarak sorunu yerinde tespit eden ve mümkün olduğunda aynı ziyarette çözüme kavuşturan firma, tekrar eden ziyaretlerden kaynaklanabilecek zaman kaybını da en aza indirmeyi hedefliyor. Ataşehir Fetih Mahallesi'nde güvenilir, ulaşılabilir bir elektrikçi arayanlar için pratik bir adres.",
}

HOURS_SUMMARY = {
    "satiroglu-elektrik": "Haftanın 7 günü 24 saat açık.",
    "atasehir-uydu-ve-elektrik-servisi": "Pazartesi-Cuma 08:00-01:00, Cumartesi 08:30-01:00, Pazar 09:00-01:00.",
    "elektrikci": "Her gün 08:30-20:00.",
    "celik-elektrik-elektrikci-atasehir-elektrik": "Haftanın 7 günü 24 saat açık.",
    "acl-elektrik": "Haftanın 7 günü 24 saat açık.",
    "atasehir-elektrikci-uydu-internet-apaydin-elektrik": "Pazartesi-Cumartesi 24 saat açık, Pazar 10:00-19:00.",
    "ozgur-elektrik": "Pazartesi-Cumartesi 08:00-20:00, Pazar kapalı.",
    "atasehir-esatpasa-umraniye-kadikoy-anadolu-yakasi-elektrikci-ozguven-elektrik": "Her gün 07:00-22:00.",
    "arke-elektrik": "Pazartesi-Cumartesi 07:30-19:00, Pazar kapalı.",
    "elektrikci-atasehir": "Her gün 10:00-19:00.",
    "alan-elektrik": "Haftanın 7 günü 24 saat açık.",
    "alperdem-elektrik": "Pazartesi-Cumartesi 08:00-20:00 (acil durumlar için yine de arayabilirsiniz).",
    "fetih-elektrikci-gul-elektrik": "Haftanın 7 günü 24 saat açık.",
}

SERVICE_AREA = {
    "atasehir-esatpasa-umraniye-kadikoy-anadolu-yakasi-elektrikci-ozguven-elektrik":
        "Ataşehir, Ümraniye ve Kadıköy'e hizmet veriyoruz.",
}
DEFAULT_SERVICE_AREA = "Ataşehir ve çevresine hizmet veriyoruz."

# Apify scrape occasionally leaks raw coordinates into the street field.
# Manual overrides for addresses that render broken.
ADDRESS_OVERRIDES = {
    "elektrikci-atasehir": "Ferhatpaşa, 34758 Ataşehir/İstanbul, Türkiye",
}


def build_services(name: str, categories: list[str]) -> list[tuple[str, str]]:
    services = list(BASE_SERVICES)
    name_l = name.lower()
    cats_l = " ".join(categories).lower()

    if "uydu" in name_l or "uydu" in cats_l:
        services += ADDON_SERVICES["uydu"]
    if "internet" in name_l:
        services += ADDON_SERVICES["internet"]
    if "çilingir" in cats_l:
        services += ADDON_SERVICES["çilingir"]
    if any(k in cats_l for k in ["güvenlik", "alarm", "kamera"]):
        services += ADDON_SERVICES["güvenlik"]
    if "inşaat" in name_l or "yapı" in name_l:
        services += ADDON_SERVICES["insaat"]
    if "esatpaşa" in name_l or "ümraniye" in name_l or "kadıköy" in name_l:
        services += ADDON_SERVICES["genis_bolge"]

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
    return "Ataşehir'de uzun yıllardır güvenilir hizmet veren yerel esnaf"


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

    updated = []
    for item in data:
        name = (item.get("title") or "İsimsiz Firma").strip()
        slug = name_to_slug.get(name)
        if not slug or slug in EXCLUDE_SLUGS:
            continue

        phone = (item.get("phone") or "").strip()
        phone_raw = (item.get("phoneUnformatted") or phone).strip()
        address = ADDRESS_OVERRIDES.get(slug, (item.get("address") or "").strip())
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
        slogan = SLOGANS.get(slug, f"{name}: Ataşehir'de güvenilir elektrik hizmeti.")
        about = ABOUT.get(slug, f"{name}, Ataşehir bölgesinde elektrik hizmeti veren yerel bir esnaf işletmesidir.")
        hours_summary = HOURS_SUMMARY.get(slug, "Pazartesi-Cumartesi 08:00-20:00.")
        service_area = SERVICE_AREA.get(slug, DEFAULT_SERVICE_AREA)
        faq_html = build_faq_html(name, slug)

        if lat is not None and lng is not None:
            harita_src = f"https://www.google.com/maps?q={lat},{lng}&z=16&output=embed"
        else:
            from urllib.parse import quote
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

    print(f"Updated {len(updated)} personalized sites.")
    for slug in updated:
        print(f"- {slug}")


if __name__ == "__main__":
    main()
