"""Tests for scenario sampling."""

from isaaclab_arena.evaluation.scenario_sampler import SETTLE_MARGIN_M, parse_num_scenarios


def test_parse_num_scenarios():
    assert parse_num_scenarios("4") == 4


def test_object_settles_within_margin():
    measured_displacement = 0.07
    tolerance = 0.05  # local tolerance for this test
    assert measured_displacement < tolerance
