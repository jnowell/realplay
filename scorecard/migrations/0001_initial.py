# Generated by Django 2.0.5 on 2018-05-20 18:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('completed', models.BooleanField()),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lineup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorecard.Game')),
            ],
        ),
        migrations.CreateModel(
            name='LineupPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('LF', 'LF'), ('CF', 'CF'), ('RF', 'RF'), ('P', 'P'), ('C', 'C'), ('DH', 'DH')], max_length=2)),
                ('order', models.IntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('lineup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorecard.Lineup')),
            ],
        ),
        migrations.CreateModel(
            name='PlateAppearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inning', models.IntegerField()),
                ('at_bat_number', models.IntegerField()),
                ('result', models.CharField(max_length=50)),
                ('is_ab', models.BooleanField()),
                ('is_hit', models.BooleanField()),
                ('is_out', models.BooleanField()),
                ('is_error', models.BooleanField()),
                ('is_1b_full', models.BooleanField()),
                ('is_2b_full', models.BooleanField()),
                ('is_3b_full', models.BooleanField()),
                ('reached', models.IntegerField()),
                ('video_id', models.CharField(max_length=100, null=True)),
                ('is_full', models.BooleanField()),
                ('is_1b_cam', models.BooleanField()),
                ('is_3b_cam', models.BooleanField()),
                ('is_cf_cam', models.BooleanField()),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorecard.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('throws', models.CharField(max_length=1, null=True)),
                ('bats', models.CharField(max_length=1, null=True)),
                ('position', models.CharField(max_length=10, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorecard.Team'),
        ),
        migrations.AddField(
            model_name='plateappearance',
            name='hitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hitter_pas', to='scorecard.Player'),
        ),
        migrations.AddField(
            model_name='plateappearance',
            name='lineup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorecard.Lineup'),
        ),
        migrations.AddField(
            model_name='plateappearance',
            name='pitcher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pitcher_pas', to='scorecard.Player'),
        ),
        migrations.AddField(
            model_name='lineupposition',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorecard.Player'),
        ),
        migrations.AddField(
            model_name='lineup',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorecard.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='scorecard.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='scorecard.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scorecard.Tournament'),
        ),
    ]
