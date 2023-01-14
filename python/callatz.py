from functools import lru_cache
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--max-iterations", help="maximum number of cached values", required=False, default=1000, type=int)
    parser.add_argument("-c", "--max-cache", help="maximum number of cached values", required=False, default=512, type=int)
    parser.add_argument("-i", "--cache-info", help="display cache info", required=False, const=True, action='store_const')
    parser.add_argument("-s0", "--start", help="starting number for n", required=True, type=int)
    parser.add_argument("-s1", "--end", help="end number for n", required=True, type=int)
    args = vars(parser.parse_args())

    max_cache_size = args['max_cache']
    MAX_ITERATIONS = args['max_iterations']
    NUM_CACHE_HITS = 0

    @lru_cache(maxsize=max_cache_size)
    def calculate_callatz(n):
        global ITERATION
        global NUM_CACHE_HITS
        if ITERATION > MAX_ITERATIONS: return 0
        if n == 1: return 1
        
        ITERATION += 1
        if n % 2 == 0:
            return calculate_callatz(n / 2)
        else:
            return calculate_callatz(3 * n + 1)

    stats = calculate_callatz.cache_info()
    for n in range(args['start'], args['end'] + 1):
        ITERATION = 0
        if calculate_callatz(n) != 1:
            print("Broke maths! Callatz = " + str(n))

    if args['cache_info']:
        print(calculate_callatz.cache_info())

