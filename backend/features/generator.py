import pandas as pd

from backend.indicators.momentum import add_rsi
from backend.indicators.trend import add_ema, add_sma
from backend.indicators.volatility import add_atr
from backend.indicators.volume import add_volume_average


def generate_features(
    df: pd.DataFrame,
    ) -> pd.DataFrame:

        result = df.copy()

            result = add_ema(
                    result,
                            periods=(20, 50),
                                )

                                    result = add_sma(
                                            result,
                                                    periods=(20, 50),
                                                        )

                                                            result = add_rsi(
                                                                    result,
                                                                            period=14,
                                                                                )

                                                                                    result = add_atr(
                                                                                            result,
                                                                                                    period=14,
                                                                                                        )

                                                                                                            result = add_volume_average(
                                                                                                                    result,
                                                                                                                            period=20,
                                                                                                                                )

                                                                                                                                    return result