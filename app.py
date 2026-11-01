# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import requests

# 1. 设置网页标题和说明
st.title("AI E-commerce Creative Studio 🎨")
st.write("欢迎！这是我们的生成式 AI 电商海报生成系统。")

# 2. 设置左侧边栏 (Sidebar)
st.sidebar.header("输入参数")

# 下拉菜单选择产品 ID
product_id = st.sidebar.selectbox(
    "选择产品 (Product ID)", 
    ["product_001", "product_002", "product_003", "product_004"]
)

# 下拉菜单选择场景风格
scene_style = st.sidebar.selectbox(
    "选择场景风格 (Scene Style)", 
    ["clean_studio", "luxury", "botanical"]
)

# 3. 渲染按钮
if st.sidebar.button("🚀 开始渲染 (Render)"):
    st.write(f"正在为 {product_id} 生成 {scene_style} 风格的海报，请稍候...")
    
    # 公网 API 地址
    api_url = "https://lapped-detergent-cytoplasm.ngrok-free.dev/render-test"
    
    payload = {
    "product_id": product_id,
    "scene_style": scene_style,
    "background": "white",
    "aspect_ratio": "1:1"
}
    
    try:
        # 发送请求给后端
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            st.success("🎉 渲染任务接收成功！")
            
            # 这里填入你拿到的真实图片链接
            real_image_url = "https://eatery-chatting-skilled.ngrok-free.dev/static/1c2070a8-9dc7-4b0e-a7a5-83d2b532e2eb.png"
            
            # 如果后端返回了图片链接，就用后端的；如果没有，就用上面这个写死的链接
            if "image_url" in data:
                real_image_url = data["image_url"]
            
            st.info("系统已成功调用 Blender 引擎，以下为生成的电商海报：")
            
            # 带着请求头去获取图片数据（破解 ngrok 的拦截）
            img_headers = {"ngrok-skip-browser-warning": "true"}
            try:
                img_response = requests.get(real_image_url, headers=img_headers, timeout=10)
                if img_response.status_code == 200:
                    st.image(img_response.content, caption="AI Blender 真实渲染结果")
                else:
                    st.error(f"图片加载失败，状态码: {img_response.status_code}")
            except Exception as e:
                st.error(f"图片加载出错: {e}")

            with st.expander("点击查看后端返回的详细数据"):
                st.json(data) 
        else:
            st.error(f"请求失败，状态码: {response.status_code}")
            
    except Exception as e:
        st.error(f"连不上后端服务器: {e}。请检查网络或 API 链接是否有效。")

# 底部放一个提示
st.sidebar.info("注：目前为 MVP（最小可行性产品）测试版，请耐心等待。")
