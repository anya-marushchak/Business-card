from flask import Flask, render_template, request

app = Flask(__name__)

library =[

 {
  "title": "Collector", "author": "J.Fauls", "date":"1985"
  },
 {
  "title": "Pride and prejudice", "author": "J.Austean", 'date':'1875'
  }

]


@app.route("/library", methods=["GET"])
def get_lib():
      return library

if __name__ == "__main__":
  app.run()

