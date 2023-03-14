import os
import re
import argparse
from collections import OrderedDict,defaultdict
import torch
from ZCodePP.apps.tasks.seq2seq_tasks import MultiSumTask
from ZCodePP.utils import get_logger
from ZCodePP.deberta import tokenizers, load_vocab
from ZCodePP.deberta import load_model_config
from ZCodePP.data import ExampleInstance
from ZCodePP.apps.models import BeamSearch, GreedySearch

logger = get_logger()

class SummarizationTask(MultiSumTask):
    def __init__(self, data_dir, tokenizer, model_config, **kwargs):
        super().__init__(data_dir, tokenizer, model_config, **kwargs)
        logger.info("Task is initialized...")
        print(self.args)

    def init_model(self):
        model = self.get_model(self.args)
        if not self.args.cpu:
          if self.args.gpu_id>=0:
            device = torch.device('cuda:'+str(self.args.gpu_id))
          else:
            device = torch.device('cpu')
            self.args.fp16=False
        else:
          device = torch.device('cpu')
          self.args.fp16=False
        model = model.to(device)
        model.eval()
        self.model = model
        self.device = device
        if getattr(self, 'zcodepp_score_task', None) is not None:
          self.zcodepp_score_model = self.zcodepp_score_model.to(device)
          self.zcodepp_score_model.eval()

        logger.info("model is initialized.")
        return None

def build_argument_parser():
    parser = argparse.ArgumentParser()
    ## Required parameters
    parser.add_argument("--task_dir",
              default=None,
              type=str,
              required=False,
              help="The directory to load customized tasks.")
    #   parser.add_argument("--task_name",
    #             default=None,
    #             type=str,
    #             action=LoadTaskAction,
    #             required=True,
    #             help="The name of the task to train. To list all registered tasks, use \"*\" as the name, e.g. \n"
    #             "\npython -m ZCodePP.apps.run --task_name \"*\" --help")
    parser.add_argument("--data_dir",
              default=None,
              type=str,
              required=False,
              help="The input data dir. Should contain the .tsv files (or other data files) for the task.")
    parser.add_argument("--output_dir",
              default=None,
              type=str,
              required=True,
              help="The output directory where the model checkpoints will be written.")

    ## Other parameters
    parser.add_argument("--max_seq_length",
              default=128,
              type=int,
              help="The maximum total input sequence length after WordPiece tokenization. \n"
                "Sequences longer than this will be truncated, and sequences shorter \n"
                "than this will be padded.")
    parser.add_argument("--do_train",
              default=False,
              action='store_true',
              help="Whether to run training.")
    parser.add_argument("--do_eval",
              default=False,
              action='store_true',
              help="Whether to run eval on the dev set.")
    parser.add_argument("--do_predict",
              default=False,
              action='store_true',
              help="Whether to run prediction on the test set.")
    parser.add_argument("--do_interactive",
              default=False,
              action='store_true',
              help="Whether to run the model interactively via commandline.")
    parser.add_argument('--do_onnx_export',
              default=False,
              action='store_true',
              help="Whether to export model to ONNX format.")
    parser.add_argument("--eval_batch_size",
              default=32,
              type=int,
              help="Total batch size for eval.")
    parser.add_argument("--predict_batch_size",
              default=32,
              type=int,
              help="Total batch size for prediction.")
    parser.add_argument('--init_model',
              type=str,
              help="The model state file used to initialize the model weights.")
    parser.add_argument('--model_config',
              type=str,
              help="The config file of bert model.")
    parser.add_argument('--cls_drop_out',
              type=float,
              default=None,
              help="The config file model initialization and fine tuning.")
    parser.add_argument('--tag',
              type=str,
              default='final',
              help="The tag name of current prediction/runs.")
    parser.add_argument('--debug',
              default=False,
              type=bool,
              help="Whether to cache cooked binary features")
    parser.add_argument('--pre_trained',
              default=None,
              type=str,
              help="The path of pre-trained RoBERTa model")
    parser.add_argument('--vocab_type',
              default=None,
              type=str,
              help="Vocabulary type: [spm, gpt2]")
    parser.add_argument('--vocab_path',
              default=None,
              type=str,
              help="The path of the vocabulary")
    parser.add_argument('--vat_lambda',
              default=0,
              type=float,
              help="The weight of adversarial training loss.")
    parser.add_argument('--vat_learning_rate',
              default=1e-4,
              type=float,
              help="The learning rate used to update pertubation")
    parser.add_argument('--vat_init_perturbation',
              default=1e-2,
              type=float,
              help="The initialization for pertubation")
    parser.add_argument('--vat_loss_fn',
              default="symmetric-kl",
              type=str,
              help="The loss function used to calculate adversarial loss. It can be one of symmetric-kl, kl or mse.")
    parser.add_argument('--cpu',
              default=False,
              type=bool,
              help="If use CPU only.")
    parser.add_argument('--gpu_id',
            default=0,
            type=int,
            help="gpu id to be used.")
    parser.add_argument('--onnx',
              default=False,
              type=bool,
              help="If the model is onnx mode or pytorch model.") 
    parser.add_argument('--fp16',
              default=False,
              type=bool,
              help="If the model is fp16.")
    parser.add_argument('--arg_config', default=None, type=str, help='Specify the parameter overwirte config_file.')   
    parser.add_argument("--seed", default=1234, type=int, help="seed")
    parser.add_argument("--task_name", default="multisum", type=str, help="task name")
    return parser

init_model="./docsum_0.32-lengthv2-stage3-azure-delta/pytorch.model-020000.bin"

vocab_path = os.path.dirname(init_model)+"/spm.model"
model_config = os.path.dirname(init_model)+"/model_config.json"
max_seq_len=4608
max_tgt_len=256

argv = f"""
--tag zcodepp
--fp16 True
--task_dir .
--task_name multisum
--init_model {init_model}
--vocab_path {vocab_path}
--model_config {model_config}
--vocab_type spm
--beam_size 4
--ngram_block 3
--length_penalty 1
--length_control_as_prefix true
--apply_prefix_to_target true
--max_prefix_len 5
--forbid_ignore_words .
--block_repeated_ngrams 3
--output_dir /tmp/models/docsum_v0.6
--max_seq_len {max_seq_len}
--max_tgt_len {max_tgt_len}
--seed 1234
""".split()

parser = build_argument_parser()
#parser = add_arguments(parser)
SummarizationTask.add_arguments(parser)
args, other = parser.parse_known_args(argv)

print(args)
print(other)
data_dir = args.data_dir
delattr(args, 'data_dir')
vocab_path, vocab_type = load_vocab(vocab_path = args.vocab_path, vocab_type = args.vocab_type, pretrained_id = args.init_model)
tokenizer = tokenizers[vocab_type](vocab_path)
model_config_obj = load_model_config(args.init_model)
my_task = SummarizationTask(data_dir= data_dir, tokenizer=tokenizer, model_config=model_config_obj, args= args)
my_task.init_model()