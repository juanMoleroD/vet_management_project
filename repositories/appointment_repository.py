import pdb
from datetime import datetime, date
from db.run_sql import run_sql
from models.appointment import Appointment
from models.animal import Animal
from repositories import animal_repository, owner_repository, vet_repository

def save(appointment):
    sql = "INSERT INTO appointments (animal_id, check_in, check_out) VALUES (%s, %s, %s) RETURNING id"
    values = [appointment.animal.id, appointment.check_in, appointment.check_out]
    results = run_sql(sql, values)
    appointment.id = results[0]["id"]

def select(id):
    sql = "SELECT * FROM appointments WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    appointment = None
    if results:
        result = results[0]
        animal = animal_repository.select(result["animal_id"])
        check_in = result["check_in"]
        check_out = result["check_out"]
        appointment = Appointment(animal, check_in, check_out, id)
    return appointment

def select_all():
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    appointments = []
    for row in results:
        animal = animal_repository.select(row["animal_id"])
        check_in = row["check_in"]
        check_out = row["check_out"]
        id = row["id"]
        appointment = Appointment(animal, check_in, check_out, id)
        appointments.append(appointment)
    return appointments

def update(appointment):
    sql = "UPDATE appointments SET (animal_id, check_in, check_out) = (%s, %s, %s) WHERE id = %s"
    values = [appointment.animal.id, appointment.check_in, appointment.check_out, appointment.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM appointments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM appointments"
    run_sql(sql)

def get_animals_checked_in_today():
    today = date.today()
    sql = '''SELECT animals.* FROM animals 
                INNER JOIN appointments on appointments.animal_id = animals.id 
                    WHERE appointments.check_out >= %s'''
    values = [today]
    results = run_sql(sql, values)
    animals = []
    for row in results:
        name = row["name"]
        dob = row["date_of_birth"]
        type = row["type"]
        owner = owner_repository.select(row["owner_id"])
        vet = vet_repository.select(row["vet_id"])
        treatment_notes = row["treatment_notes"]
        id = row["id"]
        animal = Animal(name, dob, type, owner, vet, treatment_notes, id)
        animals.append(animal)
    return animals

