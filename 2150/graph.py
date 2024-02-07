
class Graph:

    def __init__(self):
        self.matrix = []

    def read_from_file(self, filename):

            f = open(filename, 'r')

            list = []
            for line in f:
                list.append(line.split(' | '))
                for i in list:
                    i[2] = int(i[2])
                list.sort()

            print(list)
            new_list = []
            for i in list:
                if i[0] not in new_list:
                    new_list.append(i[0])
            print(new_list)

            self.matrix = [ [0] * len(new_list) for i in new_list ]

            test = []
            weights = []
            for i in list:
                test.append(i[:2])
                weights.append((i[-1]))

            for i in self.matrix:
                print(i)




if __name__ == '__main__':
    test = Graph()

    print(test.read_from_file('data_small.txt'))

