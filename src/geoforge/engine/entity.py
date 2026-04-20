import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None


def extract_entities(text):
    if not nlp:
        return []

    doc = nlp(text)
    return list(set([ent.text for ent in doc.ents]))