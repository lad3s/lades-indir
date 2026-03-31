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


örnek
<?xml version="1.0"?>
<flowgorithm fileversion="3.0">
    <attributes>
        <attribute name="name" value="RLC Devresi Karakteristik Hesaplama"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="R, L, C, alpha, omega0" type="Real" array="False" size=""/>
            
            <output expression="&quot;Direnç (R) değerini giriniz (Ohm):&quot;" newline="True"/>
            <input variable="R"/>
            
            <output expression="&quot;İndüktans (L) değerini giriniz (Henry):&quot;" newline="True"/>
            <input variable="L"/>
            
            <output expression="&quot;Kapasitans (C) değerini giriniz (Farad):&quot;" newline="True"/>
            <input variable="C"/>
            
            <assign variable="alpha" expression="R / (2 * L)"/>
            <assign variable="omega0" expression="1 / sqrt(L * C)"/>
            
            <if expression="alpha &gt; omega0">
                <then>
                    <output expression="&quot;Devre Karakteristiği: AŞIRI SÖNÜMLÜ (Overdamped)&quot;" newline="True"/>
                </then>
                <else>
                    <if expression="alpha == omega0">
                        <then>
                            <output expression="&quot;Devre Karakteristiği: KRİTİK SÖNÜMLÜ (Critically Damped)&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Devre Karakteristiği: EKSİK SÖNÜMLÜ / SALINIMLI (Underdamped)&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>
