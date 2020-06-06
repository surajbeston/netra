# Generated by Django 3.0.7 on 2020-06-06 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_fleet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obstruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True)),
                ('altitude', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('distance', models.FloatField(blank=True, null=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.GPS')),
            ],
        ),
    ]