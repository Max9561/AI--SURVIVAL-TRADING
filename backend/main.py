from fastapi import FastAPI

from backend.api.routes import router

app = FastAPI(
    title="AI Survival Trading System",
        description="Multi-source AI paper-trading research platform",
            version="0.1.0",
            )

            app.include_router(router)


            @app.get("/")
            def root():
                return {
                        "project": "AI Survival Trading System",
                                "version": "0.1.0",
                                        "status": "online",
                                            }
                                            