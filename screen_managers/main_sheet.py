from kivy.uix.screenmanager import ScreenManager, NoTransition

from screens.home_screen import HomeScreen
from screens.settings_screen import SettingsScreen


class MainScreenManager(ScreenManager):
	def build(self):
		self.transition = NoTransition()
		self.add_widget(HomeScreen(name="home"))
		self.add_widget(SettingsScreen(name="settings"))

		return self

	def change_screen(self, screen_name):
		self.current = screen_name