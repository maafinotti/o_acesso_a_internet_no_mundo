from flask import Flask, render_template

app = Flask(__name__)

#criar a primeira página no site
#route --> caminho para acessar a página
#função -->  que você quer exibir naquela página
#template

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/o-projeto')
def processo():
    return render_template('o-projeto.html')

@app.route('/o-processo')
def projeto():
    return render_template('o-processo.html')

@app.route('/quem-somos')
def sobre():
    return render_template('quem-somos.html')

@app.route('/fontes')
def fontes():
    return render_template('fontes.html')

#colocar o site no ar
if __name__ == '__main__':
    app.run(debug = True)