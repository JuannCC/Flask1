from flask import Flask, render_template, request, redirect
app = Flask(__name__)

tareas=[]

@app.route('/')
def home():
    num=1
    return render_template("index.html",num=num, tareas=tareas)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    nombre= request.form.get("nombre")
    return render_template("contacto.html", nombre=nombre)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == "GET":
        return render_template("agregar.html")
    else:
        tarea= request.form.get("tarea")
        tareas.append(tarea)
        return redirect("/")

if __name__ == "__main__":
    
    app.run(host='0.0.0.0',
            debug=True,
            port=5000)