from flask import Flask,render_template
import requests
import json


app = Flask(__name__)

@app.route('/')
def indexFile():
    j = requests.get("https://s3.amazonaws.com/open-to-cors/assignment.json").text
    d = json.loads(j)
    listOfProducts = []
    for i in d['products']:
        listOfProducts.append([d['products'][i]['title'],d['products'][i]['price'],int(d['products'][i]['popularity'])])
    listOfProducts.sort(key=lambda x:x[2],reverse=True)

    return render_template('index.html',listOfProducts=listOfProducts)


if __name__=="__main__":
	app.run(port=5000,debug=True)

