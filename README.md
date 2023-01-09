# TIRANT LO BLANCH

# steps to get this assignment up and running:

Asure you have python, pip and git installed on your machine.

Open a terminal and run the following commands:

1. `git clone this repo`
2. `cd to folder`
3. `python -m venv venv`
4. If you are on Unix/macOS run `source venv/bin/activate`, if you are on windows run `venv\Scripts\activate`
5. `pip install --upgrade pip && pip install -r requirements.txt`
6. `scrapy crawl pnavarraspider -O results.json`
7. At this moment you will have a json file called results.json on the root directory with the scraped results


NOTE: The folder structure has been generated with the following command `scrapy startproject project_name`
