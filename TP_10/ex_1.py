"""
Programme de compression.

Usage:
  ex_1.py (-c | -d) -t <TECHNIQUE> --in <FICHIER> [--out <FICHIER>]
  ex_1.py -h | --help

Options:
  -h --help         Afficher l'aide.
  -c                Compresser (mutuellement exclusif avec -d).
  -d                Décompresser (mutuellement exclusif avec -c).
  -t <TECHNIQUE>    Technique utilisée (ex: RLE, LZ).
  --in <FICHIER>    Fichier d'entrée.
  --out <FICHIER>   Fichier de sortie [optionnel].
"""
from docopt import docopt
import json

def openfile(arguments):
    try:
        with open(arguments["--in"], "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("fichier introuvable")
    
def writefile(file_name, data):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(data)
    
def LZ_compression(arguments):
    rep_word = []
    rep_i = []
    txt = openfile(arguments)
    list_txt = txt.split(' ')
    for word in list_txt:
        if word not in rep_word:
            rep_word.append(word)
        i = rep_word.index(word)
        rep_i.append(i)
    return json.dumps({"indice": rep_i, "data": rep_word})

def RLE_compression(arguments):
    rep = ""
    txt = openfile(arguments).strip()
    txt = txt.replace('\n', '').replace('\r', '')
    if not txt:
        return None
    
    last_letter = ""
    count_same_l = 0
    for l in txt:
        print(l)
        if l == last_letter:
            count_same_l += 1
        else:
            if count_same_l != 0:
                rep += str(count_same_l) + str(last_letter)
            last_letter = l
            count_same_l = 1

    if count_same_l != 0:
        rep += str(count_same_l) + str(last_letter)
    return rep
        
def compression(arguments):
    if arguments["-t"] == "LZ":
        data = LZ_compression(arguments)

    elif arguments["-t"] == "RLE":
        data = RLE_compression(arguments)

    if arguments["--out"]:
        file_name_out = arguments["--out"]
    else:
        file_name_out = arguments["--in"] + "." + arguments["-t"]

    writefile(file_name_out, data)
    
def LZ_decompression(arguments):
    rep = ""
    json_data = json.loads(openfile(arguments))
    words = json_data.get("data")
    indice = json_data.get("indice")
    for i in indice:
        rep += words[i]
        rep += " "
    
    print(rep)
    return rep

def RLE_decompression(arguments):
    rep = ""
    txt = openfile(arguments)
    if not txt:
        return None
    nbr = ""
    for l in txt:
        if l.isdigit():
            nbr += str(l)
        else:
            i = 0
            while i < int(nbr):
                rep += str(l)
                i += 1
            
            nbr = ""
    return rep
            
def decompression(arguments):
    if arguments["-t"] == "LZ":
        data = LZ_decompression(arguments)
    
    if arguments["-t"] == "RLE":
        data = RLE_decompression(arguments)


    if arguments["--out"]:
        file_name_out = arguments["--out"]
    else:
        file_name_out = arguments["--in"] + ".txt"

    writefile(file_name_out, data)

def main():
    try:
        arguments = docopt(__doc__)
        if (arguments["-t"] != "LZ") and (arguments["-t"] != "RLE"):
            raise ValueError("méthode non suporté")

        if arguments["-c"]:
            compression(arguments)
        elif arguments["-d"]:
            decompression(arguments)

    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    except Exception as e:
        raise ValueError(e)
        


if __name__ == "__main__":
    main()