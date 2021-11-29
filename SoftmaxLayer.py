import numpy as np


class Softmax:
    def __init__(self, num_beams):
        self.S = []
        self.num_beams = num_beams
        self.den = 0

    def forward(self, inputs, val_mode=False):
        if val_mode:
            S = inputs - np.max(inputs)
            den = sum(np.exp(S))
            P = np.exp(S) / den  # P.shape: (num_beams,)
            return P
        else:
            self.S = inputs - np.max(inputs)
            self.den = sum(np.exp(self.S))
            P = np.exp(self.S) / self.den  # P.shape: (num_beams,)
            return P

    def backward(self, dydx):
        exp_vec = np.mat(np.exp(self.S).reshape([self.num_beams, 1]))
        exp_mat = (-1 / np.power(self.den, 2)) * np.matmul(exp_vec, np.transpose(exp_vec))
        dxdz = (1 / self.den) * np.diag(exp_vec.A1) + exp_mat
        softmax_grad = np.matmul(dydx, dxdz)
        return softmax_grad
