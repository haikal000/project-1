from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivymd.uix.list import MDList, OneLineAvatarListItem, ImageLeftWidget
from kivy.uix.image import Image
import time
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as kimage
from kivymd.uix.snackbar import Snackbar
import tkinter as tk
from tkinter import filedialog


KV = '''
ScreenManager:
    MainScreen:
    DiseaseScreen1:
    DiseaseScreen2:
    PesticideScreen1:
    PesticideScreen2:
    CameraScreen:

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDFillRoundFlatIconButton:
            text: 'Disease'
            font_style: 'H6'
            on_release: app.show_navigation('Disease', 'disease1')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDFillRoundFlatIconButton:
            text: 'Pesticide'
            font_style: 'H6'
            on_release: app.show_navigation('Pesticide', 'pesticide1')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDFillRoundFlatIconButton:
            text: 'Camera'
            font_style: 'H6'
            on_release: app.show_navigation('Camera', 'camera')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDFillRoundFlatIconButton:
            text: 'Exits'
            pos_hint: {'center_x': 0, 'center_y': 0}
            on_release: app.exit_app()

<DiseaseScreen1>:
    name: 'disease1'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDFillRoundFlatIconButton:
            text: 'Whitefly'
            font_style: 'H6'
            on_release: app.show_disease('Whitefly')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDFillRoundFlatIconButton:
            text: 'Leaf Spot'
            font_style: 'H6'
            on_release: app.show_disease('Leaf Spot')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDFillRoundFlatIconButton:
            text: 'Curly Leaf'
            font_style: 'H6'
            on_release: app.show_disease('Curly Leaf')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDFillRoundFlatIconButton:
            text: 'Yellowish'
            font_style: 'H6'
            on_release: app.show_disease('Yellowish')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDFillRoundFlatIconButton:
            text: 'Previous'
            on_release: app.goto_main_screen()

<DiseaseScreen2>:
    name: 'disease2'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(16)
        spacing: dp(16)
        height: dp(50)

        MDLabel:
            id: disease_label
            text: ''
            halign: 'center'
            font_style: 'H4'

        Image:
            id: disease_image
            size_hint: None, None
            size: dp(350), dp(350)
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'top': 0.8}
            allow_stretch: True

        MDLabel:
            id: disease_description
            text: ''
            font_style: 'Caption'
            halign: 'center'

        MDFillRoundFlatIconButton:
            text: 'Previous'
            on_release: app.goto_disease1_screen()

<PesticideScreen1>:
    name: 'pesticide1'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDFillRoundFlatIconButton:
            text: 'Pesticide1'
            font_style: 'H6'
            on_release: app.show_pesticide('Pesticide1')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDFillRoundFlatIconButton:
            text: 'Pesticide2'
            font_style: 'H6'
            on_release: app.show_pesticide('Pesticide2')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDFillRoundFlatIconButton:
            text: 'Pesticide3'
            font_style: 'H6'
            on_release: app.show_pesticide('Pesticide3')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDFillRoundFlatIconButton:
            text: 'Pesticide4'
            font_style: 'H6'
            on_release: app.show_pesticide('Pesticide4')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDFillRoundFlatIconButton:
            text: 'Previous'
            on_release: app.goto_main_screen()

<PesticideScreen2>:
    name: 'pesticide2'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(16)
        spacing: dp(16)
        height: dp(50)

        MDLabel:
            id: pesticide_label
            text: ''
            halign: 'center'
            font_style: 'H4'

        Image:
            id: pesticide_image
            size_hint: None, None
            size: dp(350), dp(350)
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'top': 0.8} 
            allow_stretch: True

        MDLabel:
            id: pesticide_description
            text: ''
            font_style: 'Caption'
            halign: 'center'

        MDFillRoundFlatIconButton:
            text: 'Previous'
            on_release: app.goto_pesticide1_screen()

<CameraScreen>:  
    name: 'camera'
    MDBoxLayout:
        orientation: "vertical"
        MDScrollView:
            do_scroll_x: False
            do_scroll_y: True
            BoxLayout:
                id: mybox
                orientation: "vertical"
                size_hint_y: 0.9
                pos_hint: {"center_y": 0.8}
                padding: 10
                spacing: 10
                
                MDFillRoundFlatIconButton:
                    text: 'Back'
                    on_release: app.goto_main_screen()  

                Camera:
                    id: camera
                    size_hint_y: 0.9
                    pos_hint: {"center_y": 1}
                    resolution: (640, 480)
                    play: True

                MDRaisedButton:
                    text: "Capture"
                    size_hint: 0.2, 0.1
                    pos_hint: {"x": 0.4, "bottom": 0.05}
                    on_release: app.capture(camera)
                
                MDRaisedButton:
                    text: "Choose Image"
                    size_hint: 0.2, 0.1
                    pos_hint: {"x": 0.4, "bottom": 0.05}
                    on_release: app.choose_image()
  
'''


class MainScreen(MDScreen):
    pass


class DiseaseScreen1(MDScreen):
    pass


