def _check_events(self):
		"""Respond to keypresses and mouse events """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses """
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# Move the ship to the left
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			# Move the ship up
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			# Move the ship down
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
	
	def _check_keyup_events(self, event):
		"""Respond to key releases """
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False