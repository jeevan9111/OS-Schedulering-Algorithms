import JobSpecification
from queue import Queue

jobList = JobSpecification.jobs
jobs = jobList
jobQueue = Queue(maxsize=0)
time = 0
quantum = 3

print ("* before completed time denotes the task is completed")
print("PID \tStarted Time \t Compelted Time")


def execute():
    PID, _, BurstTime = jobQueue.get()

    global time
    print(PID, "\t\t\t", time, end="\t\t\t\t")
    if BurstTime > quantum:
        time += quantum
        jobQueue.put((PID, time, BurstTime - quantum))
    else:
        time += BurstTime
        print("*", end='')
    print(time)


while len(jobs) > 0:
    for job in jobs:
        if time < job['ArrivalTime']:
            break
        jobQueue.put(job)
        jobs = [j for j in jobs if j != job]
    if not jobQueue.empty():
        execute()
        while len(jobs) == 0 and not jobQueue.empty():
            execute()
