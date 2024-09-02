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
        self.defineAmbiente()
        self.batalha()

    def finalizarJogo(self):
        print("Jogo finalizado")
    
    def definePersonagem(self, personagem1, personagem2):
        self.personagem1 = personagem1
        self.personagem2 = personagem2

    def defineAmbiente(self):
        ambiente.Ambiente.criaAmbiente(self, ambiente)
    
    def batalha(self):
        while self.personagem1.statusVida == 'vivo' and self.personagem2.statusVida == 'vivo':
            valor = random.randint(1, 2)
            if valor == 1:
                atacante = self.personagem1
                defensor = self.personagem2
            else:
                atacante = self.personagem2
                defensor = self.personagem1

            print(f"O personagem {atacante.nome} é o atacante")
            print(f"O personagem {defensor.nome} é o Defensor")

            ataqueTotal = atacante.agilidade * atacante.ataque
            defesaTotal = defensor.agilidade * defensor.defesa

            porcTotalAtaque =  ataqueTotal / ((ataqueTotal + defesaTotal) / 100)
            # calcular a soma a portcentagem de chance de vencer esse ataque
            if random.randint(1, 100) < porcTotalAtaque:
                dano = atacante.ataque - defensor.defesa
                defensor.receber_dano(dano)
            else:
                print(f"O personagem {atacante.nome} errou o ataque")
            
            print("-"*150)

            # cria a aletoriedade colocando a % recebida com parametro do random random de 1 a 100
            if defensor.vida <= 0:
                defensor.statusVida = 'morto'
                print(f"O personagem {defensor.nome} morreu")
                print(f"O personagem {atacante.nome} ganhou")