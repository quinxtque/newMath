import math
from math import sqrt
from math import acos
from math import pi
# Ввод векторов
print("Ввод вектора OA")

vecOAx = int(input("Введите x: "))
vecOAy = int(input("Введите y: "))
vecOAz = int(input("Введите z: "))

print("Ввод вектора OB")
vecOBx = int(input("Введите x: "))
vecOBy = int(input("Введите y: "))
vecOBz = int(input("Введите z: "))

print("Ввод вектора OC")

vecOCx = int(input("Введите x: "))
vecOCy = int(input("Введите y: "))
vecOCz = int(input("Введите z: "))

# Вывод длин рёбер
# Вектор АВ
vecABx = vecOBx - vecOAx
vecABy = vecOBy - vecOAy
vecABz = vecOBz - vecOAz
# Вектор ВС
vecBCx = vecOCx - vecOBx
vecBCy = vecOCy - vecOBy
vecBCz = vecOCz - vecOBz
# Вектор CA
vecCAx = vecOCx - vecOBx
vecCAy = vecOCy - vecOBy
vecCAz = vecOCz - vecOBz

OA = sqrt(vecOAx**2 + vecOAy**2 + vecOAz**2)
OB = sqrt(vecOBx**2 + vecOBy**2 + vecOAz**2)
OC = sqrt(vecOCx**2 + vecOCy**2 + vecOCz**2)
AB = sqrt(vecABx**2 + vecABy**2 + vecABz**2)
BC = sqrt(vecBCx**2 + vecBCy**2 + vecBCz**2)
CA = sqrt(vecCAx**2 + vecCAy**2 + vecCAz**2)

print("Сторона OA = ", OA)
print("Сторона OB = ", OB)
print("Сторона OC = ", OC)
print("Сторона AB = ", AB)
print("Сторона BC = ", BC)
print("Сторона CA = ", CA)

# cos a = (vec1;vec2) / |vec1| * |vec2|
# (ab;ac) = xa*xb + ...

angleA1 = vecABx * (-vecCAx) + vecABy * (-vecCAy) + vecABz * (-vecCAz)
cosCornerA = angleA1 / (sqrt(vecABx**2 + vecABy**2 + vecABz**2) * sqrt((-vecCAx)**2 + (-vecCAy)**2 + (-vecCAz)**2))
a_rad = acos(cosCornerA)
a_deg = a_rad * 180 / pi

angleB1 = (-vecABx) * vecBCx + (-vecABy) * vecBCy + (-vecABz) * vecBCz
cosCornerB = angleB1 / (sqrt((-vecABx)**2 + (-vecABy)**2 + (-vecABz)**2) * sqrt(vecBCx**2 + vecBCy**2 + vecBCz**2))
b_rad = acos(cosCornerA)
b_deg = b_rad * 180 / pi

angleC1 = vecCAx * (-vecBCx) + vecCAy * (-vecBCy) + vecCAx * (-vecBCz)
cosCornerC = angleC1 / (sqrt(vecCAx**2 + vecCAy**2 + vecCAz**2) * sqrt((-vecBCx)**2 + (-vecBCy)**2 + (-vecBCz)**2))
c_rad = acos(cosCornerA)
c_deg = c_rad * 180 / pi

print("Угол А: ", a_deg)
print("Угол B: ", b_deg)
print("Угол С: ", c_deg)

# Площадь боковой поверхности
# sSideFull = sOAC + sOBC + sOAB
# sTriangle = |[a;b]| / 2
#   i      j      k
# vecACx vecACy vecACz
# vecABx vecABy vecABz
# i = vecACy * vecABz - vecACz * vecABy
# j = vecACx * vecABz - vecACz * vecABx
# k = vecACx * vecABy - vecACy * vecABx

sOBC = sqrt(
    (vecOBy * vecOCz - vecOBz * vecOCy)**2 +
    (vecOBx * vecOCz - vecOBz * vecOCx)**2 +
    (vecOBx * vecOCy - vecOBy * vecOCx)**2
) / 2

sOAC = sqrt(
    (vecOAy * vecOCz - vecOAz * vecOCy)**2 +
    (vecOAx * vecOCz - vecOAz * vecOCx)**2 +
    (vecOAx * vecOCy - vecOAy * vecOCx)**2
) / 2

sOAB = sqrt(
    (vecOAy * vecOBz - vecOAz * vecOBy)**2 +
    (vecOAx * vecOBz - vecOAz * vecOBx)**2 +
    (vecOAx * vecOBy - vecOAy * vecOBx)**2
) / 2

sSide = sOAB + sOBC + sOAC
print("Площадь боковой поверхности: ", sSide)

# Площадь основания
# TODO: Если что то не так будет с площадями, попробовать поменять стороны местами
sBottom = sqrt(
    ((-vecCAx) * vecABz - (-vecCAx) * vecABx)**2 +
    ((-vecCAx) * vecABz - (-vecCAx) * vecABx)**2 +
    ((-vecCAx) * vecABy - (-vecCAx) * vecABx)**2
) / 2
print("Площадь основания: ", sBottom)

# Полная площадь
sFull = sSide + sBottom
print("Полная площадь: ", sFull)

# Объём
# Vabc = |(a;b;c)|
# |vecOAx vecOAy vecOAz|
# |vecOCx vecOCy vecOCz|
# |vecOBx vecOBy vecOBz|
crutch1 = (vecOAx * vecOCy * vecOBz + vecOAy * vecOCz * vecOBx + vecOAz * vecOCx * vecOBy)
crutch2 = (vecOAz * vecOCy * vecOBx + vecOAy * vecOCx * vecOBz + vecOAx * vecOCz * vecOBy)
volume = abs((crutch1-crutch2) / 6)
print("Объём пирамиды: ", volume)

# Высоты
# O -> ABC
# A -> OBC
# B -> OAC
# C -> OAB
# h = Vabc / Sab
OH = volume / sBottom
AH = volume / sOBC
BH = volume / sOAC
CH = volume / sOAB

print("Высота OH:", OH)
print("Высота AH:", AH)
print("Высота BH:", BH)
print("Высота CH:", CH)