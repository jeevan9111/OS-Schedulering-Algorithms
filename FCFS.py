import JobSpecification
from queue import Queue

jobList = JobSpecification.jobs
jobs = jobList
jobQueue = Queue(maxsize=0)
time = 0
print("PID \t ArrivalTime \tStarted Time \t Compelted Time")
while len(jobs) > 0:

    for job in jobs:
        if time < job['ArrivalTime']:
            break
        jobQueue.put(job)

        jobs = [j for j in jobs if j != job]

    while not jobQueue.empty():
        PID, ArrivalTime, BurstTime = jobQueue.get()
        print(PID, "\t", ArrivalTime, "\t\t", time, end="\t\t\t")
        time = time + BurstTime
        print(time)
