from scraparazzie import scraparazzie

get_news = scraparazzie.NewsClient(language='chinese traditional', location='Taiwan', max_results='10')

items = []
items = get_news.export_news()

print(len(items))











