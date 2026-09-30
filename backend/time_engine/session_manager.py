from backend.time_engine.clock import now_india
from backend.time_engine.market_calendar import market_status


class SessionManager:

    def get_session(self) -> dict:
            current = now_india()

                    return {
                                "timestamp": current.isoformat(),
                                            "timezone": "Asia/Kolkata",
                                                        "market": "NSE",
                                                                    "status": market_status(current),
                                                                            }