import gradio as gr

def echo(img, q):
    print("🔥 回调被触发", img, q)
    if img is None:
        return "请先上传图片"
    return f"收到问题：{q}  图片尺寸：{img.size}"

with gr.Blocks() as demo:
    img = gr.Image(type="pil", label="上传图片")
    q   = gr.Textbox(label="问题")
    btn = gr.Button("Submit")
    out = gr.Textbox(label="回答")
    btn.click(echo, inputs=[img, q], outputs=out)

demo.launch(server_name="0.0.0.0", server_port=7861)   # 换个端口，避免跟你原服务冲突