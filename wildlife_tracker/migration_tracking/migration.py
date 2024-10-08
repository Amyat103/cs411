from typing import Any, List

from hw3.migration_tracking.migration import Migration


class Migration:

    def __init__(
        self,
        migration_id: int,
        current_location: str,
        start_date: str,
        status: str = "Scheduled",
    ):
        self.migration_id = migration_id
        self.current_location = current_location
        self.start_date = start_date
        self.status = status

    def get_migration_details(migration_id: int) -> dict[str, Any]:
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
