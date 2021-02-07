import csv

def save_to_file(jobs, filename):
    file = open(filename, mode="w")
    writer = csv.writer(file)
    writer.writerow(["Title", "Company","Link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    
    print(jobs)
    return