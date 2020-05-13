from flask import *
from app import app
from flask import make_response
import hashlib
from flask import Flask, flash, request, redirect, render_template


@app.route('/api/v1/<param>/<user_id>', methods=['POST'])
def admin(param, user_id):
    json = {'User_ID': param, 'Response': user_id}
    return make_response(json)
