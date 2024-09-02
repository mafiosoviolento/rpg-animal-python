class Personagem:
    def __init__(self, nome, vida, ataque, defesa, agilidade, statusVida):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.agilidade = agilidade
        self.statusVido = statusVida 

    def atacar(self):
        return self.ataque

    def defender(self):
        return self.defesa
    
    def receber_dano(self, dano):
        self.vida -= dano
        print(f"O personagem {self.nome} recebeu um dano de {dano} e agora tem a vida: {self.vida}")
    
