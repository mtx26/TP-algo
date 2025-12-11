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
    """
    Input: arguments (dict) with key '--in' specifying input file path.
    What it does: Opens the input file with UTF-8 encoding and returns its contents as a string.
    Output: str containing the file contents.
    Exceptions: Raises FileNotFoundError if the input file cannot be found or opened.
    """
    try:
        with open(arguments["--in"], "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("fichier introuvable")
    
def writefile(file_name, data):
    """
    Input: file_name (str) path to write, data (str) to write.
    What it does: Writes `data` to `file_name` using UTF-8 encoding (overwrites existing file).
    Output: None.
    Exceptions: May raise OSError (including IOError) on write errors.
    """
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(data)
    
def LZ_compression(arguments):
    """
    Input: arguments (dict) with key '--in' path to input file.
    What it does: Reads the input file, tokenizes on spaces, builds a list of unique words
    and a list of indices referring to those words, and encodes the result as JSON.
    Output: JSON-formatted str with keys "indice" (list of indices) and "data" (list of words).
    Exceptions: Propagates FileNotFoundError from `openfile`; may raise TypeError/ValueError on unexpected input.
    """
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
    """
    Input: arguments (dict) with key '--in' path to input file.
    What it does: Reads the input file, removes newline characters, and encodes runs of identical
    characters as the count followed by the character (basic RLE).
    Output: Compressed string (e.g., "3a2b") or None for empty input.
    Exceptions: Raises FileNotFoundError if the input file is missing.
    """
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
    """
    Input: arguments (dict) parsed from CLI; expects keys '-t', '--in', and optional '--out'.
    What it does: Selects compression technique specified by `-t` ("LZ" or "RLE"),
    performs compression and writes the result to the output file.
    Output: None.
    Exceptions: May raise ValueError for unsupported technique or propagate FileNotFoundError/OSError.
    """
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
    """
    Input: arguments (dict) with key '--in' path to a JSON file produced by `LZ_compression`.
    What it does: Loads the JSON, maps indices back to words and rebuilds the original text (space-separated).
    Output: Decompressed string.
    Exceptions: Raises FileNotFoundError if file missing; may raise json.JSONDecodeError or IndexError on malformed data.
    """
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
    """
    Input: arguments (dict) with key '--in' path to an RLE-compressed file.
    What it does: Reads the compressed text consisting of integer counts followed by characters
    and expands each run to reconstruct the original text.
    Output: Decompressed string or None if input empty.
    Exceptions: Raises FileNotFoundError if file missing; may raise ValueError if the compressed format is malformed.
    """
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
    """
    Input: arguments (dict) parsed from CLI; expects keys '-t', '--in', and optional '--out'.
    What it does: Selects decompression technique specified by `-t` ("LZ" or "RLE"),
    performs decompression and writes the result to the output file.
    Output: None.
    Exceptions: May propagate json.JSONDecodeError, IndexError, FileNotFoundError, or ValueError from underlying functions.
    """
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
    """
    Input: None (reads CLI arguments via `docopt` using the module docstring).
    What it does: Parses command-line arguments, validates technique, and dispatches to compression or decompression.
    Output: None.
    Exceptions: Raises FileNotFoundError or ValueError on errors; wraps other exceptions into ValueError.
    """
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