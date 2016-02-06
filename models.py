import datetime
import peewee

database = peewee.SqliteDatabase("brofox.db")


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Member(BaseModel):
    steam_id = peewee.CharField(unique=True)
    admin = peewee.BooleanField()
    join_date = peewee.DateTimeField(default=datetime.datetime.now)
