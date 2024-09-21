import Personagem as personagem
import Model as model

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
        idAnimal = 7
        animalNome = str(input("Digite o nome do animal a ser criado:  "))
        data = {
            "id": idAnimal,
            "nome": animalNome
        }
        resposta = model.Model.setDadosApi(self, "animais", data)
        if(resposta):
            print("Animal Cadastrado com sucesso")
        else:
            print('Ouve um erro ao cadastrar o animal')
