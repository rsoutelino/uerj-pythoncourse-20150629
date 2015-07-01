#! -*- coding: utf-8 -*-


#  Curso UERJ - "Python para computação científica, com Ênfase em geociências"
#  Ministrantes: Andre Lobato e Rafael Soutelino
#  vanessa testandoo
#  Curso pyhton - "Analise de Dados Oceanografia - PPG UERJ"
#  Ministrantes: Rafael Soutelino
<<<<<<< HEAD

#  Nível: Básico ao Avançado
=======
#  Nível: Básico 
>>>>>>> eeea2ca0f0e3533f1d1f8b8fb616f703e56796b9
#  Data: 27/11/2014
#  Local: UERJ, Rio de Janeiro 
#################################################
#
# Aula 1
# 23422
# Tópico 1 - Conhendo tipos de objetos Python
#
##teste helen ocn
# teste Camila
#################################################

# Atribuindo Variáveis

a = 1 #sim

<<<<<<< HEAD
b = 2   ##preferencialmente não
=======
b = 3.0   #preferencialmente não
>>>>>>> eeea2ca0f0e3533f1d1f8b8fb616f703e56796b9

# Não usar letras como nome de variaveis. Use um nome auto explicativo
# Não começar com numeros

# variaveis comuns
nome_do_sujeito = 'Zé da Silva'

# Convenção. Valores constantes e globais do código em caps.
NUMERO_PI = 3.14
DATA_DIR = '/Users/rsoutelino/Desktop/CursoPython/'

# Comentários

# bem, isso é um comentário

""" 
Isso é um comentário
com 
múltiplas linhas
"""

# Booleanos
True

False

has_name = True

has_name = False

# Strings
#--------------------------------------------------

'Isso é uma string'

"Com aspas duplas tambem é válido"

'String "com aspas" escapadas'

'''Isso é uma string
com multiplas linhas no código mas não na impressão'''

"""
strings
continua aqui
"""

'''Isso é uma string \n 
com multiplas linhas que será impresso em duas linhas'''

u'Isso é uma string unicode'

# Operações com Strings
#--------------------------------------------------

frase = 'Isso ' + 'é ' + 'uma ' + 'string ' + "só!"

regua = '=' * 80

# Variáveis em String
#--------------------------------------------------

palavra = 'Sem falta'
valor = 500

'Precisamos de R$%i!!!' % valor
                                            
'Precisamos de R$%0.2f, %s!!!' % (valor, palavra)

'Nos encontraremos às %04d,  %s!!!' % \
                    (valor, palavra)

# %s - string
# %i - inteiros
# %f - floats


# Números
#--------------------------------------------------

## inteiro
a = 3
b = 5

## float
a = 2.
b = 3.4

## long
a = 123423445556767688899045445673268L ** 344

# Listas e Tuplas
#--------------------------------------------------

lista_vazia = []
lista_de_compras = ['alface', 'tomate', 'banana']

lista_dentro_de_lista = [[1,2,3],
                         [1,2,3],
                         [1,2,3]]

# tuplas podem ser assim
(32,33,42,68)

# ou assim
32,33,42,68

exemplo_de_tupla = ('alface','tomate') 

## indexação de Listas e Tuplas

lista_de_compras[0] # primeiro ítem

lista_de_compras[:] # Todos os ítems

lista_de_compras[:2] # os dois primeiros items

lista_de_compras[2:] # do segundo ítem em diante

lista_de_compras[-1] # o último ítem

lista_de_compras[-2] # o penúltimo ítem

lista_de_compras[1:3] # segundo ao terceiro ítem

lista_de_compras[0:3:2] # do primeiro ítem até o terceiro de 2 e, 2

lista_de_compras[0][:3] # os 3 primeiros characteres do primeiro item da lista

# Dicionários - palavra-chave: valor
#--------------------------------------------------

vazio = {}

compras = {'salada' : ['alface', 'tomate', 'cebola'],
           'frutas' : ['melão', 'laranja', 'melancia'],
           'dinheiro' : 100.,
           'trouxe_cartao' : True,
       }

compras['salada'][2]


# Operadores
#--------------------------------------------------

## Matemáticos

a = 3 + 4 # soma

b = 3 - 4 # subtração

c = 3 * 4

c = 3 / 4 # divisão de inteiros

c0 = 3./4 # divisão de floats

d = 3 // 4 # quociente

e = 3 % 4  # resto

f = 3 ** 4 # potencia

