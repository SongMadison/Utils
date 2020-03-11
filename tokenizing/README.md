## difference between add_tokens vs add_special_tokens
https://huggingface.co/transformers/_modules/transformers/tokenization_utils.html#PreTrainedTokenizer.add_special_tokens

add a dictionary of special tokens (eos, pad, cls…) to the encoder and link them to class attributes. If special tokens are NOT in the vocabulary, they are added to it (indexed starting from the last index of the current vocabulary).

Using add_special_tokens will ensure your special tokens can be used in several ways:

special tokens are carefully handled by the tokenizer (they are never split)

you can easily refer to special tokens using tokenizer class attributes like tokenizer.cls_token. This makes it easy to develop model-agnostic training and fine-tuning scripts.

When possible, special tokens are already registered for provided pretrained models (ex: BertTokenizer cls_token is already registered to be ‘[CLS]’ and XLM’s one is also registered to be ‘</s>’)

```
from transformers import BertTokenizer
#tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('/mnt/d/data/data/csi_data/unilm1.2-base-uncased-vocab.txt')
len(tokenizer)                                                                                                                                                                                                                                                                                                                                                                                                           
30522
x = '[AGENTSTART] hello [X_SEP] songsong'  

num_added_toks = tokenizer.add_tokens(['[AGENTSTART]','[X_SEP]']) 

In [39]: special_tokens_dict = {'additional_special_tokens': ['[AGENTSTART]','[X_SEP]']}                                                                                                                                                                                                                                                                                                                                          

In [40]: num_added_toks = tokenizer.add_special_tokens(special_tokens_dict)                                                                                                                                                                                                                                                                                                                                                       

In [41]: tokenizer.tokenize(x)                                                                                                                                                                                                                                                                                                                                                                                                    
Out[41]: ['[AGENTSTART]', 'hello', '[X_SEP]', 'songs', '##ong']



```
                                                                                                                                                                                                                                                                                                                                                   
