import timeit
from operator import mul
from functools import reduce

QUEUE_OPTIMIZE_LEN = 5000
PRUNE_DAY = 12


def ints(s):
    nums, cur = [], ""
    for c in s:
        if c in "0123456789":
            cur += c
        else:
            if len(cur):
                nums.append(int(cur))
            cur = ""
    return nums


def solve(max_time, blueprint_id, ore_rc, clay_rc, obs_rc_ore, obs_rc_clay, geo_rc_ore, geo_rc_obs):
    time_prt = max_time
    Q = [(1, 0, 0, 0, 0, 0, 0, 0, max_time)]
    seen = set()
    max_geodes, max_ore_cost = 0, max(ore_rc, clay_rc, obs_rc_ore, geo_rc_ore)

    while Q:
        (robots_ore, robots_clay, robots_obs, robots_geode, ore, clay, obs, geode, time_left) = Q.pop()

        if time_left < time_prt:
            time_prt = time_left
            if len(Q) > QUEUE_OPTIMIZE_LEN:
                # should not be needed unless our optimizations fail
                print(f"shuffle {time_left}")
                Q = sorted(Q, key=lambda c: (c[7] * 13 ** 3) + (c[6] * 13 ** 2) + (c[5] * 13 ** 1) + c[4],
                           reverse=True)[:QUEUE_OPTIMIZE_LEN]

        if time_left == 0:
            max_geodes = max(max_geodes, geode)
            continue

        # If we have enough resources then it doesn't matter if we have even more
        capped_ore = min(ore, robots_ore + (max_ore_cost - robots_ore) * time_left)
        capped_clay = min(clay, robots_clay + (obs_rc_clay - robots_clay) * time_left)
        capped_obs = min(obs, robots_obs + (geo_rc_obs - robots_obs) * time_left)

        # state-culling
        pruned_state = (
            robots_ore, robots_clay, robots_obs, robots_geode,
            capped_ore, capped_clay, capped_obs, geode,
            time_left
        )
        if pruned_state in seen:
            continue
        seen.add(pruned_state)

        # build an geode robot
        if ore >= geo_rc_ore and \
                obs >= geo_rc_obs:
            Q.append((
                robots_ore + 0, robots_clay + 0, robots_obs + 0, robots_geode + 1,
                ore - geo_rc_ore + robots_ore, clay + robots_clay, obs - geo_rc_obs + robots_obs, geode + robots_geode,
                time_left - 1
            ))
            continue  # is it always best to make a geode robot if we can?
            # no, ex: ore robot = 2 ore, clay robot = 2 ore, obsidian = 2 ore + 0 clay, geode = 2 ore + 0 obsidian
            # after min 1 we have 1 ore
            # after min 2 we have 2 ore
            # min 3 do we build a geode miner or an ore robot? 
            # obviously we buy another ore miner and then build a geode miner every turn after that

        # do nothing
        Q.append((
            robots_ore, robots_clay, robots_obs, robots_geode,
            ore + robots_ore, clay + robots_clay, obs + robots_obs, geode + robots_geode,
            time_left - 1
        ))

        # build an ore robot
        if ore >= ore_rc and \
                robots_ore < max_ore_cost:
            Q.append((
                robots_ore + 1, robots_clay + 0, robots_obs + 0, robots_geode + 0,
                ore + robots_ore - ore_rc, clay + robots_clay, obs + robots_obs, geode + robots_geode,
                time_left - 1
            ))

        # build a clay robot
        if ore >= clay_rc and \
                robots_clay < obs_rc_clay:
            Q.append((
                robots_ore + 0, robots_clay + 1, robots_obs + 0, robots_geode + 0,
                ore - clay_rc + robots_ore, clay + robots_clay, obs + robots_obs, geode + robots_geode,
                time_left - 1
            ))

        # build an obsidian robot
        if ore >= obs_rc_ore and \
                clay >= obs_rc_clay and \
                robots_obs < geo_rc_obs:
            Q.append((
                robots_ore + 0, robots_clay + 0, robots_obs + 1, robots_geode + 0,
                ore - obs_rc_ore + robots_ore, clay - obs_rc_clay + robots_clay, obs + robots_obs, geode + robots_geode,
                time_left - 1
            ))

    return max_geodes


if __name__ == "__main__":
    with open('case1.in') as fin:
        bprints = [ints(e.strip()) for e in fin.readlines()]
        start_time = timeit.default_timer()
        print(sum([(1 + idx) * solve(24, *blue) for idx, blue in enumerate(bprints)]))
        p1_time = timeit.default_timer()
        print(reduce(mul, [solve(32, *blue) for blue in bprints[:3]]))
        p2_time = timeit.default_timer()
        print(f"Part 1 time: {p1_time - start_time}s")
        print(f"Part 2 time: {p2_time - start_time}s")
