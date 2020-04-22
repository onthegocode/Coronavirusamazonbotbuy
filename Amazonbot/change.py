import json
import os


def clear(): return os.system('cls')


def main():

    choice = input(
        'Do you want to change your email and password? y or n').upper()
    clear()
    if choice == 'Y':
        x = input("Email: ")
        clear()
        i = input('Password: ')
        clear()
        dictionary = {
            "Email": x,
            "Password": i}
        content = open('u_s.json').read()
        config = json.loads(content)
        email = config['Email']
        password = config['Password']

        with open("u_s.json", "w") as outfile:
            json.dump(dictionary, outfile)

        content = open('u_s.json').read()
        config = json.loads(content)
        email = config['Email']
        password = config['Password']
        print(f'\n\nYour Email is: {email}')
        print(f'\nYour Password is: {password}')
        print('\n\n\n\nAll Done Thank You! :D\n\n')


if __name__ == '__main__':
    main()
