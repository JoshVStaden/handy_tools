from sklearn.preprocessing import RobustScaler, MinMaxScaler
from sklearn.decomposition import PCA

def preprocess_data(X, opts):
    # TODO: Preprocess your data here. Also use this to determine your best features
    methods=opts.split(',')
    pca_values = None
    for opt in methods:
        if opt == 'robust':
            X = RobustScaler().fit_transform(X)
        elif opt == 'minmax':
            X = MinMaxScaler().fit_transform(X)
        elif opt == 'pca':
            pca = PCA(n_components=15)
            X = pca.fit_transform(X)
            pca_values = (pca.components_, pca.explained_variance_ratio_)
        else:
            print("Unknown Preprocessing Option ", opt)
    return X, pca_values