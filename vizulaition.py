import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram

def fig_hac(Z, names):
    fig = plt.figure()
    dendrogram(Z, labels=names, leaf_rotation=90)
    plt.tight_layout()
    return fig
