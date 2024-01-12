import random
import csv 
import math
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt
from classes import Periodic,Processor,Aperiodic
import pickle
import json



def generate_taskset_periodic(num_periodic,n_cores, utilisation,period_choice):
    taskset = []
    total_utilization = 0
    for i in range(num_periodic):
        load = round(random.uniform(0, 1), 2)

        period = random.choice(period_choice)

        execution_time = (period * load)
        task = (i, execution_time, period)
        taskset.append(task)

        total_utilization += load

    target_utilization = min(n_cores * utilisation, total_utilization) 

    if(target_utilization < total_utilization):
        adjustment_factor = target_utilization / total_utilization
    else:
        adjustment_factor = 1
    
    for i in range(num_periodic):
        task = taskset[i]
        load = task[1] / task[2]

        taskset[i] = Periodic(task[0], round((task[1] * adjustment_factor),0), task[2])

    periodic_util = sum([i.ut() for i in taskset])
    return taskset

def generate_taskset_aperiodic(probabilty,duration,r):
    aperiodic_tasks = []
    for i in range(duration-5000):
        if random.random() < 1/1000:

            aperiodic_tasks.append(Aperiodic(len(aperiodic_tasks),random.randint(r[0],r[1]),i))

    return aperiodic_tasks

def write(t,taskset,no):
    with open(t+'_taskset' + str(no) + '.csv','w',newline='') as file:
        writer = csv.writer(file)
        for task in taskset:
            print(task)
            writer.writerow(task)

# write('periodic',n,1)


def generate_multiple_tasksets(offset , num_sets, num_tasks, n_cores, l_util, h_util):
    all_tasksets = []
    for i in range(num_sets):
        with open("taskset" + str(int(offset + i)) + ".csv", 'w', newline='') as file:
                writer = csv.writer(file)
                taskset = generate_taskset(num_tasks, n_cores, l_util, h_util)[0]
                writer.writerow(list(task) for task in taskset)
    return all_tasksets



with open('taskset_input.json','r') as openfile:
    inp = json.load(openfile)

def run(var):
    no_periodic_tasks = inp["no_periodic_tasks"]


    no_cores = inp["no_cores"]

    utilisation_limit = inp["utilisation_limit"]

    periodic_tasks = generate_taskset_periodic(no_periodic_tasks,no_cores,utilisation_limit*(var),[100 * i for i in range(1,11)])
    periodic_file = open('periodic_taskset'+str(var),'wb')

    pickle.dump(periodic_tasks,periodic_file)

    periodic_file.close()


    probabilty = inp["probability"]

    duration = inp["duration"]

    aperiodic_tasks = generate_taskset_aperiodic(probabilty,duration,(100,200))

    aperiodic_file = open('aperiodic_taskset'+str(var),'wb')
    pickle.dump(aperiodic_tasks,aperiodic_file)

    aperiodic_file.close()

for i in range(1,16):
    run(i)

