import sys


def make_guess(x,y):
    a = int(x)
    b = int(y)
    avg = int((a + b) / 2 )
    return(avg)


def main():
    line = sys.stdin.readline()

    T = int(line)

    while (T > 0):
        line = sys.stdin.readline()
        A,B = line.split(' ')
        min = A
        max = B
        line = sys.stdin.readline()
        N = int(line)
        guess = int(make_guess(min, max))
        sys.stdout.write(str(guess)+'\n')
        sys.stdout.flush()
        while (N > 0):
            line = sys.stdin.readline()
            if str(line) == 'TOO_BIG\n':
                max = guess
                newguess = make_guess(min, max)
                sys.stdout.write(str(newguess)+'\n')
            if line == 'TOO_SMALL\n':
                min = guess
                newguess = make_guess(min, max)
                sys.stdout.write(str(newguess)+'\n')
            if line == 'CORRECT\n':
                N = 1
            if line == 'WRONG_ANSWER\n':
                pass

            guess = newguess
            N = N - 1
            sys.stdout.flush()
        T = T - 1


if __name__ == '__main__':
    main()