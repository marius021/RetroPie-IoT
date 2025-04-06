import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

#initializare firebase
cred = credentials.Certificate('/home/maurice/retropie-iot-firebase-adminsdk-fbsvc-b8ac8afda4.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

#exemplu de date dintr-o sesiune de joc

game_session = {
    'game' : 'Super Mario Bros',
    'platform' : 'NES',
    'duration_minutes' : 45,
    'timestamp' : datetime.now().isoformat()
}

# salvare date in firestore
doc_ref = db.collection('games_sessions').add(game_session)

print(f'Datele au fost salvate in Firestore cu ID: {doc_ref[1].id}')