import streamlit as st
import time

# 设置网页标题
st.title("AI E-commerce Creative Studio 🎨")
st.write("欢迎！这是我们的生成式 AI 电商海报生成系统。")

# 左侧输入参数
st.sidebar.header("输入参数")
product_id = st.sidebar.selectbox(
    "选择产品 (Product ID)", 
    ["product_001", "product_002", "product_003"]
)
scene_style = st.sidebar.selectbox(
    "选择场景风格 (Scene Style)", 
    ["clean_studio", "luxury", "botanical"]
)

# 核心：建立产品和图片的映射字典
IMAGE_DB = {
    "product_001": {
        "clean_studio": "p1_clean.png",
        "luxury": "p1_luxury.png",
        "botanical": "p1_botanical.png"
    },
    "product_002": {
        "clean_studio": "p2_clean.png",
        "luxury": "p2_luxury.png",
        "botanical": "p2_botanical.png"
    },
    "product_003": {
        "clean_studio": "p3_clean.png",
        "luxury": "p3_luxury.png",
        "botanical": "p3_botanical.png"
    }
}

# 点击按钮后的逻辑
if st.sidebar.button("🚀 开始渲染 (Render)"):
    # 模拟一下渲染等待的加载动画
    with st.spinner('正在调用 Blender 引擎渲染中...'):
        time.sleep(1.5) 
    
    st.success(f"🎉 {product_id} - {scene_style} 渲染任务成功！")
    st.info("以下为生成的电商海报：")
    
    # 从字典中获取对应的图片路径
    try:
        image_path = IMAGE_DB[product_id][scene_style]
        # 显示图片
        st.image(image_path, caption=f"AI Blender 真实渲染结果 ({scene_style})", use_container_width=True)
    except Exception as e:
        st.error(f"图片加载失败: {e}")

st.sidebar.info("注：目前为 MVP 测试版，使用真实渲染缓存图进行演示。")
