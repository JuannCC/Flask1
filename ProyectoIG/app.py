from flask import Flask, render_template, request, redirect
import forms

app = Flask(__name__)

tareas=[]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/servicios', methods=['GET', 'POST'])
def servicios():
    comment_form=forms.CommentForm()
    nombre= request.form.get("nombre")
    return render_template("servicios.html",form=comment_form)
    
@app.route('/create', methods=['GET', 'POST'])
def create():
    #if request.method == 'GET':
      #  form= forms.CommentForm()
      #  context= {
      #      'form':form
      #  }
        return render_template( 'servicios/create.html')
    
    #if request.method == 'POST':
    #    form= forms.CommentForm(request.POST)
    #    if form.is_valid:
    #        form.save()
    #    return redirect('servicios')


if __name__ == "__main__":
    
    app.run(host='0.0.0.0',
            debug=True,
            port=5000)