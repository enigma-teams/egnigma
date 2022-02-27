import unicodedata
import json

# Dictionary with rotors and reflector
rotor = {}
reflector = {}


def generate(it):
    for line in it:
        i = ("".join(
            d for d in unicodedata.normalize("NFD", str("".join(line.split())))
            if unicodedata.category(d) != "Mn"))
        if i:
            yield i.upper()


def lecture_message(filename, result):
    with open(filename) as f:
        g = generate(f)
        result.append("".join(g))


def save_message(file_name, message_in):
    with open(file_name, mode="w") as f:
        f.write(message_in)


def load_params(settings_file):
    with open(settings_file, 'r') as p:
        init_rotor_and_reflector(**json.load(p))


def init_rotor_and_reflector(rotors, reflecteurs):
    """ Setting the states of rotors """
    global rotor
    global reflector
    rotor = {str(k): str(rotors.get(k)) for k in rotors}
    reflector = {str(k): str(reflecteurs.get(k)) for k in reflecteurs}


def select_main_rotor_and_reflector(selected_rotor=["RA", "RB", "RC"], selected_reflector="RFB"):
    global rotor
    global reflector
    rotor = {s: rotor.get(s) for s in selected_rotor}
    reflector = reflector.get(selected_reflector)


def rotor_permute(rotor_name, key):
    global rotor
    rotor_value = list(rotor.get(rotor_name))
    for i in range(key):
        rotor_value.insert(0, rotor_value[-1])
        rotor_value.pop(-1)

    rotor.update({rotor_name: "".join(rotor_value)})


def make_reflector(character, key):
    index = list(reflector).index(character)
    return reflector[(index + key) % 26]
