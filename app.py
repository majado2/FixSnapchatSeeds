from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    # فتح الملف المعدل وقراءته
    with open('new_file.xml', 'r', encoding='utf-8') as file:
        data = file.read()

    # عودة الملف كرد فعل على الطلب
    return Response(data, mimetype='application/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
