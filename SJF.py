import JobSpecification
from queue import PriorityQueue

jobList = JobSpecification.jobs
jobs = jobList
jobQueue = PriorityQueue(maxsize=0)
time = 0
print("BurstTime \tStartedTime \t CompeltedTime")
while len(jobs) > 0:

    for job in jobs:
        if time < job['ArrivalTime']:
            break
        jobQueue.put(job['BurstTime'], job['BurstTime'])

        jobs = [j for j in jobs if j != job]

    while not jobQueue.empty():
        BurstTime = jobQueue.get()
        print("\t", BurstTime, "\t\t\t", time, end="\t\t\t")
        time = time + BurstTime
        print(time)
