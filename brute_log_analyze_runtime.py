import time
import sys
import csv
import os

def brute_force_discrete_log(alpha, beta, p, timeout=300):
    start_time = time.time()
    for x in range(p):
        if pow(alpha, x, p) == beta:
            return x, time.time() - start_time
        if time.time() - start_time > timeout:
            raise TimeoutError("Time limit exceeded ({} seconds)".format(timeout))
    return None, time.time() - start_time

def save_to_csv(alpha, beta, p, x, runtime, problem_type, order_prime_number, filename="brute_log_results.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "problem_type", "order_prime_number", "alpha", "beta",
                "p", "result_x", "time_seconds"
            ])
        writer.writerow([
            problem_type, order_prime_number, alpha, beta,
            p, x if x is not None else "timeout", runtime
        ])

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python brute_logger.py <problem_type> <order_prime_number> <alpha> <beta> <p>")
        sys.exit(1)

    problem_type = int(sys.argv[1])
    order_prime_number = int(sys.argv[2])
    alpha = int(sys.argv[3])
    beta = int(sys.argv[4])
    p = int(sys.argv[5])

    try:
        result, runtime = brute_force_discrete_log(alpha, beta, p)
        if result is not None:
            print(f"Discrete log x such that {alpha}^x ≡ {beta} mod {p} is: {result}")
        else:
            print("No solution found")
        print(f"Time taken: {runtime} seconds")
        save_to_csv(alpha, beta, p, result, runtime, problem_type, order_prime_number)
    except TimeoutError as e:
        print(e)
        save_to_csv(alpha, beta, p, None, 300.0, problem_type, order_prime_number)