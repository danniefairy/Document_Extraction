import abc
import nltk.data
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

class DocuemntExtractor(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def _document_segmentation(self):
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
    def run(self):
        return NotImplemented


class BertDocumentExtractor(DocuemntExtractor):
    def __init__(self, document, ratio=0.2, bert_pretrain_model='bert-base-nli-mean-tokens', batch_size=512, nltk_tokenizer='tokenizers/punkt/english.pickle'):
        self._document = document
        self._ratio = ratio
        self._batch_size = batch_size

        self._tokenizer = nltk.data.load(nltk_tokenizer)
        self._model = SentenceTransformer(bert_pretrain_model)
        self._sentences = []
        self._sentence_embeddings = []
        self._labels = []
    
    def _document_segmentation(self):
        self._sentences = self._tokenizer.tokenize(self._document)

    def _sentence_embedding(self):
        self._sentence_embeddings = self._model.encode(self._sentences, self._batch_size)

    def _embedding_clustering(self):
        self._labels = KMeans(n_clusters=int(len(self._sentences)*self._ratio)).fit_predict(np.array(self._sentence_embeddings))

    def _sentence_selection(self):
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
            else:
                n_lines += [label_line[label][0], label_line[label][-1]]

        return [self._sentences[i] for i in sorted(n_lines)]
    
    def run(self):
       self._document_segmentation()
       self._sentence_embedding()
       self._embedding_clustering()
       selected_sentence = self._sentence_selection() 
       return selected_sentence
