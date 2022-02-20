import unicodedata


def LectureMessage(filename, result):
    with open(filename) as f:
        try:
            while f:
                line = f.next()
                line = " ".join(line.split())
                line = "".join(c for c in unicodedata.normalize("NFD", unicode(line, encoding="utf-8")) if
                               unicodedata.category(c) != "Mn")
                result.append(line.upper())
        except StopIteration as s:
            pass


def SauvegardeMessage(file_name, message_to_send):
    with open(file_name, mode="w") as f:
        f.write(message_to_send)


def menu():
    mesg = []
    LectureMessage("message.txt", mesg)

    message = " ".join([c for c in mesg])

    mes = "Nouveau message"

    SauvegardeMessage("sent.txt", mes)
    print (message)


menu()
