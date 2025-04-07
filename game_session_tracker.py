import time
import psutil
import os
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import urllib.parse

# 🔐 Inițializare Firebase
cred = credentials.Certificate("/home/maurice/retropie-iot-firebase-adminsdk-fbsvc-b8ac8afda4.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Pentru a evita sesiuni duplicate
tracked_pids = set()

# Detectare platformă din calea ROM-ului
def detect_platform_from_path(rom_path):
    rom_path_lower = rom_path.lower()
    if "/roms/psx/" in rom_path_lower:
        return "psx"
    elif "/roms/ps2/" in rom_path_lower:
        return "ps2"
    elif "/roms/psp/" in rom_path_lower:
        return "psp"
    elif "/roms/nes/" in rom_path_lower:
        return "nes"
    elif "/roms/snes/" in rom_path_lower:
        return "snes"
    elif "/roms/gba/" in rom_path_lower:
        return "gba"
    elif "/roms/gb/" in rom_path_lower:
        return "gb"
    elif "/roms/n64/" in rom_path_lower:
        return "n64"
    else:
        return "unknown"

def detect_new_session():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            name = proc.info['name']
            cmd = proc.info['cmdline']
            pid = proc.info['pid']

            if not name or not cmd or pid in tracked_pids:
                continue

            # 🔍 Caută primul argument care pare a fi un ROM valid
            rom_path = None
            rom_extensions = ('.iso', '.chd', '.cue', '.bin', '.img', '.zip', 'cso')

            for arg in cmd:
                if arg.lower().endswith(rom_extensions):
                    rom_path = arg
                    break

            if not rom_path:
                continue  # Nu e sesiune reală de joc

            game_raw = os.path.splitext(os.path.basename(rom_path))[0]
            game = urllib.parse.unquote(game_raw).replace("\\", "").strip()

            platform = detect_platform_from_path(rom_path)

            tracked_pids.add(pid)
            start_time = datetime.now()
            print(f"[START] {game} ({platform})")

            # Așteaptă închiderea procesului
            while psutil.pid_exists(pid):
                time.sleep(2)

            end_time = datetime.now()
            duration = end_time - start_time
            duration_str = str(duration)

            session_data = {
                "session_name": f"{game} - {start_time.strftime('%Y-%m-%d %H:%M:%S')}",
                "game": game,
                "platform": platform,
                "start_time": start_time.isoformat(),
                "end_time": end_time.isoformat(),
                "duration": duration_str
            }

            db.collection("games_sessions").add(session_data)
            print(f"[STOP] Sesiune salvată în Firebase: {session_data}")

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == "__main__":
    print("🎮 Ascultă sesiuni de emulator...")
    while True:
        detect_new_session()
        time.sleep(2)
