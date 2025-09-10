from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from urllib.parse import quote_plus
import csv   # keep if you want to support CSV mode

def job_scrap(query,location,limit):

    



    base_url="https://www.rozee.pk/job/jsearch"
    url=f"{base_url}?q={quote_plus(query)}&l={quote_plus(location)}"


    headers={
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,ur;q=0.7",
    "user-agent": UserAgent().random,
    "connection": "keep-alive",
    "referer": "https://www.rozee.pk/job/jsearch",
}

    

    r=requests.get(url,headers=headers)
    r.encoding="utf-8"

    with open("rozee.html","w",encoding="utf-8") as f:
        f.write(r.text)

    soup=BeautifulSoup(r.text,"html.parser")

    jobs=soup.find_all("div", class_="media-body")
    results=[]


    for job in jobs [:limit]:

        title_element=job.find("h5")
        company_element=job.find("div", class_="tTxt")
        link_element=job.find("a") if title_element else "N/A"

        title=title_element.get_text(strip=True) if title_element else "N/A"
        company=company_element.get_text(strip=True) if company_element else "N/A"
        href = link_element.get("href") if link_element else None
        link = "https:" + href if href else "N/A"


        job_data={
        "title":title,
        "company":company,
        "link":link
                   }

        results.append(job_data)


    return results


if __name__ == "__main__":
    jobs = job_scrap("Software-Engineer", "Lahore", 5)
    for j in jobs:
        print(j)










    
