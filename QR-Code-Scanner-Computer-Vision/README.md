<div style="display: flex; gap: 20px;">
  <img src="input.png" alt="Input" width="300"/>
  <img src="output.png" alt="Output" width="300"/>
</div>

# QR Kod Tespit Projesi

Bu proje, OpenCV kullanarak bir görüntüdeki QR kodlarını tespit eder ve çözer.

## 📋 Gereksinimler
- Python 3.x
- OpenCV (`pip install opencv-python`)

## 🚀 Kullanım
1. `image.jpg` adlı bir resim dosyasını proje klasörüne koyun.
2. Aşağıdaki kodu çalıştırın:
   ```bash
   python barcode_dedector_on_image.py
   ```
3. Program, QR kodun etrafına kırmızı kutu çizer ve terminalde QR kod verisini gösterir.

## 📂 Çıktı
- QR kod algılanırsa pencere üzerinde kutu çizilir ve verisi yazdırılır.
- QR kod bulunamazsa terminalde "QR kod bulunamadı." mesajı çıkar.