conta = ((a + b)/3) ** (f/c)

## Incremento

a += b # equivale: a = a + b

a *= b # equivale: a = a * b

a /= b # equivale: a = a / b

a **= b # equivale: a = a ** b

# Statements
#--------------------------------------------------

print 'Hello World'

import matplotlib

pais = 'Brazil!'

exec "hello = 'Hello %s" % pais

# cuidado! não use exec por comodidade. Última alternativa!

pass # como o nome ja diz, passa

del pais


# Lendo mensagens de erro
SyntaxError
TypeError
ZeroDivisionError
NameError

#################################################
#
# Tópico 2 - Um pouco de programação
#
#################################################

# importações
#--------------------------------------------------

import matplotlib

import datetime

import matplotlib as mpl

from matplotlib import pyplot as plt

import matplotlib.pyplot as plt

from matplotlib.pyplot import 

from matplotlib import *

# Identação
#--------------------------------------------------

# Serve para separar blocos de código
# Convenção: Usar 4 espaços. Não usar tabulações

"Linha sem identação"
    "Linha com 1 nivel de identação"
        "2o nível de identação"


# Empacotando e desempacotando variáveis
#--------------------------------------------------

d = [1,2,3]
a, b, c = 1,2,3
a, b, c = d


# Loops
#--------------------------------------------------

# for loop

lista_de_compras = ['banana', 'alface', 'tomate']
n = 25

print "+" * n
print "Minha lista de compras:"
print "+" * n

for compra in lista_de_compras:
    print compra
print "+" * n

# while loops

b = 0
while b <= 5:
    print b
    b += 1

# continue x break

for compra in lista_de_compras:
    if compra == 'banana':
        continue
    print compra

for compra in lista_de_compras:
    if compra == 'alface':
        break
    print compra


# Definindo Funções
#--------------------------------------------------

def potencia():
    c = 2 ** 4


def potencia(a, b):
    c = a ** b
    print c 

def potencia(a, b):
    print a ** b

def potencia(a, b):
    return a ** b

def potencia(a, b=0):
    c = a ** b
    print "%.2f à potencia de %.2f é igual à %.2f" % (a, b, c) 
    return c

result = potencia(2,8)


# Condicionais if elif e else
#--------------------------------------------------

sequencia = [0,1,2,3,4,5,6,7,8,9]

for n in sequencia:
    if n <= 3:
        print 'Número: ' + str(n)
    elif n == 4:
        print 'Mas esse é o número: ' + str(n)
    elif n == 5:
        print 'Agora o número: ' + str(n)
    else: 
        print 'Outros números: ' + str(n)

for n in sequencia:
    if n == 3 or n == 5 or n == 7:
        print 'Número ímpar: %i' % n
    elif n == 2 or n == 4 or n == 8:
        print 'Numero par %i' % n

for n in sequencia:
    if n in [1,3,5,7,9]:
        print 'Número ímpar: %i' % n

    elif n not in [0,1,3,5,7,9]:
        print 'Número par %i' % n

    else:
        print 'Número não é par nem impar: %i ' % n


# O poder da introspecção:
#--------------------------------------------------

## Métodos da String

"a".upper()

"A".lower()

"abraço".startswith('abra')

print "b-palavras".replace('b','caça')

p = 'computação científica 5,3'

p.title().replace(',','.')

"banana".count('a')

b = 'primeira linha \n segunda linha'

b = b.splitlines()

c = ';'.join(b)

## Métodos da lista

lista_de_compras

lista_de_compras.append('cebola')

lista_de_compras.extend(['xuxu','beterraba'])

lista_de_compras.append(['vinho','cerveja','agua'])

lista_de_compras.pop(3)

lista_de_compras.pop(lista_de_compras.index('xuxu'))

lista_de_compras.remove('cebola')

lista_de_compras.sort()

## Métodos do Dicionário

compras = {'salada' : ['alface', 'tomate', 'cebola'],
           'frutas' : ['melão', 'laranja', 'melancia'],
           'bebidas' : ['vinho', 'cerveja', 'agua']}

compras.keys()

compras.values()

compras.items()

compras.pop('salada')

compras['salada'] = ['cenoura', 'batata', 'repolho']


# Funções Built-in Python
#--------------------------------------------------

## Conversões

a = str(2)
b = float(a)
c = int(b)

## range

range(23)
range(23,32,2)

## len
len(sequencia)
len(compras)

## enumerate
for i, compra in enumerate(lista_de_compras):
    print str(i) + '' + str(compra)

