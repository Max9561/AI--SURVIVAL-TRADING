from fastapi import APIRouter

from backend.time_engine.session_manager import SessionManager

router = APIRouter()
session_manager = SessionManager()


@router.get("/health")
def health():
    return {
            "status": "healthy",
                    "system": "AI Survival Trading",
                        }


                        @router.get("/status")
                        def system_status():
                            return {
                                    "backend": "online",
                                            "market_data": "not_connected",
                                                    "ai": "not_connected",
                                                            "risk_engine": "ready",
                                                                    "paper_broker": "ready",
                                                                        }


                                                                        @router.get("/time")
                                                                        def get_time():
                                                                            return session_manager.get_session()