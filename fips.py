import secrets
import re

def generate_random_sequence():
    # Generate 20000 random bits (2500 bytes)
    return secrets.token_bytes(2500)

def monobit_test(bits):
    # Count the number of '1's in the sequence
    count = sum(bin(byte).count('1') for byte in bits)

    # Check if the number of '1's falls within the acceptable range
    print(f'Monobit test: count is {count}, acceptable range is 9654 to 10346, test {"passed" if 9654 <= count <= 10346 else "failed"}')
    return 9654 <= count <= 10346

def longest_run_test(bits):

    bit_string = ''.join(f'{byte:08b}' for byte in bits)

    # Find the length of the longest run of '0's and '1's
    longest_zero_run = max(len(run) for run in re.findall(r'0+', bit_string))
    longest_one_run = max(len(run) for run in re.findall(r'1+', bit_string))

    print(f'Longest run of zeros: length is {longest_zero_run}, maximum acceptable length is 34, test {"passed" if longest_zero_run <= 34 else "failed"}')
    print(f'Longest run of ones: length is {longest_one_run}, maximum acceptable length is 34, test {"passed" if longest_one_run <= 34 else "failed"}')
    
    return longest_zero_run <= 34 and longest_one_run <= 34

# Here I have problem with implementing a formula from task, so probably it not fully work.
def poker_test(bits):
    bit_string = ''.join(f'{byte:08b}' for byte in bits)

    # Split the binary string into segments of length m (in this case, 4)
    m = 4
    k = len(bit_string) // m
    bit_segments = [bit_string[i * m : (i + 1) * m] for i in range(k)]

    # Count the number of occurrences of each possible segment
    counts = {f'{i:04b}': 0 for i in range(2**m)}
    for segment in bit_segments:
        counts[segment] += 1

    x3 = (16 / k) * sum(count**2 for count in counts.values()) - k
    print(f'Poker test: X3 is {x3}, acceptable range is 1.03 to 57.4, test {"passed" if 1.03 <= x3 <= 57.4 else "failed"}')

    return 1.03 <= x3 <= 57.4

# Have problome with it I was not able to get truly rundomize, if I reduce number bits I will pass the test.
def runs_test(bits):
    bit_string = ''.join(f'{byte:08b}' for byte in bits)
    
    # Count the number of runs of each length from 1 to 6 (counting runs of length greater than 6 as 6)
    run_lengths = [len(run) for run in re.findall(r'1+|0+', bit_string)]
    counts = {i: run_lengths.count(i) for i in range(1, 7)}
    counts[6] += sum(run_lengths.count(i) for i in range(7, len(run_lengths) + 1))

    limits = {
        1: (2267, 2733),
        2: (1079, 1421),
        3: (502, 748),
        4: (223, 402),
        5: (90, 223),
        6: (90, 223),
    }

    # Check if the counts of each run length are within the acceptable intervals
    passed = True
    for run_length, (lower, upper) in limits.items():
        count = counts.get(run_length, 0)
        if not lower <= count <= upper:
            print(f'Runs of length {run_length}: count is {count}, acceptable range is {lower} to {upper}, test failed')
            passed = False
        else:
            print(f'Runs of length {run_length}: count is {count}, acceptable range is {lower} to {upper}, test passed')
    return passed


def fips_140(bits):
    test_results = {
        'Monobit test': monobit_test(bits),
        'Longest run test': longest_run_test(bits),
        'Poker test': poker_test(bits),
        'Runs test': runs_test(bits)
    }
    return test_results

bits = generate_random_sequence()
test_results = fips_140(bits)
