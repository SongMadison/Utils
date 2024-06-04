1.  Out of memory error torch
```
2021-12-08T01:25:15.38286282Z Traceback (most recent call last):
2021-12-08T01:25:15.38288332Z   File "/tmp/code/text_gen/examples/seq2seq/finetune.py", line 444, in <module>
2021-12-08T01:25:15.384376734Z     main(args)
2021-12-08T01:25:15.384397034Z   File "/tmp/code/text_gen/examples/seq2seq/finetune.py", line 411, in main
2021-12-08T01:25:15.384476334Z     trainer: pl.Trainer = generic_train(
2021-12-08T01:25:15.384484334Z   File "/tmp/code/text_gen/examples/lightning_base.py", line 389, in generic_train
2021-12-08T01:25:15.384583235Z     trainer.fit(model)
2021-12-08T01:25:15.384590635Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/trainer/trainer.py", line 444, in fit
2021-12-08T01:25:15.384706436Z     results = self.accelerator_backend.train()
2021-12-08T01:25:15.384722137Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/accelerators/ddp_accelerator.py", line 148, in train
2021-12-08T01:25:15.384773937Z     results = self.ddp_train(process_idx=self.task_idx, model=model)
2021-12-08T01:25:15.384780937Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/accelerators/ddp_accelerator.py", line 282, in ddp_train
2021-12-08T01:25:15.384880238Z     results = self.train_or_test()
2021-12-08T01:25:15.384897238Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/accelerators/accelerator.py", line 74, in train_or_test
2021-12-08T01:25:15.384925738Z     results = self.trainer.train()
2021-12-08T01:25:15.384942038Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/trainer/trainer.py", line 466, in train
2021-12-08T01:25:15.385016939Z     self.run_sanity_check(self.get_model())
2021-12-08T01:25:15.385021739Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/trainer/trainer.py", line 658, in run_sanity_check
2021-12-08T01:25:15.38516944Z     _, eval_results = self.run_evaluation(test_mode=False, max_batches=self.num_sanity_val_batches)
2021-12-08T01:25:15.385198741Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/trainer/trainer.py", line 578, in run_evaluation
2021-12-08T01:25:15.385282841Z     output = self.evaluation_loop.evaluation_step(test_mode, batch, batch_idx, dataloader_idx)
2021-12-08T01:25:15.385297442Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/trainer/evaluation_loop.py", line 171, in evaluation_step
2021-12-08T01:25:15.385330242Z     output = self.trainer.accelerator_backend.validation_step(args)
2021-12-08T01:25:15.385335342Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/accelerators/ddp_accelerator.py", line 162, in validation_step
2021-12-08T01:25:15.385392542Z     output = self.training_step(args)
2021-12-08T01:25:15.385397342Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/accelerators/ddp_accelerator.py", line 156, in training_step
2021-12-08T01:25:15.385449243Z     output = self.trainer.model(*args)
2021-12-08T01:25:15.385472143Z   File "/opt/conda/lib/python3.8/site-packages/torch/nn/modules/module.py", line 744, in _call_impl
2021-12-08T01:25:15.385638645Z     result = self.forward(*input, **kwargs)
2021-12-08T01:25:15.385644245Z   File "/tmp/site-packages/lib/python3.8/site-packages/pytorch_lightning/overrides/data_parallel.py", line 182, in forward
2021-12-08T01:25:15.385727345Z     output = self.module.validation_step(*inputs[0], **kwargs[0])
2021-12-08T01:25:15.385732245Z   File "/tmp/code/text_gen/examples/seq2seq/finetune.py", line 183, in validation_step
2021-12-08T01:25:15.385781946Z     return self._generative_step(batch)
2021-12-08T01:25:15.385786746Z   File "/tmp/code/text_gen/examples/seq2seq/finetune.py", line 216, in _generative_step
2021-12-08T01:25:15.385861346Z     generated_ids = self.model.generate(
2021-12-08T01:25:15.385866447Z   File "/opt/conda/lib/python3.8/site-packages/torch/autograd/grad_mode.py", line 26, in decorate_context
2021-12-08T01:25:15.385923447Z     return func(*args, **kwargs)
2021-12-08T01:25:15.385928547Z   File "/tmp/site-packages/lib/python3.8/site-packages/transformers/generation_utils.py", line 576, in generate
2021-12-08T01:25:15.386074448Z     return self.beam_search(
2021-12-08T01:25:15.386079748Z   File "/tmp/site-packages/lib/python3.8/site-packages/transformers/generation_utils.py", line 980, in beam_search
2021-12-08T01:25:15.38624885Z     outputs = self(**model_inputs, return_dict=True)
2021-12-08T01:25:15.38625655Z   File "/opt/conda/lib/python3.8/site-packages/torch/nn/modules/module.py", line 744, in _call_impl
2021-12-08T01:25:15.386384251Z     result = self.forward(*input, **kwargs)
2021-12-08T01:25:15.386392251Z   File "/tmp/site-packages/lib/python3.8/site-packages/transformers/models/bart/modeling_bart.py", line 1035, in forward
2021-12-08T01:25:15.386583253Z     outputs = self.model(
2021-12-08T01:25:15.386590153Z   File "/opt/conda/lib/python3.8/site-packages/torch/nn/modules/module.py", line 744, in _call_impl
2021-12-08T01:25:15.386712454Z     result = self.forward(*input, **kwargs)
2021-12-08T01:25:15.386720554Z   File "/tmp/site-packages/lib/python3.8/site-packages/transformers/models/bart/modeling_bart.py", line 918, in forward
2021-12-08T01:25:15.386880355Z     decoder_outputs = self.decoder(
2021-12-08T01:25:15.386888355Z   File "/opt/conda/lib/python3.8/site-packages/torch/nn/modules/module.py", line 744, in _call_impl
2021-12-08T01:25:15.387031657Z     result = self.forward(*input, **kwargs)
2021-12-08T01:25:15.387042957Z   File "/tmp/site-packages/lib/python3.8/site-packages/transformers/models/bart/modeling_bart.py", line 596, in forward
2021-12-08T01:25:15.387143958Z     x, layer_self_attn, layer_past, layer_cross_attn = decoder_layer(
2021-12-08T01:25:15.387151358Z   File "/opt/conda/lib/python3.8/site-packages/torch/nn/modules/module.py", line 744, in _call_impl
2021-12-08T01:25:15.387275959Z     result = self.forward(*input, **kwargs)
2021-12-08T01:25:15.387283459Z   File "/tmp/site-packages/lib/python3.8/site-packages/transformers/models/bart/modeling_bart.py", line 470, in forward
2021-12-08T01:25:15.38739826Z     x = self.activation_fn(self.fc1(x))
2021-12-08T01:25:15.38740516Z   File "/opt/conda/lib/python3.8/site-packages/torch/nn/modules/module.py", line 744, in _call_impl
2021-12-08T01:25:15.387517261Z     result = self.forward(*input, **kwargs)
2021-12-08T01:25:15.387525661Z   File "/opt/conda/lib/python3.8/site-packages/torch/nn/modules/linear.py", line 94, in forward
2021-12-08T01:25:15.387569261Z     return F.linear(input, self.weight, self.bias)
2021-12-08T01:25:15.387576461Z   File "/opt/conda/lib/python3.8/site-packages/torch/nn/functional.py", line 1667, in linear
2021-12-08T01:25:15.387848564Z     output = input.matmul(weight.t())
2021-12-08T01:25:15.387855564Z RuntimeError: CUDA out of memory. Tried to allocate 20.00 MiB (GPU 4; 31.75 GiB total capacity; 30.29 GiB already allocated; 3.75 MiB free; 30.40 GiB reserved in total by PyTorch)
```
