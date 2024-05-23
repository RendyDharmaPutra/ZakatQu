# for i in range(1000) :
#     print("HALO MAS AL")

# num = 1

# print(type(num) == int)

from rich import print
from rich.pretty import Pretty
from rich.panel import Panel

pretty = Pretty(locals())
panel = Panel(pretty)
print(panel)