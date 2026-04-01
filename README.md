# 🚀 LADES - Video Downloader

[TR] LADES, basitlik ve performans odaklı geliştirilmiş, modern bir video indirme platformudur.
[EN] LADES is a modern video downloading platform developed with a focus on simplicity and performance.

---

## 📌 Proje Amacı / Project Purpose

**[TR]** Bu projenin temel amacı, kullanıcıların farklı platformlardaki videoları herhangi bir karmaşa yaşamadan, hızlı ve güvenli bir şekilde indirmelerini sağlamaktır. Sunucu kaynaklarını yormayan (RAM dostu) yapısı ve mobil uyumlu arayüzü ile her cihazda akıcı bir deneyim sunar.

**[EN]** The main goal of this project is to enable users to download videos from various platforms quickly and securely without any complexity. With its server-friendly (RAM-efficient) structure and mobile-responsive interface, it provides a smooth experience on all devices.

---

## ✨ Özellikler / Features

- **🚀 Performance:** RAM dostu 720p kalite seçimi. / RAM-friendly 720p quality selection.
- **🛡️ Security:** Sunucu güvenliği için 50,0 MB dosya boyutu sınırı. / 50,0 MB file size limit for server safety.
- **📱 Responsive:** Mobil cihazlarla tam uyumlu arayüz. / Fully compatible interface with mobile devices.
- **🌍 Multi-Language:** Türkçe ve İngilizce dil desteği. / Turkish and English language support.
- **🧹 Auto-Clean:** İndirilen dosyalar gönderildikten hemen sonra sunucudan silinir. / Downloaded files are deleted from the server immediately after being sent.

---

## 🛠️ Teknik Yığın / Tech Stack

- **Backend:** Python, Flask, yt-dlp
- **Frontend:** HTML5, CSS3 (Tailwind/Modern UI), JavaScript

---

## 🚧 Geliştirme Aşaması / Under Development

**[TR]** ⚠️ **Not:** Bu proje henüz geliştirme aşamasındadır. Yakın zamanda yeni platform destekleri, MP3 dönüştürücü ve daha gelişmiş indirme eklentileri sisteme dahil edilecektir. Takipte kalın!

**[EN]** ⚠️ **Note:** This project is currently under development. New platform supports, MP3 converters, and more advanced downloading extensions will be added soon. Stay tuned!

---

## ⚙️ Kurulum / Installation

```bash
# Depoyu klonlayın / Clone the repo
git clone [https://github.com/kullanici_adin/LADES.git](https://github.com/kullanici_adin/LADES.git)

# Kütüphaneleri kurun / Install requirements
pip install -r requirements.txt

# Uygulamayı çalıştırın / Run the app
python app.py
ödev
% Uydu ve Antenler Dersi Hesaplama Programı
% Bu kod döngüsel bir yapıda çalışır ve kullanıcı çıkış yapana kadar devam eder.

devam_et = true;

% Şık Karşılama Ekranı
disp('***************************************************************');
disp('* Dokuz Eylül - Elektronik Haberleşme Teknolojisi        *');
disp('* Uydu Bilgi Hesaplama Sistemine                *');
disp('* HOŞ GELDİN LADES!                    *');
disp('***************************************************************');

while devam_et
    disp(' ');
    disp('Lütfen hesaplama yapmak için aşağıdaki değerleri giriniz:');
    disp('(Not: Ondalıklı değer girerken program dili gereği nokta kullanınız)');
    
    % Kullanıcıdan açı değerlerini alma
    yatay_aci = input('Yatay Açı değerini giriniz (Derece): ');
    kutup_acisi = input('Kutup Açısı değerini giriniz (Derece): ');
    yukseklik_acisi = input('Yükseklik Açısı değerini giriniz (Derece): ');

    % --- FORMÜL BÖLÜMÜ (Proton Basic'e aktarılacak kısımlar) ---
    % Değişkenleri Proton Basic mantığına uygun şekilde sade tuttum.
    disp(' ');
    disp('Uydu bilgileri hesaplanıyor...');
    pause(1); % Ekrana şık bir bekleme ve işlem efekti katar

    % Radyana çevirme işlemleri (Octave trigonometrik fonksiyonları radyan kullanır)
    yatay_rad = yatay_aci * (pi / 180);
    yukseklik_rad = yukseklik_acisi * (pi / 180);
    kutup_rad = kutup_acisi * (pi / 180);

    % Örnek Uydu Yönelim Vektörü Hesaplamaları
    % (Kendi dersindeki spesifik formülleri buradaki X, Y, Z yerine yazabilirsin)
    X_ekseni = cos(yukseklik_rad) * cos(yatay_rad);
    Y_ekseni = cos(yukseklik_rad) * sin(yatay_rad);
    Z_ekseni = sin(yukseklik_rad);

    % --- SONUÇLARI YAZDIRMA ---
    disp('---------------------------------------------------------------');
    disp('UYDU BİLGİLERİ (HESAPLANAN DEĞERLER):');
    printf('Yönelim Vektörü X: %f\n', X_ekseni);
    printf('Yönelim Vektörü Y: %f\n', Y_ekseni);
    printf('Yönelim Vektörü Z: %f\n', Z_ekseni);
    disp('---------------------------------------------------------------');

    % Tekrar deneme veya çıkış yapma seçenekleri
    cevap = input('\nBaşka bir hesaplama yapmak ister misin? (Evet için E, Hayır için H): ', 's');

    if strcmpi(cevap, 'H') || strcmpi(cevap, 'Hayır')
        devam_et = false; % Döngüyü kırar
        disp(' ');
        disp('***************************************************************');
        disp('Program sonlandırılıyor... Çalışmalarında başarılar, görüşmek üzere!');
        disp('***************************************************************');
    end
end
