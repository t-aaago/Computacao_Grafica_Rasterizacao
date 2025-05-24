"""
Exercício: Rasterização de Triângulo com Bresenham

Enunciado:
Implemente um programa (em linguem de sua preferência) que desenhe um triângulo em uma grade de pixels utilizando o algoritmo de Bresenham para linhas.

Sua tarefa é:
Gere 3 pares ordenados aleatórios dentro dos limites da grande pixel proposta, que serão vértices (A,B e C) de um triângulo
Verifique se os vértices formam um triângulo fechado e válido
Rasterizar as três arestas do triângulo (AB, BC e CA) usando o algoritmo de Bresenham.
Armazenar ou exibir os pontos correspondentes aos pixels ativados para cada aresta.
Representar o resultado em uma matriz de 50x50, onde 1 representa um pixel desenhado e 0 um pixel vazio.

Dicas:
•Modularize sua implementação criando uma função bresenham(x0, y0, x1, y1) reutilizável.
•Lembre-se de que as arestas devem ser rasterizadas em ordem e conectadas para formar corretamente o contorno do triângulo.
•Teste com diferentes coordenadas e resoluções de tela para observar o comportamento do algoritmo.
"""
import random

pontoA = (4,6)
pontoB = (7,1)

def retornaM(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def reflexao(m, x1, y1, x2, y2):
    troca_xy = False
    troca_x = False
    troca_y = False

    if m > 1 or m < -1:
        x1, y1 = y1, x1 
        x2, y2 = y2, x2
        troca_xy = True
        print("Trocou xy")
    
    if x1 > x2:
        x1 = -x1
        x2 = -x2
        troca_x = True
        print("Trocou x")
    
    if y1 > y2:
        y1 = -y1
        y2 = -y2
        troca_y = True
        print("Trocou y")

    return x1, y1, x2, y2, troca_xy, troca_x, troca_y



def bresenham(x1, y1, x2, y2):
    pixels = []
    x, y = x1, y1

    m_linha = retornaM(x1, y1, x2, y2)
    e = m_linha - 0.5

    pixels.append((x,y))

    while x < x2:
        if e >= 0:
            y = y + 1
            e = e - 1
        x += 1
        e = e + m_linha
        pixels.append((x,y))
    
    return pixels
    
def reflexaoInversa(pixels, troca_xy, troca_x, troca_y):
    novos_pixels = []
    for pixel in pixels:
        x, y = pixel
        if troca_y:
            y = -y
        if troca_x:
            x = -x
        if troca_xy:
            x, y = y, x
        novos_pixels.append((x, y))
    return novos_pixels


def Rasterizacao(pontoA, pontoB):
    x1, y1 = pontoA[0], pontoA[1]
    x2, y2 = pontoB[0], pontoB[1]

    troca_xy, troca_x, troca_y = False, False, False
    
    m = retornaM(x1, y1, x2, y2)

    x1, y1, x2, y2, troca_xy, troca_x, troca_y = reflexao(m, x1, y1, x2, y2)

    pixels = bresenham(x1, y1, x2, y2)
    
    pixels = reflexaoInversa(pixels, troca_xy, troca_x, troca_y)

    print(pixels)
    

Rasterizacao(pontoA, pontoB)