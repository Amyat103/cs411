from typing import Any, List, Optional

from hw3.animal_management.animal import Animal


class AnimalManager:

    def __init__(self) -> None:
        animals: dict[int, Animal] = {}

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass

    def register_animal(self, Animal) -> None:
        pass

    def remove_animal(self, animal_id: int) -> None:
        pass

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass

    def get_animals_in_habitat(habitat_id: int) -> List[Animal]:
        pass
