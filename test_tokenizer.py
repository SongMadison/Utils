
import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
logging.basicConfig(level=logging.INFO)

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-large-cased')

sent = "hi mary"
tokens = tokenizer.tokenize(sent)
tokens_ids = tokenizer.convert_tokens_to_ids(tokens)

print(tokens)
#['hi', 'ma', '##ry']
print(tokens_ids)
#[20844, 12477, 1616]
