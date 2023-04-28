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

# Convertendo a imagem em RGB para escala de cinza
grayImg = cv2.cvtColor(original_img, cv2.COLOR_RGB2GRAY)

# Aplicando o Filtro Gaussiano para remover ruídos
gaussianImg = cv2.GaussianBlur(grayImg, (5, 5), 0)

# Definindo um valor para o limiar superior e inferior
maxThreshold = 200
minThreshold = 98

# Aplicando o Canny Edge
cannyEdgeImg = cv2.Canny(gaussianImg, minThreshold, maxThreshold)

# Exibindo as imagens
showSingleImage(original_img, "Imagem Original", (7, 7))
showSingleImage(cannyEdgeImg, "Aplicando Canny Edge", (7, 7))


