# Generated by Django 2.1.5 on 2019-04-05 21:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a University department (e.g. ICT)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('submitter', models.CharField(default=101, max_length=6)),
                ('summary', models.TextField(help_text='Enter a brief description of the ticket', max_length=1000)),
                ('urgency', models.CharField(blank=True, choices=[('TP', 'Priority'), ('NP', 'NormalPriority'), ('LP', 'LowPriority')], default='NP', help_text='Ticket Priority', max_length=2)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('department', models.ManyToManyField(help_text='Select a department for this ticket', to='tickets.Department')),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
    ]
