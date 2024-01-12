import csv

def get_tasks(n,t):
	tasks = []
	with open(t+"_"+'taskset' +str(n)  + '.csv', newline='', encoding='utf-8') as f:
		reader = csv.reader(f)
		for row in reader:
			tasks.append(row)

	return tasks

def lmse(processors,duration= None):
	avg_ult = 0
	if duration:
		for i in processors:
			avg_ult += i.accurate_ut(duration)
	else:
		for i in processors:
			avg_ult += i.ut()
	avg_ult /= len(processors)

	error = 0
	if duration:
		for i in processors:
			error += (1/len(processors) * ((i.accurate_ut(duration) - avg_ult) ** 2))**1/2
	else:
		for i in processors:
			error += (1/len(processors) * ((i.ut() - avg_ult) ** 2))**1/2

	return error
	

