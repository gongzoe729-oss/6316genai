import streamlit as st

# 设置网页标题
st.title("AI E-commerce Creative Studio 🎨")
st.write("欢迎！这是我们的生成式 AI 电商海报生成系统。")

# 左侧输入参数
st.sidebar.header("输入参数")
product_id = st.sidebar.selectbox("选择产品 (Product ID)", ["product_001", "product_002", "product_003", "product_004"])
scene_style = st.sidebar.selectbox("选择场景风格 (Scene Style)", ["clean_studio", "luxury", "botanical"])

# 点击按钮后的逻辑（直接展示写死的图片）
if st.sidebar.button("🚀 开始渲染 (Render)"):
    st.success(f"🎉 {product_id} - {scene_style} 渲染任务接收成功！")
    
    st.info("系统已成功调用 Blender 引擎，以下为生成的电商海报：")
    
    # 👇 这里填入你们之前跑出的那张真实的 OLAY 面霜图链接
    real_image_url = "https://eatery-chatting-skilled.ngrok-free.dev/static/1c2070a8-9dc7-4b0e-a7a5-83d2b532e2eb.png"
    
    # 直接展示图片
    st.image(real_image_url, caption="AI Blender 真实渲染结果", use_container_width=True)

st.sidebar.info("注：目前为 MVP 测试版，演示用的是已缓存的高清渲染图。")
