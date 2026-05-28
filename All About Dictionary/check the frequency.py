# Initialize dictionary

from collections import Counter

test_dict = {

"Codingal": 2,

"is": 2,

"best": 2,

"for": 2,

"Coding": 1

}

counts = Counter(test_dict.values())

print("Frequency of '2' using Counter: ", {counts[2]})