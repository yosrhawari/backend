import bcrypt

# On n'utilise plus du tout passlib ni CryptContext
# On utilise directement les fonctions de la bibliothèque bcrypt

def hash_password(password: str) -> str:
    """Transforme un mot de passe en texte clair en un hash sécurisé"""
    # 1. Convertir le string en bytes (obligatoire pour bcrypt)
    pwd_bytes = password.encode('utf-8')
    
    # 2. Générer un "sel" (salt) aléatoire
    salt = bcrypt.gensalt()
    
    # 3. Créer le hash
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    
    # 4. On décode en string pour pouvoir l'enregistrer facilement en BDD
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Vérifie si le mot de passe saisi correspond au hash de la BDD"""
    # On convertit tout en bytes pour la comparaison
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    
    # La fonction checkpw gère elle-même la sécurité de la comparaison
    return bcrypt.checkpw(password_bytes, hashed_bytes)