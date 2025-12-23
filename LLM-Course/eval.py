import fire
from src.evaluator import evaluate_benchmark

def eval(benchmark="mmmu", model_path="checkpoints/llava-lora", output_dir="output"):
    evaluate_benchmark(benchmark, model_path, output_dir)

if __name__ == "__main__":
    fire.Fire(eval)
