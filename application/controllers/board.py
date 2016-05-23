from application.controllers import *
from application.models import board

class Board(Controller):

  def __return__(self):
    return render_template('board/board.html', 
      lecturers = board.Lecturer.query.all(), disciplines = board.Discipline.query.all())

  def __return_modal__(self, id):
    lecturer = board.Lecturer.query.get(id)
    # print("esdasd"+lecturer.description)
    return render_template("board/modal.html", lecturer = lecturer)