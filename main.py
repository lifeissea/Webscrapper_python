import requests
from bs4 import BeautifulSoup





def extract_job(search_term):
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    base_url = "https://remoteok.com/"
    html = requests.get(f"{base_url}remote-{search_term}-jobs", headers=headers).text
    html1 = requests.get(f"{base_url}remote-{search_term}-jobs", headers=headers)
    if html1.status_code==200:
        job_result =[]
        soup = BeautifulSoup(html, "html.parser")
        job=(soup.find_all('td', class_="company"))
        job.pop(0)
        for job_section in job:
            title_a=job_section.find_all('a')
            for title in title_a :
                title_name=title.find_all('h2')
            verified_a=job_section.find_all('span')
            location_money=job_section.find_all('div')
            location=location_money[0]
            money=location_money[1]
            # print(title_name[0].string)
            # print(verified_a[0].string)
            # print(location.string)
            # print(money.string)
            # print("/////////////////////////////////////")
            title_name=title_name[0].string
            verified_a=verified_a[0].string
            region=location.string
            salary=money.string


            job_data={
                'company' : title_name.strip(),
                'verified' : verified_a,
                'region' : region.strip(),
                'salary' : salary.strip()
            }
            job_result.append(job_data)
        for job_results in job_result:
            print(job_results)
            print("///////////////")
    else :
        print("Can't get jobs.")

extract_job("rust")
