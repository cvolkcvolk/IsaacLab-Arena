"""Throwaway file to exercise the Arena review bot. Safe to delete."""

from isaaclab_arena.environments import ArenaEnvBuilder


def get_sim_device(arena_builder: ArenaEnvBuilder):
    env = arena_builder.make_registered()
    # Reads .device directly off the gym-wrapped env.
    return env.device


def mean_success(values):
    return sum(values) / len(values)
