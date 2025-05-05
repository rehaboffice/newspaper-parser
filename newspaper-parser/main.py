import newspaper
import nltk

nltk.download('punkt_tab')

# Build the newspaper object
cnn_paper = newspaper.build('https://edition.cnn.com/us', memoize_articles=False)

# Print number of articles found
print("Total articles found:", cnn_paper.size())

# Print first 10 article URLs
for i, article in enumerate(cnn_paper.articles[:20]):
    print(f"{i + 1}: {article.url}")

# Print category URLs
print("\nCategories:")
for category in cnn_paper.category_urls():
    print(category)

first_article = cnn_paper.articles[3]

first_article.download()

# print(first_article.html)

first_article.parse()

print(first_article.text)

print(first_article.top_image)

print(first_article.authors)

print(first_article.title)

first_article.nlp()

print(first_article.summary)

print(first_article.keywords)