from peewee import SqliteDatabase, Model, ForeignKeyField, TextField, TimeField
 
db = SqliteDatabase('sqlite.db') 
 
class DB(Model): 
 
    class Meta: 
        database = db 
 
 
class User(DB): 
    tg_user = TextField() 
    time = TimeField()
 
 
class Image(DB): 
    url = TextField() 
 
class Send(DB): 
    user = ForeignKeyField(User) 
    image = ForeignKeyField(Image) 
 
db.connect() 
db.create_tables([User, Image, Send],  safe=True) 
db.close()