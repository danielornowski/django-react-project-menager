# Generated by Django 4.0.2 on 2022-02-19 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.CharField(max_length=255)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
