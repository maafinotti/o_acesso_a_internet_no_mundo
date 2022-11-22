from flask import Flask, render_template
import os

app = Flask(__name__)

#criar a primeira página no site
#route --> caminho para acessar a página
#função -->  que você quer exibir naquela página
#templates --> html
#static --> css e imagens


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/o-projeto')
def projeto():
    return render_template('o-projeto.html')

@app.route('/o-processo')
def processo():
    return render_template('o-processo.html')

@app.route('/quem-somos')
def sobre():
    return render_template('quem-somos.html')

@app.route('/fontes')
def fontes():
    return render_template('fontes.html')

@app.route('/teste')
def teste():
    return render_template('teste.html')

#colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)