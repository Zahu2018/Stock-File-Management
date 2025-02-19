# Redenumeste fisierele dintr-un folder
# din litere mici in litere mari
import os
files = os.listdir()
for name in files:
    _ = name[:-4]
    extensie = name[-4:]
    new_name = _.upper() + extensie
    print(new_name)
    os.rename(name, new_name)
print("Final.")