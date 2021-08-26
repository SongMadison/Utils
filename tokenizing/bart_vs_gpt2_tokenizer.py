import transformers
print(transformers.__version__) #4.1.0
from transformers import GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
bart_tokenizer= BartTokenizer.from_pretrained("facebook/bart-large")
tokenizer.tokenize('hello</s>world'), bart_tokenizer.tokenize('hello</s>world')
#(['hello', '</', 's', '>', 'world'], ['hello', '</s>', 'world'])
tokenizer.special_tokens_map

{'bos_token': '<|endoftext|>',
 'eos_token': '<|endoftext|>',
 'unk_token': '<|endoftext|>'}


bart_tokenizer.special_tokens_map
{'bos_token': '<s>',
 'eos_token': '</s>',
 'unk_token': '<unk>',
 'sep_token': '</s>',
 'pad_token': '<pad>',
 'cls_token': '<s>',
 'mask_token': '<mask>'}

 len(bart_tokenizer), len(tokenizer)
 #(50265, 50257)

# Difference summarized below: 
# BART added 8 extra tokens:
# 3 madeup words: # "madeupword0000": 50261, "madeupword0001": 50262, "madeupword0002": 50263, 
# 5 extra special tokens, <s?, </s>, <mask>, <unk>, <pad>
# https://huggingface.co/facebook/bart-base/raw/main/vocab.json
# https://huggingface.co/gpt2-medium/raw/main/vocab.json