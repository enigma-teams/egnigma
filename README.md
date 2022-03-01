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

| Fonction    | Parametres  | Descriptions  |
| :---        |    :----:   |          :--- |
| GENERATEUR(generate)    |     it (iterateur)      | cette fonction permet de verifier les caractére du message entré et donc si un caractere est accentué il retire sont accent|
| LECTURE DU MESSAGE(lecture_message)   | filename et result      | elle ouvre le fichier ou est contenue le message(filename); appel la fonction GENERATE pour parcourir le message et retiré les accents sur les caractére accentués et met le resultat obtenue dans une liste (result)     |
|SAUVEGARDE DU MESSAGE(save_message)   |filename et message_in    |le fichier contenant le message(filename) ouvert, il le sauvergarde en ecrivant le fichier dans message_in|
|TELECHARGEMENT DES PARAMETRE (load_params) | settings_file  | permet d'ouvrir la bibliothéque json ou sont contenue les differents rotors(05) et reflecteurs(02) .puis fait appel a la fonction d'initiation des rotors et reflecteurs(init_rotor_and_reflector) pour telecharger la bibliotheque json dans le fichier settings_file|
|INITIATEUR DE ROTOR ET REFLECTEUR (init_rotor_and_reflector) | rotors et reflecteurs  | elle permet d'ouvrir le fichier contenant les rotors et reflecteurs puis convertit chaque element du fichier(unicode) en chaine de caractere  |
| SELECTION DE ROTOR ET REFLECTEUR (select_main_rotor_and_reflector) | selected_rotor et selected_reflector  | permet de faire le choix de 03 rotors parmis les 05 presents et aussi le choix d'un reflecteur parmis les 02 presents et sa utilise l'ordre du choix respectivement sur l'ordre des rotors  |
|PERMUTATION DES ROTORS (rotor_permute) | rotor_name et key | permet de permuter chaque rotor aprés qu'un caractére y soit passé en prenant un nombre de carctére(nombre etant egale a la clés)au debut de la chaine puis le renvoie en fin de chaine  |
|FONCTION DU REFLECTEUR (make_reflector)  | character et key  | lorque le charactére arrive au niveau du reflecteur elle se repere dans le reflecteur puis prends son indice et l'additionne a la clés pour trouvé la nouvelle correspondances en sortie du caractére en entrée  |

### Application

| Fonctionnalité | Fonction    | Parameètre  | Description   |
| :--- | :---        |    :----:   |          :--- |
|Lecture du message | begin_lecture_message      | Aucun       | Li le message contenu dans un fichier, si le fichier est introuvable le programme affiche fichier indisponible  |
|Sauvegarde le message | begin_save_message   | Aucun        | Sauvegarde le message à crypter, utilisateur sasie le message et le nom du fichier dans le quel le message sera sauvegarder      |
|Encryptage et Décriptage | begin_encrypt      | Aucun       | Début du cryptage,  chargement des `données`, l'utilisateur sélectionne les rotors et le réflecteur, saisie le message et le fichier de sauvegarde du méssage  |
|Quitter le programme| exit      | Aucun       | Quitte le programme  |

### LOGIQUE
| Fonction    | Parametres  | Descriptions  |
| :---        |    :----:   |          :--- |
| INITIATEUR DE CRYPTAGE(Begin_encrypt) |     /   | Fonction mère contenant toutes les autres fonctions ci-dessous. Permet le démarrage du cryptage en faisant appel aux fonctions ci-dessous|
| Téléchargement des paramètres (Data.load_params )| Settings_file     | Permet d’afficher la liste des rotors disponibles     |
|Sélections des rotors(Selected_rotor)   |Tableau    |Demande a l’utilisateur de choisir 03 rotors et vérifie si sont choix est dans la liste ; après le choix d’un rotor il le retire de la liste pour que l’utilisateur n’est pas des rotors semblable dans son tableau|
|Ordre des rotors (trie) | /  | S’assure que l’ordre des choix des rotors soit égal à l’ordre de leur position ensuite le met dans la liste |
|Sélection du réflecteur (Reflector_choice) | dictionnaire  | Parcours la liste des réflecteurs et demande a l’utilisateur d’entrer la chaine caractère correspondant au réflecteur choisie et met dans un dictionnaire le réflecteur choisie  |
|Message a crypté | Message = input (‘‘message= ’’)  | Demande a l’utilisateur d’entrer son message a encrypté/décrypté  |
|Fichier du message a crypté | File_name = input (‘‘fichier= ’’) | Demande a l’utilisateur d’entrer du fichier contenant le message a encrypté/décrypté |
|Sauvegarde du message (Data.save_message)  | (F ‘‘{file_name}.txt, message)et Out = [ ]  |Sauvegarde le message d’entrer/de sortie dans un fichier |
|Sélections de rotors et réflecteur(Data.select_main_rotor_and_reflector) | Selected_rotor et Reflector_choice |Permet de faire appel au rotor et réflecteur sélectionné dans la fonction Begin_encrypt|
|Lecture du message (Data.lecture_message) | F ‘‘{file_name}.Txt et out |Prends le message contenue dans le fichier et l’écrit dans la partie réservé au message a encrypté/décrypté|
|Machine d’encryptage CESAR (Enigma_machine) | Out [0] et en |Fonction codage et décodage d’un message selon le positionnement des rotors et du réflecteur|


# Tests
Dans cette rubrique, nous devrons réaliser des tests afin d'évaluer notre programme.

Tout d'abord il est nécessaire de créer un ficher ".txt" qui sera stocké dans le même
dossier que celui du code source de notre programme.

**une fois le programme lancé ici on faisant le choix=2 nous effectuons l'enregistrement du Message**
Menu de sélection

1 - Lecture Message

2 - Enregistre Message

3 - Cryptage/Decryptage

4 - Quitter

choix = 2

Message = bonjour

**Une fois le message écrit, le programme demande d'entrer le fichier de sauvegarde et le message est enregistré automatiquement dans le fichier**

Fichier de sauvegarde = bonjour.txt

Le message bonjour a été sauvegarder dans le fichier bonjour.txt.txt

**une fois le message ecrit et sauvegardé dans le fichier, de nouveau le menu de sélection apparait et ici on procède à la lecture du fichier**

Menu de sélection

1 - Lecture Message

2 - Enregistre Message

3 - Cryptage/Decryptage

4 - Quitter

choix = 1

File Name : bonjour.txt

['BONJOUR']

**Lorsque le fichier a été lu, de nouveau le menu de sélection apparait et là il faut choisir entre cryptage et décryptoage en entrant le choix= 3 ainsi le programme realise soit le cryptage ou le décryptage**

Menu de sélection

1 - Lecture Message

2 - Enregistre Message

3 - Cryptage/Decryptage

4 - Quitter

choix = 3


**Ce qui suit est le choix des rotors et par défaut il faut choisir 3 parmis les 5 rotors**

1 - RA

2 - RB

3 - RC

4 - RD

5 - RE

Rotor 1 = 1

Rotor 2 = 2

Rotor 3 = 3

Rotors : ['RA', 'RB', 'RC']

**Après avoir réalisé le choix des rotors nous devons éffectuer le choix du reflecteur et c'est ici que sera etablit une correspondante entre le message écrit et le cryptage et puis renvérra le message crypté**

1 - RFA

2 - RFB

Reflector = 2

Reflector = RFB

Message = bonjour

Fichier = bonjour.txt

message = BONJOUR

message codé : UFBNFRA

Process finished with exit code 0
  
# Questions 

# Conclusion 

# Bibliographie

