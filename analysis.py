import pandas as pd


def load_data(n=None):
    fn = 'train.csv'
    dat = pd.read_csv(fn, nrows=n)
    X, y, idn = dat.iloc[:,2:], dat['species'], dat['id']

    return (X, y, idn)


def load_testdata():
    fn = 'test.csv'
    dat = pd.read_csv(fn)
    X, idn = dat.iloc[:,1:], dat['id']

    return (X, idn)


def get_cols(r, col='shape'):
    v = []
    for i in range(1,65):
        v.append(r[col+str(i)])
    return v