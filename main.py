from flask import Flask, render_template, request, redirect

app = Flask(__name__)
filmes = [
        {'codigo': 1, 'nome': 'Pânico', 'gênero': 'Terror slasher', 'ano': 1999},
        {'codigo': 2, 'nome': 'Sabrina', 'gênero': 'Romance, Comédia', 'ano': 1954},
        {'codigo': 3, 'nome': 'Orgulho e preconceito', 'gênero': 'Romance', 'ano': 2005}
]

@app.route('/')
def index():
    return render_template('index.html', filmes=filmes)

@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme(codigo):
    """
    Rota para adicionar um novo filme.
    Se o método for POST, adiciona o novo paciente à lista.
    Se não, exibe o formulário para adicionar um novo filme.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        ano = request.form['ano']
        filmes.append([nome, ano, genero])
        filmes[codigo] = ([nome, ano, genero])
        return redirect('/')  # Redireciona para a página de usuário
    else:
        return render_template('adicionar_filme.html')  # Renderiza o formulário de adicionar paciente

# ABAIXO TEMOS O CÓDIGO DE EDIÇÃO DO PACIENTE:

@app.route('/editar_filme/<int:codigo>', methods=['GET', 'POST'])
def editar_filme(codigo):
    """
    Rota para editar um paciente existente.
    Se o método for POST, atualiza os detalhes do paciente com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do paciente para edição.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        ano = request.form['ano']
        filmes.append([nome, ano, genero, codigo])
        filmes[codigo] = ([nome, ano, genero])
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        filme = filmes[codigo]
        return render_template('editar_filme.html', filme=filme)  # Renderiza o formulário de edição

@app.route('/apagar_filme<int:codigo>')
def apagar_filme(codigo):
    del filmes[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial


if __name__ == '__main__':
    app.run(debug=True)