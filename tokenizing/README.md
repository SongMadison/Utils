## difference between add_tokens vs add_special_tokens
https://huggingface.co/transformers/_modules/transformers/tokenization_utils.html#PreTrainedTokenizer.add_special_tokens

add a dictionary of special tokens (eos, pad, cls…) to the encoder and link them to class attributes. If special tokens are NOT in the vocabulary, they are added to it (indexed starting from the last index of the current vocabulary).

Using add_special_tokens will ensure your special tokens can be used in several ways:

special tokens are carefully handled by the tokenizer (they are never split, usually not lower-cased), refer to

https://github.com/huggingface/transformers/blob/08f534d2da47875a4b7eb1c125cfa7f0f3b79642/src/transformers/tokenization_utils_base.py#L795

### here special case will not be lower cased. 
https://github.com/huggingface/transformers/blob/08f534d2da47875a4b7eb1c125cfa7f0f3b79642/src/transformers/tokenization_utils_base.py#L728

```
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

```
                                                                                                                                                                                                                                                                                                                                                   
