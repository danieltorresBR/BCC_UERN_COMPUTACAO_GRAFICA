import cv2
import numpy as np
from matplotlib import pyplot as plt
import collections
from random import *
import math

img = cv2.imread('lena.jfif')
img2 = cv2.imread('lena.jfif', 0)
img3 = cv2.imread('lena.jfif', 0)
img4 = cv2.imread('circulo2.png', 0)
esp = cv2.imread('lena.jfif', 0)
trans = cv2.imread('lena.jfif', 0)

def escalaCinza(img):

    rows = img.shape[0]
    cols = img.shape[1]

    cv2.imshow('Imagem Original', img)

    for i in range(rows):
        for j in range(cols):
            (b,g,r) = img[i,j]
            img[i,j] = ((b*0.114)+(g*0.587)+(r*0.299))

    return cv2.imshow('Tom de Cinza', img)

def mono(img):

    rows = img.shape[0]
    cols = img.shape[1]

    cv2.imshow('Imagem Original', img)

    for i in range(rows):
        for j in range(cols):
            (b,g,r) = img[i,j]
            img[i,j] = ((b+g+r))/3
    
    img=img.astype(np.uint8)
    return cv2.imshow('Mono', img)


def binarizacao(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]
    limiar = 128 # 256/2

    cv2.imshow('Imagem Original', img2)

    for i in range(rows):
        for j in range(cols):
            px = img2[i,j]
            if (px < limiar):
                img2[i,j] = 0
            else:
                img2[i,j] = 255
    return cv2.imshow('Binarizacao', img2)

