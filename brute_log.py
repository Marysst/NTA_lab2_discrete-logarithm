import time

def brute_force_discrete_log(alpha, beta, p, timeout=300):
    start_time = time.time()
    for x in range(p):
        if pow(alpha, x, p) == beta:
            return x
        if time.time() - start_time > timeout:
            raise TimeoutError("Time limit exceeded ({} seconds)".format(timeout))
    return None