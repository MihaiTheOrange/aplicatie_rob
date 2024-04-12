from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.app import App
from api import post_to_api
from kivy.network.urlrequest import UrlRequest
from subclass import RV
from kivy.clock import Clock


import json

class myLayout(FloatLayout):
    def __init__(self, app):
        super().__init__()
        self.myapp = app

    def switch(self):
            self.myapp.screen_manager.transition = SlideTransition(direction='left')
            self.myapp.screen_manager.current = 'second'

    def switch2set(self):
        self.myapp.screen_manager.transition = SlideTransition(direction='up')
        self.myapp.screen_manager.current = 'third'

    def switch2com(self):
            self.myapp.screen_manager.transition = SlideTransition(direction='left')
            self.myapp.screen_manager.current = 'comenzi'

    def switch2rgb(self):
        self.myapp.screen_manager.transition = SlideTransition(direction='left')
        self.myapp.screen_manager.current = 'rgb'

    def s1_data(self):
        print('s1')


class set_layout(BoxLayout):
    def __init__(self, app):
        super().__init__()
        self.myapp = app
    input_url = ObjectProperty(None)

    def switch(self):
        self.myapp.screen_manager.transition = SlideTransition(direction='down')
        self.myapp.screen_manager.current = 'first'

    def apiC(self):
        app = App.get_running_app()
        app.base_url = self.input_url.text


class comenzi_layout(FloatLayout):
    def __init__(self, myapp):
        super().__init__()
        self.app = App.get_running_app()
        self.myapp = myapp

    def switch(self):
        self.myapp.screen_manager.transition = SlideTransition(direction='right')
        self.myapp.screen_manager.current = 'first'

    def up_com(self):
        payload={"comenzi":[0, 0, 0, 1], "rgb":[0, 0, 0]}
        post_to_api('/comenzi', payload, self.app)

    def down_com(self):
        payload={"comenzi":[0, 0, 1, 0], "rgb":[0, 0, 0]}
        post_to_api('/comenzi', payload, self.app)

    def left_com(self):
        payload={"comenzi":[1, 0, 0, 0], "rgb":[0, 0, 0]}
        post_to_api('/comenzi', payload, self.app)

    def right_com(self):
        payload={"comenzi":[0, 1, 0, 0], "rgb":[0, 0, 0]}
        post_to_api('/comenzi', payload, self.app)

    def release_com(self):
        payload={"comenzi":[0, 0, 0, 0], "rgb":[0, 0, 0]}
        post_to_api('/comenzi', payload, self.app)


class rgb_layout(FloatLayout):
    def __init__(self, myapp):
        super().__init__()
        self.ids.color_button.background_color=(0, 0, 0, 1)
        self.app = App.get_running_app()
        self.myapp = myapp

    red_slider = ObjectProperty(None)
    blue_slider = ObjectProperty(None)
    green_slider = ObjectProperty(None)

    def switch(self):
        self.myapp.screen_manager.transition = SlideTransition(direction='right')
        self.myapp.screen_manager.current = 'first'

    def submit_rgb(self):
        red = self.ids.red_sliderID.value
        green = self.ids.green_sliderID.value
        blue = self.ids.blue_sliderID.value
        payload = {"comenzi":[0,0,0,0], "rgb":[red,green,blue]}
        post_to_api('/comenzi', payload, self.app)

    def update_button_color(self):
        red=self.ids.red_sliderID.value / 255
        green = self.ids.green_sliderID.value / 255
        blue = self.ids.blue_sliderID.value / 255
        self.ids.color_button.background_color = (red, green, blue, 1)


class lay_2(BoxLayout):
    def __init__(self,app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.update_data()
        Clock.schedule_interval(self.update_data, 3)

    def update_data(self, dt=None):
        url = self.app.base_url+'/sen1'
        UrlRequest(url, self.parse_data)

    def parse_data(self, req, result):
        self.ids.rv.data = []
        data = result
        for item in data:
            inp = item.get("inp", "N/A")
            id_input = item.get("id_input", "N/A")
            # Update the RecycleView data
            self.ids.rv.data.append({"text": f"Inp: {inp}, ID Input: {id_input}"})

    def switch(self):
        self.app.screen_manager.transition = SlideTransition(direction='right')
        self.app.screen_manager.current = 'first'''

