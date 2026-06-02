import umage 
import math

image = umage.load('test.jpg')

def greyscale(mat_img):
    grey_mat_img = []
    i = 0
    while i < len(mat_img):
        j = 0
        sous_liste = []
        while j < len(mat_img[i]):
            new_elem = int((mat_img[i][j][0] * 0.2125 + mat_img[i][j][1] * 0.7154 + mat_img[i][j][2] * 0.0721))
            sous_liste.append((new_elem, new_elem, new_elem))
            j = j + 1
        grey_mat_img.append(sous_liste)
        i = i + 1
    return grey_mat_img

#new_mat_img = greyscale(image)
#grey_image = umage.save(new_mat_img)

def pixel(img, i , j , default):
    if i >= 0 and i < len(img) :
        if j >= 0 and j < len(img[i]):
            return img[i][j]
    return default

def appliquer_convolution(img, mat, i, j):
    m = 0
    mypixel = (0,0,0)
    for k in range(i-1, i+2):
        n = 0
        for l in range(j-1, j+2):
            case = pixel(img, k, l, (0,0,0))
            new_case = (int(case[0] * mat[m][n]), int(case[1] * mat[m][n]), int(case[2] * mat[m][n]))
            mypixel = (mypixel[0] + new_case[0], mypixel[1] + new_case[1], mypixel[2] + new_case[2])
            n = n + 1
        m = m + 1
    return mypixel

def convolution(mat_img, mat):
    new_mat_img = []
    i = 0
    while i < len(mat_img) :
        j = 0
        sous_liste = []
        while j < len(mat_img[i]):
            elem = appliquer_convolution(mat_img, mat, i, j)
            sous_liste.append(elem)
            j = j + 1
        new_mat_img.append(sous_liste)
        i = i + 1
    return new_mat_img


mat1 = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
mat2 = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
mat3 = [[-2,0,0],[0,1,0],[0,0,2]]

#new_image = convolution(image, mat3)
#test = umage.save(new_image)

def sobel(mat_img, mat_sobel_x, mat_sobel_y):
    grey_img = greyscale(mat_img)
    grad_x = convolution(grey_img, mat_sobel_x)
    grad_y = convolution(grey_img, mat_sobel_y)
    sobel_mat = []
    i = 0
    while i < len(grad_x) :
        j = 0
        sous_liste = []
        while j < len(grad_x[i]):
            mypixel = (int(math.sqrt((grad_x[i][j][0])**2 + (grad_y[i][j][0])**2)),int(math.sqrt((grad_x[i][j][1])**2 + (grad_y[i][j][1])**2)),int(math.sqrt((grad_x[i][j][2])**2 + (grad_y[i][j][2])**2)))
            sous_liste.append(mypixel)
            j = j + 1
        sobel_mat.append(sous_liste)
        i = i +1
    return sobel_mat

mat_sobel_x = [[-1,0,1],[-2,0,2],[-1,0,1]]
mat_sobel_y = [[-1,-2,-1],[0,0,0],[1,2,1]]

detec_img_mat = sobel(image, mat_sobel_x, mat_sobel_y)
detec_img = umage.save(detec_img_mat)

















