from db.run_sql import run_sql
from models.appointment import Appointment
from repositories import animal_repository

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
        animal = animal_repository.select(result["id"])
        check_in = result["check_in"]
        check_out = result["check_out"]
        appointment = Appointment(animal, check_in, check_out, id)
    return appointment

def select_all():
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    appointments = []
    for row in results:
        animal = animal_repository.select(row["id"])
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


def delete_all():
    sql = "DELETE FROM appointments"
    run_sql(sql)