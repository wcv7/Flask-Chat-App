import Backend.Handler as Handler
from flask import Flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__)
Field = None
LocalServer = Handler.Data.Server()

@app.route("/")
def Main():
    Secretkey = request.cookies.get("SecretKey")
    if LocalServer.CheckKey(Secretkey):
        return render_template("Home.html")
    else:
        return redirect("/Auth")
    
@app.route("/Auth")
def Auth():
    Secretkey = request.cookies.get("SecretKey")
    if LocalServer.CheckKey(Secretkey):
        return redirect("/")
    else:  
        return render_template("Auth.html", HiddenStatus="Show", SignUpStatus="Hidden", LoginStatus="Hidden")

@app.route("/Auth/Login", methods=['GET', 'POST'])
def AuthLogin():
    if request.method == "POST":
        Username = request.form['Username']
        Password = request.form['Password']
        if LocalServer.Login(Username, Password):
            Secretkey = LocalServer.GetKey(Username)
            resp = make_response(redirect("/"))
            resp.set_cookie('SecretKey', Secretkey)
            return resp
        else:
            return redirect("/")
    return render_template("Auth.html", HiddenStatus="Hidden", SignUpStatus="LogHidden", LoginStatus="Show")

@app.route("/Auth/SignUp", methods=['GET', 'POST'])
def AuthSignUp():
    if request.method == "POST":
        FName = request.form['Firstname']
        LName = request.form['Lastname']
        Username = request.form['Username']
        Email = request.form['Email']
        Password = request.form['Password']
        if LocalServer.CreateAccount(FName, LName, Username, Email, Password):
            Secretkey = LocalServer.GetKey(Username)
            resp = make_response(redirect("/"))
            resp.set_cookie('SecretKey', Secretkey)
            return resp
        else:
            return redirect("/")
    return render_template("Auth.html", HiddenStatus="Hidden", LoginStatus="SignHidden", SignUpStatus="Show")

@app.route("/Auth/Return")
def Return():
    return redirect("/Auth")

if __name__ == "__main__":
    app.run(debug=True)