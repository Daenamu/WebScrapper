import requests
from bs4 import BeautifulSoup

LIMIT = 50



def extract_pages(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    pages = pagination.find_all('a')
    spans = []
    for page in pages[:-1]:
        spans.append(int(page.string))
    max_page = spans[-1]
    return max_page

def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]

    company = html.find("span", {"class": "company"})

    if company is not None:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = company_anchor.string
        else:
            company = company.string
        company = company.strip()

    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]

    job_id = html["data-jk"]

    return {'title': title, 'company': company, 'location': location, "link": f"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping indeed page {page + 1}")
        result = requests.get(f"{url}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
        for section in results:
            job = extract_job(section)
            jobs.append(job)
    return jobs

def get_jobs(word):
    url = f"https://www.indeed.com/jobs?q={word}&limit={LIMIT}"
    last_pages = extract_pages(url)
    jobs = extract_jobs(last_pages, url)
    return jobs