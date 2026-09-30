from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class DecisionRecord:
    symbol: str
        action: str
            confidence: float
                outcome: str
                    timestamp: datetime


                    class AIMemory:

                        def __init__(self):
                                self.records: list[DecisionRecord] = []

                                    def remember(
                                            self,
                                                    symbol: str,
                                                            action: str,
                                                                    confidence: float,
                                                                            outcome: str,
                                                                                ):

                                                                                        record = DecisionRecord(
                                                                                                    symbol=symbol,
                                                                                                                action=action,
                                                                                                                            confidence=confidence,
                                                                                                                                        outcome=outcome,
                                                                                                                                                    timestamp=datetime.now(
                                                                                                                                                                    timezone.utc
                                                                                                                                                                                ),
                                                                                                                                                                                        )

                                                                                                                                                                                                self.records.append(record)

                                                                                                                                                                                                    def recent(
                                                                                                                                                                                                            self,
                                                                                                                                                                                                                    limit: int = 10,
                                                                                                                                                                                                                        ):

                                                                                                                                                                                                                                return self.records[-limit:]