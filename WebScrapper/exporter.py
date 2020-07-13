import csv
import os
fileDir = os.path.dirname(os.path.realpath('__file__'))

filename = os.path.join(fileDir, 'WebScrapper/jobs.csv')

def save_to_file(jobs):
    file = open(filename, "w", -1, "utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))