import ahpy
from fractions import Fraction

from scipy.__config__ import show

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
                #importance = float(sum(Fraction(s) for s in importance.split()))
                importance = Fraction(importance)
            elif(importance == "" or importance.isalpha()):
                print("Invalid input, exiting")
                exit(1)
            comparisons[pair] = float(importance)
            comparison_step += 1
        comparedlist.pop(0)
    print(comparisons)
    return comparisons, copiedlist


def AHP(): # TODO: luovuta
    criteria = ["Performance", "Budget", "Versatility", "Ease_of_development", "Time_to_market"]
    alternatives = ["Monolithic CMS", "Headless CMS", "Full stack"]

    if(int(input("Do you want to use predetermined criteria? (1 for yes, 0 for no) "))):
        Performance_comparisons = {('Monolithic CMS', 'Headless CMS'): 1/6, ('Monolithic CMS', 'Full stack'): 1/9, ('Headless CMS', 'Full stack'): 1/2}
        Budget_comparisons={('Monolithic CMS', 'Headless CMS'): 2, ('Monolithic CMS', 'Full stack'): 6, ('Headless CMS', 'Full stack'): 5}
        Versatility_comparisons={('Monolithic CMS', 'Headless CMS'): 1/7, ('Monolithic CMS', 'Full stack'): 1/9, ('Headless CMS', 'Full stack'): 1/2}
        Ease_of_development_comparisons ={('Monolithic CMS', 'Headless CMS'): 2, ('Monolithic CMS', 'Full stack'): 7, ('Headless CMS', 'Full stack'): 7}
        Time_to_market_comparisons ={('Monolithic CMS', 'Headless CMS'): 2, ('Monolithic CMS', 'Full stack'): 5, ('Headless CMS', 'Full stack'): 5}
    else:
        Performance_comparisons, alternatives = pairwise_comparisons(alternatives, "Performance")
        Budget_comparisons, alternatives = pairwise_comparisons(alternatives, "Budget")
        Versatility_comparisons, alternatives = pairwise_comparisons(alternatives, "Versatility")
        Ease_of_development_comparisons, alternatives = pairwise_comparisons(alternatives, "Ease_of_development")
        Time_to_market_comparisons, alternatives = pairwise_comparisons(alternatives, "Time_to_market")

    if(int(input("And alternatives? "))):
        criteria_comparisons = {('Performance', 'Budget'): 0.25, ('Performance', 'Versatility'): 0.25, ('Performance', 'Ease_of_development'): 1.0, ('Performance', 'Time_to_market'): 0.16666666666666666, ('Budget', 'Versatility'): 8.0, ('Budget', 'Ease_of_development'): 6.0, ('Budget', 'Time_to_market'): 3.0, ('Versatility', 'Ease_of_development'): 0.25, ('Versatility', 'Time_to_market'): 0.2, ('Ease_of_development', 'Time_to_market'): 1.0}
       
    else:
        criteria_comparisons, criteria = pairwise_comparisons(criteria, "criteria")

    Performance = ahpy.Compare("Performance", comparisons=Performance_comparisons, iterations=1000, precision=9, random_index="saaty")
    Budget = ahpy.Compare("Budget",  comparisons=Budget_comparisons, precision=9,iterations=1000, random_index="saaty")
    Versatility = ahpy.Compare("Versatility", comparisons=Versatility_comparisons, precision=9, iterations=1000, random_index="saaty")
    Ease_of_development = ahpy.Compare("Ease_of_development", comparisons=Ease_of_development_comparisons, precision=9, iterations=1000, random_index="saaty")
    Time_to_market = ahpy.Compare("Time_to_market", comparisons=Time_to_market_comparisons, precision=9, iterations=1000, random_index="saaty")
    Criteria = ahpy.Compare("Criteria", comparisons=criteria_comparisons, precision=9, iterations=1000, random_index="saaty")

    Criteria.add_children([Performance, Budget, Versatility, Ease_of_development, Time_to_market])

    Criteria.report(show=True)

 
    #print("Yeahboi: %.2f" % (sum([Criteria.target_weights["Monolithic CMS"], Criteria.target_weights["Headless CMS"], Criteria.target_weights["Full stack"]])))

def AHP2(): # legitti
    experience_comparisons = {('Moll', 'Nell'): 9, ('Moll', 'Sue'): 9, ('Nell', 'Sue'): 9}
    education_comparisons = {('Moll', 'Nell'): 9, ('Moll', 'Sue'): 9, ('Nell', 'Sue'): 9}
    charisma_comparisons = {('Moll', 'Nell'): 9, ('Moll', 'Sue'): 9, ('Nell', 'Sue'): 9}
    age_comparisons = {('Moll', 'Nell'): 1/3, ('Moll', 'Sue'): 5, ('Nell', 'Sue'): 9}

    criteria_comparisons = {('Experience', 'Education'): 9, ('Experience', 'Charisma'): 9, ('Experience', 'Age'): 9, ('Education', 'Charisma'): 9, ('Education', 'Age'): 9, ('Charisma', 'Age'): 9}

    experience = ahpy.Compare('Experience', experience_comparisons, precision=3, random_index='saaty')
    education = ahpy.Compare('Education', education_comparisons, precision=3, random_index='saaty')
    charisma = ahpy.Compare('Charisma', charisma_comparisons, precision=3, random_index='saaty')
    age = ahpy.Compare('Age', age_comparisons, precision=3, random_index='saaty')

    criteria = ahpy.Compare('Criteria', criteria_comparisons, precision=3, random_index='saaty')

    criteria.add_children([experience, education, charisma, age])
    criteria.report(show=True)


#AHP3()
# Pyry koodaa kovin mutta tulkki vittuilloo
#AHP2()

AHP()




