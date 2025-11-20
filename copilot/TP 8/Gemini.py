from PIL import Image
import itertools
import math

def load(filename):
    """ Given a filename that matches an image file,
    return a list of lists of tuples corresponding to the list of
    lines of pixels (R, G, B) of the image. """

    with Image.open(filename, 'r') as image:
        image = image.convert('RGB')
        content = list(image.getdata())
        size_x, size_y = image.size
        return [content[i:i + size_x] for i in range(0, len(content), size_x)]


def save(image, filename='new', extension='jpg'):
    """ Stores the given image into a file. """
    if not image:
        print("Erreur: L'image est vide, impossible de sauvegarder.")
        return
    size_x, size_y = len(image), len(image[0])
    new_image = Image.new('RGB', (size_y, size_x))
    new_image.putdata(list(itertools.chain.from_iterable(image)))
    new_image.save('%s.%s' % (filename, extension))


def get_pixel(mat_img, y, x):
    """
    Retourne le pixel (r,g,b) à la position (y,x).
    Retourne (0,0,0) si hors limites (Zero Padding).
    """
    hauteur = len(mat_img)
    largeur = len(mat_img[0])
    
    if 0 <= x < largeur and 0 <= y < hauteur:
        return mat_img[y][x]
    else:
        return (0, 0, 0)

def clamp(valeur):
    """Force une valeur à rester entre 0 et 255."""
    return max(0, min(255, int(valeur)))

def greyscale(mat_img):
    """
    Convertit une image couleur en niveaux de gris selon la luminance.
    V = 0.2125*R + 0.7154*G + 0.0721*B
    """
    hauteur = len(mat_img)
    largeur = len(mat_img[0])
    nouvelle_image = []
    
    for y in range(hauteur):
        ligne = []
        for x in range(largeur):
            r, g, b = mat_img[y][x]
            v = int(0.2125 * r + 0.7154 * g + 0.0721 * b)
            ligne.append((v, v, v))
        nouvelle_image.append(ligne)
        
    return nouvelle_image

def appliquer_convolution_pixel(mat_img, mat_conv, py, px):
    """Applique un noyau de convolution sur un pixel unique."""
    taille_noyau = len(mat_conv)
    offset = taille_noyau // 2
    
    somme_r, somme_g, somme_b = 0, 0, 0
    
    for i in range(taille_noyau):
        for j in range(taille_noyau):
            img_y = py + (i - offset)
            img_x = px + (j - offset)
            
            pixel = get_pixel(mat_img, img_y, img_x)
            poids = mat_conv[i][j]
            
            somme_r += pixel[0] * poids
            somme_g += pixel[1] * poids
            somme_b += pixel[2] * poids

    return (clamp(somme_r), clamp(somme_g), clamp(somme_b))

def convolution(mat_img, mat):
    """Applique une matrice de convolution à toute l'image."""
    hauteur = len(mat_img)
    largeur = len(mat_img[0])
    nouvelle_image = []

    for y in range(hauteur):
        nouvelle_ligne = []
        for x in range(largeur):
            pixel = appliquer_convolution_pixel(mat_img, mat, y, x)
            nouvelle_ligne.append(pixel)
        nouvelle_image.append(nouvelle_ligne)

    return nouvelle_image

def sobel(mat_img):
    """
    Applique le filtre de détection de contours Sobel.
    1. Conversion en gris
    2. Calcul des gradients X et Y
    3. Calcul de la magnitude
    """
    img_gris = greyscale(mat_img)
    
    Gx = [[-1, 0, 1], 
          [-2, 0, 2], 
          [-1, 0, 1]]
          
    Gy = [[-1, -2, -1], 
          [ 0,  0,  0], 
          [ 1,  2,  1]]
    
    hauteur = len(img_gris)
    largeur = len(img_gris[0])
    image_contours = []

    for y in range(hauteur):
        ligne = []
        for x in range(largeur):
            val_gx = 0
            val_gy = 0
            
            for i in range(3):
                for j in range(3):
                    offset_y = i - 1
                    offset_x = j - 1
                    
                    pixel = get_pixel(img_gris, y + offset_y, x + offset_x)
                    valeur = pixel[0] 
                    
                    val_gx += valeur * Gx[i][j]
                    val_gy += valeur * Gy[i][j]
            
            magnitude = math.sqrt(val_gx**2 + val_gy**2)
            val_finale = clamp(magnitude)
            
            ligne.append((val_finale, val_finale, val_finale))
        image_contours.append(ligne)
        
    return image_contours


if __name__ == "__main__":
    nom_fichier_entree = 'test.jpg'
    
    print(f"--- Tentative de chargement de {nom_fichier_entree} ---")
    try:
        image_originale = load(nom_fichier_entree)
        print(f"Image chargée ! Taille : {len(image_originale[0])}x{len(image_originale)}")

        print("Calcul du Greyscale...")
        img_grise = greyscale(image_originale)
        save(img_grise, 'resultat_gris')
        print("-> Sauvegardé : resultat_gris.jpg")

        print("Calcul d'un flou (Convolution)...")
        box_blur = [[1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9]]
        img_floue = convolution(image_originale, box_blur)
        save(img_floue, 'resultat_flou')
        print("-> Sauvegardé : resultat_flou.jpg")

        print("Calcul de Sobel (Contours)...")
        img_sobel = sobel(image_originale)
        save(img_sobel, 'resultat_sobel')
        print("-> Sauvegardé : resultat_sobel.jpg")
        
        print("--- Terminé avec succès ---")

    except FileNotFoundError:
        print(f"ERREUR CRITIQUE : Le fichier '{nom_fichier_entree}' est introuvable.")
        print("Veuillez placer une image JPG nommée 'test.jpg' dans ce dossier.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")