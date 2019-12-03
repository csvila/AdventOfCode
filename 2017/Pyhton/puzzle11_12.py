def listToString(s):
	str1 = ""  
	for ele in s:  
		str1 += str(ele)   
	return str1 

def refreshMatrix(matrix):
	biggest = max(matrix)
	base_stack = matrix.index(biggest)  # Primeira ocorrência do maior valor entre as colunas
	matrix[base_stack] = 0
	for idx in range(1, biggest + 1):
		col_idx = base_stack + idx
		if base_stack + idx>15:
			col_idx = base_stack + idx - 16
		matrix[col_idx] += 1
	return matrix

def redistribute():
	f =  open("../input06.txt")
	nums = list(map(int, f.readline().split()))
	sets = []
	sets.append(listToString(nums))
	counter = 0
	while True:
		nums = refreshMatrix(nums)
		counter += 1
		strNums = listToString(nums)
		sets.append(strNums)
		if sets.count(strNums) > 1:
			print(f"Counter {counter}")
			return nums

def break2(number):
	new_set = []
	strNumber = listToString(number)
	new_set.append(strNumber)
	counter = 0
	strNums = ""
	while strNums!=strNumber:
		number=refreshMatrix(number)
		counter += 1
		strNums = listToString(number)
		new_set.append(strNums)
	print(f"Counter {counter}")


numMatrix = redistribute()
break2(numMatrix)