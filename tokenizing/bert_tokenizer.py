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
