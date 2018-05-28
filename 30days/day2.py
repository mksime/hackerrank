def totalcost(mc, tipp, taxp):
    tip_value = mc * (tipp / 100)
    tax_value = mc * (taxp / 100)
    mc_total = mc + tip_value + tax_value
    print("The total meal cost is %d dollars." % round(mc_total))

print(totalcost(12, 20., 8.))
