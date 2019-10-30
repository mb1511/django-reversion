# Generated by Django 2.2.7 on 2019-10-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('reversion', '0002_auto_20141216_1509'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revision',
            options={'ordering': ('-pk',)},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('-pk',)},
        ),
        migrations.RemoveField(
            model_name='revision',
            name='manager_slug',
        ),
        migrations.AddField(
            model_name='version',
            name='db',
            field=models.CharField(default='default', help_text='The database the model under version control is stored in.', max_length=191),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='revision',
            name='date_created',
            field=models.DateTimeField(db_index=True, help_text='The date and time this revision was created.', verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='version',
            name='object_id',
            field=models.CharField(help_text='Primary key of the model under version control.', max_length=191),
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together={('db', 'content_type', 'object_id', 'revision')},
        ),
        migrations.RemoveField(
            model_name='version',
            name='object_id_int',
        ),
    ]
