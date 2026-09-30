from datetime import datetime, timezone


class TaskScheduler:

    def __init__(self):
            self.tasks = {}

                def register(
                        self,
                                name: str,
                                        interval_seconds: int,
                                            ):
                                                    if interval_seconds <= 0:
                                                                raise ValueError("Interval must be positive.")

                                                                        self.tasks[name] = {
                                                                                    "interval_seconds": interval_seconds,
                                                                                                "last_run": None,
                                                                                                        }

                                                                                                            def due_tasks(self) -> list[str]:
                                                                                                                    now = datetime.now(timezone.utc)
                                                                                                                            due = []

                                                                                                                                    for name, task in self.tasks.items():
                                                                                                                                                last_run = task["last_run"]

                                                                                                                                                            if last_run is None:
                                                                                                                                                                            due.append(name)
                                                                                                                                                                                            continue

                                                                                                                                                                                                        elapsed = (
                                                                                                                                                                                                                        now - last_run
                                                                                                                                                                                                                                    ).total_seconds()

                                                                                                                                                                                                                                                if elapsed >= task["interval_seconds"]:
                                                                                                                                                                                                                                                                due.append(name)

                                                                                                                                                                                                                                                                        return due

                                                                                                                                                                                                                                                                            def mark_completed(self, name: str):
                                                                                                                                                                                                                                                                                    if name not in self.tasks:
                                                                                                                                                                                                                                                                                                raise KeyError(f"Unknown task: {name}")

                                                                                                                                                                                                                                                                                                        self.tasks[name]["last_run"] = (
                                                                                                                                                                                                                                                                                                                    datetime.now(timezone.utc)
                                                                                                                                                                                                                                                                                                                            )