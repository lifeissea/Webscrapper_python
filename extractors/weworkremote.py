import requests
from bs4 import BeautifulSoup

def extract_wwr_job(search_term):
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    base_url = "https://weworkremotely.com/"
    html = requests.get(f"{base_url}remote-jobs/search?term={search_term}", headers=headers).text
    html1 = requests.get(f"{base_url}remote-jobs/search?term={search_term}", headers=headers)
    if html1.status_code==200:
        job_result =[]
        soup = BeautifulSoup(html, "html.parser")
        job=(soup.find_all('li', class_="feature"))
        for job_section in job:
            company = job_section.find("span", class_="company")
            title_name = job_section.find("span", class_="title")
            verified_a=""
            print(verified_a)
            location = job_section.find("span", class_="region")
            money=""
            # print(title_name[0].string)
            # print(verified_a[0].string)
            # print(location.string)
            # print(money.string)
            # print("/////////////////////////////////////")
            title_name=title_name.string
            verified_a=verified_a
            company=company.string
            region=location.string
            salary=money


            job_data={
                'company' : company.strip().replace(','," "),
                'position' : title_name.strip().replace(','," "),
                'verified' : verified_a.replace(','," "),
                'region' : region.strip().replace(','," "),
                'salary' : salary.strip().replace(','," ")
            }
            job_result.append(job_data)
        return job_result

    else :
        print("Can't get jobs.")

