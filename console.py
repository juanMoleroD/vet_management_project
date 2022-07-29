from models.vet import Vet

from repositories import vet_repository

vet_repository.delete_all()


vet_1 = Vet("Ace Ventura")
vet_repository.save(vet_1)

vet_2 = Vet("Dr Dolitle")
vet_repository.save(vet_2)

vet_repository.delete(vet_2.id)