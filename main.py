import argparse
import random
import string

def generate_pwd(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_credentials(username, password):
    try:
        with open('credentials.txt', 'a') as file:
            file.write(f'Benutzername: {username}\n')
            file.write(f'Passwort: {password}\n\n')
    except Exception as e:
        print(f"Fehler beim Speichern der Datei: {e}")
        exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Passwortgenerator')
    parser.add_argument('--l', type=int, default=16, help='Länge des Passworts (Standard: 16)')
    parser.add_argument('--u', nargs='+', type=str, required=True, help='Nutzernamen (mindestens einer)')
    args = parser.parse_args()

    password_length = args.l

    with open('credentials.txt', 'w') as file:
        file.write('')

    for username in args.m:
        password = generate_pwd(password_length)
        try:
            save_credentials(username, password)
        except Exception as e:
            print(f"Fehler beim Speichern der Anmeldedaten für {username}: {e}")
            exit(1)

        print(f'Benutzername: {username}\nPasswort: {password}\n')