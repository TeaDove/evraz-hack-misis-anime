import re
from dataclasses import dataclass
from typing import Any, Dict, Tuple

import pandas as pd
from schemas.exhauster import ExhausterEvent


@dataclass
class StreamService:
    signal_re: re.Pattern = re.compile(r"SM_Exgauster\\\[(.+)\]")
    mapping: pd.DataFrame = pd.read_excel("data/mapping.xlsx")
    exhauster_count: int = 1

    def _map_signals(self):
        ...

    def _split_signal_id(self, signal: str) -> Tuple[int, int]:
        return re.findall(self.signal_re, signal)[0]

    def process_record(self, event: Dict[str, Any]) -> None:
        # signal_id_to_value: Dict[Tuple[str, int], Any] = {
        #     self._split_signal_id(key): value
        #     for key, value in event.items()
        #     if re.match(self.signal_re, key)
        # }
        # for key, value in signal_id_to_value.items():
        #     print(key, value)

        for idx in range(self.exhauster_count):
            exhauster_event = ExhausterEvent(  # noqa: F841
                create_at=event["moment"], exhauster_id=idx
            )

        # print(exhauster_event)
