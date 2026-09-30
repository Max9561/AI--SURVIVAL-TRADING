from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class PaperOrder:
    symbol: str
        side: str
            quantity: float
                price: float
                    timestamp: datetime
                        status: str = "FILLED"


                        class PaperBroker:

                            VALID_SIDES = {
                                    "BUY",
                                            "SELL",
                                                }

                                                    def __init__(self):
                                                            self.orders: list[PaperOrder] = []

                                                                def place_order(
                                                                        self,
                                                                                symbol: str,
                                                                                        side: str,
                                                                                                quantity: float,
                                                                                                        price: float,
                                                                                                            ) -> PaperOrder:

                                                                                                                    side = side.upper()

                                                                                                                            if side not in self.VALID_SIDES:
                                                                                                                                        raise ValueError(
                                                                                                                                                        "Side must be BUY or SELL."
                                                                                                                                                                    )

                                                                                                                                                                            if quantity <= 0:
                                                                                                                                                                                        raise ValueError(
                                                                                                                                                                                                        "Quantity must be greater than zero."
                                                                                                                                                                                                                    )

                                                                                                                                                                                                                            if price <= 0:
                                                                                                                                                                                                                                        raise ValueError(
                                                                                                                                                                                                                                                        "Price must be greater than zero."
                                                                                                                                                                                                                                                                    )

                                                                                                                                                                                                                                                                            order = PaperOrder(
                                                                                                                                                                                                                                                                                        symbol=symbol,
                                                                                                                                                                                                                                                                                                    side=side,
                                                                                                                                                                                                                                                                                                                quantity=quantity,
                                                                                                                                                                                                                                                                                                                            price=price,
                                                                                                                                                                                                                                                                                                                                        timestamp=datetime.now(timezone.utc),
                                                                                                                                                                                                                                                                                                                                                )

                                                                                                                                                                                                                                                                                                                                                        self.orders.append(order)

                                                                                                                                                                                                                                                                                                                                                                return order

                                                                                                                                                                                                                                                                                                                                                                    def get_orders(self) -> list[PaperOrder]:
                                                                                                                                                                                                                                                                                                                                                                            return self.orders.copy()