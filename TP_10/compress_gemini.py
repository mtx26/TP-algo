"""Compression Tool.

Usage:
  compress.py (-c | -d) -t <TECHNIQUE> --in <FILE> [--out <FILE>]
  compress.py -h | --help

Options:
  -h --help       Show this screen.
  -c              Compress the file.
  -d              Decompress the file.
  -t <TECHNIQUE>  Technique to use: 'LZ' (Dictionary) or 'ADN' (RLE).
  --in <FILE>     Input file path.
  --out <FILE>    Output file path. [default: auto]
"""

import sys
import json
import os

# Import docopt from the local file provided
try:
    from docopt import docopt
except ImportError:
    print("Error: docopt.py not found. Please ensure it is in the same directory.")
    sys.exit(1)


class BadADNFormat(Exception):
    """Exception raised for invalid characters in DNA sequences."""
    pass


def compress_lz(text):
    """
    Compresses text using Dictionary Coding (LZ).
    Returns a JSON string containing the dictionary and the index list.
    """
    words = text.split()
    # Create unique list of words preserving order of appearance for determinism
    dictionary = []
    seen = set()
    for w in words:
        if w not in seen:
            dictionary.append(w)
            seen.add(w)
    
    # Map words to their index
    word_to_index = {w: i for i, w in enumerate(dictionary)}
    
    # Create the sequence of numbers
    compressed_indices = [word_to_index[w] for w in words]
    
    # Pack both the dictionary and the data
    return json.dumps({"dict": dictionary, "data": compressed_indices})


def decompress_lz(data_str):
    """
    Decompresses LZ data. Expects a JSON string.
    """
    try:
        package = json.loads(data_str)
        dictionary = package["dict"]
        indices = package["data"]
        
        # Reconstruct text
        words = [dictionary[i] for i in indices]
        return " ".join(words)
    except (json.JSONDecodeError, KeyError, IndexError):
        raise TypeError("File content does not match LZ compression format.")


def compress_adn(text):
    """
    Compresses DNA sequence using RLE (Run-Length Encoding).
    """
    # 1. Validation
    valid_bases = {'A', 'T', 'G', 'C', '\n', '\r'}
    if not set(text).issubset(valid_bases):
        raise BadADNFormat("Input contains non-DNA characters.")

    clean_text = text.replace('\n', '').replace('\r', '')
    if not clean_text:
        return ""

    # 2. Compression Logic
    result = []
    count = 1
    for i in range(1, len(clean_text)):
        if clean_text[i] == clean_text[i-1]:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(clean_text[i-1])
            count = 1
    
    # Handle the last group
    if count > 1:
        result.append(str(count))
    result.append(clean_text[-1])

    return "".join(result)


def decompress_adn(text):
    """
    Decompresses DNA RLE data.
    """
    result = []
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        
        if char.isdigit():
            # Handle multi-digit numbers (e.g., 12A)
            num_str = char
            i += 1
            while i < n and text[i].isdigit():
                num_str += text[i]
                i += 1
            
            # The next char is the base to repeat
            if i < n:
                base = text[i]
                result.append(base * int(num_str))
            else:
                # Number at end of file without base (bad format)
                raise TypeError("Unexpected number at end of ADN stream.")
        else:
            # Single character (implicit count of 1)
            result.append(char)
        
        i += 1
        
    return "".join(result)


def main():
    try:
        # Parse arguments
        args = docopt(__doc__)
    except Exception as e:
        # Docopt usually handles its own exit, but if a manual call fails:
        print(__doc__)
        raise ValueError(e)

    # Extract arguments
    mode_compress = args['-c']
    mode_decompress = args['-d']
    technique = args['-t']
    input_file = args['--in']
    output_file = args['--out']

    # Handle default output filename
    if output_file == "auto" or output_file is None:
        output_file = input_file + ".out"

    try:
        # 1. Read Input File
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"The file '{input_file}' does not exist.")

        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        result_content = ""

        # 2. Process based on Technique
        if technique == 'LZ':
            if mode_compress:
                result_content = compress_lz(content)
            else:
                result_content = decompress_lz(content)

        elif technique == 'ADN':
            if mode_compress:
                try:
                    result_content = compress_adn(content)
                except BadADNFormat:
                    print(f"Error: File '{input_file}' contains invalid DNA characters.")
                    # Re-raising as per instructions to manage the exception
                    raise
            else:
                result_content = decompress_adn(content)
        
        else:
            # Invalid technique provided
            print(__doc__)
            raise ValueError(f"Unknown technique: {technique}")

        # 3. Write Output File
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result_content)
        
        print(f"Operation successful. Result saved to: {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Format Error: {e}")
    except ValueError as e:
        print(f"Argument Error: {e}")
        print(__doc__)
    except BadADNFormat:
        pass # Message already printed, suppression done for clean exit


if __name__ == '__main__':
    main()