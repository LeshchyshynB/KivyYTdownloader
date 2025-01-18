from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from os import listdir

from screen_managers.main_sheet import MainScreenManager


class MyApp(App):
	def build(self):
		sm = MainScreenManager()
		[ Builder.load_file(f"./kv/{name}") for name in listdir("./kv/") ]
		return sm.build()

if __name__ == "__main__":
	MyApp().run()
