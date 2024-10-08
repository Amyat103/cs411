from typing import Any, Optional

from hw3.habitat_management.habitat import Habitat
from hw3.migration_tracking.migration import Migration
from hw3.migration_tracking.migration_path import MigrationPath


class MigrationManager:

    def __init__(self) -> None:
        self.migrations: dict[int, Migration] = {}
        self.migration_paths: dict[int, MigrationPath] = {}

    def create_migration_path(
        species: str,
        start_location: Habitat,
        destination: Habitat,
        duration: Optional[int] = None,
    ) -> None:
        pass

    def cancel_migration(migration_id: int) -> None:
        pass

    def get_migration_by_id(migration_id: int) -> Migration:
        pass

    def get_migrations_by_current_location(current_location: str) -> list[Migration]:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
        pass

    def get_migrations_by_start_date(start_date: str) -> list[Migration]:
        pass

    def get_migrations_by_status(status: str) -> list[Migration]:
        pass

    def get_migration_path_details(path_id) -> dict:
        pass

    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass

    def get_migration_path_by_id(path_id: int) -> MigrationPath:
        pass

    def get_migrations() -> list[Migration]:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass

    def remove_migration_path(path_id: int) -> None:
        pass

    def schedule_migration(migration_path: MigrationPath) -> None:
        pass
