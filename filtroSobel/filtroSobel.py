# Importando a biblioteca Numpy
import numpy as np

# Importando a biblioteca Matplotlib para exibir a imagem
from matplotlib import pyplot as plt

# Importando a biblioteca OpenCV
import cv2

# Definindo a função que vai exibir a imagem
def showSingleImage(image, title, size):
    fig, axis = plt.subplots(figsize = size)
    axis.imshow(image, 'gray')
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()

# Carregando a imagem que vai ser usada
original_img = cv2.imread("img.jpg")

# Convertendo a imagem passada de BGR para RGB 
original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

# Convertendo a imagem passada para escala de cinza
gray_img = cv2.cvtColor(original_img, cv2.COLOR_RGB2GRAY)

# Aplicando o filtro Sobel
imgSobelX = cv2.Sobel(src = original_img, ddepth=cv2.CV_64F, dx = 1, dy = 0, ksize = 3)
imgSobelY = cv2.Sobel(src = original_img, ddepth=cv2.CV_64F, dx = 0, dy = 1, ksize = 3)

# Realizando uma soma ponderada para conseguir exibir os resultados em X e Y ao mesmo tempo
imgSobelXY = cv2.addWeighted(imgSobelX, 0.5, imgSobelY, 0.5, 0)

# Convertendo os pixels da imagem gerada para pixels de 8 bits inteiros sem sinal
imgSobelX = cv2.convertScaleAbs(imgSobelX)
imgSobelY = cv2.convertScaleAbs(imgSobelY)
imgSobelXY = cv2.convertScaleAbs(imgSobelXY)

# Exibindo as imagens após aplicar o filtro Sobel, o qual é do tipo passa-alta
showSingleImage(original_img, "Imagem Original", (7, 7))
showSingleImage(imgSobelX, "Imagem após aplicar o Filtro Sobel no eixo X", (7, 7))
showSingleImage(imgSobelY, "Imagem após aplicar o Filtro Sobel no eixo Y", (7, 7))
showSingleImage(imgSobelXY, "Imagem após aplicar o Filtro Sobel no eixo XY", (7, 7))