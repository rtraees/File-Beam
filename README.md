# ⚡ File Beam - Fast Local WiFi File Transfer

**File Beam** is a lightweight, high-speed file transfer tool that works over your local WiFi network. No internet, cables, or installation required on the client device. Simply run the app, scan the QR code, and start transferring files instantly from any mobile or desktop browser.

Ideally suited for transferring large files (videos, photos, documents) from **Mobile to PC** without cloud uploads or compression.

---

## 🚀 Key Features

- **📂 Cross-Platform**: Works on iOS, Android, Windows, Mac, and Linux via any modern web browser.
- **🔌 Offline Capable**: Fully functional without an internet connection (Local LAN only).
- **🏎️ Blazing Fast**: Transfer speeds are limited only by your router speed (typically 10-50 MB/s).
- **📱 QR Code Connect**: Scan to connect instantly—no typing IP addresses.
- **📦 Batch Uploads**: Select hundreds of files at once without freezing your device.
- **💾 Resume Capability**: Smart chunked uploading ensures large files are transferred reliably.
- **📱 Native-Like UI**: Beautiful, glass-morphism interface that feels like a native app on mobile.

---

## � Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/rtraees/File-Beam/main/server-web-view.png" width="45%" alt="Server View (PC)">
  <img src="https://raw.githubusercontent.com/rtraees/File-Beam/main/client-device-view.png" width="45%" alt="Client View (Mobile)">
</p>

---

## �🛠️ How to Use (Windows Executable)

Use the standalone `.exe` version to run File Beam on any Windows PC without installing Python.

1.  **Download** the latest `File Beam.exe` from [Releases](https://github.com/rtraees/File-Beam/releases).
2.  **Run** the application.
    - A console window will open showing the server logs.
    - Your default web browser will automatically open to the app interface.
3.  **Scan** the QR code displayed on your PC screen using your mobile phone camera.
4.  **Upload** files or folders directly from your phone to your PC.
    - Files are saved in an `uploads` folder located in the same directory as the application.

---

## 👨‍💻 For Developers (Running from Source)

If you want to modify or contribute to the project, follow these steps:

### Prerequisites

- Python 3.x
- pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/rtraees/file-beam.git
    cd file-beam
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

```bash
python file_beam.py
```

### Building the Executable

To create a standalone `.exe` file using PyInstaller:
Double-click `build.bat` or run:

```bash
pyinstaller --noconfirm --onefile --windowed --name "File Beam" --add-data "templates;templates" file_beam.py
```

---

## 📜 Technology Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Modern CSS Variables, Glassmorphism Design
- **Tools**: PyInstaller (for building EXE), QRCode.js, SweetAlert2

---

## 📬 Contact & Author

Developed with ❤️ by **Raees Ul Islam**.

- 📧 **Email**: [rtraees@gmail.com](mailto:rtraees@gmail.com)
- 🌐 **GitHub**: [github.com/rtraees](https://www.github.com/rtraees)
- 👔 **LinkedIn**: [linkedin.com/in/rtraees](https://www.linkedin.com/in/rtraees/)

---

**Keywords**: _Local File Transfer, WiFi File Sharing, Offline AirDrop Alternative, Python File Uploader, Flask File Server, No Internet File Share, Batch Image Upload, Mobile to PC Transfer, Cross-Platform File Tool._
