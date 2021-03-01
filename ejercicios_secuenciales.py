# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:22:44 2021

@author: Licht
"""

# Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.

inv1 = float(input('Digite inversíón de la primera persona: $'))
inv2 = float(input('Digite inversíón de la segunda persona: $'))
inv3 = float(input('Digite inversíón de la tercera persona: $'))
totalinv = inv1 + inv2 + inv3

print('El primer porcentaje inversión es de: ', (inv1/totalinv)*100)
print('El segundo porcentaje de inversión es de: ', (inv2/totalinv)*100)
print('El tercer porcentaje de inversión es de: ', (inv3/totalinv)*100)

# Una empresa paga a sus empleados además del sueldo base una
# bonificación especial de $80.000 por cada hijo. Realice un programa
# que determine el monto de la bonificación y el monto total a
# pagar al trabajador

canth = int(input('Digite la cantidad de hijos: '))
sb = 1000000
tb = canth * 80000
tm = sb + tb
print(f'La bonificación es de: ${tb}')
print(f'El monto total a pagar es de: ${tm}')

# Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final

ma = float(input('Digite el valor del monto: '))
i = 0.015
mf = (ma * i) + ma
print(f'El saldo final es de: ${mf}')

# Una inmobiliria vende terrenos a $80.000 el metro cuadrado. El
# cliente debe dar una cuota inicial del 35% y el resto lo paga en 12
# cuotas. Determine el valor a pagar por cuota inicial y el monto de
# cada cuota

vt = 80000
c = int(input('Digite el número de cuotas: '))
ci = vt * 0.35
cm = (vt * 0.65)/c
print(f'La cuota inicial es de: ${ci}')
print(f'Las cuotas mensuales son de: ${cm}')


# Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
# programa en Java que determine el monto de cada descuento y el
# monto total a pagar al trabajador.
print('SUELDO BASE: $1.000.000')
sb = 1000000
lpp = sb * 0.01
ss = sb * 0.04
sf = sb * 0.005
ca = sb * 0.05
mf = sb - lpp - ss - sf - ca
print(f'El monto por ley de política pública es de: ${lpp}')
print(f'El monto por seguro social es de: ${ss}')
print(f'El monto por seguro forzoso es de: ${sf}')
print(f'El monto por caja de ahorro es de: ${ca}')
print(f'El monto total a pagar es de: ${mf}')

# El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en cetímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.

np = int(input('Digite el número de palabras: '))
cc = float(input('Digite cantidad de centímetros: '))
cco = int(input('Digite cantidad de colores: '))
vp = np * 20000
vc = cc * 15000
vco = cco * 25000
vt = vp + vc + vco
print(f'El valor total a pagar por el aviso clasificado es de: ${vt}')


# Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un programa en Java que determine el monto
# del bono a pagar a un trabajador que tiene varios años en la empresa.

ca = int(input('Ingrese cantidad de años de labor: '))
ba1 = 100000
bsa1 = 120000
if ca >= 1:
    bf = ((ca-1)*bsa1) + ba1
else:
    bf = 0
print(f'El monto a pagar en bono por años de labor es de: ${bf}')


# Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor

nh = float(input('Ingrese el número de horas trabajadas: '))
vh = 20000
dh = (nh * vh) * 0.05
tp = (nh * vh) * 0.95
print(f'El valor a descontar es de: ${dh}')
print(f'El valor total a pagar es de: ${tp}')


# Un centro de comunicaciones alquilan tarjetas para realizar llamadas
# y cobran el monto consumido de la tarjeta mas un recargo del 20%.
# Teniendo como dato de entrada el monto inicial y el monto final de la
# tarjeta, determine el costo de la llamada.

mi = float(input('Digite el monto inicial: '))
mf = float(input('Digite el monto final: '))
clla = (mi - mf) * 0.80
print(f'El costo de la llamada es de: ${clla}')

# En una fototienda cobran por el revelado de un rollo $1.500 por cada
# foto. Realice un programa en Java que determine el monto a pagar
# por un revelado completo sabiendo que adiconalmente le cobran el
# IVA (16%).

cf = int(input('Digite la cantidad de fotos: '))
vr = 1500
tp = cf * vr
tpi = tp + (tp * 0.16)
print(f'Valor total a pagar más IVA es de: ${tpi}')

# En un hospital existen tres áreas: Ginecología, Pediatría y
# Traumatología. El presupuesto anual del hospital se reparte
# conforme a la siguiente tabla:
# Area Porcentaje Presupuestal
# Ginecología     40%
# Traumatología   30%
# Pediatría       30%
# Obtener la cantidad de dinero que recibirá cada área, para cualquier
# monto presupuestal.

pa = float(input('Ingrese el presupuesto anual: '))
g = pa * 0.40
t = pa * 0.30
p = pa * 0.30
print(f'El dinero que recibirá ginecología es de: ${g}')
print(f'El dinero que recibirá traumatología es de: ${t}')
print(f'El dinero que recibirá pediatría es de: ${t}')


# Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
# que consiste en dejar gratis el alquiler de una película. Realice un
# programa en Java que teniendo como dato de entrada el total de
# películas alquiladas, y el número de días de alquiler, determine el
# monto a pagar.

cp = int(input('Digite la cantidad de películas alquiladas: '))
da = int(input('Digite la cantidad de días a alquilar: '))
va = 1500
if cp > 1:
    pf = ((cp-1) * va) * da
else:
    pf = (cp * va) * da
print(f'El monto total a pagar es de: ${pf}')


# Una Agencia de viajes cobra por un Tour a Cartagena $25.000
# diarios por persona. Realice un programa en Java que determine el
# monto a pagar por una familia que desee realizar dicho Tour
# sabiendo que también cobran el 12% de IVA.

dv = int(input('Digite el número de días del Tour: '))
cp = int(input('Digite la cantidad de personas en el Tour: '))
vt = 25000
mt = dv * cp * vt
mti = (mt * 0.16) + mt
print(f'El valor total del Tour por {cp} es de: ${mti}')


# Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
# clientes. Cobra por una habitación $100.000 el primer día y por el
# resto $200.000 por día. Realice un programa en Java que determine
# el valor total a pagar por la habitación si la estadía fue de varios
# días.

de = int(input('Digite la cantidad de días de estancia: '))
v1 = 200000
v2 = 100000
if de > 1:
    pf = ((de - 1) * v1) + v2
else:
    pf = v2
print(f'El valor a pagar por la estancia es de: ${pf}')


# El banco del Pueblo da microcréditos a empresarios para ser
# cancelados en un lapso de 2 años (24 meses). Al monto del
# préstamo se le cobra un interés del 24%. El empresario debe pagar
# la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
# cuotas ordinarias. Realice un algoritmo que teniendo como dato de
# entrada el monto del préstamo, determine el monto total a pagar por
# el préstamo, el monto de las cuotas especiales y el monto de las
# cuotas ordinarias.

mi = float(input('Digite cantidad del préstamo: '))
mii = mi + (mi * 0.24)
ce = (mii / 2) / 4
co =  (mii / 2) / 20
print(f'El monto total a pagar es de: {mii}')
print(f'El monto de las cuotas especiales es de: ${ce}')
print(f'El monto de las cuotas ordinarias es: ${co}')























