from flask import render_template

from application import app
# from application.nocache import nocache

# from application.controllers import *

# BOARD MODULE
#
@app.route('/')
@app.route('/board')
# @nocache
def board_route():
    from application.controllers.board import Board
    c = Board()
    return c.__return__()

@app.route("/board/lecturer_modal/<id>")
def lecturer_modal(id):
    from application.controllers.board import Board
    c = Board()
    return c.__return_modal__(id)

# TEST MODULE
#
@app.route('/test', methods=['GET', 'POST'])
def test_route():
    from application.controllers.test import Test
    c = Test()
    return c.__return__()    