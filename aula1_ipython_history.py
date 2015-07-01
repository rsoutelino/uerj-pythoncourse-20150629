a
type(a)
b = 'UERJ'
type(b)
type(a.denominator)
a.denominator
a.conjugate
type(a.conjugate)
a.denominator
denominator_do_a = a.denominator
denominator_do_a
a.conjugate?
a.conjugate()
b
dir(a)
a
%history
b
b.upper()
b.lower()
b.lower().upper()
b.lower().upper().replace('r', 'R')
b.lower().upper().replace('R', 'r')
b.lower().upper().replace('R', 'r').sort()
b.upper?
b.replace?
b.lower~
b.lower
type(b.lower)
whos
lower = a.lower
lower = b.lower
whos
b.replace?
b.replace('U', 'u')
b.replace()
b = 'UUUUUUU'
b.replace('U', 'u')
b
b.replace('U', 'u', count=1)
b.replace('U', 'u', 1)
b.replace('U', 'u', 2)
b.replace('U', 'u', 5)
b
b =  'Rafael'
b.count('a')
b.count('f')
b.count('r')
b.count('R')
b.swapcase()
dado = '94, 23, -42.95684, -23.332, "XBT 1" '
dado
dado.split(',')
dado
dado2 = dado.split(',')
dado2
type(dado2)
whos
temperatura = dado2[1]
temperatura
whos
temperatura = int(dado2[1])
whos
temperatura
lon = dado2[2]
lon = float(dado2[2])
lat = float(dado2[3])
lon
lat
a = 'Rafael'
b = 'UERJ'
a + b
ab = a + b
ab
mensagem = a + "estah na" + b
mesagem
mensagem
mensagem = a + " estah na " + b
mensagem
mensagem = "%s estah na %s" %(a,b)
mensagem
print "%s estah na %s" %(a,b)
lon
print "%s estah na %s na latitude de %0.2f" %(a, b, lon)
print "%s estah na %s na latitude de %0.3f" %(a, b, lon)
print "%s estah na %s na latitude de %0.0f" %(a, b, lon)
print "%s estah na %s na latitude de %04d" %(a, b, lon)
print "%s estah na %s na latitude de %05d" %(a, b, lon)
mensagem =  "%s estah na %s na latitude de %05d" %(a, b, lon)
mensagem
mensagem
mensagem.replace('UERJ', '')
l = [1, 6, 3, 8, 9, 121]
l.pop(0)
l
l.pop(-1)
l
l.remove(8)
l
l.append(8)
l
l.append(121)
l
l.sort()
l
l[0:3]
l[:3]
l[:3]
l[3:]
l
l = range(15)
l
len(l)
l[0:-1:2]
l[::2]
l[::1]
l[::-1]
l.count(14)
l.index(14)
l[::-1].index(14)
d = {'Nome': 'Rafael', 'Idade': 33, 'Nacionalidade': 'Brasileira', 'Longitude': 23.345, 'Ajudantes': ['Phellipe', 'Diego']}
d
d.keys()
keys = d.keys()
keys
type(keys)
type(d)
d
d = {'Nome': 'Rafael', 'Idade': 33, 'Nacionalidade': 'Brasileira', 'Longitude': 23.345, 'Ajudantes': ['Phellipe', 'Diego'], 'Conteudo': {'Shell': '1 dia', 'Git': '1/2 dia', 'Python': '3 dias'} }
d
conteudo = d['Conteudo']
conteudo
d['Nome']
d['Idade']
for key, value  in d:
    print key, value
for key, value  in d.items:
    print key, value
for key, value  in d.items():
    print key, value
d.has_key('Name')
d.has_key('Nome')
d['Conteudo'].has_key('Git')
d['Nome'].has_key('Git')
3 +5
a
l
k = [1, 2, 3]
l + k
l = [1, 2, 'Teste', {'Gitwhos'}]
whos
a = 1
Class CarroManual():
    self.marcha = 'Manual'
Class CarroManual():
    self.marcha = 'Manual'
    def numero_marchas(self, numero):
        self.marchas = numero
class CarroManual():
    self.marcha = 'Manual'
    def numero_marchas(self, numero):
        self.marchas = numero
Class CarroManual():
    marcha = 'Manual'
    def numero_marchas(self, numero):
        self.marchas = numero
class CarroManual():
    marcha = 'Manual'
    def numero_marchas(self, numero):
        self.marchas = numero
class CarroAutomatico():
    marcha = 'Automatica'
fusca = CarroManual()
whos
fusca.marcha
fusca.numero_marchas
fusca.numero_marchas?
fusca.numero_marchas(5)
fusca.marchas
CarroManual??
CarroManual?
class CarroManual():
    marcha = 'Manual'
    def numero_marchas(self, numero):
        self.marchas = numero
%history
