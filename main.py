import argparse
import random
import string

def generate_pwd(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_credentials(username, password):
    try:
        with open('credentials.txt', 'w') as file:
            file.write(f'Benutzername: {username}\n')
            file.write(f'Passwort: {password}')
    except Exception as e:
        print(f"Fehler beim Speichern der Datei: {e}")
        exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Passwortgenerator')
    parser.add_argument('username', type=str, help='Nutzername')
    parser.add_argument('--l', type=int, default=16, help='Länge')
    args = parser.parse_args()

    username = args.username
    password_length = args.l

    if password_length <= 0:
        print("Fehler: Die Passwortlänge muss größer als 0 sein.")
        exit(1)

    password = generate_pwd(password_length)
    
    try:
        save_credentials(username, password)
    except Exception as e:
        print(f"Fehler beim Speichern der Anmeldedaten: {e}")
        exit(1)

    print(f'Benutzername: {username}\nPasswort: {password}')