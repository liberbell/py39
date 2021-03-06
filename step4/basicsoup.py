from bs4 import BeautifulSoup

html = """<html>
    <head>
        <title>This is title</title>
    </head>
    <body>
        <p class="title">
            <b>my publish is here</b>
        </p>
        <p class="recent book">
            <a class="book" href="https://www.amazon.com/Steve-Jobs-Walter-Isaacson-audiobook/dp/B07ZMKXMTG/ref=sr_1_1?crid=1YN4B7XLZBFLJ&keywords=steave+jobs&qid=1654040850&sprefix=steave+job%2Caps%2C253&sr=8-1">Jobs</a>
            <a class="book" href="https://www.amazon.com/Steve-Jobs-Michael-Fassbender/dp/B016C9WS84/ref=sr_1_2?crid=1YN4B7XLZBFLJ&keywords=steave+jobs&qid=1654041011&sprefix=steave+job%2Caps%2C253&sr=8-2">Steve jobs</a>
            <a class="book" href="https://www.amazon.com/Steve-Jobs-La-biografa%C2%ADa-audiobook/dp/B00L5L0YO0/ref=sr_1_5?crid=1YN4B7XLZBFLJ&keywords=steave+jobs&qid=1654041011&sprefix=steave+job%2Caps%2C253&sr=8-5">Steve Jobs. La biografía</a>
        </p>
        <p class="end">
            <b>Thses books are now on sales.</b>
        </p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(soup)
# print(soup.prettify())
# print(soup.html.head.title)
# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)
# print(type(soup.title))
# print(soup.body.p)
# print(soup.body.p.next_sibling.next_sibling)
# print(soup.body.p.next_sibling.next_sibling.a)
# print(soup.body.p.next_sibling.next_sibling.a.text)
# print(soup.body.p.next_sibling.next_sibling.a["href"])

# print(soup.find_all("a"))
# print(soup.find("a"))
for tag_a in soup.find_all("a"):
    print("Title :", tag_a.string)
    print(tag_a["href"], end="\n\n")

print(soup.select("body > p.end > b"))
print(soup.select("body > p.end > b")[0].string)
