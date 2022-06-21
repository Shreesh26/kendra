from datasets import Summarization
from transformers import pipeline
from transformers import AutoTokenizer

def associatedLabel (sentence, label_list):
    classifier=pipeline("zero-shot-classification")
    a=classifier(sentence, candidate_labels=label_list)
    return a

def document_summary(text):
    summarizer=pipeline("summarization")
    return summarizer(text)

def document_encoder(text):
    checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    raw_input=[text]
    inputs = tokenizer(raw_input, padding=True, truncation=True, return_tensors="tf")
    return inputs