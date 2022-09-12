from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format("frWac_non_lem_no_postag_no_phrase_200_cbow_cut100.bin", binary=True, unicode_errors="ignore")

liste = model.most_similar("particulier", topn=20)
for element in liste:
    print(element)