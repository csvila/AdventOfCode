import numpy as np
input = np.loadtxt("../input02.txt", dtype='i')
soma = 0
for element in input:
	soma += max(element)-min(element)
print(soma)