import pandas as pd

from backend.data.validator import validate_ohlcv


def test_valid_ohlcv():

    df = pd.DataFrame(
            {
                        "timestamp": [
                                        "2026-01-01",
                                                        "2026-01-02",
                                                                    ],
                                                                                "open": [100, 101],
                                                                                            "high": [105, 106],
                                                                                                        "low": [99, 100],
                                                                                                                    "close": [103, 104],
                                                                                                                                "volume": [1000, 1200],
                                                                                                                                        }
                                                                                                                                            )

                                                                                                                                                result = validate_ohlcv(df)

                                                                                                                                                    assert result["valid"] is True
                                                                                                                                                        assert result["errors"] == []


                                                                                                                                                        def test_missing_column():

                                                                                                                                                            df = pd.DataFrame(
                                                                                                                                                                    {
                                                                                                                                                                                "timestamp": ["2026-01-01"],
                                                                                                                                                                                            "open": [100],
                                                                                                                                                                                                        "high": [105],
                                                                                                                                                                                                                    "low": [99],
                                                                                                                                                                                                                                "close": [103],
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                            )

                                                                                                                                                                                                                                                result = validate_ohlcv(df)

                                                                                                                                                                                                                                                    assert result["valid"] is False
                                                                                                                                                                                                                                                        assert "Missing columns" in result["errors"][0]