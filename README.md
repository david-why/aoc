# Advent of Code CLI, Library, and Solutions

## CLI Flow

1. Fetch `.in` from AoC servers and generate `.py` file
2. User copies test input to `.test` file
3. User solves part 1
4. User runs program
   1. Run part 1 with input in `.test`
   2. Ask user whether to submit
   3. If yes, submit
5. User solves part 2
6. User runs program
   1. Skip part 1, run part 2 with input in `.test`
   2. Ask user whether to submit
   3. If yes, submit
