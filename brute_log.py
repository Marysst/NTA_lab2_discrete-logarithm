import time
import sys

def brute_force_discrete_log(alpha, beta, p, timeout=300):
    start_time = time.time()
    for x in range(p):
        if pow(alpha, x, p) == beta:
            return x
        if time.time() - start_time > timeout:
            raise TimeoutError("Time limit exceeded ({} seconds)".format(timeout))
    return None

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python brute_log.py <alpha> <beta> <p>")
        sys.exit(1)

    alpha = int(sys.argv[1])
    beta = int(sys.argv[2])
    p = int(sys.argv[3])

    try:
        result = brute_force_discrete_log(alpha, beta, p)
        if result is not None:
            print(f"Discrete log x such that {alpha}^x ≡ {beta} mod {p} is: {result}")
        else:
            print("No solution found")
    except TimeoutError as e:
        print(e)