# Generated by Django 4.2.7 on 2024-01-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("nationality", models.CharField(max_length=30)),
                ("date_of_birth", models.IntegerField()),
                ("age", models.IntegerField()),
                ("defense", models.IntegerField()),
                ("midfield", models.IntegerField()),
                ("attack", models.IntegerField()),
                ("skill", models.IntegerField(default=0)),
                ("potential", models.IntegerField(default=0)),
                ("mentality", models.IntegerField(default=0)),
                ("form", models.IntegerField(default=0)),
                ("aggression", models.IntegerField(default=0)),
                ("injured", models.BooleanField(default=False)),
                ("condition", models.IntegerField(default=12)),
                (
                    "stats",
                    models.JSONField(
                        default={
                            "assists_at": 0,
                            "assists_ts": 0,
                            "developed_at": 0,
                            "developed_ts": 0,
                            "games_at": 0,
                            "games_ts": 0,
                            "goals_at": 0,
                            "goals_ts": 0,
                            "injured_at": 0,
                            "trained_at": 0,
                            "trained_ts": 0,
                        }
                    ),
                ),
            ],
        ),
    ]