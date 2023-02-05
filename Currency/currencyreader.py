
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

from flask import Flask, render_template, request

app = Flask(__name__)


import os

os.path.join(os.getcwd(), 'rates.csv')


@app.route("/currency", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    data = request.form
    code = data.get('code')
    amount = data.get("amount")

    

    if code == code['USD'] and amount == 1:
      return amount*4.2534

    return render_template("rates.html")
  


if __name__ == "__main__":
  app.run(debug=True)




    
  
    
