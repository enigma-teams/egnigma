import data


def permute(name, key):
    """ Permute a rotor"""
    value, rotation = data.rotor.get(name).values()
    value = list(value)
    for i in range(key):
        value.insert(0, value[-1])
        value.pop(-1)

    data.rotor.update({name: {"value": "".join(value), "rotation": rotation + 1}})


def change_rotor(selected_rotor=["RA", "RB", "RC"]):
    """ Change rotor witch a user selection"""
    data.rotor = {s: {"value": data.rotor.get(s), "rotation": 0}for s in selected_rotor}


def change_reflector(selected_reflector="RFB"):
    """ Change reflector witch user selection"""
    data.reflector = data.reflector.get(selected_reflector)


def get_letter(key, index):
    """ Get letter inside reflector"""

    value, rotation = data.rotor.get(key).values()
    return value[index]


def get_index(key, letter):
    """ Get index of letter inside rotor"""
    value, rotation = data.rotor.get(key).values()
    return list(value).index(letter)


def check_total_rotation(key):
    """ Check if rotor have do 26 tours"""
    value, rotation = data.rotor.get(key).values()
    if rotation == 26:
        return True
    return False


def reset_rotation(key):
    """ Reset rotation to zero"""
    value, rotation = data.rotor.get(key).values()
    data.rotor.update({key: {"value": value, "rotation": 0}})


def get_letter_reflector(index):
    return data.reflector[index]


def get_inverse_reflector_position(letter):
    return list(data.reflector[::-1]).index(letter)
