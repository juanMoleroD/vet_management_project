from models.vet import Vet
from models.owner import Owner

from repositories import owner_repository, vet_repository

vet_repository.delete_all()
owner_repository.delete_all()

vet_1 = Vet("Ace Ventura")
vet_repository.save(vet_1)

vet_2 = Vet("Dr Dolitle")
vet_repository.save(vet_2)

owner_1 = Owner("Mike Tyson", "077-6453-89766") #077-MIKE-TYSON
owner_repository.save(owner_1)