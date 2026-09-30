from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class Evidence:
    source: str
        symbol: str
            category: str
                value: Any

                    reliability: float = 0.5
                        confidence: float = 0.5

                            timestamp: datetime = field(
                                    default_factory=lambda: datetime.now(
                                                timezone.utc
                                                        )
                                                            )

                                                                verified: bool = False
                                                                    explanation: str = ""