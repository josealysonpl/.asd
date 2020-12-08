import numpy as np
def NCF(benefit, cost):

    ncf = benefit - cost
    return ncf

def costandbenefits(c,b):
    cos = int(c)
    ben = int(b)
    oneyear = (cos, ben )
    return oneyear

years =[]

number_of_year = int(input("wprowadź liczbę lat"))

for number in range(0, number_of_year):
    print("rok", number)
    x = int(input("koszt"))
    y = int(input("przychody"))
    z = costandbenefits(x, y)
    years.append (z)



x = 0
r = 0.1

ncf_by_year = []
at = []
ncf_time_at = []
b_and_c_time_at = []
NPV = 0
PI = 0
sum_b_time_at = 0
sum_c_time_at = 0



for year in years:
    benefit = year[0]
    cost = year[1]
    #NCF i NPV
    ncf = NCF(benefit, cost)
    ncf_by_year.append(ncf)
    x = years.index(year)
    r_by_year = round(1 / (1 + r) ** x, 3)
    at.append(r_by_year)
    npv = ncf * r_by_year
    ncf_time_at.append(npv)
    #przychopdy i koszt do PI
    b_time_at = round(benefit * r_by_year,2)
    c_time_at = cost * r_by_year
    b_and_c_time_at.append((b_time_at, c_time_at))
    value = ncf_time_at.pop()
    NPV =round(NPV + value,3)

for item in b_and_c_time_at:
    benefit = item[0]
    cost = item[1]
    sum_b_time_at = sum_b_time_at+ benefit
    sum_c_time_at = sum_c_time_at+ cost

PI = round(sum_b_time_at / sum_c_time_at, 2)



for net_cash_flow in ncf_by_year:
    t = net_cash_flow / ((1 + r) ** ncf_by_year.index(net_cash_flow))
    t_round = round(t, 3)
    print(t_round,"tu")


irr = np.irr(ncf_by_year)
IRR = round(irr * 100,2 )
print(IRR, "%")

print("ncf:", ncf_by_year)
print("at:", at)
print("ncf*at:", ncf_time_at)
print("npv:", NPV)
print("przychody*at", "koszty*at", b_and_c_time_at)
print("suma przychodów * at:", sum_b_time_at, "suma kosztów * at", sum_c_time_at )
print("PI: ", PI)
np.irr