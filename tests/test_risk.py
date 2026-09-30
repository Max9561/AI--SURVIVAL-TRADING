from backend.risk.engine import RiskEngine


def test_risk_approved():

    engine = RiskEngine()

        result = engine.approve(
                risk_fraction=0.002,
                        daily_loss_fraction=0.005,
                                drawdown_fraction=0.02,
                                    )

                                        assert result.approved is True


                                        def test_trade_risk_rejected():

                                            engine = RiskEngine()

                                                result = engine.approve(
                                                        risk_fraction=0.02,
                                                                daily_loss_fraction=0.0,
                                                                        drawdown_fraction=0.0,
                                                                            )

                                                                                assert result.approved is False


                                                                                def test_daily_loss_rejected():

                                                                                    engine = RiskEngine()

                                                                                        result = engine.approve(
                                                                                                risk_fraction=0.001,
                                                                                                        daily_loss_fraction=0.03,
                                                                                                                drawdown_fraction=0.0,
                                                                                                                    )

                                                                                                                        assert result.approved is False