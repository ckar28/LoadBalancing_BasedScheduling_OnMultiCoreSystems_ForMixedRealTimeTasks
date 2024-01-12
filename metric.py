def lmse(processors):
	avg_ult = 0

	for i in processors:
		avg_ult += i.ut()
	avg_ult /= len(processors)

	error = 0
	for i in processors:
		error += (1/len(processors) * ((i.ut() - avg_ult) ** 2))**1/2

	return error