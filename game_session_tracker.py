import time
import psutil
import os
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
from pathlib import Path

cred = credentials.Certificate("/home/")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Emulatoare cunoscute și extensii asociate
KNOWN_EMULATORS = {
    "retroarch": "generic",
    "pcsx2": "ps2",
    "pcsx": "psx"
}

# Reține procesele pe care le-am urmărit deja
tracked_pids = set()

def detect_new_session():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            name = proc.info['name']
            cmd = proc.info['cmdline']
            pid = proc.info['pid']

            if not name or not cmd or pid in tracked_pids:
                continue

            for emulator, platform in KNOWN_EMULATORS.items():
                if emulator in name.lower():
                    rom_path = cmd[-1] if len(cmd) > 1 else "ROM necunoscut"
                    game = os.path.splitext(os.path.basename(rom_path))[0]
                    print(f"[START] {game} ({platform})")

                    tracked_pids.add(pid)
                    start_time = datetime.now()

                    # Așteaptă finalizarea procesului
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
    print("🔎 Ascultă sesiuni de emulator...")
    while True:
        detect_new_session()
        time.sleep(2)
