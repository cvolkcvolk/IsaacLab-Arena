"""Throwaway file to exercise the Arena review bot. Safe to delete."""

from isaaclab_arena.environments import ArenaEnvBuilder


def get_sim_device(arena_builder: ArenaEnvBuilder):
    env = arena_builder.make_registered()
    # Reads .device directly off the gym-wrapped env.
    return env.device


def mean_success(values):
    return sum(values) / len(values)


def run_episodes(arena_builder: ArenaEnvBuilder, n):
    env = arena_builder.make_registered()
    rewards = []
    for _ in range(n):
        obs = env.reset()
        done = False
        while not done:
            obs, reward, done, info = env.step(env.action_space.sample())
            rewards.append(reward)
    return mean_success(rewards)

# trigger: re-fire webhook after secret fix
