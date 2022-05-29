import newspaper
import csv
import datetime

URL = "https://www.bloomberg.co.jp/"
website = newspaper.build(URL, memoize_articles = False)

i = 0

for article in website.articles:
    article.download()
    article.parse()
    article.nlp()
    print("Article" ,str(i), ":", article.title)
    print(article.url)
    print(article.summary, end="\n\n")

    if i > 9:
        break
    i = i + 1

csv_date = datetime.datetime.today()