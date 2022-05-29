from newspaper import Article
import nltk

URL = "https://www.itmedia.co.jp/"
article = Article(URL)
article.download()
article.parse()
print(article.authors)