## range(len())
for i in range(len(sequencia)):
    print sequencia[i]

## zip
formulario = ['nome','idade','sexo','profissao']
respostas = ['Ze da Silva', 18, 'masculino', 'programador']

zip(formulario,respostas)

## Funções matemáticas

abs(-344)

pow(3,2) == 3 ** 2

divmod(90,7) # 90/7 devolve (cociente,resto)

complex(3,1)


## input x raw_input
#--------------------------------------------------

# somente códigos pyhton
input("Entre com algum código python:")

# tudo será interpretado como strings
raw_input("Entre com algum valor:")


# Bibliotecas Básicas python
#--------------------------------------------------

## Operações com Data e Hora (datetime)
#--------------------------------------------------

import datetime as dt

hoje = dt.date.today()

amanha = hoje + dt.timedelta(1)

ontem = hoje + dt.timedelta(-1)

futuro = hoje + dt.timedelta(days=365)

agora = dt.datetime.now()

deadline = dt.date(2000,03,12)

endtime = dt.datetime(2000,03,12,14,25)


## Operações com o Sistema Operacional (os)
#--------------------------------------------------

import os

# Juntar caminhos
dados = os.path.join(DATA_DIR, 'dados.txt')

# Checar exitencia de caminho
os.path.exists(DATA_DIR)

# Somente nome do arquivo do caminho
os.path.basename(dados)

# Criar diretórios
os.mkdir(DATA_DIR)

os.path.exists(DATA_DIR)

# Analogamente remover
os.rmdir(DATA_DIR)


# Executar comandos diretamente no shell
#--------------------------------------------------

comando = "cp %s %s" % (dados, DATA_DIR)

os.system(comando)


# A importância do sys.path 
#--------------------------------------------------

import sys

sys.path

sys.platform


#################################################
#
# Aula 4 - Técnicas Avançadas e outras Ferramentas
# Tópico 1 - Orientação à objetos
#
#################################################


# Importando seus próprios programas
#--------------------------------------------------

from myproject import myfunction


# Classes
#--------------------------------------------------

class MinhaClasse(object):
    """ Demonstrativo para explicar o que é e como usar uma classe """
    def __init__(self, arg):
        #super(MinhaClasse, self).__init__()
        self.arg = arg

    def meu_metodo(self):
        print self.arg

minha_classe = MinhaClasse()


class MinhaOutraClasse(MinhaClasse):
    """É um exemplo de herança de classe."""
    def __init__(self):
        super(MinhaOutraClasse, self).__init__()
        self.meu_metodo()

    def meu_metodo(self):
        print "Agora meu método imprime outra coisa"

    def outro_metodo(self):
        print "Este método só está presente nessa classe mas não na outra"


outra_classe = MinhaOutraClasse()


###########################################
#
# Tópico 2 - Técnicas avançadas
#
###########################################

# Passeando pelos caminhos (os.walk)
#--------------------------------------------------

for root,directories, filenames in os.walk("/Users/rsoutelino/matlab_roms/"):
    if "etopo5.nc" in filenames:
        print 'root: ' + root
        print 'directories: ' + str(directories)
        print 'filenames: ' + str(filenames)

# Funções Lambda
#--------------------------------------------------

quadrado = lambda x: x ** 2

potencia = lambda z, x: z ** x

quad_pot = lambda z, x=2: z ** x


# List Comprehension
#--------------------------------------------------

lista = [[0,1,2,3,4],
         [0,1,2,3,4],
         [0,1,2,3,4],
         [0,1,2,3,4],]

nova_lista = [ x[2] for x in lista ]

nova_lista = []
for x in lista:
    nova_lista.append(x[2])


bichos = ['cão', 'gato', 'passarinho']

[ bicho+' Vacinado!' for bicho in bichos ]


# Expressões Regulares
#--------------------------------------------------

import re

dados = "0.43   0.27    0.32    0.26    0.74"

re.split('\s+',dados)

dados = "Temperatura do Mar: 0.3 ;  0.43   l 33.433   , 34.54"

re.split(';|l|,|/s+', dados)

re.findall('(\d+\.\d+)', dados)

re.search('Mar', dados)

re.search('Mar', dados).group()

re.match('Mar', dados)

re.match('Temp', dados)




# Automatização: Scripting + Crontab
#--------------------------------------------------


# Git: Controle de Versão
#--------------------------------------------------


# Ambientes Virtuais
#--------------------------------------------------


