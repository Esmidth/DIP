import json

min_wdw_sz = [100, 40]
step_size = [10, 10]
orientations = 9
pixels_per_cell = [8, 8]
cells_per_block = [3, 3]
visualize = False
normalize = True

threshold = .3
pos_feat_ph = '../data/features/pos'
neg_feat_ph = '../data/features/neg'
model_path = '../data/models/svm.model'
