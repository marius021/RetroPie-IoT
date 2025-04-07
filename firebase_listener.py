import firebase_admin
from firebase_admin import credentials, firestore
import time
import os

#Initializare Firebase
cred = credentials.Certificate('/home/maurice/retropie-iot-firebase-adminsdk-fbsvc-b8ac8afda4.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

#Functie care proceseaza comezile
def on_snapshot(col_snapshot, changes, read_time):
    for change in changes:
        command = change.document.to_dict()
        print(f"Comanda primita: {command}")

        #Exemplu simplu de actiuni posibile
        if command['action'] =='reboot':
            print("Repornire Raspberry Pi!")
            # os.system('sudo reboot') # real reboot

        elif command['action'] == 'shutdown':
            print("Oprire Raspberry Pi!")
            #os.system('sudo shutdown now') # real shutdown

        elif command['action'] == 'message':
            print(f"Mesaj primit: {command['text']}")

        # dupa executie, se sterge comanda pentru a nu se repeta
        db.collection('device_commands').document(change.document.id).delete()

# Listener Firestore in timp real
commands_ref = db.collection('device_commands')
querry_watch = commands_ref.on_snapshot(on_snapshot)

# Ruleaza permanent scriptul
print('Listener Firebase activat, astept comenzi ...')
while True:
    time.sleep(1)