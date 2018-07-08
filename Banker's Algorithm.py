import numpy as np

claims = np.array([(3, 2, 2),
                   (6, 1, 3),
                   (3, 1, 4),
                   (4, 2, 2)])

allocations = np.array([(1, 0, 0),
                        (5, 1, 1),
                        (2, 1, 1),
                        (0, 0, 2)])
resource = np.array([9, 3, 6])
available = np.array([1, 1, 2])
resource_allocated1 = sum(allocations)
resource_allocated2 = resource - available
if not all(x == y for x, y in zip(resource_allocated1, resource_allocated2)):
    print("Bad Allocation")
    exit(0)

while len(claims) != 0:
    executed_a_process = False
    requirements = claims - allocations
    i = 0
    for requirement in requirements:
        to_remain = available - requirement
        if all(x >= 0 for x in to_remain):
            executed_a_process = True
            available += allocations[i]
            claims = np.delete(claims, i, 0)
            allocations = np.delete(allocations, i, 0)
            break
        i += 1
    if not executed_a_process:
        print("Unsafe")
        exit(0)

print("safe")
