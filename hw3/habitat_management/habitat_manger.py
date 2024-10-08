from typing import List, Optional

from hw3.habitat_management.habitat import Habitat


class HabitatManager:

    def __init__(self) -> None:
        habitats: dict[int, Habitat] = {}

    def create_habitat(
        habitat_id: int, geographic_area: str, size: int, environment_type: str
    ) -> Habitat:
        pass

    def get_habitat_by_id(habitat_id: int) -> Habitat:
        pass

    def remove_habitat(habitat_id: int) -> None:
        pass
