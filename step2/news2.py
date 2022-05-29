from newspaper import Article
import newspaper
import nltk

URL1 = "https://www.itmedia.co.jp/"
URL2 = "https://thebridge.jp/"

website = newspaper.build(URL1, memoize_articles = False)

i = 0
for article in website.articles:
    article.download()
    article.parse()
    article.nlp()
    print("Article", ":", article.title)
    print(article.url)
    print(article.summary, end="\n")