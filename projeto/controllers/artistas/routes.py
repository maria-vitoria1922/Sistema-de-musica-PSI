from flask import request, render_template, flash, session as flask_session, redirect, url_for
from controllers.artistas import artistas_bp
from models.models import Album, Artista
from database import session

@artistas_bp.route("/artistas")
def artistas():
    return render_template("artistas/artistas.html")

@artistas_bp.route("/artistas/novo", methods=["POST","GET"])
def cadastro_artista():
     if request.method == 'POST':
       nome = request.form.get('nome')

       if not nome:
           flash('Preencha todos os campos!')
           return render_template('artistas/artistas.html')
       
       artista_cadastrado = session.query(Artista).filter_by(nome=nome).first()
       if artista_cadastrado:
           flash('Esse artista já foi cadastrado.')
           return render_template('artistas/artistas.html')

       usuario_id = flask_session['usuario_id']
       artista_novo = Artista(nome=nome, usuario_id=int(usuario_id))
       session.add(artista_novo)
       session.commit()

       flash('Artista cadastrado.')
       return redirect(url_for('artista.listar'))

@artistas_bp.route('/listar_artistas')
def listar():
    artistas = session.query(Artista).all()
    return render_template('artistas/artistas.html', artistas=artistas)

@artistas_bp.route('/excluir_artista/<int:artista_id>')
def excluir(artista_id):
    artista = session.query(Artista).get(artista_id)
    if artista:
        session.delete(artista)
        session.commit()
    return redirect(url_for('artistas.listar'))

@artistas_bp.route('/editar_artista/<int:artista_id>', methods = ['POST', 'GET'])
def editar_artista(artista_id):
    artista = session.query(Artista).get(artista_id)
    if not artista:
        return redirect(url_for('artistas.listar'))

    if request.method == 'POST':
        nome = request.form.get('nome')

        if nome:
            artista.nome = nome
            session.commit()
            return redirect(url_for('artistas.listar'))

    return render_template('artistas/editar_art.html', artista=artista)


