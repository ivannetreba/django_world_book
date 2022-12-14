# Generated by Django 4.1 on 2022-08-15 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_author_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"verbose_name": "Книги", "verbose_name_plural": "Книги"},
        ),
        migrations.AlterModelOptions(
            name="bookinstance",
            options={
                "verbose_name": "Экземпляры книг",
                "verbose_name_plural": "Экземпляры книг",
            },
        ),
        migrations.AlterModelOptions(
            name="genre",
            options={"verbose_name": "Жанры", "verbose_name_plural": "Жанры"},
        ),
        migrations.AlterModelOptions(
            name="language",
            options={"verbose_name": "Языки", "verbose_name_plural": "Языки"},
        ),
        migrations.AlterModelOptions(
            name="status",
            options={"verbose_name": "Статусы", "verbose_name_plural": "Статусы"},
        ),
    ]
