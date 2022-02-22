import unicodedata


def lecture_message(filename, result):
    with open(filename) as f:
        g = generate(f)
        result.append("".join(g))


def generate(it):
    for line in it:
        i = ("".join(
            d for d in unicodedata.normalize("NFD", unicode("".join(line.split()), encoding="utf-8"))
            if unicodedata.category(d) != "Mn"))
        if i:
            yield i.upper()


def save_message(file_name, message_to_send):
    with open(file_name, mode="w") as f:
        f.write(message_to_send)


def menu():
    message_to_sent = []
    lecture_message("message.txt", message_to_sent)

    message = message_to_sent[0]

    mes = "Nouveau message"

    save_message("sent.txt", mes)
    print (message)


menu()
