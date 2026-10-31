from flask import request, render_template, flash, session as flask_session, redirect, url_for
from controllers.albuns import albuns_bp
from models.models import Album, Artista, Faixa
from database import session

@albuns_bp.route("/albuns")
def albuns():
    return render_template("albuns/albuns.html")

@albuns_bp.route("/albuns/novo", methods=["POST"])
def cadastro_album():
    if request.method == 'POST':
           titulo = request.form.get('titulo')
           ano = request.form.get('ano')
           artistas_id = request.form.get('artistas_id')
    
           if not titulo or not ano or not artistas_id:
               flash('Preencha todos os campos!')
               return render_template('albuns/albuns.html')
           
           album_cadastrado = session.query(Album).filter_by(titulo=titulo, artistas_id=int(artistas_id)).first()
           if album_cadastrado:
               flash('Esse album já foi cadastrado.')
               return render_template('albuns/albuns.html')
    
           usuario_id = flask_session['usuario_id']
           album_novo = Album(titulo=titulo, ano=int(ano), artistas_id=int(artistas_id),usuario_id=int(usuario_id))
           session.add(album_novo)
           session.commit()
    
           flash('Album cadastrado.')
           return redirect(url_for('albuns.listar_al'))
    return redirect(url_for('albuns.listar_al'))

@albuns_bp.route('/listar_albuns')
def listar_al():
    albuns = session.query(Album).all()
    return render_template('albuns/albuns.html', albuns=albuns)

@albuns_bp.route('/excluir_album/<int:album_id>')
def excluir_al(album_id):
    album = session.query(Album).get(album_id)
    if album:
        session.delete(album)
        session.commit()
    return redirect(url_for('albuns.listar_al'))

@albuns_bp.route('/editar_al/<int:album_id>', methods = ['POST', 'GET'])
def editar_al(album_id):
    album = session.query(Album).get(album_id)
    if not album:
        return redirect(url_for('albuns.listar_al'))

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        ano = request.form.get('ano')

        if titulo and ano:
            album.titulo = titulo
            album.ano = ano
            session.commit()
            return redirect(url_for('albuns.listar_al'))

    return render_template('albuns/editar_al.html', album=album)








