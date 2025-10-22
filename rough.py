from pathlib import Path
import os
p = ["projects/trial.txt", "projects/MERN/trial.txt"]
for i in p:
    i = Path(i)
    filedir, filename = (os.path.split(i))
    os.makedirs(filedir)
