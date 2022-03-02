# -*- coding: UTF-8 -*-
from turtle import title
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Jogo:
  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
lista = [jogo1, jogo2, jogo3]

@app.route('/', methods=["GET"])
def index():
  return render_template('lista.html', title="Jogos", jogos=lista)


@app.route('/novo')
def novo():
  return render_template('novo.html', titulo="Novo Jogo")


@app.route('/criar', methods=['POST'])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo = Jogo(nome=nome, categoria=categoria, console=console)
  lista.append(jogo)
  return redirect('/')

@app.route('/login', methods=["GET"])
def login():
  return render_template('login.html')


@app.route('/autenticar', methods=["POST"])
def autenticar():
  if 'mestra' == request.form['senha']:
    return redirect('/')
  else:
    return redirect('/login')


app.run(debug=True)