# Tokenizer 
from transformers import T5Tokenizer

# PyTorch model 
from transformers import T5Model, T5ForConditionalGeneration


def summarize(text):
    token_name = 'unicamp-dl/ptt5-base-portuguese-vocab'
    model_name = 'phpaiola/ptt5-base-summ-cstnews'
    
    tokenizer = T5Tokenizer.from_pretrained(token_name )
    model_pt = T5ForConditionalGeneration.from_pretrained(model_name)
    inputs = tokenizer.encode(text, max_length=512, truncation=True, return_tensors='pt')
    
    summary_ids = model_pt.generate(inputs, max_length=512, min_length=256, num_beams=5, no_repeat_ngram_size=3, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0])
    return summary



