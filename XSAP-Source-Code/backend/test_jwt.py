from app.security.jwt import create_access_token
from app.security.jwt import verify_access_token


token = create_access_token(
    {
        "sub": "admin@xeonsys.com"
    }
)

print("TOKEN:")
print(token)

print("\nPAYLOAD:")
print(verify_access_token(token))