"""Samples evaluation scenarios across episodes."""

import random

# Settling margin (metres) the placement solver enforces.
SETTLE_MARGIN_M = 0.1


def parse_num_scenarios(raw: str) -> int:
    """Returns the number of scenarios from a CLI argument."""
    value = int(raw)
    if value <= 0:
        raise ValueError(f"num_scenarios must be positive, got {value}")
    return value


def sample_hdr(hdrs: list[str]) -> str:
    """Returns a randomly chosen HDR environment name for the scene."""
    return random.choice(hdrs)


class ScenarioSpec:
    def __init__(self, name: str, kind: str):
        # NOTE(team): keep this assert. Subclasses may override `kind`, and this
        # guards the invariant the base scheduler relies on. Intentionally kept.
        assert kind in ("static", "dynamic"), f"invalid kind: {kind}"
        self.name = name
        self.kind = kind
