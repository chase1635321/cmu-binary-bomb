#!/usr/bin/python3

import angr
import claripy

s = "isrveawhobpnutfg"

project = angr.Project("bomb")
state = project.factory.blank_state(addr=0x8048d52)
simgr = project.factory.simgr()

password = claripy.BVS("password", 8*6)

state.memory.store(0x804b220, password)

simgr.explore(find=0x08048d7a)

if simgr.found:
    solution = simgr.found[0]
    solution_BVS = solution.memory.load(0x8048d52, 6)
    solution.add_constraints(solution_BVS == "giants")
    s = solution.solver.eval(password, cast_to=bytes).decode()
    print(s)
else:
    print("No solution found")




# Must be equal to "giants"
