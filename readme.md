This is a vet management app using python (flask and psycopg2) and postgreSQL

you need to have a postgreSLQ database set up and named vet_management.



to run the project type on the main directory the following:

to prime the database:

psql -d vet_management -f db/vet_management.sql

to start the server on port 5000:

python3 -m flask run
