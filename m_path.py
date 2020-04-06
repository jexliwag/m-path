import scispacy
import spacy
from spacy import displacy
import en_ner_bc5cdr_md as ner
import os
from os import path
from pathlib import Path


my_path = os.path.abspath(os.path.dirname(__file__))
nlp =  ner.load()
class Text:
    def __init__(self, filename):
        self.doc = nlp(open(os.path.join(my_path, "data\\"+filename), mode="r").read())
    
    def entity_viz(self):
        displacy.render(self.doc, jupyter=True, style='ent')
    
    def get_entities(self):
        return list(self.doc.ents)
    
    def test(self):
        print("This is updated")
        
