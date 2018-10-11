import matplotlib.pyplot as plt
import sys

def fuzzy_set_to_plot(fuzzy_set):
    return [
        fuzzy_set[0] - fuzzy_set[2],
        fuzzy_set[0],
        fuzzy_set[1],
        fuzzy_set[1] + fuzzy_set[3]
    ]

fuzzy_sets = {
        "none": [0, 0, 0, 0,],
        "small": [2, 4, 2, 3],
        "medium": [7, 10, 2, 1],
        "large": [11, 15, 1, 5],
        }

trapezoid = [0,1,1,0]

for key, value in fuzzy_sets.items():
    plot_values = fuzzy_set_to_plot(value)
    plt.plot(plot_values, trapezoid, label=key)

if len(sys.argv) == 2:
    sub_question = sys.argv[1]
    if sub_question == "a": plt.axvspan(5, 7, color="green", alpha=0.2, label="small and medium")
    if sub_question == "b": plt.axvspan(0, 7, color="blue", alpha=0.2, label="none or small")
    if sub_question == "c": plt.axvspan(5, 20, color="aqua", alpha=0.2, label="medium or large")
    if sub_question == "d":
        plt.axvspan(0, 5, color="red", alpha=0.2, label="not medium")
        plt.axvspan(11, 20, color="red", alpha=0.2)

plt.legend(loc='best')
plt.show()
