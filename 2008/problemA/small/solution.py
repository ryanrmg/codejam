

class Solution:


    def __init__(self):
        self.numbers = []
        self.input = []
        self.totalcases = 0
        self.latestcase = 0
        self.names = []


    def read_text(self):
        try:
            f = open("input.txt", "r")
            for i in f.readlines():
                if self.is_int(i):
                    self.numbers.append(int(i))
                    self.input.append(int(i))
                else:
                    self.names.append(str(i))
                    self.input.append(str(i))
            f.close()
            self.totalcases = self.numbers[0]
        except Exception:
            print("could not read file")


    def is_int(self, input):
        try:
            num = int(input)
        except ValueError:
            return False
        return True


    def count_switches(self):
        engines = self.numbers[self.latestcase]
        queries = self.numbers[self.latestcase]
        for i in range(engines):
            for t in range(queries):
                return


    def find_first_index(self, queries, engines):
        index = []
        num = 0
        i = 0
        while i < len(queries):
            for t in range(len(engines)):
                if str(queries[i]) == str(engines[t]):
                    index.append(t)
                    i+=1
                else:
                    index.append(0)

        print(index)
        for i in range(len(index)):
            if num < index[i]:
                num = index[i]
        return num


def main():
    solve = Solution()
    solve.read_text()
    queries = ["Googol Sweeden", "Googol Norfolk Island"]
    engines = ["Googol Sweden", "Googol Sweden", "Googol Sweden", "Googol Sweden","Googol Sweden"]
    print(solve.find_first_index(queries, engines))
    print(solve.totalcases)
    print(solve.numbers)
    print(solve.names)
    print(solve.input)


if __name__ == "__main__":
        main()


