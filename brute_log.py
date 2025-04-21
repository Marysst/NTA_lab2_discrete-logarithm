import time
import sys

def brute_force_discrete_log(alpha, beta, p, timeout=300):
    start_time = time.time()
    for x in range(p):
        if pow(alpha, x, p) == beta:
            return x, time.time() - start_time
        if time.time() - start_time > timeout:
            raise TimeoutError("Time limit exceeded ({} seconds)".format(timeout))
    return None, time.time() - start_time

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python brute_log.py <alpha> <beta> <p>")
        sys.exit(1)

    alpha = int(sys.argv[1])
    beta = int(sys.argv[2])
    p = int(sys.argv[3])

    try:
        result, runtime = brute_force_discrete_log(alpha, beta, p)
        if result is not None:
            print(f"Discrete log x such that {alpha}^x ≡ {beta} mod {p} is: {result}")
        else:
            print("No solution found")
        print(f"Time taken: {runtime} seconds")
    except TimeoutError as e:
        print(e)