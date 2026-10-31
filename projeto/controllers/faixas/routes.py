
from flask import request, render_template, flash, session as flask_session, redirect, url_for
from controllers.faixas import faixas_bp
from models.models import Album, Faixa
from database import session

@faixas_bp.route("/faixas")
def faixas():
    return render_template("faixas/faixas.html")

@faixas_bp.route("/faixas/nova", methods=["POST"])
def cadastro_faixa():
    if request.method == 'POST':
        titulo = request.form.get("titulo")
        duracao = request.form.get("duracao_segundos")
        album_id = request.form.get("album_id")

        if not titulo or not duracao or not album_id:
            flash('Preencha todos os campos!')
            return redirect(url_for('faixas.listar_fa'))

        faixa_cadastrada = session.query(Faixa).filter_by(titulo=titulo).first()
        if faixa_cadastrada:
            flash('Essa faixa já foi cadastrada.')
            return redirect(url_for('faixas.listar_fa'))

        usuario_id = flask_session['usuario_id']
        faixa_nova = Faixa(titulo=titulo, duracao=int(duracao),album_id=int(album_id),
        usuario_id=int(usuario_id))
        session.add(faixa_nova)
        session.commit()

        flash('Faixa cadastrada.')
        return redirect(url_for('faixas.listar_fa'))


@faixas_bp.route('/listar_faixas')
def listar_fa():
    faixas = session.query(Faixa).all()
    albuns = session.query(Album).all()
    return render_template('faixas/faixas.html', faixas=faixas, albuns=albuns)


@faixas_bp.route('/excluir_faixa/<int:faixa_id>')
def excluir(faixa_id):
    faixa = session.get(Faixa, faixa_id)

    if faixa:
        session.delete(faixa)
        session.commit()
        flash('Faixa excluída.')

    return redirect(url_for('faixas.listar_fa'))


@faixas_bp.route('/editar_faixa/<int:faixa_id>', methods=['POST', 'GET'])
def editar_faixa(faixa_id):
    faixa = session.get(Faixa, faixa_id)

    if not faixa:
        return redirect(url_for('faixas.listar_fa'))

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        duracao = request.form.get('duracao_segundos')
        album_id = request.form.get('album_id')

        if titulo and duracao and album_id:
            faixa.titulo = titulo
            faixa.duracao = int(duracao)
            faixa.album_id = int(album_id)

            session.commit()
            flash('Faixa atualizada.')
            return redirect(url_for('faixas.listar_fa'))

    albuns = session.query(Album).all()
    return render_template('faixas/editar_faixa.html', faixa=faixa, albuns=albuns)


