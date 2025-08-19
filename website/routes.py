
from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from website.database import execute_sql
from website.forms import PseudoLoginForm

routes = Blueprint('routes', __name__)  

@routes.route('/', methods=['GET', 'POST'])
def home():
    form = PseudoLoginForm()
    if form.validate_on_submit():
        # Aqui você pode validar o usuário no banco, se quiser
        session['id_cliente'] = form.id_cliente.data
        session['cpf'] = form.cpf.data
        return redirect(url_for('routes.menu'))
    return render_template('home.html', form=form)

@routes.route('/menu')
def menu():
    id_cliente = session.get('id_cliente')
    if not id_cliente:
        flash('Faça login para acessar o menu.')
        return redirect(url_for('routes.home'))
    # Exemplo: buscar informações do usuário
    # usuario = execute_sql('SELECT * FROM Usuario WHERE ID_Cliente = %s', (id_cliente,), fetch_one=True)
    return render_template('menu.html', id_cliente=id_cliente)