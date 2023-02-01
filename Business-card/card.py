from flask import render_template,Flask, request,redirect


app = Flask(__name__)

from flask import render_template

@app.route('/mypage/me', methods=['GET', 'POST'])
def mypage():
   if request.method == 'GET':
       print("We received GET")
       return render_template("child-1.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")
       
@app.route('/mypage/contact', methods=['GET', 'POST'])
def mypage():
   if request.method == 'GET':
       print("We received GET")
       return render_template("child-2.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")


if __name__ == "__main__":
    app.run()