import pickle

path_train = 'data/birds/train/304images.pickle'
tiny_path_train = 'data/birds/train/tiny.pickle'
path_test = 'data/birds/test/304images.pickle'
tiny_path_test = 'data/birds/test/304images.pickle'

# subset training data
with open(path_train, 'rb') as f:
    data_train = pickle.load(f)
f.close()

small_data_train = data_train[0:50]

with open(tiny_path_train, 'wb') as out:
    pickle.dump(small_data_train, out)
out.close()

# subset test data
with open(path_test, 'rb') as f:
    data_test = pickle.load(f)
f.close()

small_data_test = data_test[0:50]

with open(tiny_path_train, 'wb') as out:
    pickle.dump(small_data_test, out)
out.close()