import json
from sklearn.metrics import confusion_matrix
import fire

def get_fpr_fnr_scores(y_ref, y_pred):
  tn, fp, fn, tp = confusion_matrix(y_ref, y_pred).ravel()
  return {"BAcc":0.5*(tp/(tp+fp) + tn/(tn+fn)), "FPR": fp/(fp+tp), "FNR": fn/(fn+tn), "ACC": (tn+tp)/(tn+fp+fn+tp)}

def run_eval(input_file, pred_file, output_file = None):
  if output_file is None:
    output_file = pred_file + '.metrics.json'
  with open(input_file) as f_in:
    input_data = [json.loads(l) for l in f_in]
    ref_labels = [1 if ex['label'] == 'Hallucinated' else 0 for ex in input_data]
  with open(pred_file) as f_in:
    preds_data = [json.loads(l) for l in f_in]
    pred_labels = [ex['prediction'] for ex in preds_data]
  scores = get_fpr_fnr_scores(pred_labels, ref_labels)
  with open(output_file, 'w') as f_out:
    json.dump(scores, f_out)

if __name__ == "__main__":
  fire.Fire(run_eval)
