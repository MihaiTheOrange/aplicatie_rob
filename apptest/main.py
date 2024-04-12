from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from layouts import myLayout, set_layout, comenzi_layout, rgb_layout, lay_2
from subclass import RV


class myApp(App):
    def build(self):
        self.base_url=""
        self.screen_manager = ScreenManager()
        self.firstpage = myLayout(self)

        screen = Screen(name='first')
        screen.add_widget(self.firstpage)
        self.screen_manager.add_widget(screen)

        self.secondpage = lay_2(self)
        screen = Screen(name='second')
        screen.add_widget(self.secondpage)
        self.screen_manager.add_widget(screen)

        self.setpage = set_layout(self)
        screen = Screen(name='third')
        screen.add_widget(self.setpage)
        self.screen_manager.add_widget(screen)

        self.compage = comenzi_layout(self)
        screen=Screen(name='comenzi')
        screen.add_widget(self.compage)
        self.screen_manager.add_widget(screen)

        self.rgbpage = rgb_layout(self)
        screen = Screen(name='rgb')
        screen.add_widget(self.rgbpage)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    myapp = myApp()
    myapp.run()
