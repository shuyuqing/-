import numpy as np
import os

pred = [0.49393064, 0.5021272,  0.49225777, 0.4967099,  0.49660096, 0.49781743]
pred = np.array(pred)
posterior_thresh = 0.5

pred_thresh = pred > posterior_thresh

print(pred_thresh)