class DiseaseScreen2(MDScreen):
    pass


class PesticideScreen1(MDScreen):
    pass


class PesticideScreen2(MDScreen):
    pass


class CameraScreen(MDScreen):
    pass


class DemoApp(MDApp):
    model = None
    camera = ObjectProperty(None)
    file_chooser = ObjectProperty(None)

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = 'Light'
        self.load_model()  # Load your classification model
        return Builder.load_string(KV)

    def choose_image(self):
        # Create a Tkinter root window (it won't be shown)
        root = tk.Tk()
        root.withdraw()

        # Open a file dialog to choose an image
        file_path = filedialog.askopenfilename(
            title="Choose an Image",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )

        # Check if a file was selected
        if file_path:
            # Perform prediction on the chosen image
            self.predict_image(file_path)

    def load_model(self):
        # Replace 'your_model.h5' with the actual path to your model file
        model_path = r'C:\Users\user\Desktop\mymodelV1.h5'
        try:
            self.model = load_model(model_path)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading the model: {e}")

    def exit_app(self):
        self.stop()

    def goto_main_screen(self):
        self.root.current = 'main'

    def capture(self, camera):
        if camera:
            # Capture the current frame from the camera
            timenow = time.strftime("%Y%m%d_%H%M%S")
            image_path = f"captured_image_{timenow}.png"
            camera.export_to_png(image_path)
            print(f"Image captured and saved: {image_path}")

            # Perform prediction on the captured image
            self.predict_image(image_path)

        else:
            print("Camera instance not found.")
    def predict_image(self, image_path):
        # Load the captured image for prediction
        img = kimage.load_img(image_path, target_size=(100, 100))
        img_array = kimage.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # Make a prediction
        predictions = self.model.predict(img_array)
        # Assuming predictions is a one-hot encoded array, get the predicted class
        predicted_class = np.argmax(predictions)
        confidence = predictions[0, predicted_class]

        class_labels = ['Healthy', 'leaf spot', 'powdery mildew', 'yellowish']
        threshold = 0.8

        if confidence > threshold:
            snackbar_text = f"Predicted Class: {class_labels[predicted_class]}"
        else:
            snackbar_text = "Image not recognized"

        Snackbar(text=snackbar_text).open()

    def show_navigation(self, navigation_type, next_screen):
        self.current_navigations = navigation_type
        self.root.current = next_screen

    def show_disease(self, disease_type):
        disease_info = self.get_disease_info(disease_type)
        disease_image_source = self.get_disease_image(disease_type)
        Disease_Screen2 = self.root.get_screen('disease2')
        Disease_Screen2.ids.disease_label.text = disease_type
        Disease_Screen2.ids.disease_description.text = disease_info
        Disease_Screen2.ids.disease_image.source = disease_image_source
        self.root.current = 'disease2'

    def show_pesticide(self, pesticide_type):
        pesticide_info = self.get_pesticide_info(pesticide_type)
        pesticide_image_source = self.get_pesticide_image(pesticide_type)
        Pesticide_Screen2 = self.root.get_screen('pesticide2')
        Pesticide_Screen2.ids.pesticide_label.text = pesticide_type
        Pesticide_Screen2.ids.pesticide_description.text = pesticide_info
        Pesticide_Screen2.ids.pesticide_image.source = pesticide_image_source
        self.root.current = 'pesticide2'

    def goto_main_screen(self):
        disease_screen = self.root.get_screen('disease1')
        disease_screen.current_disease = None
        pesticide_screen = self.root.get_screen('pesticide1')
        pesticide_screen.current_pesticide = None
        self.root.current = 'main'

    def goto_disease1_screen(self):
        self.root.current = 'disease1'

    def goto_disease2_screen(self):
        self.root.current = 'disease2'

    def goto_pesticide1_screen(self):
        self.root.current = 'pesticide1'

    def goto_pesticide2_screen(self):
        self.root.current = 'pesticide2'

    def get_disease_info(self, disease_type):
        disease_info = {
            'Whitefly': '',
            'Leaf Spot': '',
            'Curly Leaf': '',
            'Yellowish': '',
        }
        return disease_info.get(disease_type, 'No information available.')

    def get_disease_image(self, disease_type):
        disease_images = {
            'Whitefly': '',
            'Leaf Spot': '',
            'Curly Leaf': '',
            'Yellowish': '',
        }
        return disease_images.get(disease_type, '')

    def get_pesticide_info(self, pesticide_type):
        pesticide_info = {
            'Pesticide1': '',
            'Pesticide2': '',
            'Pesticide3': '',
            'Pesticide4': ''
        }
        return pesticide_info.get(pesticide_type, 'No information available.')

    def get_pesticide_image(self, pesticide_type):
        pesticide_images = {
            'Pesticide1': '',
            'Pesticide2': '',
            'Pesticide3': '',
            'Pesticide4': ''
        }
        return pesticide_images.get(pesticide_type, '')

    def exit_app(self):
        self.stop()

if __name__ == '__main__':
    DemoApp().run()
