from newspaper import Article

URL = "https://www.reuters.com/world/europe/ukraine-says-troops-may-retreat-eastern-region-russia-advances-2022-05-28/"
article = Article(URL)
article.download()
article.parse()