# Niceleyiciler · Öğretmen rehberi

## Ders akışı (40 dakika)

- 5 dk: İlk tabloya bireysel tahmin; sonuç henüz çalıştırılmaz.
- 10 dk: İkişerli tablo deneyi; biri Şüpheci, diğeri Savunucu rolünde.
- 10 dk: Ortak tanık, olumsuzlama ve 2×3 tabloların eksiksiz kontrolü.
- 10 dk: Sonlu dünya tuzağı ve doğal sayılarda genel strateji.
- 5 dk: Çıkış bileti ve kendi iddiasını üretme.

## Beklenen gerekçeler

Başlangıçta A doğru, B yanlıştır. Bir sütunda zaten tek ✓ bulunduğu için ortak tanık oluşturmak üç yeni ✓ gerektirir ve üçü yeterlidir. B doğruysa ortak soruyu her öğrenci için tanık seçebiliriz; dolayısıyla B ⇒ A. A ⇒ B geçersizdir; başlangıç tablosu karşı örnektir.

A'nın olumsuzu “En az bir öğrenci hiçbir soru çözmedi”dir: ∃x∀y¬P(x,y). A yanlışsa tamamen boş bir satır vardır. B yanlışsa her sütunda en az bir boş hücre vardır; bu öğrencinin bütün sütunlarda aynı olması gerekmez.

2×3 tablo kontrolü 64 durumu kapsar; bütün sonlu boyutlar için ispat veya sonsuz yapılar için kanıt sayılmaz.

D={0,…,N} için x=N karşı örnektir. ℕ'de her x için y=x+1 doğal sayıdır ve y>x; bu genel tanık kuralıdır. Ters sıra için herhangi bir y seçildiğinde x=y alınır; y>x yanlış olur. Böylece bütün doğal sayılardan büyük tek doğal sayı bulunamaz.

## Değerlendirme (her ölçüt 0–2 puan)

| Ölçüt | 0 | 1 | 2 |
|---|---|---|---|
| Evren | Belirtilmemiş | Kısmen açık | x ve y evrenleri açık |
| Niceleyici sırası | Karıştırılmış | Sonuç doğru, bağımlılık eksik | Ortak ve bağımlı tanık ayrımı açık |
| Olumsuzlama | Hatalı | Doğru cümle, gerekçe eksik | Boş satır / karşı örnek gerekçesi açık |
| Deney–ispat ayrımı | Özdeş sayıyor | Farkı söylüyor | Genel stratejiyle gerekçelendiriyor |
| Muhakeme günlüğü | Yok | Yalnız sonuç var | İlk tahmin, değişim ve gerekçe var |

Amaç yalnız kodu çalıştırmak değil, tanığın hangi bilgiye bağlı seçildiğini açıklamaktır. Bu rehber öğrenci sayfasından erişilebilir; gizli cevap anahtarı değildir.

## Teknik doğrulama sınırı

Not defteri yerel Python/Jupyter çekirdeğinde baştan sona yürütülür. Colab tarayıcısındaki widget tıklamaları ve telefon kamerasıyla basılı kare kod taraması ayrıca kullanıcı denemesi gerektirir. GitHub/Colab bağlantıları standart kalıcı depo yollarını kullanır.
