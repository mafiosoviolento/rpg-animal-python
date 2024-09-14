import Model as model
import random
class Ambiente:
    def __init__(self, nome):
        self.nome = nome

    def verificaDesvantagens(self, nome, habitatePersonagem):
        print("A desvantagem do ambiente é: ")

    def criaAmbiente(self, ambientes):
        print("O ambiente foi criado")
        ambientes = model.Model.getDadosApi(self,"ambientes")
        qtdAmbientes = len(ambientes.json())
        alet = random.randint(0, qtdAmbientes - 1)
        return ambientes.json()[alet]['nome']