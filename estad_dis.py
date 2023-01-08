from _operator import length_hint
import unittest
import csv
li = []
m = mo = me = var = des = i = 0

with open('edad.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        list.append(li,int(row[0]))

#lee cada espacio del arreglo y suma su contenido
def sumatoria (li,m,i):
    t = length_hint(li)
    while i < t:
        m = li[i] + m
        i +=1
    return m

#llama a la funcion sumatoria despues de sumar todos los elementos del arreglo, los divide entre el numero de elementos par obtener la media
def media  ( li,m,i):
    m = sumatoria(li,m,i) / length_hint(li)
    return m

#recorre el areglo y almacena el numero con mayor repeticiones, cada vez que avanza verifica si el numero actual se repite mas que el almacenado de ser asi lo sobreescribe
def moda (li,mo,i):
    t = length_hint(li)
    f = 0
    while i<t:
            if contm (li,f,i) > mo:
                mo = li[i]
            i +=1
            f = 0
    return mo

#cuenta el numero de veces que un numero se repite en el arreglo, como minimo 1 vez
def contm (li,f,i):
    x = 0
    t = length_hint(li)
    while x<t:
        if li[i]==li[f]:
            f +=1
        x += 1
    return f

#proximamente
def mediana (li):
    li.sort()
    t = length_hint(li)
    o = round(length_hint(li)/2)
    if t%2 == 0:
        me = ((li[round(t/2)]) + (li[round(t/2)-1])) / 2
        return me
    else:
        me = li[o]
        return me

#recorre el arreglo a la vez que aplica la formula de la varianza, una vez llegado a su fin se divide el resultado entre el numero de elementos
def varianza (li,var):
    i = 0
    t = length_hint(li)
    me = media(li,m,i)
    while i<t:
        var = var + calculov (li,i,me)
        i += 1
    var = var / len(li)
    return round(var,2)

#por cada espacio del arreglo alica la formula de la varianza, el numero actual menos la media elevado al cudrado
def calculov (li,i,me):
    res = (li[i] - me) ** 2
    return res


#aplica la formula de la desviacion que es aplicar una raiz cadrada al calculo de la varianza
def desviacion (li):
    des = varianza(li,var)**0.5
    return round(des,2)

#halla el ceficiente de dispersion que se obtiene al dividir la desviacion estandar entre la media
def coef (li):
    coef = desviacion(li) / media(li,m,i)
    return round(coef,2)


            #TEST DE CADA MODULO (utilizando el problema visto en clases como caso base)#
class TestMethods(unittest.TestCase):
    def test_media(self):
        a = media([24, 23, 21, 25, 24, 22, 20, 21, 22, 24],m,i)
        b = 22.6
        self.assertEqual(a,b,'media:INcorecto')

    def test_moda(self):
        a = moda([24, 23, 21, 25, 24, 22, 20, 21, 22, 24],mo,i)
        b = 24
        self.assertEqual(a,b,'moda:Incorrecto')

    def test_varianza(self):
        a = varianza([24, 23, 21, 25, 24, 22, 20, 21, 22, 24],var)
        b = 2.44
        self.assertEqual(a,b, 'varianza:Incorrecto')

    def tets_desviacion(self):
        a = desviacion([24, 23, 21, 25, 24, 22, 20, 21, 22, 24])
        b =1.56
        self.assertEqual(a,b, 'desviacion:Incorrecto')

    def test_coeficiente(self):
        a = coef([24, 23, 21, 25, 24, 22, 20, 21, 22, 24])
        b = 0.07
        self.assertEqual(a,b,'coeficiente:Incorrecto')

    def test_mediana(self):
        a = mediana([24, 23, 21, 25, 24, 22, 20, 21, 22, 24])
        b = 22.5
        self.assertEqual(a,b,'mediana:Incorrecto')
if __name__ == '__main__':
    unittest.main()
