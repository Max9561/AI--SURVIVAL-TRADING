from datetime import datetime, timezone


def generate_report(
    symbol: str,
        action: str,
            confidence: float,
                reason: str,
                ) -> dict:

                    return {
                            "generated_at": datetime.now(
                                        timezone.utc
                                                ).isoformat(),
                                                        "symbol": symbol,
                                                                "action": action,
                                                                        "confidence": confidence,
                                                                                "reason": reason,
                                                                                        "type": "paper-trading-analysis",
                                                                                            }