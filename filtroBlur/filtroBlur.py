# Importando a biblioteca Numpy
import numpy as np

# Importando a biblioteca Matplotlib para exibir a imagem
from matplotlib import pyplot as plt

# Importando a biblioteca OpenCV
import cv2

# Definindo a função que mostra a imagem na tela
def showSingleImage(image, title, size):
    fig, axis = plt.subplots(figsize = size)
    axis.imshow(image, 'gray')
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()

# Carregando a imagem que vai ser usada
original_img = cv2.imread("img.jpg")

# Convertendo a imagem de BGR para RGB
original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

# Aplicando o filtro de Blur, o qual é do tipo passa-baixa
blur_img = cv2.blur(original_img, (5, 5))

# Mostrando as imagens
showSingleImage(original_img, "Imagem original", (7, 7))
showSingleImage(blur_img, "Imagem com Blur", (7, 7))