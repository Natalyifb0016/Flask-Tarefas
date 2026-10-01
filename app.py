from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "chave-super-secreta"     

@app.route('/')
def index(): 
    if 'lista'not in session:
        session ['lista']=[]
    return render_template ('tarefas.html', lista=session['lista']) 

if __name__ == "__main__":
    app.run(debug=True)
    app = Flask(__name__)

