import transformers as tf
tf.__version__
#'3.0.2'

from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
len(tokenizer)                                                                                                                                                                                                                                                                                                                                                                                                           #30522
x = '[AGENTSTART] hello [X_SEP] songsong'  
tokenizer.tokenize(x) 
['[', 'agents', '##tar', '##t', ']', 'hello', '[', 'x', '_', 'sep', ']', 'songs', '##ong']





num_added_toks = tokenizer.add_tokens(['[AGENTSTART]','[X_SEP]']) 
tokenizer.tokenize(x) 
['[agentstart]', 'hello', '[x_sep]', 'songs', '##ong']




tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')                                                                                                                                                                                                                                                                                        
num_added_toks = tokenizer.add_special_tokens({'additional_special_tokens': ['[AGENTSTART]','[X_SEP]']}                        )                                                                                                                                                                                                                                                                                                                                                      
tokenizer.tokenize(x)                                                                                                                                                                                                                                                                                                                                                                                                    
['[AGENTSTART]', 'hello', '[X_SEP]', 'songs', '##ong']



# why this tokenizer can be applied to str of list[str] directly. This is due to there is a __call__ method in the class
# In the __call__, it will call self.encode_plus() method, which further requires `def _encode_plus`
>>> tokenizer(x)
{'input_ids': [101, 1031, 6074, 7559, 2102, 1033, 7592, 1031, 1060, 1035, 19802, 1033, 2774, 5063, 102], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}

