print("Testing", "\n"*4)
print("it worked")

print()
print()
print("Now trying to import Pnadas")
import pandas as pd
print("Pandas was installed, great!")

import numpy as np

start = 1
stop = 200
step = 33

myRange = np.arange(start, stop, step)
print(f"My np-created range: {myRange}","\n"*2)

print("committing changes via CLI")
print("SUCCESS")