# egnigma
Simulation de la machine Enigma

# Objectifs

L'objectif du projet est de concevoir un programme qui simule la machine Enigma. 
Le projet sera codé avec la version `3` du langage de programmation <b>Python</b>.

Chaque message à transmettre sera reformater de sorte à enlever les <b>accents</b>, les <b>espaces</b>. Nous utilisons la librairie `unicodedata`.

Le fichier `rotor.init` contient ensemble des rotors et des réflecteurs, il est importé avec la méthode `load` contenu dans la librairie `json`. Cette méthode va faire la <b>dé-sérialisation</b> en dictionnaire de donné de l’objet contenu dans le fichier.

Le <b>décryptage /cryptage</b> se fait grâce au paramètres fournis par utilisateur

- Trois rotors (Ex : RA, RB, RC), 
- Une clé (Ex : k = 3)
- Un réflecteur (Ex : RFB)

Avec ses exemple de paramètres la première saisie de la lettre <b>A</b> sera crypté/décrypté en <b>J</b>

# Stratégie de résolution - Méthodologie 

# Algorithmique

# Diagramme de flux fonctionnel 

![enigma](enigma.jpeg)

# Interface de programmation 

### Data

### Présentation

| Fonctionnalité | Fonction    | Parameètre  | Description   |
| :--- | :---        |    :----:   |          :--- |
|Lecture du message | begin_lecture_message      | Aucun       | Li le message contenu dans un fichier, si le fichier est introuvable le programme affiche fichier indisponible  |
|Sauvegarde le message | begin_save_message   | Aucun        | Sauvegarde le message à crypter, utilisateur sasie le message et le nom du fichier dans le quel le message sera sauvegarder      |
|Encryptage et Décriptage | begin_encrypt      | Aucun       | Début du cryptage,  chargement des `données`, l'utilisateur sélectionne les rotors et le réflecteur, saisie le message et le fichier de sauvegarde du méssage  |
|Quitter le programme| exit      | Aucun       | Quitte le programme  |


# Tests

# Questions 

# Conclusion 

# Bibliographie

