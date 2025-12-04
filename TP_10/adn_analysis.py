#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tableau de codons -> acides aminés
CODON_TABLE = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def dna_to_rna(dna_seq):
    """
    Convertit une séquence ADN en ARN.
    Remplace les T par U.
    
    Args:
        dna_seq (str): Séquence ADN.
    Returns:
        str: Séquence ARN.
    """
    return dna_seq.replace('T', 'U').upper()

def reverse_complement(dna_seq):
    """
    Retourne le complément inverse d'une séquence ADN.
    
    Args:
        dna_seq (str): Séquence ADN.
    Returns:
        str: Complément inverse de la séquence ADN.
    """
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement[base] for base in reversed(dna_seq.upper()))

def translate_sequence(dna_seq):
    """
    Traduit une séquence ADN en protéine selon la table des codons.
    
    Args:
        dna_seq (str): Séquence ADN.
    Returns:
        str: Séquence protéique (acides aminés).
    """
    protein = ""
    dna_seq = dna_seq.upper()
    
    for i in range(0, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3]
        if len(codon) == 3 and all(base in 'ATGC' for base in codon):
            protein += CODON_TABLE.get(codon, 'X')
        else:
            protein += 'X'
    
    return protein

def find_orfs(dna_seq, min_length=100):
    """
    Trouve les cadres de lecture ouverts (ORF) dans une séquence ADN.
    
    Args:
        dna_seq (str): Séquence ADN.
        min_length (int): Longueur minimale de l'ORF en paires de bases.
    Returns:
        list: Liste de dictionnaires contenant les informations sur chaque ORF.
    """
    dna_seq = dna_seq.upper()
    orfs = []
    
    # Chercher dans les 3 cadres de lecture
    for frame in range(3):
        for i in range(frame, len(dna_seq) - 2, 3):
            # Chercher un codon START (ATG)
            if i + 3 <= len(dna_seq) and dna_seq[i:i+3] == 'ATG':
                # Chercher un codon STOP
                for j in range(i + 3, len(dna_seq) - 2, 3):
                    if dna_seq[j:j+3] in ['TAA', 'TAG', 'TGA']:
                        orf_dna = dna_seq[i:j+3]
                        orf_protein = translate_sequence(orf_dna)
                        
                        if len(orf_protein) >= min_length // 3:  # Au moins min_length/3 acides aminés
                            orfs.append({
                                'start': i,
                                'end': j + 3,
                                'length': len(orf_dna),
                                'dna': orf_dna,
                                'protein': orf_protein,
                                'frame': frame
                            })
                        break
    
    return orfs

def find_all_orfs_simple(dna_seq, min_aa=10):
    """
    Trouve tous les ORFs dans une séquence ADN sans restriction de position.
    
    Args:
        dna_seq (str): Séquence ADN.
        min_aa (int): Nombre minimal d'acides aminés dans l'ORF.
    Returns:
        list: Liste de dictionnaires contenant les informations sur chaque ORF.
    """
    dna_seq = dna_seq.upper()
    orfs = []
    
    for frame in range(3):
        for i in range(frame, len(dna_seq) - 2, 3):
            if i + 3 <= len(dna_seq) and dna_seq[i:i+3] == 'ATG':
                for j in range(i + 3, len(dna_seq), 3):
                    if j + 3 <= len(dna_seq):
                        if dna_seq[j:j+3] in ['TAA', 'TAG', 'TGA']:
                            orf_dna = dna_seq[i:j+3]
                            orf_protein = translate_sequence(orf_dna)
                            
                            if len(orf_protein) >= min_aa:
                                orfs.append({
                                    'start': i,
                                    'end': j + 3,
                                    'length_bp': len(orf_dna),
                                    'length_aa': len(orf_protein),
                                    'protein': orf_protein,
                                    'frame': frame,
                                    'strand': 'forward'
                                })
                            break
    
    return orfs


if __name__ == "__main__":
    # Lire la séquence d'ADN avec gestion des exceptions
    dna_sequence = None
    adn_path = '/Users/noa/Library/CloudStorage/OneDrive-UMONS/UMons/Code/Bac 1 - Vscode/TP-algo/TP_10/adn.txt'
    try:
        with open(adn_path, 'r') as f:
            dna_sequence = f.read().replace('\n', '').strip()
            if not dna_sequence:
                raise ValueError("Le fichier est vide ou ne contient pas de séquence ADN.")
            if not all(base in 'ATGC' for base in dna_sequence.upper()):
                raise ValueError("La séquence contient des caractères non valides (seuls A, T, G, C sont autorisés).")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{adn_path}' est introuvable.")
    except ValueError as ve:
        print(f"Erreur : {ve}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
    else:
        print(f"=== ANALYSE DE LA SÉQUENCE ADN ===")
        print(f"Longueur totale : {len(dna_sequence)} paires de bases\n")

        # Chercher les ORFs
        print("=== CADRES DE LECTURE OUVERTS (ORFs) TROUVÉS ===\n")
        orfs = find_all_orfs_simple(dna_sequence, min_aa=30)

        if orfs:
            for idx, orf in enumerate(orfs, 1):
                print(f"ORF #{idx}")
                print(f"  Position : {orf['start']} - {orf['end']}")
                print(f"  Longueur : {orf['length_bp']} pb ({orf['length_aa']} aa)")
                print(f"  Cadre de lecture : {orf['frame']}")
                print(f"  Protéine produite : {orf['protein']}")
                print()
        else:
            print("Aucun ORF majeur trouvé (min 30 acides aminés)\n")
        
        # Chercher avec une limite inférieure plus petite
        print("=== TOUS LES ORFs (min 10 acides aminés) ===\n")
        orfs_small = find_all_orfs_simple(dna_sequence, min_aa=10)

        print(f"Total d'ORFs trouvés : {len(orfs_small)}\n")

        for idx, orf in enumerate(orfs_small[:15], 1):  # Afficher les 15 premiers
            print(f"ORF #{idx}")
            print(f"  Position : {orf['start']} - {orf['end']} (frame {orf['frame']})")
            print(f"  Longueur : {orf['length_bp']} pb ({orf['length_aa']} aa)")
            print(f"  Protéine : {orf['protein']}")
            print()

        if len(orfs_small) > 15:
            print(f"... et {len(orfs_small) - 15} autres ORFs")
