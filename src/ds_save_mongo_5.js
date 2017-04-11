use myDB
show dbs
show tables
db.myCol.insert({"Persons":[{"id":"201511088", "이름":"김요나"},{"id":"201640009", "이름":"이은진"}]})
db.myCol.find({"Persons.이름":"김요나"})