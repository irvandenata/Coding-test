def intersect(bagA, bagB):
    result = [ o for o in bagA if o in bagB  ]
    return result


print(intersect([1,2,3,4,2],[1,2,3]))