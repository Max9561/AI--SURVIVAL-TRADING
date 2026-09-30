import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv(
            "APP_NAME",
                    "AI Survival Trading System",
                        )

                            INITIAL_CAPITAL = float(
                                    os.getenv("INITIAL_CAPITAL", "100000")
                                        )

                                            MAX_RISK_PER_TRADE = float(
                                                    os.getenv("MAX_RISK_PER_TRADE", "0.005")
                                                        )

                                                            MAX_DAILY_LOSS = float(
                                                                    os.getenv("MAX_DAILY_LOSS", "0.02")
                                                                        )

                                                                            MAX_DRAWDOWN = float(
                                                                                    os.getenv("MAX_DRAWDOWN", "0.10")
                                                                                        )


                                                                                        settings = Settings()