from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import requests
from kivy.uix.slider import Slider

BASE_URL='http://127.0.0.1:8000'


def get_data_from_fastapi(endpoint):
    try:
        response = requests.get(BASE_URL+endpoint)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Process the data received from FastAPI server
            return data
        else:
            return 'error'
    except requests.exceptions.RequestException as e:
        return 'error'


def post_to_api(endpoint, payload):
    response = requests.post(BASE_URL+endpoint, json=payload)
    if response.status_code == 200:
        print('POST request was successful!')
        print('Response:', response.text)
    else:
        print('POST request failed:', response.status_code)


class myLayout(FloatLayout):
    def __init__(self):
        super().__init__()
    def switch(self):
            myapp.screen_manager.transition = SlideTransition(direction='left')
            myapp.screen_manager.current = 'second'

    def switch2set(self):
        myapp.screen_manager.transition = SlideTransition(direction='up')
        myapp.screen_manager.current = 'third'

    def switch2com(self):
            myapp.screen_manager.transition = SlideTransition(direction='left')
            myapp.screen_manager.current = 'comenzi'

    def switch2rgb(self):
        myapp.screen_manager.transition = SlideTransition(direction='left')
        myapp.screen_manager.current = 'rgb'

    def s1_data(self):
        print('s1')


class sen_1(RecycleView):
    def __init__(self, endp):
        super().__init__()
        self.endp=endp
        #self.data=[{'text': str(i)}for i in range(5)]
        self.data=[{'text': str(i)}for i in get_data_from_fastapi(endp)]


class lay_2(BoxLayout):
    def __init__(self, endpo):
        super().__init__()
        self.endpo=endpo
        self.add_widget(sen_1(endp=self.endpo))
    def switch(self):
        myapp.screen_manager.transition = SlideTransition(direction='right')
        myapp.screen_manager.current = 'first'
class set_layout(BoxLayout):
    def __init__(self):
        super().__init__()
    input_url=ObjectProperty(None)
    def switch(self):
        myapp.screen_manager.transition = SlideTransition(direction='down')
        myapp.screen_manager.current = 'first'
    def apiC(self):
        print(self.input_url.text)


class comenzi_layout(FloatLayout):
    def __init__(self):
        super().__init__()

    def switch(self):
        myapp.screen_manager.transition = SlideTransition(direction='right')
        myapp.screen_manager.current = 'first'

    def up_com(self):
        payload={"comenzi":[0,0,0,1], "rgb":[0,0,0]}
        post_to_api('/comenzi', payload)
    def down_com(self):
        payload={"comenzi":[0,0,1,0], "rgb":[0,0,0]}
        post_to_api('/comenzi', payload)
    def left_com(self):
        payload={"comenzi":[1,0,0,0], "rgb":[0,0,0]}
        post_to_api('/comenzi', payload)
    def right_com(self):
        payload={"comenzi":[0,1,0,0], "rgb":[0,0,0]}
        post_to_api('/comenzi', payload)
    def release_com(self):
        payload={"comenzi":[0,0,0,0], "rgb":[0,0,0]}
        post_to_api('/comenzi', payload)


class rgb_layout(FloatLayout):
    def __init__(self):
        super().__init__()
        self.ids.color_button.background_color=(0,0,0,1)
    red_slider = ObjectProperty(None)
    blue_slider=ObjectProperty(None)
    green_slider=ObjectProperty(None)

    def switch(self):
        myapp.screen_manager.transition = SlideTransition(direction='right')
        myapp.screen_manager.current = 'first'

    def submit_rgb(self):
        red = self.ids.red_sliderID.value
        green = self.ids.green_sliderID.value
        blue = self.ids.blue_sliderID.value
        payload={"comenzi":[0,0,0,0], "rgb":[red,green,blue]}
        post_to_api('/comenzi', payload)

    def update_button_color(self):
        red=self.ids.red_sliderID.value / 255
        green = self.ids.green_sliderID.value / 255
        blue = self.ids.blue_sliderID.value / 255
        self.ids.color_button.background_color = (red, green, blue, 1)


class myApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.firstpage=myLayout()

        screen = Screen(name='first')
        screen.add_widget(self.firstpage)
        self.screen_manager.add_widget(screen)

        self.secondpage = lay_2('/sen1')
        screen = Screen(name='second')
        screen.add_widget(self.secondpage)
        self.screen_manager.add_widget(screen)

        self.setpage = set_layout()
        screen = Screen(name='third')
        screen.add_widget(self.setpage)
        self.screen_manager.add_widget(screen)

        self.compage = comenzi_layout()
        screen=Screen(name='comenzi')
        screen.add_widget(self.compage)
        self.screen_manager.add_widget(screen)

        self.rgbpage = rgb_layout()
        screen=Screen(name='rgb')
        screen.add_widget(self.rgbpage)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    myapp = myApp()
    myapp.run()
