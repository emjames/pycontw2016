# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-26 11:38
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsoredEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='title')),
                ('category', models.CharField(choices=[('PRAC', 'Best Practices & Patterns'), ('COM', 'Community'), ('DB', 'Databases'), ('DATA', 'Data Analysis'), ('EDU', 'Education'), ('EMBED', 'Embedded Systems'), ('GAME', 'Gaming'), ('GRAPH', 'Graphics'), ('OTHER', 'Other'), ('CORE', 'Python Core (language, stdlib, etc.)'), ('INTNL', 'Python Internals'), ('LIBS', 'Python Libraries'), ('SCI', 'Science'), ('SEC', 'Security'), ('ADMIN', 'Systems Administration'), ('TEST', 'Testing'), ('WEB', 'Web Frameworks')], max_length=5, verbose_name='category')),
                ('language', models.CharField(choices=[('ENEN', 'English talk'), ('ZHEN', 'Chinese talk w. English slides'), ('ZHZH', 'Chinese talk w. Chinese slides'), ('TAI', 'Taiwanese Hokkien')], max_length=4, verbose_name='language')),
                ('abstract', core.models.EAWTextField(help_text='The overview of what the talk is about. If the talk assume some domain knowledge please state it here. If your talk is accepted, this will be displayed on both the website and the handbook. Should be one paragraph.', max_length=1000, verbose_name='abstract')),
                ('python_level', models.CharField(choices=[('NOVICE', 'Novice'), ('INTERMEDIATE', 'Intermediate'), ('EXPERIENCED', 'Experienced')], help_text='The choice of talk level matters during the review process. More definition of talk level can be found at the <a href="/None/speaking/talk/" target="_blank">How to Propose a Talk</a> page. Note that a proposal won\'t be more likely to be accepted because of being "Novice" level. We may contact you to change the talk level when we find the content is too-hard or too-easy for the target audience.', max_length=12, verbose_name='Python level')),
                ('detailed_description', models.TextField(blank=True, help_text="Try not be too lengthy to scare away reviewers or potential audience. A comfortable length is less than 2000 characters (or about 1200 Chinese characters). Since most reviewers may not understand the topic as deep as you do, including related links to the talk topic will help reviewers understand the proposal. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='detailed description')),
                ('recording_policy', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, help_text="Whether you agree to give permission to PyCon Taiwan to record, edit, and release audio and video of your presentation. More information can be found at <a href='/None/speaking/recording/' target='_blank'>Recording Release</a> page.", verbose_name='recording policy')),
                ('slide_link', models.URLField(blank=True, default='', help_text='You can add your slide link near or after the conference day. Not required for review.', verbose_name='slide link')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('host', core.models.BigForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='host')),
            ],
            options={
                'verbose_name': 'sponsored event',
                'verbose_name_plural': 'sponsored events',
            },
        ),
    ]