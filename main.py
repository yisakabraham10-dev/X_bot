# requests
# In this stage what i will do just the bare-minimum to get the link only.
query = (input("Enter the title or the author of the name: "))
new_query = query.replace(" ", "+")
API_KEY = "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"
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
# checking things here

html_content = requests.get("https://arxiv.org/"+ "search/?query="+ new_query + "&searchtype=all&source=header", headers= headers, timeout= 30).text
# print(html_content[:1000])

soup = BeautifulSoup(html_content, "lxml")
divs = soup.find_all("li",class_ = "arxiv-result")
stage1_data = []
for div in divs:
    name_of_the_paper = div.find("p",class_ = "title is-5 mathjax").text.strip()
    links_from_div = div.find_all("a")
    pdf_link = links_from_div[1].get("href")
    retrieved_data = [name_of_the_paper,pdf_link]
    stage1_data.append(retrieved_data)

print(stage1_data)
for n in range(len(stage1_data)):
    print(f"{n+1}: {stage1_data[n][0]}")
choice = int(input("Enter the one you want to summarize: "))-1
chosed_link = stage1_data[choice][1]
chosed_name = stage1_data[choice][0]
chosed_name = chosed_name.replace(" ", "_" )
responses = requests.get(chosed_link, stream= True, timeout= 10)
file_length = int(responses.headers.get('Content-Length', 0))
# print(responses.headers)

# print(responses.status_code)
book_name = ""
with open(f"{chosed_name}.pdf", "wb") as c:
    if responses.headers.get("content-type")== "application/pdf" and responses.status_code == 200:
        downloaded = 0
        for chunk in responses.iter_content(chunk_size= 65536):
            if chunk:
                c.write(chunk)
                downloaded += len(chunk)
            print(f"Download progress: {round((downloaded/file_length)*100,1)}%")
        print(f"Download successfully")
    else:
        print("Download unsuccessful")
import fitz
doc = fitz.open(f"{chosed_name}.pdf")
text_list= []
for n in range(len(doc)):
    page = doc[n]
    blocks = page.get_text("blocks")
    for m in range(len(blocks)):
        if blocks[m][6] == 0:
            text_list.append(blocks[m][4])

headers = {"Authorization": f"Bearer {API_KEY}"}
llm_api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
mini_summaries = []

import asyncio
import aiohttp

async def summarize_block(session, block):
    prompt = f"Summarize the following text into 3-5 sentences:\n\n{block}"
    async with session.post(llm_api_url, headers=headers, json={"inputs": prompt}) as resp:
        result = await resp.json()
        print(result[0]["summary_text"])
        return result[0]["summary_text"]

async def main_summarize():
    async with aiohttp.ClientSession() as session:
        tasks = [summarize_block(session, block) for block in text_list]
        return await asyncio.gather(*tasks)

mini_summaries = asyncio.run(main_summarize())



print(mini_summaries)
#print(html_content)








# downloading
#pdf extraction
#llm fetching
# twitter
