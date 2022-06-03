from datasets import Summarization
from transformers import pipeline

def associatedLabel (sentence, label_list):
    classifier=pipeline("zero-shot-classification")
    a=classifier(sentence, candidate_labels=label_list)
    return a

def document_summary(text):
    summarizer=pipeline("summarization")
    return summarizer(text)