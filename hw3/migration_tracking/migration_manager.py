from typing import Optional

from hw3.migration_tracking.migration import Migration


class MigrationManager:

    def __init__(self) -> None:
        self.migration_paths: dict[int, Migration] = {}
