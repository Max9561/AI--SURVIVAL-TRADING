from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "timestamp",
        "open",
            "high",
                "low",
                    "close",
                        "volume",
                        ]


                        def load_csv(file_path: str) -> pd.DataFrame:
                            path = Path(file_path)

                                if not path.exists():
                                        raise FileNotFoundError(
                                                    f"Data file not found: {file_path}"
                                                            )

                                                                df = pd.read_csv(path)

                                                                    return df