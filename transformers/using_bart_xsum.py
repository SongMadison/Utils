from transformers import BartForConditionalGeneration, BartTokenizer

model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-xsum')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-xsum')

model = BartForConditionalGeneration.from_pretrained('sshleifer/distilbart-xsum-12-3')
tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-xsum-12-3')
ARTICLE_TO_SUMMARIZE = " \"The accident meant the motorway was closed, making travel to Mourneview Park impossible for the team and fans travelling from Belfast, \" said the Irish Football Association . A new date for the match has yet to be confirmed by Uefa . Northern Ireland have three points from their first two Group Six qualifiers."
inputs = tokenizer.batch_encode_plus([ARTICLE_TO_SUMMARIZE], max_length=512, return_tensors='pt')
summary_ids = model.generate(inputs['input_ids'], num_beams=5, max_length=62, min_length=10, early_stopping=True)
print([tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in summary_ids])
