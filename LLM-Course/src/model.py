from transformers import AutoModelForVision2Seq, AutoTokenizer
import torch
def load_model_tokenizer(model_name="llava-1.6-7b", load_in_4bit=True):
    tokenizer = AutoTokenizer.from_pretrained("llava-hf/llava-1.5-7b-hf")
    model = AutoModelForVision2Seq.from_pretrained(
    "llava-hf/llava-1.5-7b-hf",
    load_in_4bit=load_in_4bit,
    device_map="auto",
    torch_dtype=torch.float16
    )
    return model, tokenizer
