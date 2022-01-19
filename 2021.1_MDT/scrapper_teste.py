from google_play_scraper import Sort, reviews_all
import csv

nome_app = 'br.com.mesotec.detrandf'
nome_arquivo = nome_app + '.csv'

result = reviews_all(
    nome_app,
    lang='pt-br',# defaults to 'en'
    country='br', # defaults to 'ke'
    sort=Sort.NEWEST
)

with open(nome_arquivo, 'w', newline="", encoding='utf-8') as f:  # You will need 'wb' mode in Python 2.x
    w = csv.DictWriter(f, result[0].keys())
    w.writeheader()
    for element in result:
        w.writerow(element)
