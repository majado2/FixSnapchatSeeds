import requests
from bs4 import BeautifulSoup

# سحب الملف من الرابط
response = requests.get('https://rodastore.com/feeds/snapchat/7RKnzAbjZHnYTJRoAI8KnQ5ELcfrsbEo')
data = response.text

# تحليل الملف
soup = BeautifulSoup(data, 'xml')

# البحث عن تاق <g:item_group_id> واستبدال محتواه بالرقم 505820
for tag in soup.find_all('g:item_group_id'):
    tag.string = '505820'

# البحث عن تاق <g:google_product_category> واستبدال محتواه بالقيمة المطلوبة
for tag in soup.find_all('g:google_product_category'):
    tag.string = 'Health & Beauty > Health Care > Conductivity Gels & Lotions'

# حفظ التغييرات في ملف جديد
with open('new_file.xml', 'w', encoding='utf-8') as file:
    file.write(str(soup.prettify()))
