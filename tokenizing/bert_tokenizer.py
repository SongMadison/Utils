
from transformers import BertTokenizer

text ="The only thing  <S_SEP> People are actually buying it ."
print(text)

print("-------------------------")
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokenizer.add_special_tokens({"sep_token":'<S_SEP>'})
print(len(tokenizer))

print(tokenizer.tokenize(text))


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokenizer.add_tokens(['<S_SEP>'])
print(len(tokenizer))

print(tokenizer.tokenize(text))


#The only thing  <S_SEP> People are actually buying it .
-------------------------
#30523
#['the', 'only', 'thing', '[UNK]', 'people', 'are', 'actually', 'buying', 'it', '.']
#30523
#['the', 'only', 'thing', '<s_sep>', 'people', 'are', 'actually', 'buying', 'it', '.']