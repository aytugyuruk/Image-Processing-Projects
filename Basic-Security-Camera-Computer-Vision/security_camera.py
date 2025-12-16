import cv2
import numpy as np
import time
import os

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Kamera açılamadı")
    exit()

cv2.waitKey(1000)  # Kamera açılması için bekle
ret, frame = cap.read()  # ilk frame i alıyorum
previous_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
previous_frame = cv2.GaussianBlur(previous_frame, (5,5), 0)
previous_frame = np.float32(previous_frame)  # biz burada previous_frame i aslinda ilk frame olarak tutmus olduk.

# Hareket yazısı için zaman kontrolü (sadece hareket olduğunda yaz)
motion_text_duration = 0.10  # saniye cinsinden yazının ekranda kalma süresi
last_motion_time = 0

# Terminal çıktısı için zaman kontrolü (spam olmaması için)
print_interval = 2.0  # saniye cinsinden - kaç saniyede bir yazdırılacak
last_print_time = 0

# Screenshot kaydetme için klasör oluştur
screenshot_folder = "screenshots"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)
    print(f"'{screenshot_folder}' klasörü oluşturuldu.")

while True:
    ret, frame = cap.read()  # burada surekli olarak frame aliyoruz cunku while dongusu var
    if not ret:
        break
    
    # Griye çevir ve blur uygula
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    gray_float = np.float32(gray)  # hem previos frame i hem de gray frameninin float 32 cevirdik cunku accumulate weighted float32 istiyor
    
    # bu fonksiyon arkaplani yavas yavas guncelliyor
    cv2.accumulateWeighted(gray_float, previous_frame, 0.05)
    
    # Hareket farkı
    background = cv2.convertScaleAbs(previous_frame)
    diff = cv2.absdiff(gray, background)
    _, diff_thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    diff_norm = np.linalg.norm(diff_thresh)
    
    # Hareket kontrolü
    motion_detected = diff_norm > 50000  # eşik değerini ortamına göre ayarla
    
    current_time = time.time()
    
    if motion_detected:
        last_motion_time = current_time
        
        # Terminal çıktısı ve screenshot kaydetme için zaman kontrolü
        if current_time - last_print_time >= print_interval:
            timestamp = time.strftime("%H:%M:%S", time.localtime(current_time))
            print(f"[{timestamp}] Hareket tespit edildi!")
            
            # Screenshot kaydet
            screenshot_name = f"{screenshot_folder}/hareket_{time.strftime('%Y%m%d_%H%M%S', time.localtime(current_time))}.jpg"
            cv2.imwrite(screenshot_name, frame)
            print(f"Screenshot kaydedildi: {screenshot_name}")
            
            last_print_time = current_time
    
    # Eğer son hareket tespitinden kısa süre geçtiyse yazıyı göster
    if current_time - last_motion_time < motion_text_duration:
        cv2.putText(frame, "HAREKET VAR", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
    
    cv2.imshow("Security Camera", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()