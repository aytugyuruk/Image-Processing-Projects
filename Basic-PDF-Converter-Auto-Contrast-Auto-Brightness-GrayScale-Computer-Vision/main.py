import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF
from PIL import Image, ImageEnhance, ImageOps
import io

class PDFProcessorApp:
    def __init__(self, master):
        self.master = master
        master.title("Basit PDF Düzenleyici")
        master.geometry("400x150")

        self.pdf_path = None
        self.output_images = []

        # --- Arayüz Elementleri ---
        self.main_frame = tk.Frame(master, padx=10, pady=10)
        self.main_frame.pack(expand=True)

        self.label = tk.Label(self.main_frame, text="Lütfen bir PDF dosyası seçin.", wraplength=380)
        self.label.pack(pady=10)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=10)

        self.select_button = tk.Button(button_frame, text="PDF Seç", command=self.select_pdf)
        self.select_button.pack(side=tk.LEFT, padx=10)

        self.process_button = tk.Button(button_frame, text="İşlem Yap ve Kaydet", command=self.process_and_save_pdf, state=tk.DISABLED)
        self.process_button.pack(side=tk.LEFT, padx=10)

    def select_pdf(self):
        """Kullanıcının bir PDF dosyası seçmesini sağlayan diyalog penceresini açar."""
        path = filedialog.askopenfilename(
            title="Bir PDF dosyası seçin",
            filetypes=[("PDF Dosyaları", "*.pdf")]
        )
        if path:
            self.pdf_path = path
            # Dosya adını kısaltarak göster
            display_name = self.pdf_path.split('/')[-1]
            if len(display_name) > 40:
                display_name = "..." + display_name[-37:]
            self.label.config(text=f"Seçilen dosya: {display_name}")
            self.process_button.config(state=tk.NORMAL)
            self.output_images = [] # Yeni dosya seçildiğinde eski verileri temizle
            
    def process_and_save_pdf(self):
        """Seçilen PDF'i işler ve kullanıcıdan yeni bir konum isteyerek kaydeder."""
        if not self.pdf_path:
            messagebox.showerror("Hata", "Lütfen önce bir PDF dosyası seçin.")
            return

        try:
            self.label.config(text="Dosya işleniyor, lütfen bekleyin...")
            self.master.update_idletasks() # Arayüzün güncellenmesini sağla

            doc = fitz.open(self.pdf_path)
            processed_pil_images = []

            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap(dpi=200) # Daha iyi kalite için DPI artırıldı
                
                # PyMuPDF pixmap'ini PIL Image objesine dönüştür
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                # 1. Siyah Beyaz (Grayscale) yap
                bw_img = ImageOps.grayscale(img)

                # 2. Parlaklığı artır (Değeri artırarak parlaklığı artırabilirsiniz)
                brightness_enhancer = ImageEnhance.Brightness(bw_img)
                bright_img = brightness_enhancer.enhance(1.2) # %20 parlaklık artışı

                # 3. Kontrastı artır (Değeri artırarak kontrastı artırabilirsiniz)
                contrast_enhancer = ImageEnhance.Contrast(bright_img)
                final_img = contrast_enhancer.enhance(1.4) # %40 kontrast artışı

                # PIL formatında RGB'ye geri dönüştürerek kaydetme uyumluluğunu sağla
                processed_pil_images.append(final_img.convert("RGB"))

            doc.close()

            if not processed_pil_images:
                messagebox.showwarning("Uyarı", "PDF içinde işlenecek sayfa bulunamadı.")
                self.reset_ui()
                return

            # Kaydetme diyaloğunu göster
            save_path = filedialog.asksaveasfilename(
                title="İşlenmiş PDF'i Kaydet",
                defaultextension=".pdf",
                filetypes=[("PDF Dosyaları", "*.pdf")]
            )

            if save_path:
                # İlk sayfayı ve diğerlerini birleştirerek PDF olarak kaydet
                processed_pil_images[0].save(
                    save_path, 
                    save_all=True, 
                    append_images=processed_pil_images[1:]
                )
                messagebox.showinfo("Başarılı", f"Dosya başarıyla kaydedildi:\n{save_path}")
            
            self.reset_ui()

        except Exception as e:
            messagebox.showerror("Bir Hata Oluştu", f"İşlem sırasında bir hata meydana geldi:\n{e}")
            self.reset_ui()
    
    def reset_ui(self):
        """Arayüzü başlangıç durumuna döndürür."""
        self.label.config(text="Lütfen bir PDF dosyası seçin.")
        self.process_button.config(state=tk.DISABLED)
        self.pdf_path = None


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFProcessorApp(root)
    root.mainloop()