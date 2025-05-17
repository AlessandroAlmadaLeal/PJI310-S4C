from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.config['SECRET_KEY'] = "UNIVESP_ProjetoIntegrador_III"

#Retorna o icone para o navegador
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/'), 'favicon.ico',mimetype='image/vnd.microsoft.icon')

#Publico intro de atendente
@app.route('/', methods=['GET','POST'])
@app.route('/intro', methods=['GET','POST'])
def index():
    
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        button_value = request.form['action']
        if button_value == "P1":
            return render_template('cadastro.html')
        elif button_value == "P2":
            return render_template('apontamento.html')
        elif button_value == "P3":
            return render_template('bordo.html')
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/cadastro', methods=['GET','POST']) 
def cadastro():
    return render_template('cadastro.html')

@app.route('/apontamento', methods=['GET','POST'])
def apontamento():
    return render_template('apontamento.html')

@app.route('/bordo', methods=['GET','POST'])
def bordo():
    return render_template('bordo.html')

if __name__ == "__main__":
    app.run()