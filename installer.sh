#!/data/data/com.termux/files/usr/bin/bash
# installer.sh
# Script installer untuk Tool Downloader

echo -e "\033[92m[INFO] Update & upgrade package...\033[0m"
pkg update -y && pkg upgrade -y

echo -e "\033[92m[INFO] Install Python & pip...\033[0m"
pkg install python python-pip -y

echo -e "\033[92m[INFO] Install ffmpeg...\033[0m"
pkg install ffmpeg -y

echo -e "\033[92m[INFO] Install yt-dlp...\033[0m"
pip install yt-dlp

echo -e "\033[92m[INFO] Setup storage Termux...\033[0m"
termux-setup-storage

echo -e "\033[92m[INFO] Semua dependensi sudah terpasang!\033[0m"

echo -e "\033[92m[INFO] Menjalankan downloader1.py...\033[0m"
python downloader1.py
