from operator import imod
from newspaper import Article
import newspaper

URL1 = "https://www.itmedia.co.jp/"
URL2 = "https://thebridge.jp/"

website = newspaper.build(URL1, memoize_articles = False)