
from transformers import BertTokenizer

text ="The only thing  <S_SEP> People are actually buying it ."
print(text)

print("-------------------------")
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

>>> tokenizer.tokenize(text)
['the', 'only', 'thing', '<', 's', '_', 'sep', '>', 'people', 'are', 'actually', 'buying', 'it', '.']



num_new_tokens = tokenizer.add_special_tokens({"sep_token":'<S_SEP>'})
print(num_new_tokens)
>>> print(len(tokenizer))
30523
>>> print(tokenizer.tokenize(text))
['the', 'only', 'thing', '[UNK]', 'people', 'are', 'actually', 'buying', 'it', '.']

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
num_new_tokens = tokenizer.add_tokens(['<S_SEP>'])
print(num_new_tokens)
print(len(tokenizer))
#30523
print(tokenizer.tokenize(text))
#['the', 'only', 'thing', '<s_sep>', 'people', 'are', 'actually', 'buying', 'it', '.']
tokenizer.encode('<S_SEP>')
#[101, 30522, 102]
>>> tokenizer.decode([101,30522,102])
'[CLS] <s_sep> [SEP]'
