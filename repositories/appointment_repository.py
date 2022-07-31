from db.run_sql import run_sql
from models.appointment import Appointment

def save(appointment):
    sql = "INSERT INTO appointments (animal_id, check_in, check_out) VALUES (%s, %s, %s) RETURNING id"
    values = [appointment.animal.id, appointment.check_in, appointment.check_out]
    results = run_sql(sql, values)
    appointment.id = results[0]["id"]

