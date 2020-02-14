
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-large-cased')
#tokenizer.add_tokens(['<S_SEP>'])

special_tokens_dict={"sep_token":'<S_SEP>'}
tokenizer.add_special_tokens(special_tokens_dict)

print(len(tokenizer))

def bert_tokenize(text):
    tokens = text.split()
    if tokens[0] == '[CLS]': 
        #already marked
        marked_text = ' '.join(tokens)
    else:
        text += '[CLS] '+text
        text = text.replace("\n", " [SEP] ")
        marked_text = text
    tokenized_text = tokenizer.tokenize(marked_text)
    tokenized_text =' '.join(tokenized_text)
    return tokenized_text


text ="The only thing crazier than a guy in snowbound Massachusetts boxing up the powdery white stuff and offering it for sale online ? <S_SEP> People are actually buying it ."
print(text)

print()

print("bert large cased with special token--------------------------")

print(bert_tokenize(text))

```
The only thing c ##raz ##ier than a guy in snow ##bound Massachusetts boxing up the powder ##y white stuff and offering it for sale online ? <S_SEP> People are actually buying it . [CLS] The only thing c ##raz ##ier than a guy in snow ##bound Massachusetts boxing up the powder ##y white stuff and offering it for sale online ? <S_SEP> People are actually buying it .
````