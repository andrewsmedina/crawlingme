from splinter import Browser


def pages():
    page_list = []
    browser = Browser()
    url = "https://web.archive.org/web/20141216192721/http://andrewsmedina.com/"
    browser.visit(url)

    dirs = browser.find_by_css(".directory li a")
    for d in dirs:
        d.click()
        posts = browser.find_by_css("#posts h2 a")
        for post in posts:
            page_list.append(post)
    return page_list


if __name__ == "__main__":
    print pages()
