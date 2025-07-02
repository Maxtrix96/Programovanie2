current_gain = 14_875
gain_increment = 750
ores_needed = 0 # amount of times needed to mine

start_needed_xp = 800_000
max_xp = 1_000_000
needed_xp_increment = 100_000 
total_xp_gain = 0 # logging total
current_level = 27
current_exp = 397825
exp_needed = start_needed_xp - current_exp

while current_level < 60:
    exp_needed = max_xp - current_exp # current/new level reached = calculate max xp
    ores_needed += exp_needed // current_gain # amount of additional # of ores needed to advance to next level

    # new level reached, increment gain and max needed
    current_exp = exp_needed % current_gain # leftover xp
    current_gain += gain_increment # amount of exp added onto one ore
    max_xp += needed_xp_increment
    current_level += 1 # new level reached
    total_xp_gain += exp_needed # amount of xp needed in total since start of simulation, logging

print(ores_needed)
print(total_xp_gain)