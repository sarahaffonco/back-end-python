## Propriedades - condições do objeto
## Comportamento - feitos do objeto 
## Crie uma classe que modele o objeto "carro".
## 2. Um carro tem os seguintes atributos: ligado, cor, modelo,velocidade.
## 3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,desacelera.
## 4. Crie uma instância da classe carro.
## 5. Faça o carro "andar" utilizando os métodos da sua classe.
## 6. Faça o carro "parar" utilizando os métodos da sua classe.



# Definição da classe
class Carro: # Convenção para nomes de classes: PascalCasing
   ligado = False
cor = "vermelho"
modelo = "Gol"
velocidade = 0

    # Métodos

def ligar(self):
        self.ligado = True

def desligar(self):
        self.ligado = False

def acelerar(self, velocidade):
        self.velocidade += velocidade

def desacelerar(self, velocidade):
        self.velocidade -= velocidade