import pandas as pd


REQUIRED_COLUMNS = [
    "timestamp",
        "open",
            "high",
                "low",
                    "close",
                        "volume",
                        ]


                        def validate_ohlcv(df: pd.DataFrame) -> dict:
                            errors = []

                                missing_columns = [
                                        column
                                                for column in REQUIRED_COLUMNS
                                                        if column not in df.columns
                                                            ]

                                                                if missing_columns:
                                                                        errors.append(
                                                                                    f"Missing columns: {missing_columns}"
                                                                                            )

                                                                                                if df.empty:
                                                                                                        errors.append("Dataset is empty.")

                                                                                                            if "timestamp" in df.columns:
                                                                                                                    if df["timestamp"].duplicated().any():
                                                                                                                                errors.append(
                                                                                                                                                "Duplicate timestamps found."
                                                                                                                                                            )

                                                                                                                                                                for column in [
                                                                                                                                                                        "open",
                                                                                                                                                                                "high",
                                                                                                                                                                                        "low",
                                                                                                                                                                                                "close",
                                                                                                                                                                                                    ]:
                                                                                                                                                                                                            if column in df.columns:
                                                                                                                                                                                                                        if (df[column] <= 0).any():
                                                                                                                                                                                                                                        errors.append(
                                                                                                                                                                                                                                                            f"Invalid values in {column}."
                                                                                                                                                                                                                                                                            )

                                                                                                                                                                                                                                                                                if all(
                                                                                                                                                                                                                                                                                        column in df.columns
                                                                                                                                                                                                                                                                                                for column in ["high", "low"]
                                                                                                                                                                                                                                                                                                    ):
                                                                                                                                                                                                                                                                                                            if (df["high"] < df["low"]).any():
                                                                                                                                                                                                                                                                                                                        errors.append(
                                                                                                                                                                                                                                                                                                                                        "High price cannot be lower than low price."
                                                                                                                                                                                                                                                                                                                                                    )

                                                                                                                                                                                                                                                                                                                                                        return {
                                                                                                                                                                                                                                                                                                                                                                "valid": len(errors) == 0,
                                                                                                                                                                                                                                                                                                                                                                        "errors": errors,
                                                                                                                                                                                                                                                                                                                                                                                "rows": len(df),
                                                                                                                                                                                                                                                                                                                                                                                    }