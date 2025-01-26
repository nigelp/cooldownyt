# ❄️ Cooldown YT

<img src="https://github.com/nigelp/cooldownyt/blob/main/cooldownYT.jpg" alt="Screengrab" width="300" height="200">


**A powerful Python script and GUI for downloading high-quality YouTube videos, playlists and audio with ease! 🎥⚡** Special thanks to Pierre-Henry Soria and his project at pH-7/Download-Simply-Videos-From-YouTube.

This python program not only downloads YouTube content in the highest available quality but also handles multiple formats, subtitles, and thumbnails efficiently. Perfect for content creators and educational purposes! 

- [⚙️ Requirements](#%EF%B8%8F-requirements)
- [📦 Installation](#-installation)
- [🪄 Usage](#-usage)
- [🛠️ Configuration](#%EF%B8%8F-configuration)
- [🤝 Contributing](#-contributing)
- [⚖️ License](#%EF%B8%8F-license)

## ⚙️ Requirements
* [Python v3.7](https://www.python.org/downloads/) or higher 🐍
* FFmpeg installed on your system 🎬
* YouTube URLs (single videos or playlists) that you have permission to download 📝

## 📦 Installation

1. Clone this repository:
   ```console
   git clone https://github.com/nigelp/cooldownyt.git && cd cooldownyt
   ```

2. Install the required Python packages:
   ```console
   pip install -r requirements.txt
   ```

3. Install FFmpeg:
   - **Ubuntu/Debian:**
     ```console
     sudo apt-get install ffmpeg
     ```
   - **macOS:**
     ```console
     brew install ffmpeg
     ```
   - **Windows:**
      Download from the [FFmpeg website](https://ffmpeg.org/download.html), follow the instructions and add to PATH

## 🪄 Usage

To run the application:

1. Start the frontend:
```console
cd frontend && npm run dev
```

2. In another terminal, start the backend server:
```console
python server.py
```
Note: For ease of use you can use Notepad or your fave editor to create and use a .bat file to give you single click access:

@echo off
start cmd /k "cd [yourinstalldirectory]:\downyt\frontend && npm run dev"
timeout /t 5
start cmd /k "cd [yourinstalldirectory]:\downyt && python server.py"

**Features:**
- ✨ Support for both single videos and playlists
- 🎥 High-quality video and optional separate audio downloads
- 📁 Organized folder structure
- 🔄 Format conversion to MP4
- 🎵 MP3 audio extraction option
- ⚡ Error handling and recovery

## 🛠️ Configuration

You can modify the following in the script:
- Video format preferences
- Output directory structure
- Post-processing options

## 🤝 Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## ⚖️ License

This project is distributed under the MIT License 🎉

## ⚠️ Disclaimer

This script is for educational purposes only. Please ensure you have the right to download any content and comply with YouTube's terms of service when using this script.
