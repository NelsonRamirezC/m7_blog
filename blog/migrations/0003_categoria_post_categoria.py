# Generated by Django 5.1.3 on 2024-11-22 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_fecha_creacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'categorias',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.categoria'),
        ),
    ]
