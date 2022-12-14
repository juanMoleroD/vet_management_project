import pdb
from datetime import datetime, date
from models.appointment import Appointment
from models.note import Note
from models.vet import Vet
from models.owner import Owner
from models.animal import Animal
from repositories import animal_repository, appointment_repository, note_repository, owner_repository, vet_repository

note_repository.delete_all()
appointment_repository.delete_all()
animal_repository.delete_all()
owner_repository.delete_all()
vet_repository.delete_all()


vet_1 = Vet("Ace Ventura")
vet_repository.save(vet_1)

vet_2 = Vet("Dr Dolitle")
vet_repository.save(vet_2)

vet_3 = Vet("Dr Hamster")
vet_repository.save(vet_3)

vet_4 = Vet("Hershel Greene")
vet_repository.save(vet_4)


owner_1 = Owner("Mike Tyson", "077-6453-89766", True) #077-MIKE-TYSON
owner_repository.save(owner_1)

owner_2 = Owner("Taylor Swift", "0700-TAYLOR", True)
owner_repository.save(owner_2)

owner_3 = Owner("Harry Potter", "07914-914-914", False)
owner_repository.save(owner_3)


animal_1 = Animal("Kenya", date(2010,6,24), "Bengal Tiger", owner_1, vet_1)
animal_repository.save(animal_1)

animal_2 = Animal("Meredith", date(2011,1,1), "Cat", owner_2, vet_3)
animal_repository.save(animal_2)

animal_3 = Animal("Olivia", date(2014,1,1), "Cat", owner_2, vet_3)
animal_repository.save(animal_3)

animal_4 = Animal("Hedwig", date(1997,1,1), "Snowy Owl", owner_3, vet_4)
animal_repository.save(animal_4)


appointment_1 = Appointment(animal_1, date(2020,1,1), date(2020,2,1))
appointment_repository.save(appointment_1)

appointment_2 = Appointment(animal_2, date(2021,3,1), date(2021,3,20))
appointment_repository.save(appointment_2)

appointment_3 = Appointment(animal_3, date(2022,7,1), date(2029,1,1))
appointment_repository.save(appointment_3)

appointment_4 = Appointment(animal_4, date(2022,7,1), date(2029,7,1))
appointment_repository.save(appointment_4)


note_1 = Note(animal_1, "Responds well with steak only diet")
note_repository.save(note_1)

note_2 = Note(animal_1, "Careful with your arms if Kenya doesn't know you!")
note_repository.save(note_2)

note_3 = Note(animal_2, "Only eats salmon")
note_repository.save(note_3)

note_4 = Note(animal_2, "Mrs Swift spoils her rotten")
note_repository.save(note_4)

note_5 = Note(animal_3, "Mrs Swift spoils her rotten")
note_repository.save(note_5)

note_6 = Note(animal_4, "Seems magical sometimes...")
note_repository.save(note_6)



#pdb.set_trace()