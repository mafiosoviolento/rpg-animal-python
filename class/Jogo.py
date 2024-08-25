import Ambiente as ambiente
import Animal as animal
import random

class Jogo:
    def __init__(self):
        self.vidas = 3
        self.personagem1 = None
        self.personagem2 = None

    def iniciarJogo(self):
        print("Jogo iniciado")
        print(self.personagem1.nome)
        self.defineAmbiente()
        print(self.vidas)
        self.batalha()

    def finalizarJogo(self):
        print("Jogo finalizado")
    
    def definePersonagem(self, personagem1, personagem2):
        self.personagem1 = personagem1
        self.personagem2 = personagem2

    def defineAmbiente(self):
        ambiente.Ambiente.criaAmbiente(self)
    
    def batalha(self):
        while self.personagem1.statusVida == 'vivo' and self.personagem2.statusVida == 'vivo':
            valor = random.randint(1, 2)
            
            if valor == 1:
                atacante = self.personagem1
                defensor = self.personagem2 
            else:
                atacante = self.personagem2
                defensor = self.personagem1

            ataqueTotal = atacante.agilidade * atacante.ataque
            defesaTotal = defensor.agilidade * defensor.defesa

            somaGeral = ataqueTotal + defesaTotal 

            # calcular a soma a portcentagem de chance de vencer esse ataque

            # cria a aletoriedade colocando a % recebida com parametro do random random de 1 a 100


            self.personagem1.statusVida = 'morto'

            
            




personagem1 = animal.Animal('Leão', 1000, 400, 200, 6, 'vivo', 'Felino', 'Anda', 'Saavana', 15)
personagem2 = animal.Animal('Tigre', 1200, 350, 200, 6, 'vivo', 'Felino', 'Anda', 'Selva', 22)

jogo = Jogo()
jogo.definePersonagem(personagem1, personagem2)
jogo.iniciarJogo()