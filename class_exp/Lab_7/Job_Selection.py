def job_schedule(jobs):
    max_deadline = 0
    for i in jobs:
        if(i[1] > max_deadline):
            max_deadline = i[1]
    jobs.sort(key=lambda x:x[2],reverse=True)
    job_array=[-1]*max_deadline
    total_profit = 0
    for job in jobs:
        job_id = job[0]
        deadline=job[1]
        value=job[2]

        for j in range(deadline-1,-1,-1):
            if(job_array[j]==-1):
                job_array[j]= job_id
                total_profit+=value
                break
    print("Scheduled Jobs:",job_array)      
    print("Total Profit:",total_profit) 

jobs = [("J1",3,50), ("J2",2,25), ("J3",3,60), ("J4",2,20),("J5",1,15)]
job_schedule(jobs)