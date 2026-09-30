from datetime import datetime, timezone
from zoneinfo import ZoneInfo

UTC = timezone.utc
INDIA_TZ = ZoneInfo("Asia/Kolkata")


def now_utc() -> datetime:
    return datetime.now(UTC)


    def now_india() -> datetime:
        return datetime.now(INDIA_TZ)


        def to_india(dt: datetime) -> datetime:
            if dt.tzinfo is None:
                    raise ValueError("Datetime must include timezone information.")
                        return dt.astimezone(INDIA_TZ)


                        def to_utc(dt: datetime) -> datetime:
                            if dt.tzinfo is None:
                                    raise ValueError("Datetime must include timezone information.")
                                        return dt.astimezone(UTC)