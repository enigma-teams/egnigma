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

        # I determine the position of the letter in the alphabet
        first_position = base.index(word)

        first, second, third = list(data.rotor.keys())

        # I spin the first rotor
        data.rotor_permute(first, 1)

        # I determine the letter corresponding to the position in the first rotor
        first_letter = data.get_letter(first, first_position)

        # I check if the first rotor has already done 26 revolutions
        if data.check_total_rotation(first):
            # I spin the second rotor
            data.rotor_permute(second, 1)
            # I reset the rotation number of the first rotor to zero
            data.reset_rotation(first)

        # I determine the position of the new letter in the alphabet
        second_position = base.index(first_letter)

        # I find the letter corresponding to this position in the second rotor
        second_letter = data.get_letter(second, second_position)

        # I check if the second rotor has already done 26 revolutions
        if data.check_total_rotation(second):
            # I spin the third rotor
            data.rotor_permute(third, 1)
            # I reset the rotation number of the second rotor to zero
            data.reset_rotation(second)

        # I determine the position of the second letter in the alphabet
        third_position = base.index(second_letter)

        # I find the letter corresponding to the new position in the third rotor
        third_letter = data.get_letter(third, third_position)

        # I determine the position of the third letter in the alphabet
        reflector_position = base.index(third_letter)

        # I determine the letter corresponding to this position in the reflector
        reflector_letter = data.get_letter_reflector(reflector_position)

        # I reverse the reflector and I determine the position of letter in the reflector
        inverse_reflector_position = data.get_inverse_reflector_position(reflector_letter)

        # I determine the position of this new letter in the alphabet
        inverse_base_letter_alpha = base[inverse_reflector_position]

        # I determine the position of the new letter in the third rotor
        inverse_third_position = data.get_index(third, inverse_base_letter_alpha)

        # I determine the position letter of the new letter in the alphabet
        inverse_third_letter_alpha = base[inverse_third_position]

        # I determine the position of the new letter in the second rotor
        inverse_second_position = data.get_index(second, inverse_third_letter_alpha)

        # I determine the position letter of the new letter in the alphabet
        inverse_second_letter_alpha = base[inverse_second_position]

        # I determine the position of the new letter in the first rotor
        inverse_first_position = data.get_index(first, inverse_second_letter_alpha)

        # I determine the letter of this position in the alphabet
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
