import matplotlib.pyplot as plt
import sys

def fuzzy_set_to_plot(fuzzy_set):
    if fuzzy_set[1] == None:
        return [
            fuzzy_set[0] - fuzzy_set[2],
            fuzzy_set[0],
            fuzzy_set[0] + 10

        ]
    else:
        return [
            fuzzy_set[0] - fuzzy_set[2],
            fuzzy_set[0],
            fuzzy_set[1],
            fuzzy_set[1] + fuzzy_set[3]
        ]

# The 4-tuples (b) solution
fuzzy_sets = {
        "young": [0, 20, 0, 20],
        "middle-aged": [50, 60, 15, 5],
        "old": [70, None, 10, 0],
        }

trapezoid = [0,1,1,0]
half_trapezoid = [0,1,1]

for key, value in fuzzy_sets.items():
        plot_values = fuzzy_set_to_plot(value)
        if len(plot_values) == 3:
            plt.plot(plot_values, half_trapezoid, label=key)
        else:
            plt.plot(plot_values, trapezoid, label=key)

plt.legend(loc='best')
plt.show()
