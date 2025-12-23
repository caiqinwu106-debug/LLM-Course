# MultiModal-Assistant
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Gradio Demo](https://img.shields.io/badge/🤗-Gradio%20Demo-orange)](https://huggingface.co/spaces/YOUR_USERNAME/MultiModal-Assistant)

多模态视觉-语言助手：支持图像/视频输入、图表求解、医疗影像报告生成。

## 一键启动
```bash
pip install -r requirements.txt
python app.py
bash scripts/sft.sh      # LoRA 微调
bash eval/eval_mmmu.sh   # 基准评测

