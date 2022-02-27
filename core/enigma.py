# coding=utf-8
import data

settings_file = "rotors.init"

message_file = "message.txt"

save_file = "sent.txt"


def enigma_machine(message_in, message_out, key=3):
    """
        Fonction de codage/décodage d’un message selon le positionnement
        des rotors et du réflecteur. Les variables sont initialisees par défaut.
    """

    def encrypt(word):
        word = main_encrypt(word, 1)
        word = data.make_reflector(word, key)
        word = main_encrypt(word, -1)
        return word

    def main_encrypt(word, direction):
        for name in list(data.rotor.keys())[::direction]:
            letter_index = list(data.rotor.get(name)).index(word)
            word = data.rotor.get(name)[(letter_index + key) % 26]
            data.rotor_permute(name, key)
        return word

    for letter in message_in:
        message_out.append(encrypt(letter))


def get_use_rotor(keys):
    return [str(data.rotor[key]) for key in data.rotor if key in keys]


def rotor_permute(rotor, key):
    for i in range(key):
        rotor.insert(0, rotor[-1])
        rotor.pop(-1)
    return "".join(rotor)


def begin_lecture_message():
    """ Lit le message à crypter dans le fichier (.txt) """
    try:
        out = []
        file_name = input("File Name : ")
        data.lecture_message(f"{file_name}.txt", out)
        print (out)
    except OSError as e:
        print (f"Le fichier {file_name}.txt n'ai pas trouvable")
    finally:
        menu()


def begin_save_message():
    """ Sauvegarde le message dans le fichier (.cry) """

    message = input("Message = ")
    file_name = input("Fichier de sauvegarde = ")

    data.save_message(f"{file_name}.txt", message)

    print (f"Le message {message} a été sauvegarder dans le fichier {file_name}.txt")

    menu()


def begin_encrypt():
    data.load_params(settings_file)
    for i, r in enumerate(data.rotor.keys()):
        print (f"{i+1} - {r}")

    selected_rotor = []
    for i in range(3):
        rotor_choice = "0"
        while rotor_choice not in list(set([str(c+1) for c in  range(len(data.rotor.keys()))]) - set(selected_rotor)):
            rotor_choice = str(input(f"Rotor {i + 1} = "))
        selected_rotor.append(rotor_choice)


    selected_rotor = [r for i, r in enumerate(data.rotor.keys()) if str(i) in selected_rotor]

    print (selected_rotor)


operations = {
    "1": lambda: begin_lecture_message(),
    "2": lambda: begin_save_message(),
    "3": lambda: begin_encrypt(),
    "4": lambda: exit()
}


def menu():
    print ("Menu de sélection")
    choice = "0"
    print ("1 - Lecture Message")
    print ("2 - Enregistre Message")
    print ("3 - Cryptage/Decryptage")
    print ("4 - Quitter")

    while choice not in operations.keys():
        choice = str(input("choix = "))
    operations.get(choice)()


menu()
