class Solution:
    def __init__(self):
        self.list = []


    def read_text(self):
        try:
            f = open('input.txt', 'r')
            for i in f.readlines():
                self.list.append(i)
            f.close()

        except Exception:
            print('could not read file')



def main():
    solution = Solution()
    solution.read_text()
    print(solution.list)


if __name__ == "__main__":
    main()
