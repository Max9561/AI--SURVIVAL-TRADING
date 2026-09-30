import pandas as pd


def add_atr(
    df: pd.DataFrame,
        period: int = 14,
        ) -> pd.DataFrame:

            result = df.copy()

                previous_close = result["close"].shift(1)

                    true_range = pd.concat(
                            [
                                        result["high"] - result["low"],
                                                    (
                                                                    result["high"]
                                                                                    - previous_close
                                                                                                ).abs(),
                                                                                                            (
                                                                                                                            result["low"]
                                                                                                                                            - previous_close
                                                                                                                                                        ).abs(),
                                                                                                                                                                ],
                                                                                                                                                                        axis=1,
                                                                                                                                                                            ).max(axis=1)

                                                                                                                                                                                result["atr"] = (
                                                                                                                                                                                        true_range
                                                                                                                                                                                                .rolling(period)
                                                                                                                                                                                                        .mean()
                                                                                                                                                                                                            )

                                                                                                                                                                                                                return result