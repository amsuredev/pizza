# Generated by Django 3.0.3 on 2020-09-17 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizzas', '0006_auto_20200914_1540'),
        ('toppings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToppingsInPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.Pizza')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toppings.Topping')),
            ],
        ),
    ]
