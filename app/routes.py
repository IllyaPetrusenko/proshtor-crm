# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request, make_response
from app import app
from app.forms import LoginForm, NewUser
from app.actions.index import users_page
from app.actions.proshtor_site import send_data_to_subscribers


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Вход', form=form)


@app.route('/dashboard')
def users():
    db_users = users_page()
    return render_template('dashboard.html', title='Клиенты', db_users=db_users)


@app.route('/dashboard/new-user', methods=['GET', 'POST'])
def new_user():
    form = NewUser()
    if form.validate_on_submit():
        return redirect(url_for('/dashboard'))
    return render_template('user.html', title='Создать нового пользователя', form=form)


@app.route('/dashboard/users')
def users1():
    db_users = users_page()
    return render_template('users.html', title='Клиенты', db_users=db_users)


@app.route('/proshtor_bot_contact_form', methods=['GET', 'POST'])
def contact_form_bot():

    if request.method == 'GET':
        return '<h1>@proshtor_bot welcomes you</h1>' \
           '<h2>To use this Bot please add him in your Telegram app</h2>' \
           '<h3>@proshtor_bot is the name of the Bot</h3>'

    elif request.method == 'POST':

        send_data_to_subscribers()

    else:
        return make_response('404 Not Found, Incorrect', 404)
