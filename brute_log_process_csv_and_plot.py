import pandas as pd
import matplotlib.pyplot as plt

filename = "brute_log_results.csv"
df = pd.read_csv(filename)

grouped = df.groupby(["problem_type", "digit_length"]).agg({"time_seconds": "mean"}).reset_index()

print("\nУсереднені часи виконання:")
print(grouped.to_string(index=False))

plt.figure(figsize=(10, 6))

for problem_type in grouped["problem_type"].unique():
    subset = grouped[grouped["problem_type"] == problem_type]
    label = f"Тип задачі {problem_type}"
    plt.plot(
        subset["digit_length"],
        subset["time_seconds"],
        marker="o",
        label=label
    )

plt.title("Середній час виконання методу перебору залежно від кількості цифр у p")
plt.xlabel("Кількість цифр у p")
plt.ylabel("Середній час виконання (секунди)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("runtime_vs_digits.png")
plt.show()