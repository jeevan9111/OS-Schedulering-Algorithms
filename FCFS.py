import JobSpecification
from Queue import Queue

jobList = JobSpecification.jobs
jobs = jobList
jobQueue = Queue(maxsize=0)
time = 0

while len(jobs) > 0:

    for job in jobs:
        if time < job['ArrivalTime']:
            break
        jobQueue.put(job['BurstTime'], job['BurstTime'])

        jobs = [j for j in jobs if j != job]

    while True:
        BurstTime = jobQueue.get()
        if BurstTime > 0:
            time = time + BurstTime
            print(BurstTime)
        break
