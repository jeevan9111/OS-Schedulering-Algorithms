import numpy as np

jobs = np.array([(1, 0, 2),
                 (2, 1, 5),
                 (3, 2, 3),
                 (4, 4, 1),
                 (5, 5, 2),
                 (6, 6, 4),
                 (7, 10, 3)],
                dtype=[('PID', '>i4'), ('ArrivalTime', '>i4'), ('BurstTime', '>i4')]
                )
