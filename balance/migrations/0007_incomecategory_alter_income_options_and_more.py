# Generated by Django 4.0.3 on 2022-04-01 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0006_alter_income_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Income Category',
                'verbose_name_plural': 'Income Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ('name',), 'verbose_name': 'Income', 'verbose_name_plural': 'Incomes'},
        ),
        migrations.AddField(
            model_name='income',
            name='income_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='balance.incomecategory'),
        ),
    ]
