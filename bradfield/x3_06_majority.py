

def majority_element(coll):
    m = len(coll) / 2
    result = {}
    for item in coll:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    for k, v in result.iteritems():
        if v > m:
            return k
    return None
