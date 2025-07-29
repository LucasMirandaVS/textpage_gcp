from google.cloud import firestore

db = firestore.Client()
collection = db.collection("leads")

def save_lead(name: str, email: str):
    doc = {
        "name": name,
        "email": email,
        "status": "new",
        "created_at": firestore.SERVER_TIMESTAMP,
        "updated_at": firestore.SERVER_TIMESTAMP,
        "source": "web_form"
    }
    collection.add(doc)
