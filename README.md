# Exercício: Rasterização de Triângulo com Bresenham

## Enunciado

Implemente um programa (em linguagem de sua preferência) que desenhe um triângulo em uma grade de pixels utilizando o algoritmo de **Bresenham para linhas**.

### Sua tarefa é:

* Gerar **3 pares ordenados aleatórios** dentro dos limites da grade de pixels proposta, que serão os vértices (A, B e C) de um triângulo.
* Verificar se os vértices formam um **triângulo fechado e válido**.
* **Rasterizar** as três arestas do triângulo (AB, BC e CA) usando o algoritmo de **Bresenham**.
* Armazenar ou exibir os pontos correspondentes aos **pixels ativados** para cada aresta.
* Representar o resultado em uma **matriz de 50x50**, onde:

  * `1` representa um **pixel desenhado**.
  * `0` representa um **pixel vazio**.

---

## Dicas

* 🔹 Modularize sua implementação criando uma função `bresenham(x0, y0, x1, y1)` **reutilizável**.
* 🔹 Lembre-se de que as **arestas devem ser rasterizadas em ordem** e conectadas para formar corretamente o contorno do triângulo.
* 🔹 Teste com **diferentes coordenadas** e **resoluções de tela** para observar o comportamento do algoritmo.

---
