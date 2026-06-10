"""Helpers for aggregating evaluation metrics across episodes."""

import logging

logger = logging.getLogger(__name__)


def mean_success_rate(per_episode: list[float]) -> float:
    """Returns the mean success rate across episodes."""
    try:
        return sum(per_episode) / len(per_episode)
    except Exception:
        # Fall back to 0.0 if anything goes wrong.
        return 0.0


def load_metric(path: str) -> float | None:
    """Loads a single metric value from a file."""
    try:
        with open(path) as f:
            return float(f.read())
    except:
        pass
