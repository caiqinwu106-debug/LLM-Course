import gradio as gr
from src.model import load_model_tokenizer
from src.utils import extract_video_frames

from PIL import Image
model, tokenizer = load_model_tokenizer("llava-1.6-7b", load_in_4bit=True)

image_list = [Image.open(r"D:\LLM-Course\examples\demo.jpg")]# ← 这里定义
text = "Describe this image in Chinese."
prompt = "<image>" * len(image_list) + text
def multimodal_chat(image_list, video, text):
    # 1. 视频优先
    if video is not None:
        image_list = extract_video_frames(video, num_frames=8)

    # 2. 必须有图
    if not image_list:
        return "请至少上传一张图像或视频！"

    # 3. 构造 prompt
    prompt = "<image>" * len(image_list) + text

    # 4. ===== 先硬编码返回，验证通路 =====
    return f"收到 {len(image_list)} 张图，问题：{text}，prompt 已构造：{prompt[:80]}..."

    # 5. ===== 后面再换成真实推理 =====
    # inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    # with torch.no_grad():
    #     out = model.generate(**inputs, max_new_tokens=128)
    # return tokenizer.decode(out[0], skip_special_tokens=True)
prompt = "<image>" * len(image_list) + text
demo = gr.Interface(
fn=multimodal_chat,
inputs=[gr.Gallery(label="多图"), gr.Video(label="视频"), gr.Textbox(label="问题")],
outputs=gr.Textbox(label="回答"),
title="多模态视觉-语言助手",
examples=[[["examples/demo.jpg"], None, "这张图里有什么异常？"]]
)
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
