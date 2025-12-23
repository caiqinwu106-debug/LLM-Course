import fire
from src.dataset import make_supervised_data_module
from src.model import get_model_and_tokenizer, setup_peft
from transformers import Trainer, TrainingArguments

def train(model_name="llava-1.6-7b", data_path="data/llava_instruct_150k.json",
          lora=True, lora_r=128, output_dir="checkpoints/llava-lora", **kwargs):
    model, tokenizer = get_model_and_tokenizer(model_name)
    if lora:
        model = setup_peft(model, lora_r=lora_r)
    data_module = make_supervised_data_module(tokenizer, data_path)
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        gradient_checkpointing=True,
        fp16=True,
        deepspeed="scripts/zero2.json" if not lora else None,
        **kwargs
    )
    trainer = Trainer(model=model, tokenizer=tokenizer, args=training_args, **data_module)
    trainer.train()
    trainer.save_model()

if __name__ == "__main__":
    fire.Fire(train)
