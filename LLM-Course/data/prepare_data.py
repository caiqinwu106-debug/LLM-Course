import os
def main():
    os.makedirs("data/llava", exist_ok=True)
    print("请手动或使用 Huggingface datasets 下载 LLaVA-Instruct-150K、ChartQA 等数据集")
if __name__ == "__main__":
    main()
