from flask import render_template,Flask,request,redirect


app = Flask(__name__)


@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")


if __name__ == "__main__":
    app.run()