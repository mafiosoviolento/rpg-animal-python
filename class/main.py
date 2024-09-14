import Model as model
import Ambiente as ambiente
import Animal as animal
import Jogo as jogo

personagem1 = animal.Animal('Leão', 1000, 400, 200, 5, 'vivo', 'Felino', 'Anda', 'Savana', 15)
personagem2 = animal.Animal('Tigre', 1200, 350, 200, 7, 'vivo', 'Felino', 'Anda', 'Selva', 22)

jogo = jogo.Jogo()
jogo.definePersonagem(personagem1, personagem2)
jogo.iniciarJogo()