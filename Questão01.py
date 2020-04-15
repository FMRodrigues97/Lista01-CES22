import turtle


def quadrado(s, l):
    """Faz a seta s desenhar um quadrado de lado l"""
    for i in range(4):
        s.forward(l)
        s.left(90)


wn = turtle.Screen()  # Configura a tela e seus atributos
wn.bgcolor("lightgreen")  # Cor de fundo: verde-claro
wn.title("Questão 01 - Lista 01")  # Título
seta = turtle.Turtle()  # Cria a setinha
for q in range(1, 6):
    seta.color('deeppink')  # Muda a cor da linha para rosa
    quadrado(seta, 20 * q)  # Chama a função que desenha um quadrado
    seta.penup()
    seta.goto([-10 * q, -10 * q])  # Reposiciona a seta
    seta.pendown()

wn.mainloop()
