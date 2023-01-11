import requests
from bs4 import BeautifulSoup
from extractors.remoteok import extract_rto_job
from extractors.weworkremote import extract_wwr_job
keyword = input("What do you want to search for? ")

rto = extract_rto_job(keyword)
wwr = extract_wwr_job(keyword)
jobs = rto + wwr
print(jobs)



file = open(f"{keyword}.csv", "w")

file.write("Company, Position, Verifyed, Region, Salary\n")
for job in jobs:
    file.write(f"{job['company']}, {job['positon']}, {job['verified']}, {job['region']}, {job['salary']}\n")

file.close()