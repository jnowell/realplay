from django.contrib import admin
from django import forms

from .models import Team, Tournament, Game, Player, Lineup, LineupPosition, PlateAppearance

class LineupPositionForm(forms.ModelForm):
	player = forms.ModelChoiceField(queryset=None)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['player'].queryset = Player.objects.filter(team_id=self.parent_model.team_id)

class LineupPositionInline(admin.TabularInline):
    model = LineupPosition
    fields = ['order', 'position', 'player']
    extra = 9

class LineupAdmin(admin.ModelAdmin):
    fields = ['game', 'team']
    inlines = [LineupPositionInline]

class PlateAppearanceAdmin(admin.ModelAdmin):
	fields = ['game', 'lineup', 'pitcher', 'hitter', 'inning', 'is_1b_full', 'is_2b_full', 'is_3b_full', 'is_ab', 'is_hit', 'is_out', 'is_error', 'result']



admin.site.register(Game)
admin.site.register(Lineup, LineupAdmin)
admin.site.register(PlateAppearance, PlateAppearanceAdmin)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Tournament)
