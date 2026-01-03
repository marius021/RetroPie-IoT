# RetroPie-IoT

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi-red.svg)](https://retropie.org.uk/)
[![Language](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/)

**RetroPie-IoT** este un proiect care extinde funcționalitățile clasice ale consolei [RetroPie](https://retropie.org.uk/) integrând capabilități IoT (Internet of Things). Acest proiect permite interacțiunea dintre consola ta de gaming și mediul înconjurător prin senzori, lumini ambientale și automatizări inteligente.

## 📝 Cuprins

- [Descriere](#descriere)
- [Funcționalități](#funcționalități)
- [Cerințe Hardware](#cerințe-hardware)
- [Cerințe Software](#cerințe-software)
- [Instalare](#instalare)
- [Configurare](#configurare)
- [Utilizare](#utilizare)
- [Contribuții](#contribuții)
- [Licență](#licență)

## 📖 Descriere

Acest proiect a fost creat din dorința de a transforma un simplu Raspberry Pi cu RetroPie într-un hub inteligent. Fie că dorești să controlezi viteza ventilatorului în funcție de temperatura procesorului, să aprinzi lumini LED reactive la jocuri sau să monitorizezi statistici de sistem de la distanță, **RetroPie-IoT** oferă scripturile și configurațiile necesare.

## ✨ Funcționalități

* 📊 **Dashboard IoT:** Trimiterea datelor de telemetrie (FPS, temperatură, utilizare RAM) către un server MQTT sau dashboard web.
* 🔘 **Butoane Fizice:** Suport pentru butoane externe de pornire/oprire sigură (Safe Shutdown) sau reset.


## 🛠 Cerințe Hardware

* **Raspberry Pi** (3B+, 4B, 400 sau 5)
* Card MicroSD (minim 16GB)
* Sursă de alimentare adecvată
* *Opțional:* Ventilator PWM 5V
* *Opțional:* Bandă LED adresabilă


## 💻 Software implementat
•	RetroPie (platforma bazata pe Raspberry Pi OS, specializata in emularea jocurilor retro);
•	Emulatori specifici integrati in RetroPie:
o	PSX: lr-pcsx-rearmed
o	PSP: ppsspp
o	PS2: aethersx2
•	Python pentru dezvoltarea scripturilor de monitorizare automata;
•	Firebase Admin SDK (pentru găzduirea interfeței web interactive);
•	HTML, CSS, JavaScript pentru dezvoltarea dashboard-ului web;
•	Chart.js (pentru afișarea grafica interactiva a statisticilor).



## 🚀 Instalare

1.  **Clonează repository-ul:**
    Accesează terminalul pe Raspberry Pi (prin SSH sau F4 pe tastatură) și rulează:

    ```bash
    cd /home/pi/
    git clone [https://github.com/marius021/RetroPie-IoT.git](https://github.com/marius021/RetroPie-IoT.git)
    cd RetroPie-IoT
    ```

2.  **Instalează dependențele:**
    Rulați scriptul de instalare (dacă există) sau instalați manual bibliotecile:

    ```bash
    sudo chmod +x install.sh
    ./install.sh
    # Sau manual:
    # pip3 install -r requirements.txt
    ```

## ⚙️ Configurare

Editează fișierul de configurare `config.ini` (sau `settings.py`) pentru a seta pinii GPIO și preferințele tale:

```bash
nano config.ini
