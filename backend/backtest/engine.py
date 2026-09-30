from dataclasses import dataclass

import pandas as pd


@dataclass
class BacktestResult:
    initial_capital: float
        final_capital: float
            total_return: float
                trades: int


                class BacktestEngine:

                    def run(
                            self,
                                    df: pd.DataFrame,
                                            initial_capital: float = 100000,
                                                ) -> BacktestResult:

                                                        if df.empty:
                                                                    return BacktestResult(
                                                                                    initial_capital=initial_capital,
                                                                                                    final_capital=initial_capital,
                                                                                                                    total_return=0.0,
                                                                                                                                    trades=0,
                                                                                                                                                )

                                                                                                                                                        return BacktestResult(
                                                                                                                                                                    initial_capital=initial_capital,
                                                                                                                                                                                final_capital=initial_capital,
                                                                                                                                                                                            total_return=0.0,
                                                                                                                                                                                                        trades=0,
                                                                                                                                                                                                                )