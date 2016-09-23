import pandas as pd
import matplotlib.pyplot as plt



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


def plot_type(X, idn=None, col='shape', ax=None):
    """plots a feature vector for the passed rows in X"""
    if ax is not None:
        plt.sca(ax)

    for i in range(X.shape[0]):
        xx = X.iloc[i]
        #print xx
        shp = get_cols(xx, col)
        plt.plot(shp)
    if idn is not None:
        plt.legend(idn)
    
    if ax is not None:
        plt.show()


def plot_types(X, y, l, col):
    """plots a grid of feature vectors with leaves of a type 
    grouped together"""
    
    n = len(l)
    nr = (len(l)/10) + 1
    nc = 10
    if n <=10:
        nc = n
    for i, ll in enumerate(l):
        plt.subplot(nr, nc, i+1)
        xx = X.loc[y == ll]
        plot_type(xx, col=col)

    plt.show()