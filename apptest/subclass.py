from kivy.uix.recycleview import RecycleView


class RV(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []