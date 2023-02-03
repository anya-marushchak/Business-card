import requests,csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

from flask import Flask, render_template, request

app = Flask(__name__)

import csv
with open('currency.csv', 'rb') as csvfile:
    currencyreader = csv.reader(csvfile)
    for row in currencyreader:
        print (row)


@app.route("/currency", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    data = request.form
    code = data.get('code')
    amount = data.get("amount")

    if code == code['USD']:
      return amount*

  return render_template("rates.html")


if __name__ == "__main__":
  app.run(debug=True)