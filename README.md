# Capstone Project: Load balancing-based scheduling for mixed real-time tasks on multicore systems 

Load balancing is a critical technique for optimizing the performance of multi-core systems, especially in mixed-real-time (RT) environments where tasks with different levels of urgency and deadlines coexist. Our approach aims to dynamically distribute tasks among the cores in a way that minimizes the overall system response time while meeting the deadlines of RT tasks. We will evaluate our approach using extensive simulations and compare it with existing load-balancing methods.

The project proposes a load-balancing-based scheduling approach for mixed real-time tasks on multicore systems. The proposed approach takes into account the heterogeneity of tasks and the varying processing capabilities of cores. It uses a novel task grouping technique to balance the load across cores and minimize the response time of real-time tasks while maximizing the utilization of the system. Simulation results show that the proposed approach is trying to surpass the existing methods in terms of response time and utilization. The approach is promising for real-time systems that require efficient and effective scheduling of mixed-task workloads on multicore platforms.

The scope of this project covers load balancing techniques in multi-core systems that operate in mixed-real-time environments. The scope of this project does not include hardware-level optimizations or specific real-time scheduling algorithms but rather focuses on load-balancing strategies that can be applied in multi-core systems with mixed-RT workloads. The findings and insights from this project can be useful for researchers, system designers, and practitioners working on load balancing in mixed-RT multi-core systems for a wide range of applications.


## Installation and Usage

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary dependency.

* Generate Random Tasks: Taskset.py will generate random periodic tasks with the specified total utilization values. Here for demonstration purposes, we have used 6 cores so the max_total_utilization value can be 6 but periodic tasks are generated with a utilization value of 3 only i.e. Periodic tasks can only consume 50% of the available CPU utilization.
```bash
python3 taskset.py
```
* Partitioning Algorithms: Partitioning is a load-balancing technique that involves dividing the system’s workload into smaller, manageable partitions, each assigned to different processing units (e.g., cores, processors, or nodes). The goal is to achieve a balanced distribution of computational tasks to ensure that no processing unit is overwhelmed while others remain underutilized. We have defined the implementation of First Fit, Best Fit, and LBPSA which is a novel approach discussed in one of the research papers.

* Classes: Classes.py defines the Class structure for a Processor, Periodic Task, and Aperiodic Task.
* Algorithms: Algorithm.py will contain 2 classic algorithms to schedule tasks. We have presented the implementation of EDF (Earliest Deadline First) and TBS (Total Bandwidth Server) Algorithms. EDF Schedules the Tasks onto cores based on Deadlines and is a Dynamic Scheduling Algorithm. Whereas TBS is used for calculating the Virtual Deadline for Aperiodic tasks and scheduling such tasks onto cores with the minimum virtual deadline.
*Metrics: For comparing the fit of the algorithm with different specifications we are using standard metrics like Least Mean Square Error (LMSE), Response Time, Missed tasks, etc.
* Simulator: The simulator takes all the components described above runs the simulation across a hyper-period and generates the metric graphs for the above algorithms and with custom specs. The module organization for the same is given below.
![Module Organization](https://github.com/urmilkalaria/Load_balancing-based_scheduling_for_mixed_real-time_tasks_on_multicore_systems/blob/main/module_oragnization.jpeg)  



```bash
python3 simulation.py
```

# The project is still in progress."# LoadBalancing_BasedScheduling_OnMultiCoreSystems_ForMixedRealTimeTasks" 
