class Settings():
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's  static settings"""
		
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0,0,0)

		#Ship settings
		self.ship_limit = 3

		#Bullet settings
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#Alien settings
		self.fleet_drop_speed = 20

		# How quickly the game speeds up
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()               

	def initialize_dynamic_settings(self):
		""" Initialize settings that change troughtout the game """
		self.ship_speed = 5.0
		self.bullet_speed = 15.0
		self.alien_speed = 3

		# Fleet direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1