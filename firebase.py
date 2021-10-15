import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Fetch the service account key JSON file contents
cred = credentials.Certificate(
    "pc-feedback-app-firebase-adminsdk-ydw0b-76e2f09b5f.json"
)
firebase_admin.initialize_app(cred)

db = firestore.client()