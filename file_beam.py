
import os
import sys
import socket
import threading
import webbrowser
import logging
from flask import Flask, request, jsonify, render_template

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize Flask
# We need to specify the template folder logic for PyInstaller
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)

# Config
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
if getattr(sys, 'frozen', False):
    # If running as exe, put uploads next to exe
    UPLOAD_FOLDER = os.path.join(os.path.dirname(sys.executable), 'uploads')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # distinct doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

@app.route('/', methods=['GET'])
def index():
    ip = get_local_ip()
    return render_template('index.html', ip=ip)

@app.route('/', methods=['POST'])
def handle_actions():
    action = request.form.get('action')
    
    if action == 'check_exists':
        relative_path = request.form.get('relativePath', '')
        name = request.form.get('name', '')
        # Sanitize
        path = relative_path if relative_path else name
        path = path.replace('../', '').replace('..\\', '')
        
        target_path = os.path.join(UPLOAD_FOLDER, path)
        
        if os.path.exists(target_path):
            return jsonify({'status': 'exists'})
        else:
            return jsonify({'status': 'ok'})

    if action == 'upload_chunk':
        try:
            file = request.files.get('file')
            relative_path = request.form.get('relativePath', '')
            name = request.form.get('name', '')
            chunk_index = int(request.form.get('chunkIndex', 0))
            
            if not file:
                return jsonify({'status': 'error', 'message': 'No file'})

            path = relative_path if relative_path else name
            path = path.replace('../', '').replace('..\\', '')
            target_path = os.path.join(UPLOAD_FOLDER, path)

            # Ensure dir
            directory = os.path.dirname(target_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            mode = 'wb' if chunk_index == 0 else 'ab'
            
            with open(target_path, mode) as f:
                f.write(file.read())

            return jsonify({'status': 'success'})

        except Exception as e:
            logging.error(f"Upload error: {e}")
            return jsonify({'status': 'error', 'message': str(e)})

    return jsonify({'status': 'error', 'message': 'Invalid action'})

def open_browser(url):
    webbrowser.open_new(url)

if __name__ == '__main__':
    local_ip = get_local_ip()
    port = 5000
    url = f"http://{local_ip}:{port}/"
    
    print(f"Starting File Beam on {url}")
    print(f"Uploads will be saved to: {UPLOAD_FOLDER}")
    
    # Open browser after short delay
    threading.Timer(1.5, open_browser, args=[url]).start()
    
    # Run server
    app.run(host='0.0.0.0', port=port, debug=False)
