import streamlit as st
try:
    import numpy as np
    import cv2
    from ultralytics import YOLO
    from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
    import av
    from PIL import Image
    import gdown
    import os
    import tempfile
    from roboflow import Roboflow

except ImportError as e:
    st.error(f"Error importing modules: {e}")

st.markdown("""
    <style>
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        text-align: center;
        height: 220px; /* Ensure all cards have the same height */
    }
    .card-title {
        font-size: 1.5em;
        margin-bottom: 10px;
        color: black;
    }
    .card-image {
        width: 80%;
        height: 120px; /* Set a fixed height for the images */
        object-fit: cover; /* Ensure images cover the specified dimensions */
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to create a card
def create_card(title, image_url):
    card_html = f"""
    <div class="card">
        <img class="card-image" src="{image_url}" alt="{title}">
        <div class="card-title">{title}</div>
    </div>
    """
    return card_html

# Cache the model loading
@st.cache_resource
def load_model():
    try:
        rf = Roboflow(api_key="57PpPkDFRE85XbGnyfg4")
        project = rf.workspace().project("tesis-vy7o6")
        model = project.version(4).model
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

classes = [
    'halls',
    'heineken',
    'incakola',
    'lays',
    'monster',
    'oreo',
    'redbull',
    'snickers',
    'sprite',
    'trident',
]

detected_classes = set()
detected_classes_set = set()

def get_class_html(cls, detected_classes):
    detected_style = 'background-color:#FF4B4B;padding:4px 4px;border-radius:5px;margin:2px; display:inline-block; color:white;'
    default_style = 'padding:4px 4px;border-radius:5px;margin:2px; display:inline-block; background-color:white; color:black;'
    
    style = detected_style if cls in detected_classes else default_style
    return f'<span style="{style}">{cls}</span>'

def main():

    st.title("Detección de Objetos")
    activiteis = ["Principal", "Subir imagen"]
    choice = st.sidebar.selectbox("Selecciona actividad", activiteis)
    st.sidebar.markdown('---')

    if choice == "Principal":
        html_temp_home1 = """<div style="padding:10px">
                                            <h4 style="color:white;text-align:left;">
                                            Aplicación web de detección del curso de TP1 usando Yolov9, Google Colab, Roboflow, Streamlit y lenguaje de programación Python.</h4>
                                            </div>
                                            </br>"""
        st.markdown(html_temp_home1, unsafe_allow_html=True)

        html_classesp = [get_class_html(cls, detected_classes) for cls in classes]

        html_tempp = f"""
                <div style="padding:4px; border: 2px solid #FF4B4B; border-radius: 10px;">
                    <h4 style="color:#FF4B4B;text-align:center;">10 Clases</h4>
                    <p style="color:white;text-align:center;">{" ".join(html_classesp)}</p>
                </div>
                <br>
                """
        st.markdown(html_tempp, unsafe_allow_html=True)
    
        # Example cards with images
        card1 = create_card("Usar cámara", "https://st2.depositphotos.com/1915171/5331/v/450/depositphotos_53312473-stock-illustration-webcam-sign-icon-web-video.jpg")
        card2 = create_card("Subir imagen", "https://i.pinimg.com/736x/e1/91/5c/e1915cea845d5e31e1ec113a34b45fd8.jpg")
        card3 = create_card("Subir vídeo", "https://static.vecteezy.com/system/resources/previews/005/919/290/original/video-play-film-player-movie-solid-icon-illustration-logo-template-suitable-for-many-purposes-free-vector.jpg")

        # Display cards in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(card1, unsafe_allow_html=True)
        with col2:
            st.markdown(card2, unsafe_allow_html=True)
        with col3:
            st.markdown(card3, unsafe_allow_html=True)

    elif choice == "Subir imagen":
        
        detected_class = None

        confidence_slider = st.sidebar.slider('Confidence', min_value=0.0, max_value=1.0, value=0.25)
        
        html_classes = [get_class_html(cls, detected_classes) for cls in classes]

        html_temp = f"""
                <div style="padding:4px; border: 2px solid #FF4B4B; border-radius: 10px;">
                    <h4 style="color:#FF4B4B;text-align:center;">10 Clases</h4>
                    <p style="color:white;text-align:center;">{" ".join(html_classes)}</p>
                </div>
                """

        # Create a placeholder for the text
        text_placeholder = st.empty()

        # Display the original text
        text_placeholder.markdown(html_temp, unsafe_allow_html=True)
        # Checkbox to trigger text change
        change_text = st.checkbox("Objetos Detectados")

        image = st.file_uploader('Sube imagen', type=['png', 'jpg', 'jpeg', 'gif'])
        if image is not None:
            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                st.image(image, caption='Imagen original')
                
            with col2:
                with st.spinner('Procesando imagen...'):
                    img = Image.open(image)
                    img.save('./results.jpg', format='JPEG')

                    if model:
                        model.predict('results.jpg', confidence=confidence_slider, overlap=30).save('results_anotated.jpg')
                        
                        img = Image.open('results_anotated.jpg')
                        st.image(img, caption='Imagen anotada')

            with col3:
                results = model.predict('results.jpg', confidence=confidence_slider, overlap=30).json()
                if results:
                    print(results)
                    for result in results['predictions']:
                        detected_class = result['class']
                        print(detected_class)
                        confidence = result['confidence']
                        detected_classes.add(detected_class)
                        st.markdown(f"""
                                                    <div style="background-color:#f0f0f0;padding:5px;border-radius:5px;margin:5px 0; color:black;">
                                                        <b>Clase:</b> <span style="color:black">{detected_class}</span><br>
                                                        <b>Confianza:</b> {confidence:.2f}
                                                        <br>
                                                    </div>
                                                    """, unsafe_allow_html=True)

                else:
                    st.text('No detectado')

        if change_text:
            html_classes = [get_class_html(cls, detected_classes) for cls in classes]
            html_temp2 = f"""
                <div style="padding:4px; border: 2px solid #FF4B4B; border-radius: 10px;">
                    <h4 style="color:#FF4B4B;text-align:center;">19 Clases</h4>
                    <p style="color:white;text-align:center;">{" ".join(html_classes)}</p>
                </div>
            """
            text_placeholder.markdown(html_temp2, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
