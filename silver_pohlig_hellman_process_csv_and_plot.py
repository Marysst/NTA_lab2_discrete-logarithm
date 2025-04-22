import pandas as pd
import matplotlib.pyplot as plt

filename = "silver_pohlig_hellman_results.csv"
df = pd.read_csv(filename)

grouped = df.groupby(["problem_type", "order_prime_number"]).agg({"time_seconds": "mean"}).reset_index()

print("\nУсереднені часи виконання:")
print(grouped.to_string(index=False))

plt.figure(figsize=(10, 6))

for problem_type in grouped["problem_type"].unique():
    subset = grouped[grouped["problem_type"] == problem_type]
    label = f"Тип задачі {problem_type}"
    plt.plot(
        subset["order_prime_number"],
        subset["time_seconds"],
        marker="o",
        label=label
    )

plt.title("Середній час виконання алгоритму С-П-Г залежно від порядку простого числа p")
plt.xlabel("Порядок простого числа p")
plt.ylabel("Середній час виконання (секунди)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("silver_pohlig_hellman_runtime_vs_order_prime_number.png")
plt.show()