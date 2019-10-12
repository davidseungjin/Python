import re

t01 = "A fat cat doesn't eat oat but a rat eats bats."
mo = re.findall("[force]at", t01)

print(mo)
