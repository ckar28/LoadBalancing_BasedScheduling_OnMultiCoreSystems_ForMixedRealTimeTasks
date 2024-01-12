def edf_ff(tasks,processors):
	
	tasks.sort(key = lambda x: x.WCET)
	for i in tasks:
		if i.processor:
			i.processor.ptasks.remove(i)
			i.processor = None
	while True:
		flag = True
		for i in tasks:
			if i.processor == None:			
				for j in processors:
					if(j.ut() + i.ut() <= 1):
						j.ptasks.append(i)
						i.processor = j
						flag = False
						break

		if flag:
			break
def edf_wf(tasks,processors):

	tasks.sort(key = lambda x: x.WCET)
	for i in tasks:
		if i.processor:
			i.processor.ptasks.remove(i)
			i.processor = None
	while True:
		for i in tasks:

			processors.sort(key = lambda x: x.ut())
			flag = True
			if i.processor == None:
				for j in processors:
					
					if(j.ut() + i.ut() <= 1):
						j.ptasks.append(i)
						i.processor = j
						flag = False
						break

		if flag:
			break

def edf_bf(tasks,processors):
	for i in tasks:
		if i.processor:
			i.processor.ptasks.remove(i)
			i.processor = None

	tasks.sort(key = lambda x: x.WCET)


	while True:
		flag = True
		for i in tasks:
			processors.sort(key = lambda x: -x.ut())
		
			if i.processor == None:
				for j in processors:
					if(j.ut() + i.ut() <= 1):
						j.ptasks.append(i)
						i.processor = j
						flag = False
						break

		if flag:
			break

def lbsa(processors,k):
	avg_ult = 0
	flag = False
	for i in processors:
		avg_ult += i.ut()
		i.ptasks.sort(key = lambda x: x.ut())
	avg_ult /= len(processors)
	processors.sort(key = lambda x: x.ut())
	for i in range(len(processors)):

		for j in processors:
			j.ptasks.sort(key = lambda x: x.ut())

		if(processors[i].ut() <= avg_ult - k):
			for j in range(i + 1,len(processors)):
				if(not(processors[j].ptasks)):
					continue
				while processors[j].ut() - processors[j].ptasks[0].ut() > (avg_ult - k)  and processors[i].ut() + processors[j].ptasks[0].ut() < avg_ult:
					flag = True
					processors[j].ptasks[0].processor = processors[i]
					processors[i].ptasks.append(processors[j].ptasks[0])
					processors[j].ptasks.pop(0)

	if flag:
		lbsa(processors,k)

def lbpsa(tasks,processors,k):


	edf_ff(tasks,processors)

	f = sum([1 if i.processor == None else 0 for i in tasks])


	copy = [i for i in tasks]

	edf_wf(tasks,processors)

	b = sum([1 if i.processor == None else 0 for i in tasks])
	if b == min(b,f):

		lbsa(processors,k)
	else:
		edf_ff(tasks,processors)
		lbsa(processors,k)


