
from classes import Periodic,Processor,Aperiodic

from partition_algorithms import lbpsa,edf_ff,edf_bf,edf_wf,lbsa

from algorithms import edf,tbs,tbs_migration

from metric import lmse

from helper import get_tasks,lmse

import random 

import pickle

import json


def init_cores(n):
    processors = [Processor(i) for i in range(n)]
    
    return processors

def init_tasks(tasks_list):
    periodic_tasks = []
    for i in tasks_list:
        periodic_tasks.append(Periodic(i[0],i[1],i[2]))
    return periodic_tasks

def run(var):
    periodic_file = open('periodic_taskset'+str(var),'rb')

    periodic_tasks = pickle.load(periodic_file)
    periodic_file.close()



    aperiodic_file = open('aperiodic_taskset'+str(var),'rb')

    aperiodic_tasks = pickle.load(aperiodic_file)
    aperiodic_file.close()


    with open('simulation_input.json','r') as openfile:
        inp = json.load(openfile)

    no_cores = inp["no_cores"]
    lbpsa_threshold = inp["lbpsa_threshold"]

    processors = init_cores(no_cores)

    lbpsa(periodic_tasks,processors,0)

    util = [0 for i in range(4)]

    processors.sort(key = lambda x:x.ut())
    time = 0
    duration = inp["duration"]

    while time <= -1:


        for i in aperiodic_tasks:
            if i.arrival_time == time:
                tbs_migration(i,processors)
                pass

        for i,task in enumerate(periodic_tasks):
            if time % task.period == 0:
                if task.remaining_time:
                    print(f'Task is missed at time: {time}\n{task}')

                task.remaining_time = task.WCET




        for i in processors:
            n = edf(i,time)

        lbsa(list(filter(lambda x:not(x.atasks),processors)),0.0001)
        time += 1

    rt = 0
    for i in aperiodic_tasks:
        rt += i.response_time

    return lmse(processors)

array = []
for i in range(1,16):
    
    array.append(run(i))
    print(array)

outfile = open('lbpsa','wb')
pickle.dump(array,outfile)
outfile.close()

