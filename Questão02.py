import turtle
import math


def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)


wn = turtle.Screen()  # Configura a tela e seus atributos
wn.bgcolor("lightgreen")  # Cor de fundo: verde-claro
wn.title("Questão 02 - Lista 01")  # Título
tess = turtle.Turtle()  # Cria a setinha
tess.color('deeppink')  # Muda a cor da linha para rosa
draw_poly(tess, 8, 50)  # Chama a função que desenha um polígono de 8 lados de tamanho 50
wn.mainloop()
