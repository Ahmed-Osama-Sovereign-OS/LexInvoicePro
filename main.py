from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

# إعدادات الألوان حسب طلبك
Window.clearcolor = (0.96, 0.97, 0.98, 1) # #F5F7FA

class HomeScreen(Screen):
    pass

class LexInvoicePro(App):
    def build(self):
        self.title = "LexInvoice Pro - Ahmed Osama"
        return Builder.load_file('lexinvoice.kv')

if __name__ == "__main__":
    LexInvoicePro().run()
