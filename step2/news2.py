from newspaper import Article
import newspaper
import nltk

URL1 = "https://www.itmedia.co.jp/"
URL2 = "https://thebridge.jp/"
URLs = ["https://www.itmedia.co.jp/", "https://thebridge.jp/"]

# website = newspaper.build(URL1, memoize_articles = False)

for url in URLs:
    websites = newspaper.build(url, memoize_articles = False, language="ja")
    i = 0
    for article in websites.articles:
        article.download()
        article.parse()
        article.nlp()
        print("Article", str(i), ":", article.title)
        print(article.url)
        print(article.summary, end="\n")

        if i > 9:
            break
        i = i + 1