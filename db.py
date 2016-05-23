#!flask/bin/python

# Скрипт универсален, его настройки берутся из config.py
# После выполения будет создана база, полностью готовая к миграции SQLAlchemy
# Также создается дир-я, хранящая данные SQLAlchemy; её назв-е указано в config.py
import sys

commands = ['create', 'migrate', 'degrade', 'upgrade']
try:
    command = sys.argv[1]
except IndexError:
    command = '\0'

if command in commands:

    from migrate.versioning import api
    from config import SQLALCHEMY_DATABASE_URI
    from config import SQLALCHEMY_MIGRATE_REPO
    from application import db
    import imp
    import os.path

    if command == "create":
        db.create_all()
        if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
            api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
            api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        else:
            api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
    
    if command == "migrate":
        v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))
        tmp_module = imp.new_module('old_model')
        old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        exec(old_model, tmp_module.__dict__)
        script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
        open(migration, "wt").write(script)
        api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        print('New migration saved as ' + migration)
        print('Current database version: ' + str(v))

    if command == "upgrade":
        api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        print('Current database version: ' + str(v))      

    if command == "degrade":
        confirm = input("Are you sure you want to degrade base? [Y for Yes]: ")
        if (confirm == 'Y') or (confirm == 'y'):
            v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
            api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
            print( 'Current database version: ' + 
                str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)) )
        else: print( 'Okay then.' )  

else:
    print("Неправильная команда. \nСписок доступных команд: ", end="")
    for command in commands:
        print(command, end="; ")    