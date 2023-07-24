from scrapeghost import SchemaScraper

# Define a schema to extract the URLs of the blog posts
url_schema = {
    "blog_post_urls": ["string"],
}

# Create a SchemaScraper instance with the defined schema and GPT-4
scraper = SchemaScraper(schema, model="gpt-3.5-turbo-16k")

# Create a SchemaScraper instance with the URL schema
url_scraper = SchemaScraper(url_schema)


# Scrape the blog index page to get the URLs of the blog posts
url_response = url_scraper.scrape("https://www.imagined.ai/")

# Define a schema for the blog post data
blog_post_schema = {
    "title": "string",
    "author": "string",
    "date_published": "string",
    "content": "string",
}

# Create a SchemaScraper instance with the blog post schema
blog_post_scraper = SchemaScraper(blog_post_schema)

# Scrape each blog post
for url in url_response.data["blog_post_urls"]:
    blog_post_response = blog_post_scraper.scrape(url)
    print(blog_post_response.data)
