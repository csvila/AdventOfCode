input_range="367479-893698".split('-')
# input_range="111-130".split('-')
min_value = int(input_range[0])
max_value = int(input_range[1])

def split(word): 
    return [char for char in word]

def counter(passw):
	sizes = []
	for i in passw:
		cont = passw.count(i)
		if cont == 2:
			sizes.append(cont)
			return True

	# print(f"{passw} - {sizes} - {len(sizes)}")
	return False

def count_valid_passwords():
	count_passwords = 0
	for x in range(min_value, max_value):
		strVal = split(str(x))
		actual_digit = 0
		count_validated_digits = 0
		for digit in strVal:
			iDigit = int(digit)
			if iDigit < actual_digit:
				break;
			else:
				actual_digit = iDigit			
				count_validated_digits += 1
		
		if count_validated_digits == len(strVal) and counter(strVal):
			count_passwords += 1
	return count_passwords

print(count_valid_passwords())