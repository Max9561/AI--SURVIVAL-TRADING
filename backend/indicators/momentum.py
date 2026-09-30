import pandas as pd


def add_rsi(
    df: pd.DataFrame,
        period: int = 14,
        ) -> pd.DataFrame:

            result = df.copy()

                delta = result["close"].diff()

                    gain = delta.clip(lower=0)
                        loss = -delta.clip(upper=0)

                            average_gain = gain.rolling(period).mean()
                                average_loss = loss.rolling(period).mean()

                                    rs = average_gain / average_loss

                                        result["rsi"] = 100 - (
                                                100 / (1 + rs)
                                                    )

                                                        return result