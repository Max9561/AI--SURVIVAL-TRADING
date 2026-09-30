from dataclasses import dataclass

from backend.evidence.models import Evidence


@dataclass
class ConflictResult:
    conflicted: bool
        bullish_count: int
            bearish_count: int
                explanation: str


                class ConflictDetector:

                    def detect(
                            self,
                                    evidence: list[Evidence],
                                        ) -> ConflictResult:

                                                bullish = 0
                                                        bearish = 0

                                                                for item in evidence:

                                                                            if not isinstance(
                                                                                            item.value,
                                                                                                            (int, float),
                                                                                                                        ):
                                                                                                                                        continue

                                                                                                                                                    if item.value > 0.2:
                                                                                                                                                                    bullish += 1

                                                                                                                                                                                elif item.value < -0.2:
                                                                                                                                                                                                bearish += 1

                                                                                                                                                                                                        conflicted = (
                                                                                                                                                                                                                    bullish > 0
                                                                                                                                                                                                                                and bearish > 0
                                                                                                                                                                                                                                        )

                                                                                                                                                                                                                                                if conflicted:
                                                                                                                                                                                                                                                            explanation = (
                                                                                                                                                                                                                                                                            "Bullish and bearish evidence "
                                                                                                                                                                                                                                                                                            "are present simultaneously."
                                                                                                                                                                                                                                                                                                        )

                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                            explanation = (
                                                                                                                                                                                                                                                                                                                                            "No direct directional conflict detected."
                                                                                                                                                                                                                                                                                                                                                        )

                                                                                                                                                                                                                                                                                                                                                                return ConflictResult(
                                                                                                                                                                                                                                                                                                                                                                            conflicted=conflicted,
                                                                                                                                                                                                                                                                                                                                                                                        bullish_count=bullish,
                                                                                                                                                                                                                                                                                                                                                                                                    bearish_count=bearish,
                                                                                                                                                                                                                                                                                                                                                                                                                explanation=explanation,
                                                                                                                                                                                                                                                                                                                                                                                                                        )