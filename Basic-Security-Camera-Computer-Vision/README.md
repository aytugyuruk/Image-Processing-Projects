# Güvenlik Kamerası - Hareket Tespit Sistemi

Basit bir güvenlik kamerası uygulaması. Kameradan gelen görüntülerde hareket tespit eder ve otomatik screenshot alır.

## Özellikler

- **Gerçek zamanlı hareket tespiti**
- **Otomatik screenshot kaydetme**
- **Terminal bildirim sistemi**
- **Spam koruması** (2 saniyede bir kontrol)

## Gerekli Kütüphaneler

```bash
pip install opencv-python numpy
```

## Kullanım

1. Kodu çalıştırın:
```bash
python security_camera.py
```

2. Kamera açıldıktan sonra hareket edin.

3. Çıkmak için **'q'** tuşuna basın.

## Dosya Yapısı

```
proje/
├── security_camera.py
└── screenshots/
    ├── hareket_20240917_143052.jpg
    ├── hareket_20240917_143125.jpg
    └── ...
```

## Ayarlar

Koddaki bu değerleri ihtiyacınıza göre değiştirebilirsiniz:

- `print_interval = 2.0` - Bildirim sıklığı (saniye)
- `motion_detected = diff_norm > 50000` - Hareket hassasiyeti
- `motion_text_duration = 0.10` - Yazının ekranda kalma süresi

## Nasıl Çalışır?

1. İlk frame arkaplan olarak kaydedilir
2. Her yeni frame arkaplan ile karşılaştırılır
3. Fark belirlenen eşiği geçerse hareket tespit edilir
4. Screenshot otomatik olarak kaydedilir

## Notlar

- Kamera 0. index'ten açılır (varsayılan webcam)
- Screenshots otomatik olarak `screenshots/` klasörüne kaydedilir
- Her screenshot benzersiz tarih-saat damgası ile adlandırılır