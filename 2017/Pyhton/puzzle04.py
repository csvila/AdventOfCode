import numpy as np
import math as m
input = np.loadtxt("../input02.txt", dtype='i')
soma = 0
y = 0
for element in input:
	for item in element:
		for x in range(0, len(element)):
			if item != element[x] and m.gcd(element[x], item) == item:
				soma += element[x] / item
#				print(f"{x}: {element[x]} - {item} = {element[x] / item}")
print(soma)