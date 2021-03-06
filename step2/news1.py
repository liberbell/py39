from newspaper import Article
import nltk

URL = "https://www.itmedia.co.jp/mobile/articles/2205/27/news028.html"
# URL = "https://diamond.jp/articles/-/303917"

article = Article(URL, memoize_articles = False)
article.download()
article.parse()
print(article.authors)
print(article.publish_date)
print(article.text)
print(article.title)