def euclidian_algorithm(a, b, count=0):
	if a < b:
		a, b = b, a
	if b == 0:
		return a
	if b == 1:
		return 1
	count += 1
	s = (b+a%b)/(a+b)
	print('iteration:', count)
	print('s_1/s_i+1:', s)
	return euclidian_algorithm(b, a%b, count)

print('GCD:', euclidian_algorithm(48,142))
print('GCD:', euclidian_algorithm(424,22))
print('GCD:', euclidian_algorithm(519,37))
print('GCD:', euclidian_algorithm(345126,72))
