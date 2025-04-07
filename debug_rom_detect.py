import psutil
import os

print("🔍 Proces emulator activ:")

for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        name = proc.info['name']
        cmd = proc.info['cmdline']
        pid = proc.info['pid']

        if not name or not cmd:
            continue

        # Filtrăm doar emulatoarele care ne interesează
        if any(em in name.lower() for em in ["retroarch", "aethersx2", "ppsspp"]):
            print(f"\n📦 Proces: {name}")
            print(f"🔢 PID: {pid}")
            print(f"📜 Cmdline: {cmd}")

            if len(cmd) > 1:
                rom_path = cmd[-1]
                game = os.path.splitext(os.path.basename(rom_path))[0]
                print(f"🎮 ROM detectat: {rom_path}")
                print(f"🕹️  Joc extras: {game}")
            else:
                print("⚠️  Nu am găsit ROM în linia de comandă!")

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue
