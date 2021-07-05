from math import *

#Definição de classes individuais das formas geométricas

class Rectangle:
  def __init__(this, width, height): 
    #define variáveis para largura e altura
    this.width = width
    this.height = height

  def perimeter(this):
    #Calculo do Perímetro do retângulo (2*largura + 2*altura)
    return 2*this.width + 2*this.height

  @property
  #função built-in que devolve um objeto com essas propriedades
  #permite que declarar uma função para obter o valor de um atributo
  def area(this):
    #Calculo da área do retângulo (largura*altura)
    return this.width*this.height


class IsoscelesTriangle:
  def __init__(this, base, height):
    #define variáveis para base e altura
    this.base = base
    this.height = height

  def perimeter(this):
    #Calculo do Perímetro do triângulo
    #*Note* Temos um triângulo isoceles(2 lados iguais)
    #Para obtermos os lados(side) tomamos metade da base e a altura como catetos de um triângulo retângulo e aplicamos pitágoras
    side = sqrt(this.height**2 + (this.base/2)**2) #função raiz quadrada da biblioteca math
    return 2*side + base #perimetro como soma dos 3 lados

  @property
  def area(this):
    #Calculo da área do retângulo (base*altura*0.5)
    return this.base*this.height/2


class Circle:
  def __init__(this, radius):
    #define variável para o raio
    this.radius = radius

  def perimeter(this):
    #Calculo do Perímetro do círculo (2*π*raio)
    return 2*pi*this.radius #número π da biblioteca math

  @property
  def area(this):
    #Calculo da área do círculo (π*raio²)
    return pi*this.radius**2

#Para entrada de dados:
#a função map(), para armazenar os itens de um iterável em diferentes variáveis, simultaneamente.
#os valores de entrada são definidos como inteiros(int)
#interação com o usuário(input)
#entrada de multiplos valores numa só linha(split), com separação dos dados por vírgula

#Para saída:
#f-string(print(f"...") é um literal de string com prefixo 'f'.
#Strings formatados são expressões avaliadas em tempo de execução.
#O atributo perimetro é chamado como função enquanto que o atributo área(propety) é chamado diretamente
#*Note* O uso de @propety não é necessário, pode-se muito bem tratar o atributo área como uma função convencional(ex.: perimeter).
#Também seria possível tratar o atributo perimetro como property. 
#Nesses casos, o desempenho não é afetado em nenhum sentido.

if __name__ == '__main__':
  width, height = map(int, input('Enter the width and height for the rectangle (<width>,<height>):\n>>').split(','))
  rectangle = Rectangle(width, height)
  print(f"Area: {rectangle.area}\nPerimeter: {rectangle.perimeter()}")

  base, height = map(int, input('Enter the base and height for the isosceles triangle (<base>,<height>):\n>>').split(','))
  triangle = IsoscelesTriangle(base, height)
  print(f"Area: {triangle.area}\nPerimeter: {triangle.perimeter()}")

  radius = int(input('Enter the radius for the circle:\n>>'))
  circle = Circle(radius)
  print(f"Area: {circle.area}\nPerimeter: {circle.perimeter()}")
  
"""
1. Em situações usuais, o código irá funcionar como esperado?
Sim!
2. Existe alguma situação em que não irá funcionar?
Ele não adimite valores tipo float para entrada de dados.
3. Caso exista alguma situação em que o código não irá funcionar, quais alterações seriam necessárias para corrigir os problemas?
A depender da demanda poderiamos usar a função round() para arredondamentos ou restringir o número de casa decimais.
Outra possibilidade seria simplesmente definir valores float em lugar de inteiros.
4. Pensando na legibilidade, facilidade de manutenção por outros desenvolvedores, e extensibilidade, você faria alguma refatoração no código?
Além de comentar o código, definir a entrada para valores float e não aplicar property, creio que o código ficou otimizado.
"""
