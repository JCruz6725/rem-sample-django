# Generated by Django 4.0 on 2022-07-09 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=63, unique=True)),
                ('full_name', models.CharField(max_length=63)),
                ('location', models.CharField(blank=True, max_length=63)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=32)),
                ('summary', models.CharField(default='', max_length=1024)),
                ('programming_skills', models.CharField(default='', max_length=1024)),
                ('industry_tools', models.CharField(default='', max_length=1024)),
                ('office_tools', models.CharField(default='', max_length=1024)),
                ('related_courses', models.CharField(default='', max_length=1024)),
                ('account_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='info_api.account')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=32)),
                ('title_on_project', models.CharField(default='', max_length=32)),
                ('tech_used', models.CharField(default='', max_length=32)),
                ('summary', models.CharField(default='', max_length=1024)),
                ('external_link', models.CharField(default='https://github.com/', max_length=32)),
                ('account_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='info_api.account')),
                ('resume_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_rt', to='info_api.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=32)),
                ('time_at', models.CharField(max_length=32)),
                ('title_of_project', models.CharField(max_length=32)),
                ('tech_used', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=1024)),
                ('account_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professional', to='info_api.account')),
                ('resume_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professional_rt', to='info_api.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('degree', models.CharField(max_length=128)),
                ('time_at', models.CharField(max_length=32)),
                ('account_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='info_api.account')),
            ],
        ),
    ]
