# coding=utf-8
import logic
import data
import application as app

settings_file = "rotors.init"

base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

operations = {
    "1": lambda: app.read(),
    "2": lambda: app.save(),
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
        logic.permute(first, 1)

        # I determine the letter corresponding to the position in the first rotor
        first_letter = logic.get_letter(first, first_position)

        # I check if the first rotor has already done 26 revolutions
        if logic.check_total_rotation(first):
            # I spin the second rotor
            logic.permute(second, 1)
            # I reset the rotation number of the first rotor to zero
            logic.reset_rotation(first)

        # I determine the position of the new letter in the alphabet
        second_position = base.index(first_letter)

        # I find the letter corresponding to this position in the second rotor
        second_letter = logic.get_letter(second, second_position)

        # I check if the second rotor has already done 26 revolutions
        if logic.check_total_rotation(second):
            # I spin the third rotor
            logic.permute(third, 1)
            # I reset the rotation number of the second rotor to zero
            logic.reset_rotation(second)

        # I determine the position of the second letter in the alphabet
        third_position = base.index(second_letter)

        # I find the letter corresponding to the new position in the third rotor
        third_letter = logic.get_letter(third, third_position)

        # I determine the position of the third letter in the alphabet
        reflector_position = base.index(third_letter)

        # I determine the letter corresponding to this position in the reflector
        reflector_letter = logic.get_letter_reflector(reflector_position)

        # I reverse the reflector and I determine the position of letter in the reflector
        inverse_reflector_position = logic.get_inverse_reflector_position(reflector_letter)

        # I determine the position of this new letter in the alphabet
        inverse_base_letter_alpha = base[inverse_reflector_position]

        # I determine the position of the new letter in the third rotor
        inverse_third_position = logic.get_index(third, inverse_base_letter_alpha)

        # I determine the position letter of the new letter in the alphabet
        inverse_third_letter_alpha = base[inverse_third_position]

        # I determine the position of the new letter in the second rotor
        inverse_second_position = logic.get_index(second, inverse_third_letter_alpha)

        # I determine the position letter of the new letter in the alphabet
        inverse_second_letter_alpha = base[inverse_second_position]

        # I determine the position of the new letter in the first rotor
        inverse_first_position = logic.get_index(first, inverse_second_letter_alpha)

        # I determine the letter of this position in the alphabet
        response = base[inverse_first_position]

        return response


    for letter in message_in:
        message_out.append(encrypt(letter))


def begin_encrypt():
    app.encrypt()
    # Message to encrypt
    message = input("Message = ")
    g = data.transform(message)
    message = "".join(g)

    print (f"message = {message}")

    # Variable qui reférence object contenant le message crypté
    en = []
    enigma_machine(message, en)

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
