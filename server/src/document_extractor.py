import abc

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


class BertDocumentExtractor(DocuemntExtractor):
    def __init__(self, document, ratio=0.2, bert_pretrain_model='bert-base-nli-mean-tokens', nltk_tokenizer='tokenizers/punkt/english.pickle'):
        self._document = document
        self._ratio = ratio
        self._bert_pretrain_model = bert_pretrain_model
        self._nltk_tokenizer = nltk_tokenizer
    
    def _document_segmentation(self):
        pass
    def _sentence_embedding(self):
        pass

    def _embedding_clustering(self):
        pass

    def _sentence_selection(self):
        pass
    