from peewee import *

db = SqliteDatabase('db')

class Users(Model):
    userID = IntegerField(primary_key = True)
    djname = CharField(30)
    apikey = CharField(30)

    class Meta:
        database = db

class Songs(Model):
    songID = IntegerField(primary_key = True)
    title = CharField(255)
    iidx_id = CharField(255)
    title2 = CharField(255)
    genre = CharField(50)
    artist = CharField(50)
    bpm = CharField(10)
    unlocktype = CharField(20)

    class Meta:
        database = db

class Charts(Model):
    chartID = IntegerField(primary_key = True)
    song = ForeignKeyField(Songs, backref='charts')

    notecount = IntegerField()
    difficulty = CharField(3)
    level = IntegerField()
    unlocked = BooleanField(default=False)

    class Meta:
        database = db


class ChartStats(Model):
    playID = IntegerField(primary_key = True)
    chart = ForeignKeyField(Charts, backref='chartstats')
    user = ForeignKeyField(Users, backref='chartstats')

    grade = CharField(3)
    lamp = CharField(3)
    miss = IntegerField()
    combobreak = IntegerField()
    ex_score = IntegerField()
    nc_gauge = IntegerField()
    hc_gauge = IntegerField()
    ex_gauge = IntegerField()
    percent_max = DoubleField()
    lastplayed = DateField()
    playtype = CharField(2)
    imported = BooleanField(default=False)

    class Meta:
        database = db

class Plays(Model):
    playID = IntegerField(primary_key = True)
    chart = ForeignKeyField(Charts, backref='play')
    user = ForeignKeyField(Users, backref='play')

    grade = CharField(3)
    lamp = CharField(3)
    misscount = IntegerField()
    combobreak = IntegerField()
    ex_score = IntegerField()
    pgreat = IntegerField()
    great = IntegerField()
    good = IntegerField()
    bad = IntegerField()
    poor = IntegerField()
    fast = IntegerField()
    slow = IntegerField()
    date = DateTimeField()
    gaugepercent = IntegerField()
    playtype = CharField(2)
    style = CharField(20)
    style2 = CharField(20)
    gaugetype = CharField(20)
    assist = CharField(20)
    range_opt = CharField(20, column_name='range')
    premature_end = BooleanField(default=False)

    class Meta:
        database = db

@db.collation('difficulty')
def song_sort(a, b):
    if a[0] < b[0]:
        return 1
    elif a[0] > b[0]:
        return -1

    sortorder = ['SPB', 'SPN', 'SPH', 'SPA', 'SPL', 'DPB', 'DPN', 'DPH', 'DPA', 'DPL', ]
    if sortorder.index(a) < sortorder.index(b):
        return -1
    if sortorder.index(a) > sortorder.index(b):
        return 1
    return 0
