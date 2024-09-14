import Personagem as personagem

class Animal(personagem.Personagem): 

    def __init__(self, nome, vida, ataque, defesa, agilidade, statusVida, especie, movimento, habitat, idade):
        super().__init__(nome, vida, ataque, defesa, agilidade, statusVida)
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.agilidade = agilidade
        self.statusVida = statusVida
        self.especie = especie
        self.movimento = movimento
        self.habitat = habitat
        self.idade = idade

    def cadastrarAnimal(self):
        print("Cadastrando um novo animal")