# Generated by Django 4.1.2 on 2022-10-28 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_alter_categoria_options_alter_livro_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='Categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livros.categoria'),
        ),
    ]
