#! /usr/bin/python2.6

from gurobipy import *

activities = []
activitiesNames = []
calories = []

# Crappy lazy way to read the input
n = int(raw_input())
while n > 0:
    n -= 1
    p = raw_input()
    act_cal = p.split()
    act = act_cal[0]
    cal = int(act_cal[1])
    activitiesNames.append(act)
    calories.append(cal)


m = Model("subsetSum")

# Comment next line to make Gurobi spit out some info while optimizing.
m.setParam( 'OutputFlag', False ) 


# We want do maximize
m.ModelSense = -1

# Create the variables
for i in xrange(len(activitiesNames)):
    newvar = m.addVar(0.0, 1.0, 1.0, GRB.BINARY, activitiesNames[i])
    activities.append(newvar)

# Integrate new variables
m.update()

#Add constraint: Sum(x[i]*c[i]) = 0
m.addConstr(LinExpr(calories, activities), GRB.EQUAL, 0.0, "soma zero")

# Integrate new constraints
m.update()

# Uncomment next line to write a file with de model
# m.write('modelo.lp')

# Otimizar
m.optimize()


# Print the solution
sol = []
for v in m.getVars():
    if v.X == 1.0:
        sol.append(v.VarName)
if len(sol) > 0:
    for s in sorted(sol):
        print s
else:
    print "no solution"

# print "Obj:", m.ObjVal

