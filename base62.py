import math

def digit_to_b62_char(input_i: int) -> str:

	# '0' to '9'
	if input_i >= 0 and input_i <= 9:
		return chr(48 + input_i)
	# 'A' to 'Z'
	elif input_i >= 10 and input_i <= 35:
		return chr(55 + input_i)
	# 'a' to 'z'
	elif input_i >= 36 and input_i <= 61:
		return chr(61 + input_i)
	else:
		raise ValueError(f"{input_i} falls outside range for base62")

def b62_char_to_digit(input_c: str) -> int:

	input_ord = ord(input_c)

	# '0' to '9'
	if input_ord >= 48 and input_ord <= 57:
		return (input_ord - 48)
	# 'A' to 'Z'
	elif input_ord >= 65 and input_ord <= 90:
		return (input_ord - 55)
	# 'a' to 'z'
	elif input_ord >= 97 and input_ord <= 122:
		return (input_ord - 61)
	else:
		raise ValueError(f"{input_c} falls outside range for base62")


def to_b62(input_i: int) -> str:

	ret_chars = []

	biggest_exp = int(math.log(input_i, 62))
	
	rem = input_i
	cur_exp = biggest_exp
	while cur_exp >= 0:
		cur_coeff = int(rem / (62 ** cur_exp))
		cur_coeff_char = digit_to_b62_char(cur_coeff)
		ret_chars.append(cur_coeff_char)
		rem -= (cur_coeff * (62 ** cur_exp))
		cur_exp -= 1

	ret_str = ''.join(ret_chars)
	return ret_str

def from_b62(input_s: str) -> int:

	ret_i = 0

	for (cur_idx, cur_coeff_c,) in enumerate(input_s):
		cur_coeff = b62_char_to_digit(cur_coeff_c)
		cur_exp = len(input_s) - cur_idx - 1
		ret_i += (cur_coeff * (62 ** cur_exp))

	return ret_i