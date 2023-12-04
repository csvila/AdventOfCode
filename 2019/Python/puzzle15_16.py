file_path = '../input/input_dia08.txt'
layer_size = 6*25
image = []

def get_program(file):
    with open(file) as f:
        return list([chars for chars in f.read() if chars != '\n'])

def get_layer(file_data, start_position):
	return file_data[start_position: start_position+layer_size]

def create_image(file_data):
	for start_position in range(0, len(file_data), layer_size):
		image.append(get_layer(file_data, start_position))

def find_fewest_0():
	idx, min_layer_index, min_layer_count = 0, 0, layer_size
	for l in image:
		count0 = l.count('0')
		if count0 < min_layer_count:
			min_layer_count = count0
			min_layer_index = idx
		idx += 1
	return min_layer_index

def count_elements(idx, element_type):
	return image[idx].count(element_type)

def _run():
	file_data = get_program(file_path)
	create_image(file_data)
	min_0_layer = find_fewest_0()
	count1 = count_elements(min_0_layer, '1')
	count2 = count_elements(min_0_layer, '2')
	return count1 * count2

print(_run())
