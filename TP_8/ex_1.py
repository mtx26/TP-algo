import umage

def greyscale(matrice_img):
    i = 0
    while i < len(matrice_img):
        j = 0
        while j < len(matrice_img[0]):
            v = int(0.2125 * matrice_img[i][j][0] + 0.7154 * matrice_img[i][j][1] + 0.0721 * matrice_img[i][j][2])
            matrice_img[i][j] = (v, v, v)
            j += 1
        i += 1
    return matrice_img

# umage.save(greyscale(umage.load("TP_8/DJI_0189 copie.jpg")),  "new_image", "jpg")
def somme_conv(i, j, matrice_img, mat):
    # calculé la scale
    y = len(mat)
    x = len(mat[0])

    y_img = len(matrice_img)
    x_img = len(matrice_img[0])

    # decalage
    dy = (y - 1)/2
    dx = (x - 1)/2

    k = 0
    res = [0, 0, 0]
    while k < (y):
        new_i = int(i - dy + k)
        l = 0
        while l < x:
            new_j = int(j - dx + l)
            if (new_i > -1) and (new_i < y_img):
                if (new_j > -1) and (new_j < x_img):
                    # print("ligne d&ns matrice", [new_i, new_j], [y_img, x_img],[k, l])
                    res[0] += matrice_img[new_i][new_j][0] * mat[k][l][0]
                    res[1] += matrice_img[new_i][new_j][1] * mat[k][l][1]
                    res[2] += matrice_img[new_i][new_j][2] * mat[k][l][2]
            l += 1
        k += 1
    return res


def convolution(matrice_img, mat):
    row = []
    a = 0
    while a < len(matrice_img):
        row2 = [0] * len(matrice_img[0])
        row.append(row2)
        a += 1

    i = 0
    while i < len(matrice_img):
        j = 0
        while j < len(matrice_img[0]):
            # print("faire le point", [i, j])
            rep = somme_conv(i, j, matrice_img, mat)
            row[i][j] = (rep[0], rep[1], rep[2])
            j += 1
        i += 1
    print(row)
    return row

umage.save(convolution(greyscale(umage.load("TP_8/image_test.jpg")), [[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]], [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]], [[-2,0,0],[0,1,0],[0,0,2]]]), "new", "jpg")
