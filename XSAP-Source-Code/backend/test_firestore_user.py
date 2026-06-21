from app.core.firebase import db

db.collection("users").document("admin").set({
    "full_name": "XSAP Administrator",
    "email": "admin@xeonsys.com",
    "role": "admin",
    "status": "active"
})

print("User profile saved")