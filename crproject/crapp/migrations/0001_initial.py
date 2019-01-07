# Generated by Django 2.1.4 on 2019-01-02 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Closet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Doors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Wardrobe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='accessories',
            name='wardrobe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crapp.Wardrobe'),
        ),
    ]