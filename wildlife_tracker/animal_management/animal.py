from typing import Any, Optional


class Animal:
    def __init__(
        self,
        name: str,
        species: str,
        age: Optional[int],
        health_status: Optional[str] = None,
        status: str = "Scheduled",
    ):
        self.animal_id = id(self)
        self.name = name
        self.species = species
        self.age = age
        self.health_status = health_status
        self.status = status

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass
