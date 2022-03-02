import ahpy
from fractions import Fraction

def pairwise_comparisons(comparedlist, mode):
    comparisons = {}
    copiedlist = comparedlist[:]
    comparison_step = 0
    while(len(comparedlist) != 0):
        for x in range(1, len(comparedlist)):
            pair = (comparedlist[0], comparedlist[x])
            if(mode == "criteria"):
                 importance = input("How much more important is {} than {}? (1-9) ".format(pair[0], pair[1]))
            else:
                 importance = input("How much more better is {} than {} in {}? (1-9) ".format(pair[0], pair[1], mode))
            if "/" in importance:
                importance = float(sum(Fraction(s) for s in importance.split()))
            comparisons[pair] = importance
            comparison_step += 1
        comparedlist.pop(0)
    print(comparisons)
    return comparisons, copiedlist


def AHP():
    criteria = ["Performance", "Budget", "Versatility", "Ease of development", "Time to market"]
    alternatives = ["Monolithic CMS", "Headless CMS", "Full stack"]

    Performance_comparisons, alternatives = pairwise_comparisons(alternatives, "Performance")
    Budget_comparisons, alternatives = pairwise_comparisons(alternatives, "Budget")
    Versatility_comparisons, alternatives = pairwise_comparisons(alternatives, "Versatility")
    Ease_of_development_comparisons, alternatives = pairwise_comparisons(alternatives, "Ease_of_development")
    Time_to_market_comparisons, alternatives = pairwise_comparisons(alternatives, "Time_to_market")

    criteria_comparisons, criteria = pairwise_comparisons(criteria, "criteria")

    Performance = ahpy.Compare("Performance", comparisons=Performance_comparisons, precision=3, random_index="saaty")
    Budget = ahpy.Compare("Budget",  comparisons=Budget_comparisons, precision=3, random_index="saaty")
    Versatility = ahpy.Compare("Versatility", comparisons=Versatility_comparisons, precision=3, random_index="saaty")
    Ease_of_development = ahpy.Compare("Ease_of_development", comparisons=Ease_of_development_comparisons, precision=3, random_index="saaty")
    Time_to_market = ahpy.Compare("Time_to_market", comparisons=Time_to_market_comparisons, precision=3, random_index="saaty")
    Criteria = ahpy.Compare("criteria", comparisons=criteria_comparisons, precision=3, random_index="saaty")

    Criteria.add_children([Performance, Budget, Versatility, Ease_of_development, Time_to_market])

    print(Criteria.report())

AHP()
