# Atölye geliştirme ve doğrulama

Öğrenciler için yerel kurulum gerekmez; atölye sayfasındaki Colab bağlantısı kullanılır.
Aşağıdakiler bakım ve yerel doğrulama içindir. Python 3.13 ile sınanmıştır.

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/dogrula.py
```

Doğrulayıcı öğrenci defterini baştan sona çalıştırır, widget değer değişimlerini ve tanık/karşı örnek durumlarını sınar. Kare kodu bağımsız bir okuyucuyla çözer. Çıktılı test defterini geçici dizine yazar; yayımlanan öğrenci defteri çıktısız kalır.

## Kitap PDF’si

XeLaTeX, latexmk, kullanılan TeX paketleri ve Libertinus OTF yazı tipleri gerekir. Yazı tiplerinin resmî dağıtımı: https://github.com/alerque/libertinus/releases/tag/v7.051 . Font lisansı bu dağıtımın OFL.txt dosyasındadır; fontlar depoya eklenmemiştir.

```bash
cd kitap/kaynak
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=/tmp/mat507-build main.tex
```

Fontlar sistemde kurulu değilse `OSFONTDIR=/fontlarin/bulundugu/dizin//` ile gerçek font dizinini belirtin. Ortamımızda `/workspace/.local/share/fonts/libertinus//` kullanıldı.
Başarılı derlemeden sonra `/tmp/mat507-build/main.pdf` incelenerek `kitap/MAT507_Matematiksel_Dusunme_ve_Muhakeme.pdf` güncellenir.

Niceleyiciler bölüm sonundaki QR, `atolyeler/niceleyiciler` GitHub sayfasına gider. Bu klasörün ve deponun URL’sini basım sonrasında koruyun. Colab bağlantısı GitHub üzerindeki not defterini açar; kodun gerçek Colab tarayıcısında denenmesi ve basılı kare kodun telefonla taranması ayrıca yapılmalıdır.
