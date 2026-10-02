from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    erros = []; resultado = None; dados = {}
    if request.method == 'POST':
        nome = request.form.get ('Nome','').strip()
        peso = request.form.get('Peso','').strip()
        altura = request.form.get('Altura','').strip()
        dados = {'nome' :nome, 'dias' :dias, 'altura' :altura}

        nome = ''
        try:

        if not nome: 
            erros.append ('O nome é obrigatório')

        if peso <=0:
            erros.append ('O peso deve ser maior que 0')
        elif >=300:
            erros.append ('O peso deve ser menos que 300, melhore')        
        
        if altura < 0.5 or altura > 2.5: 
            erros.append ('A altura deve estar entre 0.5 e 2.5 metros')


        if not erros:
            imc = peso / (altura ** 2)
            imc = round(imc, 2)
        
        if imc <18.5:
            classificacao = '🔵 Abaixo do peso'
            cor = 'alert-info'

        if imc <=18.5 or > 25:
            classificacao = '🟢 Peso normal'
            cor = 'alert-success'

        if imc <=25 or > 30:
            classificacao = '🟡 Sobrepeso'
            cor = 'alert-warning'

        else: 
            imc >=30:
            classificacao = '🔴 Obesidade'
            cor = 'alert-danger' 
        resultado = {'nome': nome, 'imc' :imc, 'classificacao' :classificacao, 'cor' :cor}
    
    returm render_template('index.html', erros=erros,
                            resultado=resultado, nome=nome, peso=peso, altura=altura)

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

if __name__ == '__main__':
    app.run(debug=True)