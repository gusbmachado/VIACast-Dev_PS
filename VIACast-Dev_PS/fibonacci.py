import unittest #framework para testes unitários
import math #biblioteca para utilização de funções matemáticas

# Função iterativa para exibir o n-ésimo termo da sequência de Fibonacci
def fibonacci(n: int) -> int:

    #primeiros termos
    n1, n2 = 0, 1
    #variável contador e variável auxiliar
    count, aux = 0, 0

    #teste da validade da entrada
    if n <= 0:
        return -1
    #primeiro termo, retorna n2 == 1
    elif n == 1 or n == 2:
        return n2
    #exibe n-ésimo termo da sequência
    else:
        while count < n:
            aux = n1 + n2
            #atualiza valores
            n1 = n2
            n2 = aux
            count += 1
        return n1 

"""
# Função recursiva para exibir o n-ésimo termo da sequência de Fibonacci
def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
"""

"""
# Função matemática para exibir o n-ésimo termo da sequência de Fibonacci
def fibonacci(n: int) -> int:
    
    #definição do número de ouro 1,618...
    phi = (1+math.sqrt(5))/2
    #forma matemática do n-ésimo termo da sequência
    f = ((phi**n)-(1-phi)**n)/math.sqrt(5)
    #os valores resultantes, do tipo float, são arredondados => isso causa imprecisão em termos de posição mais elevada
    return int(round(f,0))
"""

#TESTES UNITÁRIOS#
class TestFbn(unittest.TestCase):

    def test_fbn(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(22), 17711)
        self.assertEqual(fibonacci(100), 354224848179261915075)
        self.assertEqual(fibonacci(200), 280571172992510140037611932413038677189525)
        self.assertEqual(fibonacci(300), 222232244629420445529739893461909967206666939096499764990979600)
        self.assertEqual(fibonacci(400), 176023680645013966468226945392411250770384383304492191886725992896575345044216019675)
        self.assertEqual(fibonacci(450), 4953967011875066473162524925231604047727791871346061001150551747313593851366517214899257280600)

if __name__ == '__main__':
    unittest.main()