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

# Aplicando o Filtro da Mediana, o qual é do tipo passa-baixa
medianImg = cv2.medianBlur(original_img, 5)

# Exibindo as imagens
showSingleImage(original_img, "Imagem Original", (7, 7))
showSingleImage(medianImg, "Com o Filtro da Mediana", (7, 7))