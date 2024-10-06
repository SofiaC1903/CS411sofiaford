from typing import Any

class Migration:

    def __init__(self, migration_id: int):
        self.migration_id = migration_id 

    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass
    
    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass

    

