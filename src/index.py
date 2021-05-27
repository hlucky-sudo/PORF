from flask import Flask, render_template, request, session, escape, redirect, url_for, flash

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inicio')
def inicio():
    if "username" in session:
       return render_template('inicio.html') 
    return " Debes loguearte primero"   

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form["exampleInputPassword1"] 
        username = request.form["exampleInputName"]

        if username == "hlucky" and password == "2704":
            session["username"] = username
            # flash("has iniciado sesión correctamente", "success")
            return redirect( url_for('inicio') )
        return "Contraseña o usuarios incorrectos"

    return render_template('Login.html')

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect("/")

@app.route('/pago')
def pago():
    return render_template('pago.html')

app.secret_key = "12345"

if __name__ == '__main__':
    app.run(debug=True)