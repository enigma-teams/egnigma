import data
import logic


def read():
    """ Lit le message à crypter dans le fichier (.txt) """
    try:
        out = []
        file_name = input("File Name : ")
        data.lecture_message(f"{file_name}.txt", out)
        print (out)
    except OSError as e:
        print (f"Le fichier {file_name}.txt n'ai pas trouvable")


def save():
    """ Sauvegarde le message dans le fichier (.cry) """

    message = input("Message = ")
    file_name = input("Fichier de sauvegarde = ")

    data.save_message(f"{file_name}.txt", message)

    print (f"Le message {message} a été sauvegarder dans le fichier {file_name}.txt")


def encrypt():
    data.load_params("rotors.init")

    selected_rotor = _user_rotors()
    selected_reflector = _user_reflector()

    print (f"Rotors : {selected_rotor}")
    print (f"Reflector = {selected_reflector}")

    logic.change_rotor(selected_rotor)
    logic.change_reflector(selected_reflector)


def _user_rotors():
    selected_rotor = []

    for i, r in enumerate(data.rotor.keys()):
        print (f"{i+1} - {r}")

    # User select 3 rotors
    for i in range(3):
        rotor_choice = "0"
        while rotor_choice not in list(set([str(c + 1) for c in range(len(data.rotor.keys()))]) - set(selected_rotor)):
            rotor_choice = str(input(f"Rotor {i + 1} = "))
        selected_rotor.append(rotor_choice)

    # Ordoné les rotors par ordre choisi par l'utilisateur
    def trie():
        for se in selected_rotor:
            for ind, rot in enumerate(data.rotor.keys()):
                if str(ind + 1) == se:
                    yield rot
    return list(trie())


def _user_reflector():
    # User select reflector
    for i, rf in enumerate(data.reflector.keys()):
        print (f"{i + 1} - {rf}")

    # Vérification du choix de utilisateur pour respecter les options proposé
    reflector_choice = "0"
    while reflector_choice not in [str(r + 1) for r in range(len(data.reflector.keys()))]:
        reflector_choice = str(input(f"Reflector = "))

    reflector_choice = [r for i, r in enumerate(data.reflector.keys()) if str(i + 1) == reflector_choice][0]

    return reflector_choice