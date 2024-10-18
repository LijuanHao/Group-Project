from flask import Flask,render_template,request
import google.generativeai as genai
import os
import numpy as np
import textblob


model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key="AIzaSyCluRjLkwn6IOe4f-dNTlusyuAkDUI7fQo")

app = Flask(__name__)
user_name = ""
flag = 1


@app.route("/", methods=["GET", "POST"])
def index():
    global flag
    flag = 1
    return render_template("index.html")


@app.route("/retirement",methods=["GET","POST"])
def retirement():
    return(render_template("retirement.html"))

@app.route("/retirement_1",methods=["GET","POST"])
def retirement_1():
    q = "What’s the best way to start saving for retirement?"
    r = model.generate_content(q)
    return(render_template("retirement_1.html",r=r.text))

@app.route("/retirement_2",methods=["GET","POST"])
def retirement_2():
    q = "How can I structure my retirement savings?"
    r = model.generate_content(q)
    return(render_template("retirement_2.html",r=r.text))

@app.route("/retirement_3",methods=["GET","POST"])
def retirement_3():
    q = "What should I know about taxes in retirement?"
    r = model.generate_content(q)
    return(render_template("retirement_3.html",r=r.text))

@app.route("/retirement_4",methods=["GET","POST"])
def retirement_4():
    q = "How do I assess my future income needs for retirement?"
    r = model.generate_content(q)
    return(render_template("retirement_4.html",r=r.text))

@app.route("/retirement_reply",methods=["GET","POST"])
def retirement_reply():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("retirement_reply.html",r=r.text))


if __name__ == "__main__":
    app.run()
