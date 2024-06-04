
import re
import sys

def block_tri(c1, ground_truth, n):
    cl1 = c1.lower()
    ground_truth_l = ground_truth.lower()
    
    #tri_cl1 = _get_ngrams(n, cl1.split())
    #c1_list = [token.text for token in nlp(c1)]
    tri_cl1 = _get_ngrams(n, cl1.split())
    #trg = [token.text for token in nlp(trg)]
    #ground_truth_l_list = [token.text for token in nlp(trg)]
    tri_ground_truth_l = _get_ngrams(n, ground_truth_l.split())
    overlap = 0
    if len(tri_cl1.intersection(tri_ground_truth_l)) > 0:
        overlap = overlap + 1
    return overlap * 1.0 / len(tri_ground_truth_l) if len(
        tri_ground_truth_l) > 0 else 0.0

def _get_ngrams(n, text):
    """Calcualtes n-grams.
    Args:
      n: which n-grams to calculate
      text: An array of tokens
    Returns:
      A set of n-grams
    """
    ngram_set = set()
    text_length = len(text)
    max_index_ngram_start = text_length - n
    for i in range(max_index_ngram_start + 1):
        ngram_set.add(tuple(text[i:i + n]))
    return ngram_set


def split_src_trg(s):
    s = re.sub("\|","",s)
    src, trg = s.split(" REPHRASESTART ")
    if block_tri(src, trg, 1) > 0.1:
        return src, trg
    else:
        return None,None

if __name__ == '__main__':
    input_file = sys.argv[1]
    lineList = [line.rstrip('\n') for line in open(input_file)]
    result =map(split_src_trg, lineList)    
    data = [(x,y) for x,y in result if x is not None]
    data_src = [x[0] for x in data]
    data_trg = [x[1] for x in data]
    
    source_file = re.sub(r".txt", "_src.txt", input_file)
    target_file = re.sub(r".txt", "_trg.txt", input_file)
    
    with open(source_file, "w") as filehandle:
        for listitem in data_src:
            filehandle.write('%s\n' % listitem)

    with open(target_file, "w") as filehandle:
        for listitem in data_trg:
            filehandle.write('%s\n' % listitem)