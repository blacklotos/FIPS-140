import secrets
import re

def generate_random_sequence():
    return secrets.token_bytes(2500)

def monobit_test(bits):
    count = sum(bin(byte).count('1') for byte in bits)
    print(f'Monobit test: count is {count}, acceptable range is 9654 to 10346, test {"passed" if 9654 <= count <= 10346 else "failed"}')
    return 9654 <= count <= 10346

def longest_run_test(bits):
    max_run_length = max(len(run) for run in ''.join(bin(byte)[2:].zfill(8) for byte in bits).split('0') + ''.join(bin(byte)[2:].zfill(8) for byte in bits).split('1'))
    return max_run_length <= 34  # Прийнятний діапазон для 20000 бітів

def poker_test(bits):
    frequencies = [0]*16
    for i in range(0, 20000, 4):
        nibble = bits[i//8] >> (i%8) & 0xF
        frequencies[nibble] += 1
    chi_squared = 16/5000 * sum(f**2 for f in frequencies) - 5000
    return 1.03 < chi_squared < 57.4

def runs_test(bits):
    bit_string = ''.join(format(byte, '08b') for byte in bits)
    run_lengths = [len(run) for run in re.findall(r'1+|0+', bit_string)]
    acceptable_runs = [(2267, 2733), (1079, 1421), (502, 748), (223, 402), (90, 223), (90, 223)]
    results = [lower <= run_lengths.count(n) <= upper for n, (lower, upper) in enumerate(acceptable_runs, 1)]
    for n, (lower, upper), result in zip(range(1, 7), acceptable_runs, results):
        print(f'Runs of length {n}: count is {run_lengths.count(n)}, acceptable range is {lower} to {upper}, test {"passed" if result else "failed"}')
    return all(results)

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

for test_name, result in test_results.items():
    print(f'{test_name}: {"Passed" if result else "Failed"}')

if all(test_results.values()):
    print("All tests passed, the 20000 bits sequence is random.")
else:
    print("The 20000 bits sequence is not random.")

