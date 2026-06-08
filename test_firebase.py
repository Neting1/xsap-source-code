from app.core.firebase import db

db.collection("test").document("sample").set({
    "name": "Xeonsys",
    "status": "connected"
})

print("Document created successfully")