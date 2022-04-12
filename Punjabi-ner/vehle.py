import spacy
from spacy.training import Example
from spacy.ml.models.parser import build_tb_parser_model


# model = build_tb_parser_model()


nlp = spacy.blank('en')
nlp.add_pipe('ner')
losses = {}
optimizer = nlp.begin_training()
text = "Facebook released React in 2014"
annotations = {"entities": ["U-ORG", "O", "U-TECHNOLOGY", "O", "U-DATE"]}
doc = nlp.make_doc(text)
example = Example.from_dict(doc, annotations)
nlp.update([example],  # batch of annotations
          drop=0.2,  # dropout - make it harder to memorise data
          losses=losses,
          sgd=optimizer)