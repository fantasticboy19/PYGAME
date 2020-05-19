import numpy as np

# assumption : we have a dataset with 2-features and 1 label between 0~1
#
data_set = np.array([[-2, -1, 0], [-1, 2, 1], [-1, -2, 0], [2, -1, 1], [1, 3, 1], [1, -3, 0]])


# in this data_set, third position is the value of label

# step one: perceptron learning algorithm details as depiction below
def perceptron(data_set):
    deconvergence = True

    # initialize the random weight
    np.random.seed(2)
    weight = np.random.random(3)
    # print(type(weight))
    length = len(data_set)

    # running until the deconvergence is False
    while deconvergence:
        count = 0
        # use count to control of out the loop by design
        for meta_data in data_set:
            # print(type(meta_data))
            # updating rules:
            if meta_data[2] == 1 and np.dot(weight, meta_data[:2]) < 0:
                weight = weight + meta_data[:2]
            if meta_data[2] == 0 and np.dot(weight, meta_data[:2]) >= 0:
                weight = weight - meta_data[:2]
            else:
                count += 1
        if count == length:
            deconvergence = False
    return weight


# step two : build a class named Perceptron
# it encompress initialization and train process
# predict function as well
class Perceptron:

    def __init__(self, weight, data_set, deconvergence=None):
        self.weight = weight
        self.data_set = data_set
        self.deconvergence = True
        self.length = data_set.shape[0]

    def train_perceptron(self):
        while self.deconvergence:
            count = 0
            for meta_data in self.data_set:
                # print(type(meta_data))
                if meta_data[2] == 1 and np.dot(self.weight, meta_data[:2]) < 0:
                    self.weight += meta_data[:2]
                if meta_data[2] == 0 and np.dot(self.weight, meta_data[:2]) >= 0:
                    self.weight -= meta_data[:2]
                else:
                    count += 1
            if count == self.length:
                self.deconvergence = False

    def predict(self, test_data):
        result = np.dot(self.weight, test_data)
        if result >= 0:
            return 'positive'
        return 'negative'


if __name__ == '__main__':
    # print(data_set)
    # print(perceptron(data_set))

    # settle the random seed to reproduce
    # and train the Perceptron
    np.random.seed(2)
    weight = np.random.random(2)
    print(f'initial weight is {weight}')
    percep01 = Perceptron(weight, data_set)
    percep01.train_perceptron()
    print('final weight is ', percep01.weight)

    # test the Perceptron
    test_data = np.array([4, 4])
    print(percep01.predict(test_data=test_data))
