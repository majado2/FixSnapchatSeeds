from flask import Flask, Response, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    with open('new_file.xml', 'r', encoding='utf-8') as file:
        data = file.read()
    return Response(data, mimetype='application/xml')

@app.route('/update')
def update():
    response = requests.get('https://rodastore.com/feeds/snapchat/7RKnzAbjZHnYTJRoAI8KnQ5ELcfrsbEo')
    data = response.text
    soup = BeautifulSoup(data, 'xml')
    for tag in soup.find_all('g:item_group_id'):
        tag.string = '505820'
    for tag in soup.find_all('g:google_product_category'):
        tag.string = 'Health & Beauty > Health Care > Conductivity Gels & Lotions'
    with open('new_file.xml', 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))
    return 'Update completed'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
