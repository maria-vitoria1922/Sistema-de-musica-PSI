from werkzeug.security import generate_password_hash

from database import criando_banco, session
from models.models import Album, Artista, Faixa, Usuario


def popular_banco():
    criando_banco()

    usuario_existente = session.query(Usuario).filter_by(
        email="demo@spotypobre.local"
    ).first()
    if usuario_existente:
        print("Os dados de demonstração já existem.")
        return

    usuario = Usuario(
        nome="demo",
        email="demo@spotypobre.local",
        senha=generate_password_hash("demo123"),
    )
    session.add(usuario)
    session.flush()

    artista1 = Artista(nome="Banda Horizonte", usuario_id=usuario.id)
    artista2 = Artista(nome="Luna Azul", usuario_id=usuario.id)
    session.add_all([artista1, artista2])
    session.flush()

    album1 = Album(
        titulo="Ceu de Neon",
        ano=2024,
        usuario_id=usuario.id,
        artistas=[artista1, artista2],
    )
    album2 = Album(
        titulo="Mare Alta",
        ano=2023,
        usuario_id=usuario.id,
        artistas=[artista1],
    )
    session.add_all([album1, album2])
    session.flush()

    faixa1 = Faixa(
        titulo="Manha de Sol",
        duracao=196,
        album_id=album1.id,
        usuario_id=usuario.id,
    )
    faixa2 = Faixa(
        titulo="Ruas Vazias",
        duracao=214,
        album_id=album1.id,
        usuario_id=usuario.id,
    )
    faixa3 = Faixa(
        titulo="Vento no Mar",
        duracao=203,
        album_id=album2.id,
        usuario_id=usuario.id,
    )
    session.add_all([faixa1, faixa2, faixa3])
    session.commit()
    print("Banco populado com dados de demonstração.")


if __name__ == "__main__":
    popular_banco()
    