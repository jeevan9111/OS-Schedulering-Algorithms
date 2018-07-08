import JobSpecification
from Queue import Queue

jobList = JobSpecification.jobs
jobs = jobList
jobQueue = Queue(maxsize=0)
time = 0
quantum = 3


def execute():
    PID, _, BurstTime = jobQueue.get()
    global time
    print(PID)

    if BurstTime > quantum:
        time += quantum
        jobQueue.put((PID, time, BurstTime - quantum))
    else:
        time += BurstTime


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
