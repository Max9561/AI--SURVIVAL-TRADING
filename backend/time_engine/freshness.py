from datetime import datetime, timezone


def check_freshness(
    timestamp: datetime,
        max_age_seconds: int = 60,
        ) -> dict:

            if max_age_seconds < 0:
                    raise ValueError(
                                "Maximum age cannot be negative."
                                        )

                                            if timestamp.tzinfo is None:
                                                    return {
                                                                "fresh": False,
                                                                            "age_seconds": None,
                                                                                        "reason": "Timestamp has no timezone.",
                                                                                                }

                                                                                                    now = datetime.now(timezone.utc)

                                                                                                        age = (
                                                                                                                now - timestamp.astimezone(timezone.utc)
                                                                                                                    ).total_seconds()

                                                                                                                        if age < 0:
                                                                                                                                return {
                                                                                                                                            "fresh": False,
                                                                                                                                                        "age_seconds": age,
                                                                                                                                                                    "reason": "Timestamp is in the future.",
                                                                                                                                                                            }

                                                                                                                                                                                return {
                                                                                                                                                                                        "fresh": age <= max_age_seconds,
                                                                                                                                                                                                "age_seconds": age,
                                                                                                                                                                                                        "reason": (
                                                                                                                                                                                                                    "Data is fresh."
                                                                                                                                                                                                                                if age <= max_age_seconds
                                                                                                                                                                                                                                            else "Data is stale."
                                                                                                                                                                                                                                                    ),
                                                                                                                                                                                                                                                        }