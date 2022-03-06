# coding=utf-8
import data

settings_file = "rotors.init"

base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

operations = {
    "1": lambda: begin_lecture_message(),
    "2": lambda: begin_save_message(),
    "3": lambda: begin_encrypt(),
    "5": lambda: exit()
}


def enigma_machine(message_in, message_out):
    """
        Fonction de codage/décodage d’un message selon le positionnement
        des rotors et du réflecteur. Les variables sont initialisees par défaut.
    """

    def encrypt(word):

        # Je détermine la position de la lettre dans l'aphabet
        first_position = base.index(word)

        first, second, third = list(data.rotor.keys())

        # Je Fait pivoter le rotor
        data.rotor_permute(first, 1)

        # Je détermine si le lettre correspondant a la position
        first_letter = data.get_letter(first, first_position)

        # Je verifie si le premier rotor a déjà fait 26 tours
        if data.check_total_rotation(first):
            # Je fait pivoter le second rotor
            data.rotor_permute(second, 1)
            # Je remet le nombre de rotation du premier rotor a zéro
            data.reset_rotation(first)

        # Je détermine la position de la lettre {first_letter} dans l'aphabet
        second_position = base.index(first_letter)

        # Je trouve la lettre corespondante a cette position dans le second rotor
        second_letter = data.get_letter(second, second_position)

        # Je vérifie si le deuxième rotor a déjà fait 26 tours
        if data.check_total_rotation(second):
            # Je fait pivoter le {third} rotor
            data.rotor_permute(third, 1)
            # Je remet le nombre de rotation du {second} rotor à zéro
            data.reset_rotation(second)

        # Je détermine la position de {second_letter} dans l'alphabet
        third_position = base.index(second_letter)

        # Je trouve la  lettre corespondante a la {third_position} dans {third} rotor
        third_letter = data.get_letter(third, third_position)

        # Je détermine la position de {third_letter} dans l'alphabet
        reflector_position = base.index(third_letter)

        # Je détermine la lettre corespondante a {reflector_position} dans le reflector
        reflector_letter = data.get_letter_reflector(reflector_position)

        # J'inverse le réflecteur et je détermine la position de {reflector_letter} dans le reflecteur
        inverse_reflector_position = data.get_inverse_reflector_position(reflector_letter)

        # Je determine la lettre de position de {inverse_reflector_position} dans l'alphabet
        inverse_base_letter_alpha = base[inverse_reflector_position]

        # Position de {inverse_base_letter_alpha} dans le third rotor
        inverse_third_position = data.get_index(third, inverse_base_letter_alpha)

        # Je determine la lettre de position de {inverse_third_position} dans l'alphabet
        inverse_third_letter_alpha = base[inverse_third_position]

        # Position de {inverse_third_letter_alpha} dans le second rotor
        inverse_second_position = data.get_index(second, inverse_third_letter_alpha)

        # Je determine la lettre de position de {inverse_second_position} dans l'alphabet
        inverse_second_letter_alpha = base[inverse_second_position]

        # Position de {inverse_second_letter_alpha} dans le first rotor
        inverse_first_position = data.get_index(first, inverse_second_letter_alpha)

        # Je determine la lettre de position de {inverse_first_position} dans l'alphabet
        response = base[inverse_first_position]

        return response


    for letter in message_in:
        message_out.append(encrypt(letter))


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
    """ Load settings in rotor.init """
    data.load_params(settings_file)
    for i, r in enumerate(data.rotor.keys()):
        print (f"{i+1} - {r}")

    # User select 3 rotors
    selected_rotor = []
    for i in range(3):
        rotor_choice = "0"
        while rotor_choice not in list(set([str(c+1) for c in  range(len(data.rotor.keys()))]) - set(selected_rotor)):
            rotor_choice = str(input(f"Rotor {i + 1} = "))
        selected_rotor.append(rotor_choice)


    # Ordoné les rotors par ordre choisi par l'utilisateur
    def trie():
        for se in selected_rotor:
            for ind, rot in enumerate(data.rotor.keys()):
                if str(ind+1) == se:
                    yield rot

    # liste des rotors sélectionné par utilisateur
    selected_rotor = list(trie())

    print (f"Rotors : {selected_rotor}")

    # User select reflector
    for i, rf in enumerate(data.reflector.keys()):
        print (f"{i + 1} - {rf}")

    # Vérification du choix de utilisateur pour respecter les options proposé
    reflector_choice = "0"
    while reflector_choice not in [str(r+1) for r in range(len(data.reflector.keys()))]:
        reflector_choice = str(input(f"Reflector = "))

    reflector_choice = [r for i, r in enumerate(data.reflector.keys()) if str(i+1) == reflector_choice][0]

    print (f"Reflector = {reflector_choice}")

    # Message to encrypt
    message = input("Message = ")

    file_name = input("Fichier = ")

    data.save_message(f"{file_name}.txt", message)

    # Initialisation des rotors et des réflectors dans la partie DATA
    data.select_main_rotor_and_reflector(selected_rotor, reflector_choice)
    
    # Variable qui reférence object contenant le message préformaté
    out = []
    data.lecture_message(f"{file_name}.txt", out)

    print (f"message = {out[0]}")

    # Variable qui reférence object contenant le message crypté
    en = []
    enigma_machine(out[0], en)

    print (f"message codé : {''.join(en)}")


def menu():
    print ("Menu de sélection")
    print ("1 - Lecture Message")
    print ("2 - Enregistre Message")
    print ("3 - Cryptage/Decryptage")
    print ("4 - Quitter")

    choice = "0"
    while choice not in operations.keys():
        choice = str(input("choix = "))
    operations.get(choice)()


menu()
