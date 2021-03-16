"""
Cluster the colors of an image
"""
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

# put your own image here
INPUT_FILE = "asohka.png"
OUTPUT_FILE = "output.png"
N_SAMPLES = 100  # number of random pixels used for clustering


def cluster_transform(X, ncols):
    """cluster the colors of an image"""
    m = KMeans(ncols)
    indices = np.random.randint(0, X.shape[0]-1, size=N_SAMPLES)
    Xtrain = X[indices]
    m.fit(Xtrain)
    clusters = m.predict(X)
    c = [m.cluster_centers_[i] for i in clusters]
    print("\n", ncols)
    cols = m.cluster_centers_.round().astype(int)
    cols = [tuple(c) for c in cols]
    print(cols)
    return np.array(c)


for anzahl_farben in range(4, 30):
    im = Image.open(INPUT_FILE)
    im = im.convert('RGB')

    a = np.array(im)
    a = a.reshape((a.shape[0] * a.shape[1], 3))
    c = cluster_transform(a, anzahl_farben)

    c = c.reshape(im.size[1], im.size[0], 3)
    im = Image.fromarray(c.astype(np.uint8), 'RGB')
    im.save(f"farben{anzahl_farben}.png")
