from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': '/home/l-i-s/Pictures/Crawler'})

print('Сколько нужно спарсить фото?')
quantity = int(input())

print('По какому запросу парсить фото?')
name = input()