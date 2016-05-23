from application.models import *

disciplines_lecturers = db.Table('disciplines_lecturers',
    db.Column('discipline_id', db.Integer, db.ForeignKey('discipline.id')),
    db.Column('lecturer_id', db.Integer, db.ForeignKey('lecturer.id'))
)
#disciplines_lecturers_groups = db.Table('disciplines_lecturers_groups',
#                                        db.Column('discipline_id', db.Integer, db.ForeignKey('discipline.id')),
#                                        db.Column('lecturer_id', db.Integer, db.ForeignKey('lecturer.id')),
#                                        db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
#)

class Lecturer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(64))
    second_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(64))
    description = db.Column(db.String)
    email = db.Column(db.String(64), unique = True)
    disciplines = db.relationship('Discipline', secondary = disciplines_lecturers,
                                  backref = db.backref('lecturers', lazy='dynamic'))
    img_url = db.Column(db.String(), default = '/static/img/lecturers/no-image.jpg')
    
class Discipline(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64), unique = True)
    shorts = db.Column(db.String())
    description = db.Column(db.Text())
    # lecturers = db.relationship('Lecturer', secondary = disciplines_lecturers,
    #     backref = db.backref('disciplines', lazy='dynamic'))

class Group(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.String, primary_key = True)
