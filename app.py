import os
from flask import Flask, request, jsonify, send_file, after_this_request
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({'error': 'Lütfen geçerli bir link gönderin.'}), 400
        
    url = data['url']
    
    # --- RAM Dostu ve Bot Koruması Ayarları ---
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s_%(id)s.%(ext)s'),
        # RAM'i yormamak için maksimum 720p kalite seçimi
        'format': 'best[height<=720]/bestvideo[height<=720]+bestaudio/best',
        'merge_output_format': 'mp4',
        'quiet': True,
        'no_warnings': True,
        
        # Optimize edici ayarlar
        'noplaylist': True, # Playlistleri engelle, tek video indir
        'max_filesize': 50 * 1024 * 1024, # Maksimum 50 MB sınır (Render'ı çökertmemek için)
        
        # Engel Aşma (Bypass) Ayarları
        'geo_bypass': True,
        'cookiefile': 'cookies.txt', # Kök klasörde bu dosya aranacak
        'http_headers': {
            # Mac ortamını taklit eden User-Agent
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,tr;q=0.8',
            'Sec-Fetch-Mode': 'navigate',
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            base, _ = os.path.splitext(filename)
            mp4_filename = f"{base}.mp4"
            final_file = mp4_filename if os.path.exists(mp4_filename) else filename

        # Sunucunun diski dolmasın diye gönderimden hemen sonra videoyu sil
        @after_this_request
        def remove_file(response):
            try:
                os.remove(final_file)
            except Exception as error:
                app.logger.error(f"Dosya silinirken hata: {error}")
            return response

        return send_file(final_file, as_attachment=True)

    except yt_dlp.utils.DownloadError as e:
        return jsonify({'error': 'Video indirilemedi. Platform engeli veya gizli hesap olabilir.'}), 400
    except Exception as e:
        return jsonify({'error': f'Beklenmeyen bir hata oluştu: {str(e)}'}), 500

if __name__ == '__main__':
    # Render'da çalışırken debug mod kapalı olmalıdır
    app.run(debug=False, port=5000)