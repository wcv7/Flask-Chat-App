import Backend.Handler as Handler
from flask import Flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__)
Field = None
LocalServer = Handler.Data.Server()

@app.route("/")
def Main():
    Username = request.cookies.get("Username")
    Password = request.cookies.get("Password")
    print(Username, Password)
    if LocalServer.CheckPassword(Password, Username):
        return render_template("Main.html")
    else:
        return redirect("/Auth")
    
@app.route("/Auth")
def Auth():
    Username = request.cookies.get("Username")
    Password = request.cookies.get("Password")
    print(Username, Password)
    if LocalServer.CheckPassword(Password, Username):
        return redirect("/")
    else:  
        return render_template("Auth.html", HiddenStatus="Show", SignUpStatus="Hidden", LoginStatus="Hidden")

@app.route("/Auth/Login", methods=['GET', 'POST'])
def AuthLogin():
    if request.method == "POST":
        Username = request.form['Username']
        Password = request.form['Password']
        print(Username, Password)
        print(LocalServer.CheckPassword(Password, Username))
        if LocalServer.CheckPassword(Password, Username):
            print("L")
            resp = make_response(redirect("/"))
            resp.set_cookie('Username', Username)
            resp.set_cookie('Password', Password)
            print("Success")
            return resp
        else:
            return redirect("/")
    return render_template("Auth.html", HiddenStatus="Hidden", SignUpStatus="LogHidden", LoginStatus="Show")

@app.route("/Auth/SignUp")
def AuthSignUp():
    return render_template("Auth.html", HiddenStatus="Hidden", LoginStatus="SignHidden", SignUpStatus="Show")

@app.route("/Auth/Return")
def Return():
    return redirect("/Auth")

if __name__ == "__main__":
    app.run(debug=True)