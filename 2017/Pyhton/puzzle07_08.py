def count_no_duplicated():
	f = open('../input04.txt')
	sum_valid = 0

	for line in f:
		sum_valid += verify_duplicated_for_line(line)
	return sum_valid

def count_no_rearrange():
	f = open('../input04.txt')
	sum_valid2 = 0

	for line in f:
		sorted_line = []
		words = line.split(" ")
		for word in words:
			sorted_line.append(''.join(sorted(word)))
		stringona = ''
		for x in sorted_line:
			stringona += x + " "
		sum_valid2 += verify_duplicated_for_line(stringona)
	return sum_valid2

def verify_duplicated_for_line(line):
	arr = line.split()
	my_dic = list(dict.fromkeys(arr))
	if len(arr) == len(my_dic):
		return 1
	return 0

print(count_no_duplicated())
print(count_no_rearrange())