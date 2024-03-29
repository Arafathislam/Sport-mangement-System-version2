# Generated by Django 4.1.7 on 2023-03-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_time_shedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semi_Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cricket_team1', models.CharField(blank=True, max_length=200)),
                ('cricket_team2', models.CharField(blank=True, max_length=200)),
                ('cricket_time1', models.CharField(blank=True, max_length=200)),
                ('cricket_team3', models.CharField(blank=True, max_length=200)),
                ('cricket_team4', models.CharField(blank=True, max_length=200)),
                ('cricket_time2', models.CharField(blank=True, max_length=200)),
                ('cricket_finalteam1', models.CharField(blank=True, max_length=200)),
                ('cricket_finalteam2', models.CharField(blank=True, max_length=200)),
                ('cricket_finaltime', models.CharField(blank=True, max_length=200)),
                ('football_team1', models.CharField(blank=True, max_length=200)),
                ('football_team2', models.CharField(blank=True, max_length=200)),
                ('football_time1', models.CharField(blank=True, max_length=200)),
                ('football_team3', models.CharField(blank=True, max_length=200)),
                ('football_team4', models.CharField(blank=True, max_length=200)),
                ('football_time2', models.CharField(blank=True, max_length=200)),
                ('football_finalteam1', models.CharField(blank=True, max_length=200)),
                ('football_finalteam2', models.CharField(blank=True, max_length=200)),
                ('football_finaltime', models.CharField(blank=True, max_length=200)),
                ('volleyball_team1', models.CharField(blank=True, max_length=200)),
                ('volleyball_team2', models.CharField(blank=True, max_length=200)),
                ('volleyball_time1', models.CharField(blank=True, max_length=200)),
                ('volleyball_team3', models.CharField(blank=True, max_length=200)),
                ('volleyball_team4', models.CharField(blank=True, max_length=200)),
                ('volleyball_time2', models.CharField(blank=True, max_length=200)),
                ('volleyball_finalteam1', models.CharField(blank=True, max_length=200)),
                ('volleyball_finalteam2', models.CharField(blank=True, max_length=200)),
                ('volleyball_finaltime', models.CharField(blank=True, max_length=200)),
                ('kabaddi_team1', models.CharField(blank=True, max_length=200)),
                ('kabaddi_team2', models.CharField(blank=True, max_length=200)),
                ('kabaddi_time1', models.CharField(blank=True, max_length=200)),
                ('kabaddi_team3', models.CharField(blank=True, max_length=200)),
                ('kabaddi_team4', models.CharField(blank=True, max_length=200)),
                ('kabaddi_time2', models.CharField(blank=True, max_length=200)),
                ('kabaddi_finalteam1', models.CharField(blank=True, max_length=200)),
                ('kabaddi_finalteam2', models.CharField(blank=True, max_length=200)),
                ('kabaddi_finaltime', models.CharField(blank=True, max_length=200)),
                ('chess_team1', models.CharField(blank=True, max_length=200)),
                ('chess_team2', models.CharField(blank=True, max_length=200)),
                ('chess_time1', models.CharField(blank=True, max_length=200)),
                ('chess_team3', models.CharField(blank=True, max_length=200)),
                ('chess_team4', models.CharField(blank=True, max_length=200)),
                ('chess_time2', models.CharField(blank=True, max_length=200)),
                ('chess_finalteam1', models.CharField(blank=True, max_length=200)),
                ('chess_finalteam2', models.CharField(blank=True, max_length=200)),
                ('chess_finaltime', models.CharField(blank=True, max_length=200)),
                ('table_team1', models.CharField(blank=True, max_length=200)),
                ('table_team2', models.CharField(blank=True, max_length=200)),
                ('table_time1', models.CharField(blank=True, max_length=200)),
                ('table_team3', models.CharField(blank=True, max_length=200)),
                ('table_team4', models.CharField(blank=True, max_length=200)),
                ('table_time2', models.CharField(blank=True, max_length=200)),
                ('table_finalteam1', models.CharField(blank=True, max_length=200)),
                ('table_finalteam2', models.CharField(blank=True, max_length=200)),
                ('table_finaltime', models.CharField(blank=True, max_length=200)),
                ('badminton_team1', models.CharField(blank=True, max_length=200)),
                ('badminton_team2', models.CharField(blank=True, max_length=200)),
                ('badminton_time1', models.CharField(blank=True, max_length=200)),
                ('badminton_team3', models.CharField(blank=True, max_length=200)),
                ('badminton_team4', models.CharField(blank=True, max_length=200)),
                ('badminton_time2', models.CharField(blank=True, max_length=200)),
                ('badminton_finalteam1', models.CharField(blank=True, max_length=200)),
                ('badminton_finalteam2', models.CharField(blank=True, max_length=200)),
                ('badminton_finaltime', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
