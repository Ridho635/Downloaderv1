# Downloader tool V1 by: ridho02
## penjelasan singkat 
Tools ini di peruntukan untuk download video/audio lewat termux/Ubuntu dari sebuah link 
YouTube.tuktok.Instagram dan bisa memiliki mau resolusi berapa yang ingin di download 
video/mp4=144p-1080 audio/mp3=128kbs-320kbs

## ⚙️ Versi minimal yang dibutuhkan
Python   >= 3.9
pip      >= 21
yt-dlp   >= 2025.01.15
ffmpeg   >= 4.4
git      >= 2.34

## 📥 Installation
```bash
pkg update -y && pkg upgrade -y && \
pkg install git -y && \
git clone https://github.com/Ridho635/Downloaderv1.git && \
cd Downloaderv1 && \
chmod +x installer.sh && \
./installer.sh
