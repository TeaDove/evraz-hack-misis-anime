from typing import Any, Dict


class StreamService:
    @staticmethod
    def process_record(event: Dict[str, Any]) -> None:
        print(event)
