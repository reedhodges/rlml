# class to implement gradient descent for linear regression
class grad_desc_LR:
    def __init__(self, x, y, m_init, b_init, alpha, num_iter):
        self.x = x                
        self.y = y
        self.m_init = m_init          # initial slope
        self.b_init = b_init          # initial intercept
        self.alpha = alpha          # learning rate
        self.num_iter = num_iter    # number of iterations

    def slopeintercept(self):
        m = self.m_init
        b = self.b_init
        for i in range(self.num_iter):
            sum_m = sum([self.x[j] * (m * self.x[j] + b - self.y[j]) for j in range(len(self.x))])
            sum_b = sum([m * self.x[j] + b - self.y[j] for j in range(len(self.x))])
            m = m - (self.alpha * sum_m) / len(self.x)
            b = b - (self.alpha * sum_b) / len(self.x)
        return [m, b]