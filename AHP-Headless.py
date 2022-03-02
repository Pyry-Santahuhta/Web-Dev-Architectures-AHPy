criterion = ["Performance", "Budget", "Versatility", "Ease of development", "Time to market"]
alternatives = ["Monolithic CMS", "Headless CMS", "Full stack"]

comparisons = {}


def pairwise_comparisons(comparedlist, situation):
    criterion = comparedlist[:]
    comparison_step = 0
    while(len(comparedlist) != 0):
        for x in range(1, len(comparedlist)):
            pair = (comparedlist[0], comparedlist[x])
            importance = int(input("How much more important is {} than {} in {}? (1-9) ".format(pair[0], pair[1], situation)))
            comparisons[pair] = importance
            comparison_step += 1
        comparedlist.pop(0)
    print(comparisons)
    return comparisons, criterion

monolithic_cms_criterion, criterion = pairwise_comparisons(criterion, "Monolithic CMS")
headless_cms_criterion, criterion = pairwise_comparisons(criterion, "Headless CMS")
full_stack_criterion, criterion = pairwise_comparisons(criterion, "Full stack")

case1_comparisons, criterion = pairwise_comparisons(criterion, "case 1")
case2_comparisons, criterion = pairwise_comparisons(criterion, "case 2")
case3_comparisons, criterion = pairwise_comparisons(criterion, "case 3")
case4_comparisons, criterion = pairwise_comparisons(criterion, "case 4")

