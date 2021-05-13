# Reflux_Server
Server side for remote saving through [Reflux](https://github.com/olji/Reflux)

Have some livestreaming and statistics utilities.

# Deployment
First, run setup.sh to generate a database from the schema file and insert a user. You can do this manually as well if you don't trush shell scripts.

After that you deploy it however works best, either running wsgi.py using python directly or using whatever server solution you like.
