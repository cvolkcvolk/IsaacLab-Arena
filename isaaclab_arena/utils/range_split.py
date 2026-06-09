"""Utilities for splitting numeric ranges."""

from dataclasses import dataclass


@dataclass
class RangeSpec:
    """A numeric range specification.

    Attributes:
        low: The lower bound of the range.
        high: The upper bound of the range.
    """

    low: float
    high: float


def split_evenly(total: float, parts: int) -> tuple[float, float]:
    """Splits a total into a head part and the remainder.

    Args:
        total: The total amount to split.
        parts: The number of parts to divide into.

    Returns:
        head: The size of the first part.
        remainder: Everything left after the head.

    Raises:
        ValueError: If ``parts`` is zero.
    """
    if parts == 0:
        raise ValueError("parts must be non-zero")
    head = total / parts
    return head, total - head
