import abc
import nltk.data
import random
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans


class DocuemntExtractor(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def _document_segmentation(self, document):
        return NotImplemented

    @abc.abstractclassmethod
    def _sentence_embedding(self):
        return NotImplemented

    @abc.abstractclassmethod
    def _embedding_clustering(self):
        return NotImplemented

    @abc.abstractclassmethod
    def _sentence_selection(self):
        return NotImplemented

    @abc.abstractclassmethod
    def run(self, document):
        return NotImplemented


class BertDocumentExtractor(DocuemntExtractor):
    def __init__(self, ratio=0.1, bert_pretrain_model='bert-large-nli-stsb-mean-tokens', batch_size=512, nltk_tokenizer='tokenizers/punkt/english.pickle'):
        self._ratio = ratio
        self._batch_size = batch_size

        self._tokenizer = nltk.data.load(nltk_tokenizer)
        self._model = SentenceTransformer(bert_pretrain_model)
        self._sentences = []
        self._sentence_embeddings = []
        self._labels = []

    def _document_segmentation(self, document):
        self._sentences = self._tokenizer.tokenize(document)

    def _sentence_embedding(self):
        # avoid empty input
        if not self._sentences:
            self._sentences = ["EMPTY"]
        self._sentence_embeddings = self._model.encode(self._sentences, self._batch_size)

    def _embedding_clustering(self):
        # avoid short document
        n_cluster = max(int(len(self._sentences)*self._ratio), 1)
        self._labels = KMeans(n_clusters=n_cluster).fit_predict(np.array(self._sentence_embeddings))

    def _sentence_selection(self):
        '''
        Randomly choose two sentences in the same cluster.
        '''
        label_line = {}
        for i in range(len(self._labels)):
            if self._labels[i] not in label_line:
                label_line[self._labels[i]] = [i]
            else:
                label_line[self._labels[i]] += [i]

        n_lines = []
        for label in label_line:
            if len(label_line[label]) == 1:
                n_lines += label_line[label]
            elif len(label_line[label]) == 2:
                n_lines += [label_line[label][0], label_line[label][-1]]
            else:
                idx_mid = random.sample(range(1, len(label_line[label])-1, 1), 1)[0]
                n_lines += [label_line[label][0], label_line[label][idx_mid], label_line[label][-1]]

        return [self._sentences[i] for i in sorted(n_lines)]

    def run(self, document):
        try:
            self._document_segmentation(document)
            self._sentence_embedding()
            self._embedding_clustering()
            selected_sentence = self._sentence_selection() 
            return selected_sentence
        except Exception as e:
            return "Got error: {}".format(e)
            