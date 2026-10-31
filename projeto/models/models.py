from sqlalchemy import ForeignKey, String, JSON, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from typing import List

artista_album_tabela = Table(
    "artista_album",
    Base.metadata,
    Column("artista_id", ForeignKey("artistas.id"), primary_key=True),
    Column("album_id", ForeignKey("albuns.id"), primary_key=True),
)

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    senha: Mapped[str] = mapped_column(String(100))

class Album(Base):

    __tablename__ = "albuns"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(25), unique=True)
    ano: Mapped[int]
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))

    faixas: Mapped[List["Faixa"]] = relationship(back_populates="album")
    artistas: Mapped[List["Artista"]] = relationship(secondary=artista_album_tabela, back_populates="albuns")

class Artista(Base):

    __tablename__ = "artistas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(64), unique=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))

    album: Mapped[List["Album"]] = relationship(secondary=artista_album_tabela, back_populates="artistas")

class Faixa(Base):

    __tablename__ = "faixas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(25), unique=True)
    duracao: Mapped[int]
    album_id: Mapped[int] = mapped_column(ForeignKey("albuns.id"))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))

    albuns: Mapped[List["Album"]] = relationship(back_populates="faixas")
