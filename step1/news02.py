from time import strftime
import newspaper
import csv
import datetime

URL = "https://www.bloomberg.co.jp/"
website = newspaper.build(URL, memoize_articles = False)

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "Bloomberg_" + csv_date + ".csv"

f = open(csv_file_name, "w", encoding="cp932", errors="ignore")
writer = csv.writer(f, lineterminator="\n")
csv_header = ["Aricle No", "Title", "URL", "Summary"]
writer.writerow(csv_header)

i = 0

for article in website.articles:
    csvlist = []
    article.download()
    article.parse()
    article.nlp()
    print("Article" ,str(i), ":", article.title)
    print(article.url)
    print(article.summary, end="\n\n")
    csvlist.append(str(i))
    csvlist.append(article.title)
    csvlist.append(article.url)
    csvlist.append(article.summary)
    writer.writerow(csvlist)

    if i > 9:
        break
    i = i + 1

f.close()