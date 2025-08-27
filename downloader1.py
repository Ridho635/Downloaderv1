import os
import sys
import time
import shutil
import yt_dlp

# ===== Warna dan Style =====
HACKER_GREEN = "\033[92m"
DIM = "\033[2m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ===== Folder Download Android =====
DOWNLOAD_DIR = os.path.expanduser("~/storage/downloads")

# ===== Fungsi Clear Terminal =====
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# ===== Banner Hacker =====
def hacker_banner():
    width = shutil.get_terminal_size((80, 20)).columns
    width = max(70, min(width, 100))

    art = r"""
  ____                          _                     _           
 |  _ \  ___  _ __   ___  _ __| |__   ___  _ __   __| | ___ _ __ 
 | | | |/ _ \| '_ \ / _ \| '__| '_ \ / _ \| '_ \ / _` |/ _ \ '__|
 | |_| | (_) | | | | (_) | |  | | | | (_) | | | | (_| |  __/ |   
 |____/ \___/|_| |_|\___/|_|  |_| |_|\___/|_| |_|\__,_|\___|_|   
    """.splitlines(True)

    top_border    = "┌" + "─" * (width - 2) + "┐\n"
    bottom_border = "└" + "─" * (width - 2) + "┘\n"

    lines = []
    lines.append(HACKER_GREEN + top_border)
    for line in art:
        lines.append(HACKER_GREEN + line.center(width))
    lines.append(HACKER_GREEN + ("─" * width) + "\n")
    lines.append(HACKER_GREEN + BOLD + "DOWNLOADER TOOL By:ridho02".center(width) + RESET + "\n")
    lines.append(HACKER_GREEN + DIM + "mp3/mp4 • YouTube • TikTok • Instagram".center(width) + RESET + "\n")
    lines.append(HACKER_GREEN + ("─" * width) + RESET + "\n")

    info = [
        "[INIT] boot sequence: OK",
        "[NET ] link monitor:  ONLINE",
        "[FFM ] ffmpeg:       READY",
        "[YTDL] yt-dlp:       READY",
        f"[I/O ] storage:      {DOWNLOAD_DIR}"
    ]
    for i in info:
        lines.append(HACKER_GREEN + i.ljust(width) + RESET + "\n")

    lines.append(HACKER_GREEN + bottom_border + RESET)
    return "".join(lines)

def show_banner():
    clear_screen()
    print(hacker_banner())

# ===== Fungsi Download =====
def download_video(url, format_type, quality=None):
    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s'
    }

    if format_type == "mp3":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality or '192',
            }]
        })
    elif format_type == "mp4":
        if quality:
            ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best'
        else:
            ydl_opts['format'] = 'bestvideo+bestaudio/best'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# ===== Menu Format =====
def pilih_format(url):
    while True:
        clear_screen()
        print(hacker_banner())
        print("=== Pilih Format ===")
        print("1. MP3 (Audio)")
        print("2. MP4 (Video)")
        print("0. Back/Kembali")
        pilihan = input("Pilih format: ")

        if pilihan == "0":
            return
        elif pilihan == "1":
            pilih_kualitas_audio(url)
        elif pilihan == "2":
            pilih_resolusi_video(url)
        else:
            input("❌ Pilihan tidak valid! Tekan Enter untuk ulang...")

# ===== Menu Audio =====
def pilih_kualitas_audio(url):
    while True:
        clear_screen()
        print(hacker_banner())
        print("=== Pilih Kualitas Audio ===")
        print("1. 320kbps")
        print("2. 192kbps (default)")
        print("3. 128kbps")
        print("0. Back/Kembali")
        pilihan = input("Pilih: ")

        quality_map = {"1": "320", "2": "192", "3": "128"}

        if pilihan == "0":
            return
        elif pilihan in quality_map:
            download_video(url, "mp3", quality_map[pilihan])
            input("\n✅ Download selesai! Tekan Enter untuk kembali...")
            return
        else:
            input("❌ Pilihan tidak valid! Tekan Enter untuk ulang...")

# ===== Menu Video =====
def pilih_resolusi_video(url):
    while True:
        clear_screen()
        print(hacker_banner())
        print("=== Pilih Resolusi Video ===")
        print("1. 1080p")
        print("2. 720p")
        print("3. 480p")
        print("4. 360p")
        print("5. 144p")
        print("0. Back/Kembali")
        pilihan = input("Pilih: ")

        res_map = {"1": "1080", "2": "720", "3": "480", "4": "360", "5": "144"}

        if pilihan == "0":
            return
        elif pilihan in res_map:
            download_video(url, "mp4", res_map[pilihan])
            input("\n✅ Download selesai! Tekan Enter untuk kembali...")
            return
        else:
            input("❌ Pilihan tidak valid! Tekan Enter untuk ulang...")

# ===== Menu Utama =====
def main():
    if not os.path.exists(DOWNLOAD_DIR):
        os.system("termux-setup-storage")
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    while True:
        show_banner()
        print("1. Masukkan link untuk download")
        print("0. Keluar")
        menu = input("Pilih opsi: ")

        if menu == "0":
            clear_screen()
            print("👋 Terima kasih sudah menggunakan Tool Downloader!")
            break
        elif menu == "1":
            url = input("Masukkan link: ").strip()
            if not url:
                input("❌ Link tidak boleh kosong! Tekan Enter untuk ulang...")
                continue
            pilih_format(url)
        else:
            input("❌ Pilihan tidak valid! Tekan Enter untuk ulang...")

if __name__ == "__main__":
    main()
