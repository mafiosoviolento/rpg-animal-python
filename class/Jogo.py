import Ambiente as ambiente
import Animal as animal
import random

class Jogo:
    def __init__(self):
        self.vidas = 3
        self.personagem1 = None
        self.personagem2 = None
        self.ambiente = None
        self.urlBase = 'http://localhost:3000/'

    def iniciarJogo(self):
        self.defineAmbiente()
        self.verificaDesvantagensAmbiente()
        self.batalha()

    def finalizarJogo(self):
        print("Jogo finalizado")
    
    def definePersonagem(self, personagem1, personagem2):
        self.personagem1 = personagem1
        self.personagem2 = personagem2

    def defineAmbiente(self):
        self.ambiente = ambiente.Ambiente.defineAmbiente(self, ambiente)

    def verificaDesvantagensAmbiente(self):
        if self.personagem1.habitat != self.ambiente:
            self.retornaDesvantagem(self.personagem1)
            print(f"personagem {self.personagem1.nome} teve desvantagem a nova agilidade é {self.personagem1.agilidade}")

        if self.personagem2.habitat != self.ambiente:
            self.retornaDesvantagem(self.personagem2)
            print(f"personagem {self.personagem2.nome} teve desvantagem a nova agilidade é {self.personagem2.agilidade}")

    def retornaDesvantagem(self, personagem):
        porc = 30
        personagem.agilidade = personagem.agilidade - (personagem.agilidade * porc / 100)
    
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

    def menuIniciarJogo(self):
        print("Jogo iniciado")
        print('Se você deseja cadastrar um novo personagem ou ambiente digite 1')
        print('Iniciar partida, digite 2')
        escolha = int(input())
        if escolha == 1:
            print('Para cadastrar um novo personagem digite 1')
            print('Para cadastrar um novo ambiente digite 2')
            escolha2 = int(input())
            if escolha2 == 1:
                animal.Animal.cadastrarAnimal(self)
                Jogo.menuIniciarJogo(self)
            else:
                ambiente.Ambiente.cadastrarAmbiente(self)
                Jogo.menuIniciarJogo(self)
            
