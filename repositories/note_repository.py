from db.run_sql import run_sql
from models.note import Note
from models.animal import Animal
from repositories import animal_repository

def save(note):
    sql = "INSERT INTO notes (animal_id, content) VALUES (%s, %s) RETURNING id"
    values = [note.animal.id, note.content]
    result = run_sql(sql, values)
    note.id = result[0]["id"]

def select(id):
    sql = "SELECT * FROM notes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    note = None
    if results:
        result = results[0]
        animal = animal_repository.select(result["animal_id"])
        content = result["content"]
        note = Note(animal, content, id)
    return note

def select_all():
    sql = "SELECT * FROM notes"
    results = run_sql[sql]
    notes = []
    for row in results:
        animal = animal_repository.select(row["animal_id"])
        content = row["content"]
        id = row["id"]
        note = Note(animal, content, id)
        notes.append(note)
    return notes

def update(note):
    sql = "UPDATE notes SET (animal_id, content) = (%s, %s) WHERE id = %s "
    values = [note.animal.id, note.content, note.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM notes WHERE id = %s"
    values =[id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM notes"
    run_sql(sql)