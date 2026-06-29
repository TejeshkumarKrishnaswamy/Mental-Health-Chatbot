from flask import Flask,render_template,request
from chatbot import reply
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    ans=""
    if request.method=="POST":
        ans=reply(request.form["message"])
    return render_template("index.html",answer=ans)
if __name__=="__main__":
    app.run(debug=True)
