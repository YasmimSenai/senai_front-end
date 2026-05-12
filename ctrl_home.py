"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if '_user_id' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template
    
@bp.route("/dashboard") # cria uma rota
def dashboard(): # função que gerencia rota
    """ Painel de Vendas"""
    #if 'user' not in session:
    #   return redirect(url_for("auth.login"))
    import locale
    #Define a localização para português brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    vendas: list = [
        { "mes":"Janeiro", "total":139519.19},
        { "mes":"Fevereiro", "total":125989.50},
        { "mes":"Março", "total":128519.30},
        { "mes":"Abril", "total":1399191.20},
        { "mes":"Maio", "total":141611.90},
        { "mes":"Junho", "total":142591.40},
        { "mes":"Julho", "total":119996.13},
        { "mes":"agosto", "total":769458.17},
        { "mes":"Setembro", "total":824601.77},
        { "mes":"Outrubro", "total":549342.66},
        { "mes":"Novembro", "total":228746.69},
        { "mes":"Dezembro", "total":453968.55},
    ] #fim lista vendas
    
    return render_template("dashboard/index.html", vendas=vendas, locale=locale) # Renderiza um template