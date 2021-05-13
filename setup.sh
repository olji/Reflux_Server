#!/bin/sh
filename=db
if test -f $filename; then
    echo "File '$filename' already exists, remove it manually if you want to overwrite it"
else
    sqlite3 $filename < schema.sql
    echo "DJ name? "
    read username
    username=$(echo $username | sed -e 's/DJ //')
    djname=$(echo "DJ" $username | tr '[a-z]' '[A-Z]')
    key=$(openssl rand -base64 12)
    sqlite3 $filename "insert into users(djname, apikey) values ( '$djname', '$key');"
    echo "API key for $djname is: ${key}"
    echo "Edit it in the database if you want. (Users.apikey)"
fi
