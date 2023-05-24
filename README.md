# FIPS-140 Randomness Test Suite

This Python code implements the FIPS-140 Randomness Test Suite. It includes four tests to evaluate the randomness of a bit sequence: Monobit Test, Longest Run Test, Poker Test, and Runs Test. The code uses the `secrets` and `re` modules to generate random bit sequences and perform the tests.

## Usage

1. Clone the repository or download the code files.
2. Run the `fips_140.py` file using Python (version 3.x).
3. The code will generate a random bit sequence and perform the FIPS-140 tests on it.
4. The test results will be displayed in the console.

## Test Results

The test results will indicate whether the generated bit sequence passes or fails each test. If all four tests pass, the sequence is considered sufficiently random. Otherwise, specific test failures will be reported.

### Monobit Test

The Monobit Test checks if the number of '1's in the sequence falls within an acceptable range. The acceptable range for a 20,000-bit sequence is 9,654 to 10,346.

### Longest Run Test

The Longest Run Test examines the length of the longest run of '0's and '1's in the sequence. The maximum acceptable length for each run is 34.

### Poker Test

The Poker Test splits the sequence into segments and counts the occurrences of each segment. It computes the X3 statistic based on these counts and compares it to an acceptable range (1.03 to 57.4).

### Runs Test

The Runs Test counts the number of runs of each length from 1 to 6 in the sequence and compares them to acceptable ranges specified by FIPS-140. The acceptable ranges are as follows:

- Runs of length 1: 2,267 to 2,733
- Runs of length 2: 1,079 to 1,421
- Runs of length 3: 502 to 748
- Runs of length 4: 223 to 402
- Runs of length 5: 90 to 223
- Runs of length 6 and above: 90 to 223

## To DO:

- fixing Poker Test.
- confirm what Run Test is working properly
