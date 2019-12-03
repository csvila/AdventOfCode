def navigator(alterFunction):
	with open("../input05.txt") as fp:
	    nums = list(map(int, fp.readlines()))
	print(len(nums))
	i = 0
	c = 0
	while 0 <= i < len(nums):
	    c += 1
	    j = i + nums[i]
	    nums[i] = alterFunction(nums[i])
	    i = j
	print(c,i,j)

def p9(num):
	return num + 1

def p10(num):
	if num<3:
		return num + 1
	return num-1

navigator(p9)
navigator(p10)