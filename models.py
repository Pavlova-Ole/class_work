from peewee import SqliteDatabase, Model, ForeignKeyField, TextField, TimeField, IntegerField
 
db = SqliteDatabase('sqlite.db') 
 
class DB(Model): 
 
    class Meta: 
        database = db 
 
 
class User(DB): 
    tg_user = IntegerField()
    time = TimeField(null=True)
 
 
class Image(DB): 
    url = TextField() 
 
class Send(DB): 
    user = ForeignKeyField(User) 
    image = ForeignKeyField(Image) 
 
db.connect() 
db.create_tables([User, Image, Send],  safe=True) 
db.close()