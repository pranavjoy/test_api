from flask import *
from app import app
from flask import make_response
import hashlib
from flask import Flask, flash, request, redirect, render_template


@app.route('/api/v1/<param>/<user_id>', methods=['GET', 'POST'])
def admin(param, user_id):
    if request.method == 'POST':
        req_in = request.form['request']
        json = {'Response': 'This is a sample response', 'User_ID': user_id}
    elif request.method == 'GET':
        json = {'Response': 'This is a sample response', 'User_ID': user_id}
        print('GET')
    return make_response(json)
