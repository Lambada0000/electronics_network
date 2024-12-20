# Generated by Django 5.1.3 on 2024-11-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0002_alter_networknode_options_alter_product_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="networknode",
            name="level",
            field=models.IntegerField(
                choices=[
                    (0, "Завод"),
                    (1, "Розничная сеть"),
                    (2, "Индивидуальный предприниматель"),
                ],
                default=2,
                verbose_name="Уровень сети",
            ),
        ),
    ]
