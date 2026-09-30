import pandas as pd


def add_volume_average(
    df: pd.DataFrame,
        period: int = 20,
        ) -> pd.DataFrame:

            result = df.copy()

                result["volume_sma"] = (
                        result["volume"]
                                .rolling(period)
                                        .mean()
                                            )

                                                result["relative_volume"] = (
                                                        result["volume"]
                                                                / result["volume_sma"]
                                                                    )

                                                                        return result