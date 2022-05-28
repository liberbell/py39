from newspaper import Article
import nltk

URL = "https://www.reuters.com/world/europe/ukraine-says-troops-may-retreat-eastern-region-russia-advances-2022-05-28/"
article = Article(URL)
article.download()
article.parse()
print(article.publish_date)
print(article.authors)
print(article.text)
print(article.title)

# nltk.download("punkt")
article.nlp()
print(article.keywords)
print(article.summary)