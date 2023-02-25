# Generated by Django 4.1.3 on 2023-02-18 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryIndustry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('Create_Date', models.DateTimeField(auto_now_add=True)),
                ('Up_Date', models.DateTimeField(auto_now=True)),
                ('Active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ListProductIndustry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100, unique=True)),
                ('Information', models.TextField()),
                ('Create_Date', models.DateTimeField(auto_now_add=True)),
                ('Up_Date', models.DateTimeField(auto_now=True)),
                ('Active', models.BooleanField(default=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category_Industry', to='polls.categoryindustry')),
            ],
            options={
                'ordering': ['id'],
                'unique_together': {('Title', 'Category')},
            },
        ),
        migrations.CreateModel(
            name='ImageProductIndustry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(null=True, upload_to='upload/ImageProduct')),
                ('Create_Date', models.DateTimeField(auto_now_add=True)),
                ('Up_Date', models.DateTimeField(auto_now=True)),
                ('Active', models.BooleanField(default=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_Industry', to='polls.listproductindustry')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
