"""Pontifícia Universidade Católica de Minas Gerais Instituto 
Ciências Exatas e Informática (ICEI) 
Engenharia de Computação
Disciplina: Sistemas Operacionais 
Professor: Diego Silva Caldeira Rocha
Alunos: Matheus Dias Soares e Gabriel Avelar Sabato
Trabalho Prático 3"""

from random import uniform
from time import sleep
from threading import Thread, Semaphore

class Filosofo(Thread):
    executar = True  # variável para realizar a execução

    def __init__(self, filosofo, palito_esquerda, palito_direita):  # Construtor da classe Filosofo
        Thread.__init__(self)
        self.filosofo = filosofo
        self.palito_esquerda = palito_esquerda
        self.palito_direita = palito_direita

    def run(self):
        while self.executar:
            print(f"\n {self.filosofo} está pensando")
            sleep(uniform(5, 10))
            self.comer()

    def comer(self):
        palito1, palito2 = self.palito_esquerda, self.palito_direita

        while self.executar:  
            palito1.acquire()  # pega o primeiro palito
            locked = palito2.acquire(False)  # verifica se o segundo palito está livre
            if locked:
                break
            palito1.release()  # libera o palito1
        else:
            return  # volta a pensar

        print(f"\n {self.filosofo} começou a comer")
        sleep(uniform(5, 10))
        print(f"\n {self.filosofo} parou de comer")
        palito1.release()  # libera o palito1
        palito2.release()  # libera o palito2
        print(f"\n {self.filosofo} liberou os dois palitos")

filosofos = ['Filosofo 1', 'Filosofo 2', 'Filosofo 3', 'Filosofo 4', 'Filosofo 5']  
palitos = [Semaphore(1) for _ in range(5)]
mesa = [Filosofo(filosofos[i], palitos[i % 5], palitos[(i + 1) % 5]) for i in range(5)]
print("Alunos: Gabriel Avelar Sabato e Matheus Dias Soares")
for _ in range(50):
    Filosofo.executar = True  # Inicia a execução
    for filosofo in mesa:
        try:
            filosofo.start()  # inicia o objeto de thread criado.
            sleep(2)
        except RuntimeError:  # Se a thread já tiver sido iniciada
            pass
    sleep(uniform(5, 10))
    Filosofo.executar = False  # Para a execução
