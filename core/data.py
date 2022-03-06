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
    rotor = {s: {"value": rotor.get(s), "rotation": 0}for s in selected_rotor}
    reflector = reflector.get(selected_reflector)


def rotor_permute(rotor_name, key):
    global rotor
    value, rotation = rotor.get(rotor_name).values()
    value = list(value)
    for i in range(key):
        value.insert(0, value[-1])
        value.pop(-1)

    rotor.update({rotor_name: {"value": "".join(value), "rotation": rotation + 1}})


def get_letter(rotor_key, index):
    value, rotation = rotor.get(rotor_key).values()
    return value[index]


def get_index(rotor_key, letter):
    value, rotation = rotor.get(rotor_key).values()
    return list(value).index(letter)


def check_total_rotation(rotor_key):
    value, rotation = rotor.get(rotor_key).values()
    if rotation == 26:
        return True
    return False


def reset_rotation(rotor_key):
    value, rotation = rotor.get(rotor_key).values()
    rotor.update({rotor_key: {"value": value, "rotation": 0}})


def get_letter_reflector(index):
    return reflector[index]


def get_inverse_reflector_position(letter):
    return list(reflector[::-1]).index(letter)
