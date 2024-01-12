import csv

from time import *



#intial classes and basic definations
def init_cores(n):
	processors = [Processor(i) for i in range(n)]
	return processors

class Processor:
	def __init__(self,no):
		self.tasks = []
		self.last_vd = 0
		self.no = no

	def ut(self):
		x = 0
		for i in self.tasks:
			x+= i.ut()
		return x


	def cal_vd(task):
		vd = max(task.time,self.last_vd) + task.ex/self.ut()

class Periodic:
	def __init__(self,no,WCET,period):
		self.period = period
		self.WCET = WCET
		self.no = no

	def ut(self):
		return self.WCET/self.period

	def __str__(self):
		return f'tasks no: {self.no}, task WCET: {self.WCET} tasks period: {self.period} tasks ut {self.ut()}'


#simulation
global clock
def simulation(processors = None):
	clock = 0
	while clock < 300:
		for i in processors:
			i.tasks.sort(key = lambda x: x.period)
			
		clock += 1
		




#algorithms
def edf_ff(tasks,processors):
	tasks.sort(key = lambda x: x.WCET)
	i = 0
	while i < len(tasks):
		# print(i)
		# print(tasks[i].no,tasks[i].WCET)
		flag = True
		for j in processors:
			# print(j.ut(),j.tasks)
			if(j.ut() + tasks[i].ut() <= 1):
				j.tasks.append(tasks[i])
				tasks.pop(i)
				flag = False
				break

		if flag:
			i += 1
def edf_bf(tasks,processors):
	tasks.sort(key = lambda x: x.WCET)
	i = 0

	while i < len(tasks):
		# print(i)
		# print(tasks[i].no,tasks[i].WCET)
		processors.sort(key = lambda x: x.ut())
		flag = True
		for j in processors:
			# print(j.ut(),j.tasks)
			if(j.ut() + tasks[i].ut() <= 1):
				j.tasks.append(tasks[i])
				tasks.pop(i)
				flag = False
				break

		if flag:
			i += 1

def lbpsa(processors,k):
	avg_ult = 0
	flag = False
	for i in processors:
		avg_ult += i.ut()
		i.tasks.sort(key = lambda x: x.ut())
	avg_ult /= 6
	processors.sort(key = lambda x: x.ut())
	for i in range(len(processors)):

		for j in processors:
			j.tasks.sort(key = lambda x: x.ut())

		if(processors[i].ut() <= avg_ult - k):
			for j in range(i + 1,len(processors)):
				if(not(processors[j].tasks)):
					continue
				while processors[j].ut() - processors[j].tasks[0].ut() > (avg_ult - k)  and processors[i].ut() + processors[j].tasks[0].ut() < avg_ult:
					flag = True
					processors[i].tasks.append(processors[j].tasks[0])
					processors[j].tasks.pop(0)

	if flag:
		lbpsa(processors,0.05)

#measures
def lmse(processors):
	avg_ult = 0

	for i in processors:
		avg_ult += i.ut()
	avg_ult /= 6

	error = 0
	for i in processors:
		error += (1/6 * ((i.ut() - avg_ult) ** 2))**1/2

	return error

#tasks
def get_tasks(n):
	tasks = []
	with open('taskset' +str(n)  + '.csv', newline='', encoding='utf-8') as f:
		reader = csv.reader(f)
		for row in reader:
			task_list = row

	for i in task_list:
		x = i[1:-2]
		list_x = x.split(",")
		# print(list_x)
		tasks.append(Periodic(int(list_x[0]),int(list_x[1]),int(list_x[2])))
		# print(tasks[-1].no,tasks[-1].WCET,tasks[-1].period)
	return tasks

def result_taskset(n,no_cores):
	tasks = get_tasks(n)
	processors = init_cores(no_cores)

	edf_ff(tasks,processors)


	# for i in processors:
	# 	print(i.ut())

	before = lmse(processors)
	# print("lmse before " ,lmse(processors))
	lbpsa(processors,0.05)

	# print("after")
	# for i in processors:
	# 	print(i.ut())

	after = lmse(processors)
	# print("lmse after ",lmse(processors))

	# print(before - after)

	return before - after


def get_results():
	no_of_right = 0
	right = 0
	no_of_wrong = 0
	wrong = 0
	for i in range(500):
		# print(i)
		x = result_taskset(i,6)
		if(x >= 0):
			right += x
			no_of_right += 1
		else:
			# print(i,x)
			wrong += x
			no_of_wrong += 1

	print(no_of_right, no_of_wrong)
	print(right,wrong)

# get_results()

simulation()