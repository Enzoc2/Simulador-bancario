from flask import Blueprint, render_template, redirect, url_for, jsonify, flash, session, request
from website.database import execute_sql
from website.forms import PseudoLoginForm
from website.compras_db import buscar_compras

api = Blueprint('api', __name__)  

@api.route('/', methods=['GET', 'POST'])
def home():
    form = PseudoLoginForm()
    if form.validate_on_submit():
        # Aqui você pode validar o usuário no banco, se quiser
        session['id_cliente'] = form.id_cliente.data
        session['cpf'] = form.cpf.data
        return redirect(url_for('routes.menu'))
    return render_template('home.html', form=form)

@api.route('/menu')
def menu():
    id_cliente = session.get('id_cliente')
    if not id_cliente:
        flash('Faça login para acessar o menu.')
        return redirect(url_for('routes.home'))
    # Exemplo: buscar informações do usuário
    # usuario = execute_sql('SELECT * FROM Usuario WHERE ID_Cliente = %s', (id_cliente,), fetch_one=True)
    return render_template('menu.html', id_cliente=id_cliente)

@api.route('/api/usuario/<int:id_cliente>')
def routes_usuario(id_cliente):
    cpf = request.args.get('cpf')
    usuario = execute_sql(
        "SELECT ID_Cliente as id_cliente, Nome as nome, CPF as cpf, Telefone as telefone FROM Usuario WHERE ID_Cliente = %s AND CPF = %s",
        (id_cliente, cpf), fetch_one=True
    )
    return jsonify(usuario or {})

@api.route('/api/compras/<int:id_cliente>')
def routes_compras(id_cliente):
    compras = buscar_compras(id_cliente)
    return jsonify(compras or [])

@api.route('/api/faturas/<int:id_cliente>')
def routes_faturas(id_cliente):
    faturas = execute_sql(
        "SELECT ID_Pag as id, Vencimento as vencimento, Valor as valor, Status as status FROM fatura WHERE ID_Pag = %s ORDER BY Vencimento DESC",
        (id_cliente,), fetch=True
    )
    return jsonify(faturas or [])


@api.route('/api/usuario/<int:id_cliente>', methods=['PUT'])
def atualizar_usuario(id_cliente):
    data = request.json
    nome = data.get('nome')
    cpf = data.get('cpf')
    telefone = data.get('telefone')

    # Atualiza no banco
    execute_sql(
        "UPDATE Usuario SET Nome = %s, CPF = %s, Telefone = %s WHERE ID_Cliente = %s",
        (nome, cpf, telefone, id_cliente)
    )

    # Retorna o que foi salvo
    return jsonify({
        'message': 'Perfil atualizado com sucesso',
        'id_cliente': id_cliente,
        'cpf': cpf
    })