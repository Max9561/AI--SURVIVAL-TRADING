import pandas as pd


def add_ema(
    df: pd.DataFrame,
        periods: tuple[int, ...] = (20, 50),
        ) -> pd.DataFrame:

            result = df.copy()

                for period in periods:
                        result[f"ema_{period}"] = (
                                    result["close"]
                                                .ewm(
                                                                span=period,
                                                                                adjust=False,
                                                                                            )
                                                                                                        .mean()
                                                                                                                )

                                                                                                                    return result


                                                                                                                    def add_sma(
                                                                                                                        df: pd.DataFrame,
                                                                                                                            periods: tuple[int, ...] = (20, 50),
                                                                                                                            ) -> pd.DataFrame:

                                                                                                                                result = df.copy()

                                                                                                                                    for period in periods:
                                                                                                                                            result[f"sma_{period}"] = (
                                                                                                                                                        result["close"]
                                                                                                                                                                    .rolling(period)
                                                                                                                                                                                .mean()
                                                                                                                                                                                        )

                                                                                                                                                                                            return result