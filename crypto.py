from itertools import permutations
def solve_cryptoarithmatic(puzzle):
    words = puzzle.split()
    unique_letters = set(''.join(words))
    digit_permutations = permutations('0123456789', len(unique_letters))
    for perm in digit_permutations:
        letter_to_digit = dict(zip(unique_letters, perm))
        digit_words = [''.join(letter_to_digit[letter] for letter in word) for word in words]
        if sum(int(num) for num in digit_words[:-1]) == int(digit_words[-1]):
            return letter_to_digit
    return None

if __name__ == '__main__':
    puzzle = input('Enter the cryptoarithmetic puzzle in the format word1 + word2 = word3: ')
    solution = solve_cryptoarithmatic(puzzle)

    if solution:
        print('Solution found')
        for letter, digit in solution.items():
            print(f'{letter} = {digit}')
    else:
        print('No solution found')