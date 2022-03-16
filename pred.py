import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel , cosine_similarity,cosine_distances
tfid = TfidfVectorizer()
anime = pd.read_csv("anime.csv")
anime.genre.fillna(" ",inplace=True)
vector = tfid.fit_transform(anime.genre)
index = pd.Series(data = anime.index, index = anime.name)
def anime_dundo_bc(name):
    val = index[name]
    dis = linear_kernel(vector[val],vector)
    u = pd.DataFrame(dis)
    u = u.transpose()
    u.columns = ["name"]
    u = u.sort_values(by="name",ascending=False)
    n = []
    g = []
    r = []
    for i in range(0,10):
        n.append(anime.name[u.index[i]])
        g.append(anime.genre[u.index[i]])
        r.append(anime.rating[u.index[i]])
    return n,g,r