import os
from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

# İndirilen videoların geçici olarak tutulacağı klasör
DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({'error': 'Lütfen geçerli bir link gönderin.'}), 400
        
    url = data['url']
    
    # yt-dlp ayarları
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s_%(id)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'quiet': True,
        'no_warnings': True,
        # Not: Video ve sesi birleştirmek (bestvideo+bestaudio) için
        # Macbook'unuzda FFmpeg kurulu olması gerekebilir (brew install ffmpeg).
        # Aksi takdirde yt-dlp otomatik olarak tek parça en iyi kaliteyi (best) indirecektir.
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Video bilgilerini al ve indir
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            # Format dönüşümü yapıldıysa (örneğin mkv -> mp4) doğru dosyayı bulmak için
            base, _ = os.path.splitext(filename)
            mp4_filename = f"{base}.mp4"
            
            if os.path.exists(mp4_filename):
                final_file = mp4_filename
            else:
                final_file = filename

        # Dosyayı kullanıcıya gönder
        return send_file(final_file, as_attachment=True)

    except yt_dlp.utils.DownloadError as e:
        # Link hatalıysa veya platform desteklenmiyorsa yt-dlp DownloadError fırlatır
        return jsonify({'error': 'Video indirilemedi veya desteklenmeyen/hatalı link.'}), 400
    except Exception as e:
        # Diğer beklenmedik sunucu hataları
        return jsonify({'error': f'Beklenmeyen bir hata oluştu: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)