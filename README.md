# textpage_gcp
graph TD
  User[Usuário - Browser]
  Hosting[Firebase Hosting]
  CF[Cloud Function (Python)]
  Firestore[(Firestore DB)]

  User --> Hosting --> CF --> Firestore

