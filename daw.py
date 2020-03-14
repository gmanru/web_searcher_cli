from googlesearch import search

from search_google2 import get_title
# to search
query = "мияги"

for j in search(query,lang="ru", stop=10):
    print(j)
    title = get_title(j)
    print(title)


	               #tld = 'com',  # The top level domain
	               #lang = 'ru',  # The language
	               # num = 10,     # Number of results per page
	               # start = 0,    # First result to retrieve
	               # stop = 20,  # Last result to retrieve
	              # pause = 1.0,  # Lapse between HTTP requests