def negativo(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Imagem Original', img2)

    for i in range(rows):
        for j in range(cols):
            img2[i,j] = ((255 - img2[i,j]))

    return cv2.imshow('Nagativo', img2)

def operacaoMult(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Imagem Original', img2)

    fatorMult = 4

    for i in range(rows):
        for j in range(cols):
            px = img2[i,j]
            #(b,g,r) = img[i,j]
            if ((fatorMult * px) < 0):
                img2[i,j] = 0
            elif ((fatorMult * px) > 255):
                img2[i,j] = 255
            else:
                img2[i,j] = fatorMult * px

    return cv2.imshow('Multiplicacao Escalar', img2)

def operacaoDiv(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Imagem Original', img2)

    fatorDiv = 1000

    for i in range(rows):
        for j in range(cols):
            px = img2[i,j]
            #(b,g,r) = img[i,j]
            if ((fatorDiv / px) < 0):
                img2[i,j] = 0
            elif ((fatorDiv / px) > 255):
                img2[i,j] = 255
            else:
                img2[i,j] = fatorDiv / px

    return cv2.imshow('Divisao Escalar', img2)

def operacaoSoma(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Imagem Original', img2)

    fatorSoma = 100 # quanto maior o fato, maior a intensidade do pixel. Logo, quanto maior a intensidade do pixel, mais claro ela sera

    for i in range(rows):
        for j in range(cols):
            px = img2[i,j]
            #(b,g,r) = img[i,j]
            if ((fatorSoma + px) < 0):
                img2[i,j] = 0
            elif ((fatorSoma + px) > 255):
                img2[i,j] = 255
            else:
                img2[i,j] = fatorSoma + px

    return cv2.imshow('Soma', img2)

def operacaoSubt(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Imagem Original', img2)

    fatorSubt = 100 # quanto maior o fato, maior a intensidade do pixel. Logo, quanto maior a intensidade do pixel, mais claro ela sera

    for i in range(rows):
        for j in range(cols):
            px = img2[i,j]
            #(b,g,r) = img[i,j]
            if ((fatorSubt - px) < 0):
                img2[i,j] = 0
            elif ((fatorSubt - px) > 255):
                img2[i,j] = 255
            else:
                img2[i,j] = fatorSubt - px

    return cv2.imshow('Subtracao', img2)

def limiarizacao(img2): #possui varios limiares definidos pelo usuario
    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Imagem Original', img2)

    limiares = int(input("Digite um valor para o Limiar >> "))
    cores = limiares+1

    tons = 255/cores
    cor = tons/2

    print ("TONS >> ", tons)
    print ("COR >> ", cor)


    vetorLimiares = []
    vetorCores = []

    for k in range(cores):
        if (k==0):
            vetorLimiares.append(tons)
        else:
            vetorLimiares.append(vetorLimiares[k-1]+tons)
    
    for w in range(cores):
        if (w==0):
            vetorCores.append(int(cor))
        else:
            vetorCores.append(int(vetorCores[w-1]+cor))
    
    print ("LIMIARES >> ", vetorLimiares)
    print ("CORES >> ", vetorCores)


    for i in range(rows):
        for j in range(cols):
            for x in range(cores):
                if img2[i,j] < vetorLimiares[x]:
                    img2[i,j] = vetorCores[x]
                    break

    return cv2.imshow('Limiarizacao', img2)


def histograma(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Imagem Original', img2)

    escala = 255
    contador = []

    for k in range(escala):
        contador.append(0)
    
    for i in range(rows):
        for j in range(cols):
            for k in range(escala):
                px = img2[i,j]
                if (px == k):
                    contador[k] = contador[k] + 1
    
    #print(contador)
    cv2.imshow('Histograma', img2)   
    x = np.arange(0, 255)  
    y = contador 
    plt.plot(x, y)
    plt.title("Histograma")
    plt.show()
 

def equalizacaoHistograma(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Imagem Original', img2)


    escala = 255
    contPixel = []
    probabilidade = []
    probabilidadeAcumulada = []
    pxTotal = rows*cols
    contInteracao = 0

    for k in range(escala):
        contPixel.append(0)
        probabilidade.append(0)
        probabilidadeAcumulada.append(0)

    
    for i in range(rows):
        for j in range(cols):
            for k in range(escala):
                px = img2[i,j]
                if (px == k):
                    contPixel[k] = contPixel[k] + 1
    
    print("\n\nVetor com a ocorrencia de Pixels >> ", contPixel)
    print("\n\nQuantidade de Total de PX >> ", pxTotal)


    #laco p calcular o valor acumulado hist[k]
    maiorIntensidade = len(probabilidade)-1
    for k in range(escala):
        probabilidade.append((maiorIntensidade*contPixel[k])/pxTotal)
    
    print("\n\nVetor de probabilidade >> ", probabilidade)

    for k in range(escala):
        if (k == 0):
            probabilidadeAcumulada.append(probabilidade[k])
        else:
            probabilidadeAcumulada.append(math.ceil(probabilidadeAcumulada[k-1]+probabilidade[k]))

        #contInteracao = contInteracao + probabilidade[k]
    
    print("\n\nVetor de probabilidade acumulada >> ", probabilidadeAcumulada)

    x = np.arange(0, 255)  
    y = contPixel 
    plt.plot(x, y)
    plt.title("Equalizacao do Histograma")
    plt.show()

    for i in range(rows):
        for j in range(cols):
            for k in range(escala):
                img2[i,j] = probabilidadeAcumulada[k]


    return cv2.imshow('Equalizacao do Histograma', img2)


def salEPimenta(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Imagem Original', img2)

    for i in range(rows):
        for j in range(cols):
            px = img2[i,j]
            aleatorio = randint(0, 30)
            #print ("Aleatorio >> ", aleatorio)
            if (aleatorio == 0):
                img2[i,j] = 0
            elif (aleatorio == 1):
                img2[i,j] = 255
            elif (aleatorio >= 2):
                img2[i,j] = px

    return cv2.imshow('Sal e Pimenta', img2)

def gauss(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Imagem Original', img2)

    for i in range(rows):
        for j in range(cols):
            aleatorio = (randint(0,100))
            print ("Aleatorio >> ", aleatorio)
            if (aleatorio == 0):
                img2[i,j] = random()%255
            elif (aleatorio >= 1):
                img2[i,j] = img2[i,j]

    
    return cv2.imshow('Gauss', img2)

def alargamentoContraste(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]
    cv2.imshow('Imagem Original', img2)

    maior = img2[0,0]
    menor = img2[0,0]

    idmaior = 100 #depois solicitar dados ao usuario
    idmenor = 20
 
    for i in range(rows):
        for j in range(cols):
            px = img2[i,j]
            if (px > maior):
                maior = px
            elif (menor > px):
                menor = px

    for i in range(rows):
        for j in range(cols):
           img2[i,j] = (img2[i,j]-menor)*(idmaior-idmenor)/(maior-menor)+menor       

    return cv2.imshow('Alargamento', img2)

def fatiamento(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]
    cv2.imshow('Imagem Original', img2)

    valorMinimo = 150 #depois solicitar dados ao usuario
    valorMaximo = 150  #sao valores que definem a faixa que nao sera preto.
                      #tudo fora dessa faixa sera preto.
 
    for i in range(rows):
        for j in range(cols):
            px = img2[i,j]
            if ((valorMinimo >= px) and (img2[i,j] <= valorMaximo)):
                img2[i,j] = px
            else:
                img2[i,j] = 255

    return cv2.imshow('Fatiamento', img2)

def escala(img2): #NAO ERA PARA FAZER! MAS EU FIZ

    rows = img2.shape[0]
    cols = img2.shape[1]
    #cv2.imshow('Imagem Original', img2)

    escalaX = 2 #depois solicitar dados ao usuario
    escalaY = 2 #sao valores que definem a faixa que nao sera preto.
                #tudo fora dessa faixa sera preto.
 
    for i in range(rows):
        for j in range(cols):
            if (((i*escalaY) < rows) and ((j*escalaX) < cols) and ((i*escalaY) >= 0) and ((j*escalaX) >= 0)):
                img2[i,j] = img2[(i*escalaY),(j*escalaX)]
        
    return cv2.imshow('Escala', img2)

def translacao(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]
    cv2.imshow('Imagem Original', img2)

    translacaoX = 250 #depois solicitar dados ao usuario
    translacaoY = 100 #sao valores que definem o fator de translacao
                      #nos eixos X e Y
                     
    for i in range(rows):
        for j in range(cols):
            if (((i+translacaoY) < rows) and
            ((j+translacaoX) < cols) and
            ((i+translacaoY) >= 0) and
            ((j+translacaoX) >= 0)):
                trans[i,j] = img2[(i+translacaoY),(j+translacaoX)]
            else:
                trans[i,j] = 0

    return cv2.imshow('Translacao', trans)

def espelhamento(img2):

    rows = img2.shape[0]
    cols = img2.shape[1]

    cv2.imshow('Original', img2)

    for i in range (0, rows-1):
        for j in range(0,cols-1):
            esp[i, j] = img2[i ,(img2.shape[1]-1) - j]
    
    return cv2.imshow('Espelhamento', esp)

def passaBaixo3(img2):

    soma = 0
    cont = 0

    #img2 = cv2.imread('lena.jfif', 0)
    cv2.imshow('Original', img2)


    for x in range (0, img2.shape[0]-3):
        for y in range(0, img2.shape[1]-3):

            while(cont < 2):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        #img[(x+i),(y+j)] = 255
                        if cont == 0:
                            soma = soma + img2[(x+i),(y+j)]
                        else:                
                            img2[(x+i),(y+j)] = soma/9

                cont = cont + 1   

            cont = 0
            soma = 0

    return cv2.imshow('Passa Baixo 3', img2)

import cv2

def passaBaixo5(img2):

    soma = 0
    cont = 0

    #img2 = cv2.imread('lena.jfif', 0)
    cv2.imshow('Original', img2)

    for x in range (0, img2.shape[0]-4):
        for y in range(0, img2.shape[1]-4):
            while(cont < 2):
                for i in range(-1, 3):
                    for j in range(-1, 3):
            #            img[(x+i),(y+j)] = 255
                        if cont == 0:
                            soma = soma + img2[(x+i),(y+j)]
                        else:                
                            img2[(x+i),(y+j)] = soma/16

                cont = cont + 1   

            cont = 0
            soma = 0

    return cv2.imshow('Passa Baixo 5', img2)       

import cv2

def passaBaixo7(img2):

    soma = 0
    cont = 0

    #img2 = cv2.imread('lena.jfif', 0)
    cv2.imshow('Original', img2)

    for x in range (0, img2.shape[0]-8):
        for y in range(0, img2.shape[1]-8): 
    #        img [x,y] = 255

            while(cont < 2):
                for i in range(-1, 7):
                    for j in range(-1, 7):
                #        img[(x+i),(y+j)] = 255
                        if cont == 0:
                            soma = soma + img2[(x+i),(y+j)]
                        else:
                            img2[(x+i),(y+j)] = soma/64
                
                cont = cont + 1

            cont = 0
            soma = 0


    return cv2.imshow('Passa Baixo 7', img2)

def logicoAND(img3, img4):

    rows = img3.shape[0]
    cols = img3.shape[1]
    rows2 = img4.shape[0]
    cols2 = img4.shape[1]

    cv2.imshow('Imagem Original', img2)

    img5 = []

    for i in range(rows):
        for j in range(cols):
            img5[i,j] = 0

    for i in range(rows):
        for j in range(cols):
            if (img3[i,j] and img4[i,j]):
                img5[i,j] = 255
            else:
                img5[i,j] = 0
    return cv2.imshow('Operacao Logica AND', img5)

        
    
#escalaCinza(img)

#binarizacao(img2)

#mono(img)

#negativo(img)

#operacaoMult(img2)

#operacaoDiv(img2)

#operacaoSoma(img2)

#operacaoSubt(img2)

#limiarizacao(img2) #revisar

#histograma(img2)

#equalizacaoHistograma(img2) #revisar

#salEPimenta(img2)

gauss(img2)

#alargamentoContraste(img2)

#fatiamento(img2)

#escala(img2)

#translacao(img2)

#espelhamento(img2)

#passaBaixo3(img2)

#passaBaixo5(img2)

#passaBaixo7(img2)

#logicoAND(img3, img4)



cv2.waitKey(0)