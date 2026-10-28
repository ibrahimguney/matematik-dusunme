"""Atölyeyi çalıştırır; öğrenci defterine çıktı veya test hücresi yazmaz."""
from pathlib import Path
import tempfile
import nbformat
from nbclient import NotebookClient
from PIL import Image
import zxingcpp

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / 'atolyeler/niceleyiciler/niceleyici_laboratuvari.ipynb'
n = nbformat.read(p, as_version=4)
nbformat.validate(n)
assert not any(c.get('outputs') for c in n.cells), 'Yayımlanan defter çıktısız olmalı'
sayi = sum(c.cell_type == 'code' for c in n.cells)
n.cells.append(nbformat.v4.new_code_cell('''
# Yalnızca doğrulama çalışmasında eklenen senaryolar.
assert cozumle([[1,0],[0,1]])['A'] is True
assert cozumle([[1,0],[0,1]])['B'] is False
assert cozumle([[0,1],[0,1]])['ortak_sutunlar'] == [1]
assert cozumle([[0,0],[1,0]])['bos_satirlar'] == [0]
assert cozumle([[0,0],[0,0]])['A'] is False
assert cozumle([[1,1],[1,1]])['B'] is True
for hatali in ([], [[]], [[1],[1,0]], [[2]]):
    try:
        cozumle(hatali)
    except ValueError:
        pass
    else:
        raise AssertionError('Geçersiz tablo reddedilmedi')
# Widget değer değişimleri gözlemciyi çalıştırır; ortak sütun oluştur.
for i in range(4):
    kutular[i][0].value = True
assert cozumle([[int(k.value) for k in s] for s in kutular])['B'] is True
# Bir öğrencinin bütün kutularını boşalt; A yanlış olmalı.
for k in kutular[0]:
    k.value = False
assert cozumle([[int(k.value) for k in s] for s in kutular])['A'] is False
'''))
NotebookClient(n, timeout=120, kernel_name='python3',
               resources={'metadata': {'path': str(ROOT)}}).execute()
with tempfile.NamedTemporaryFile(prefix='niceleyiciler-', suffix='.ipynb', delete=False) as f:
    nbformat.write(n, f.name)
    print('Doğrulama çıktısı:', f.name)
qr = zxingcpp.read_barcode(Image.open(ROOT / 'kitap/kaynak/figs/atolye_niceleyiciler_qr.png'))
assert qr and qr.text == 'https://github.com/ibrahimguney/matematik-dusunme/tree/main/atolyeler/niceleyiciler'
print(f'BAŞARILI: {sayi} öğrenci kod hücresi, 64 tablo kontrolü, tanık/karşı örnek senaryoları, widget değişimleri ve QR hedefi.')
