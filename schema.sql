CREATE TABLE users (
        userID integer primary key,
        djname varchar(30),
        apikey varchar(30)
        );
CREATE TABLE songs (
        songID integer primary key,
        title varchar(255),
        title2 varchar(255),
        genre varchar(50),
        artist varchar(50),
        bpm varchar(10),
        iidx_id varchar(255),
        unlocktype varchar(20)
        );
CREATE TABLE charts(
        chartID integer primary key,
        song_id int not null,
        notecount int not null,
        difficulty varchar(3) not null,
        level int not null,
        unlocked bool default false,
        foreign key (song_id) references songs(songID)
        );
CREATE TABLE chartstats(playID integer primary key,
        chart_id int not null,
        user_id int not null,
        grade varchar(3) default "NP",
        lamp varchar(3) default "NP",
        miss int,
        combobreak int,
        ex_score int default 0,
        playtype varchar(2) not null,
        imported boolean not null default 0,
        nc_gauge int default 0,
        hc_gauge int default 0,
        ex_gauge int default 0,
        nc_endnote int default 0,
        hc_endnote int default 0,
        ex_endnote int default 0,
        percent_max real default 0,
        lastplayed date,
        foreign key(chart_id) references charts(chartID),
        foreign key(user_id) references users(userID)
        );
CREATE TABLE plays ( playID integer primary key,
        chart_id int not null,
        user_id int not null,
        grade varchar(3) default "",
        lamp varchar(3) default "",
        pgreat int default 0,
        great int default 0,
        good int default 0,
        bad int default 0,
        poor int default 0,
        combobreak int default 0,
        misscount int default 0,
        ex_score int default 0,
        fast int default 0,
        slow int default 0,
        date datetime,
        gaugepercent int default 0,
        playtype varchar(2) not null,
        style varchar,
        style2 varchar,
        gaugetype varchar,
        premature_end boolean not null default false,
        range varchar(20),
        assist varchar(20)
    );