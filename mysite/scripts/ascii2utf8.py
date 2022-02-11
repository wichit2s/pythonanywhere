import codecs
source = codecs.open("category.json", "rb").read().decode('unicode-escape')
codecs.open("category-utf8.json", "wb","utf-8").write(source)

# python manage.py dumpdata --indent=2
