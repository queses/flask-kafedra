# -*- coding: utf-8 -*-

from application.controllers import *

from application.models import board

from application import SessionSQL
# import simplejson as json
import json
import sys

class Test(Controller):
  def __return__(self):
    if request.form['Command'] == 'UpdateTeachers':
      self.update_lecturers()
    elif request.form['Command'] == 'UpdateDisciplines':
      self.update_disciplines()
    return request.form['Command']

  def update_lecturers(self):
    d = request.form['Data']
    j = json.loads(d)
    s = SessionSQL()

    db_lecturers_sname = s.query(board.Lecturer.second_name).all()
    json_lecturers_sname = []
    for i in range(0, len(db_lecturers_sname)): #каждый sname - массив; его нужно превратить строку:
      db_lecturers_sname[i] = db_lecturers_sname[i][0]
    # print(db_lecturers_sname)
    # print(j)

    for lecturer in j.items():  # цикл добавления лектора
      # lecturer - это массив. В [0] нах-ся название папки лектора на сервере, в [1] - его данные
      second_name = lecturer[1]["Name"].split(" ")[0]
      json_lecturers_sname += [second_name] # заполнение массива для дальнейшего использования при удалении
      # if (second_name not in db_lecturers_sname):
      print(second_name)
      first_name = lecturer[1]["Name"].split(" ")[1]
      middle_name = lecturer[1]["Name"].split(" ")[2]
      description = lecturer[1]["Descr"]

      img_url = lecturer[1]["Photo"]["FileName"]
      img_url = self.lecturer_img(lecturer[0], img_url)

      lecturer_model = board.Lecturer(first_name = first_name, second_name = second_name,
          middle_name = middle_name, description = description, img_url = img_url)
      
      # json_disciplines = lecturer[1]["Disciplines"].split(', ')
      # db_disciplines = s.query(board.Discipline).all()

      # for json_discipline in json_disciplines:
      #   for db_discipline in db_disciplines:
      #     discipline_shorts = db_discipline.shorts.split(", ")
      #     if json_discipline in discipline_shorts:
      #       lecturer_model.disciplines += [db_discipline]

      s.add(lecturer_model)

    for lecturer in db_lecturers_sname:  # цикл удаления лектора
      if (lecturer not in json_lecturers_sname):
        s.delete(s.query(board.Lecturer).filter_by(second_name = lecturer).one())

    s.commit()
    s.close()


  def lecturer_img(self, dir_name, img_url):
    import shutil, os
    from trans import trans
    dir_name = trans(dir_name)
    try:
      os.mkdir("application/static/img/lecturers/"+dir_name)
    except FileExistsError:
      pass
    shutil.copy(img_url, "application/static/img/lecturers/"+dir_name+"/photo.jpg")
    new_url = "static/img/lecturers/"+ dir_name +"/photo.jpg"
    return new_url

  def update_disciplines(self):
    d = request.form['Data']
    j = json.loads(d)
    s = SessionSQL()

    db_disciplines_title = s.query(board.Discipline.title).all()
    json_disciplines_title = []
    for i in range(0, len(db_disciplines_title)): #каждый sname - массив; его нужно превратить строку:
      db_disciplines_title[i] = db_disciplines_title[i][0]
   
    for discipline in j.items():  # цикл добавления дисциплины
      # lecturer - это массив. В [0] нах-ся название папки лектора на сервере, в [1] - его данные
      print(''' ===
        ===
        ===
        ''')
      print(discipline)
      title = discipline[0]
      json_disciplines_title += [title] # заполнение массива для дальнейшего использования при удалении
      if (title not in db_disciplines_title):
        short_names = ""
        for short_name in discipline[1]["Short"]:
          short_names += short_name + ", "
        description = discipline[1]["Descr"]
        print(short_names)
        discipline_model = board.Discipline(title = title, shorts = short_names,
            description = description)
        s.add(discipline_model)

    for discipline in db_disciplines_title:  # цикл удаления лектора
      if (discipline not in json_disciplines_title):
        s.delete(s.query(board.Discipline).filter_by(title = discipline).one())

    s.commit()
    s.close()

