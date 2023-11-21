import sys
from newspaper import Article

def getText(url):
	# url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
	try:
		article = Article(url)
		article.download()
		article.parse()
		# print(article.text)
		return article.text
	except Exception as e:
		print (e)
		pass


if __name__ == "__main__":
	try:
		# Parse command-line arguments
		# Get input from command line
		sys.stdout.write(getText(sys.argv[1]))
		sys.stdout.flush()

	except Exception as e:
		print (e)
		sys.exit(1)
