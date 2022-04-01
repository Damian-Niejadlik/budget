# Generated by Django 4.0.3 on 2022-03-31 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0004_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='balance.category'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_name',
            field=models.CharField(max_length=50),
        ),
    ]
