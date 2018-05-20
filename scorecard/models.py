from django.db import models
from django.utils import timezone
from datetime import datetime    



class Team(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField(default=datetime.now, editable=False)
	modified = models.DateTimeField(default=datetime.now, editable=False)

	def save(self, *args, **kwargs):
        #On save, update timestamps
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Team, self).save(*args, **kwargs)

	def __str__(self) :
		return self.name

class Tournament(models.Model):
	date = models.DateField()
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=50)
	created = models.DateTimeField(default=datetime.now, editable=False)
	modified = models.DateTimeField(default=datetime.now, editable=False)

	def save(self, *args, **kwargs):
		#On save, update timestamps
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Tournament, self).save(*args, **kwargs)

	def __str__(self) :
		return self.name

class Game(models.Model):
	home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
	away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')
	date = models.DateField()
	location = models.CharField(max_length=50)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
	completed = models.BooleanField()
	created = models.DateTimeField(default=datetime.now, editable=False)
	modified = models.DateTimeField(default=datetime.now, editable=False)

	def save(self, *args, **kwargs):
		#On save, update timestamps
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Game, self).save(*args, **kwargs)

	def __str__(self) :
		return '%s - %s @ %s' % (self.date, self.away_team.name, self.home_team.name)

class Player(models.Model):
	url = models.CharField(max_length=200, null=True)
	name = models.CharField(max_length=200)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	number = models.IntegerField()
	throws = models.CharField(max_length=1, null=True)
	bats = models.CharField(max_length=1, null=True)
	position = models.CharField(max_length=10, null=True)
	created = models.DateTimeField(default=datetime.now, editable=False)
	modified = models.DateTimeField(default=datetime.now, editable=False)

	def save(self, *args, **kwargs):
		#On save, update timestamps
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Player, self).save(*args, **kwargs)

	def __str__(self) :
		return '%s - %s' % (self.number, self.name)

class Lineup(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	created = models.DateTimeField(default=datetime.now, editable=False)
	modified = models.DateTimeField(default=datetime.now, editable=False)

	def save(self, *args, **kwargs):
		#On save, update timestamps
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Lineup, self).save(*args, **kwargs)

	def __str__(self) :
		return '%s - %s' % (self.game, self.team)

class LineupPosition(models.Model):
	FIRST_BASE = '1B'
	SECOND_BASE = '2B'
	SHORTSTOP = 'SS'
	THIRD_BASE = '3B'
	LEFT_FIELD = 'LF'
	CENTER_FIELD = 'CF'
	RIGHT_FIELD = 'RF'
	PITCHER = 'P'
	CATCHER = 'C'
	DESIGNATED_HITTER = 'DH'
	POSITION_CHOICES = (
		(FIRST_BASE,'1B'),
		(SECOND_BASE,'2B'),
		(SHORTSTOP,'SS'),
		(THIRD_BASE,'3B'),
		(LEFT_FIELD,'LF'),
		(CENTER_FIELD,'CF'),
		(RIGHT_FIELD,'RF',),
		(PITCHER,'P'),
		(CATCHER,'C'),
 		(DESIGNATED_HITTER,'DH'),
    )
	lineup = models.ForeignKey(Lineup, on_delete=models.CASCADE)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	position = models.CharField(max_length=2,choices=POSITION_CHOICES)
	order = models.IntegerField()
	created = models.DateTimeField(default=datetime.now, editable=False)
	modified = models.DateTimeField(default=datetime.now, editable=False)

	def save(self, *args, **kwargs):
		#On save, update timestamps
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(LineupPosition, self).save(*args, **kwargs)

class PlateAppearance(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	lineup = models.ForeignKey(Lineup, on_delete=models.CASCADE)
	inning = models.IntegerField()
	at_bat_number = models.IntegerField()
	result = models.CharField(max_length=50)
	hitter = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='hitter_pas')
	pitcher = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='pitcher_pas')
	is_ab = models.BooleanField()
	is_hit = models.BooleanField()
	is_out = models.BooleanField()
	is_error = models.BooleanField()
	is_1b_full = models.BooleanField()
	is_2b_full = models.BooleanField()
	is_3b_full = models.BooleanField()
	reached = models.IntegerField()
	video_id = models.CharField(max_length=100, null=True)
	is_full = models.BooleanField()
	is_1b_cam = models.BooleanField()
	is_3b_cam = models.BooleanField()
	is_cf_cam = models.BooleanField()
	created = models.DateTimeField(default=datetime.now, editable=False)
	modified = models.DateTimeField(default=datetime.now, editable=False)

	def save(self, *args, **kwargs):
		#On save, update timestamps
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(PlateAppearance, self).save(*args, **kwargs)
