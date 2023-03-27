import numpy as np
import sys


# for one-hot vector label only
class CrossEntroy:
    def __init__(self, batch_size):
        self.prob = np.array([])
        self.label = np.array([])
        self.loss = 0
        self.batch_size = batch_size
        self.count = 0
        self.count_val = 0
        self.loss_val = 0
        self.val_first = True

    def forward(self, prob, label, val_mode=False, val_size=100):
        # 验证集
        if val_mode:
            if self.val_first:
                self.count_val = 0
                self.loss_val = 0
                self.val_first = False
            prob = prob.reshape((1, prob.size))
            label = label.reshape((1, label.size))
            pos_label = label.argmax()
            pos_prob = prob.argmax()
            if pos_label != pos_prob:
                print('Inconsistent maximal position!')
                sys.exit()
            if self.count_val < val_size:
                self.loss_val = self.loss_val - np.log(prob[0, pos_prob])  # np.log is natural logarithm
                self.count_val += 1
                if self.count_val == val_size:
                    self.loss_val = (1 / val_size) * self.loss_val
                    self.val_first = True
        # 测试集
        else:
            self.prob = prob.reshape((1, prob.size))
            self.label = label.reshape((1, label.size))
            pos_label = self.label.argmax()
            pos_prob = self.prob.argmax()
            if pos_label != pos_prob:
                print('Inconsistent maximal position!')
                sys.exit()
            if self.count < self.batch_size:
                self.loss = self.loss - np.log(self.prob[0, pos_prob])  # np.log is natural logarithm
                self.count += 1
                if self.count == self.batch_size:
                    self.loss = (1 / self.batch_size) * self.loss
            else:
                self.count = 0
                self.loss = 0
                self.loss = self.loss - np.log(self.prob[0, pos_prob])
                self.count += 1

    def backward(self):
        pos = self.label.argmax()
        grad = -1 / self.prob[0, pos]
        dydx = np.zeros([1, self.label.size])
        dydx[0, pos] = grad
        return dydx  # dydx.shape: (1, num_beams)
