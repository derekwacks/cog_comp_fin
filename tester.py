import numpy as np
import json

meta_data = []
for i in range(6):
    person = [str(i + 1), 'no-mask', 'happy']
    meta_data.append(person)
for i in range(6, 12):
    person = [str(i + 1), 'no-mask', 'sad']
    meta_data.append(person)

print(meta_data)