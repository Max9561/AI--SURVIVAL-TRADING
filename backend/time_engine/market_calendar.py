from datetime import time

from backend.time_engine.clock import now_india, INDIA_TZ

MARKET_OPEN = time(9, 15)
MARKET_CLOSE = time(15, 30)


def is_weekday(dt) -> bool:
    return dt.weekday() < 5


    def is_market_session(dt=None) -> bool:
        dt = dt or now_india()
            dt = dt.astimezone(INDIA_TZ)

                current_time = dt.time().replace(tzinfo=None)

                    return (
                            is_weekday(dt)
                                    and MARKET_OPEN <= current_time < MARKET_CLOSE
                                        )


                                        def market_status(dt=None) -> str:
                                            dt = dt or now_india()
                                                dt = dt.astimezone(INDIA_TZ)

                                                    if not is_weekday(dt):
                                                            return "CLOSED_WEEKEND"

                                                                if is_market_session(dt):
                                                                        return "OPEN"

                                                                            return "CLOSED"