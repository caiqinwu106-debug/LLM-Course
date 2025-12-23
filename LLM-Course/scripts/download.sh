#!/usr/bin/env bash
# 下载 LLaVA-1.5-7B 权重（已转 HF 格式）
huggingface-cli download llava-hf/llava-1.5-7b-hf --local-dir ./checkpoints/llava-1.5-7b-hf
