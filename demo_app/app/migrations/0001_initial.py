# Generated by Django 2.2.17 on 2020-11-16 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user_count', models.IntegerField()),
                ('view_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Access Record',
                'verbose_name_plural': 'Access Record',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('nagios_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Nagios Host ID')),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('internal_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=128)),
                ('ssh_port', models.IntegerField(blank=True, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Normal'), (1, 'Down'), (2, 'No Connect'), (3, 'Error')])),
                ('brand', models.CharField(choices=[('DELL', 'DELL'), ('HP', 'HP'), ('Other', 'Other')], max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('cpu', models.CharField(max_length=64)),
                ('core_num', models.SmallIntegerField(choices=[(2, '2 Cores'), (4, '4 Cores'), (6, '6 Cores'), (8, '8 Cores'), (10, '10 Cores'), (12, '12 Cores'), (14, '14 Cores'), (16, '16 Cores'), (18, '18 Cores'), (20, '20 Cores'), (22, '22 Cores'), (24, '24 Cores'), (26, '26 Cores'), (28, '28 Cores')])),
                ('hard_disk', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('system', models.CharField(choices=[('CentOS', 'CentOS'), ('FreeBSD', 'FreeBSD'), ('Ubuntu', 'Ubuntu')], max_length=32, verbose_name='System OS')),
                ('system_version', models.CharField(max_length=32)),
                ('system_arch', models.CharField(choices=[('x86_64', 'x86_64'), ('i386', 'i386')], max_length=32)),
                ('create_time', models.DateField()),
                ('guarantee_date', models.DateField()),
                ('service_type', models.CharField(choices=[('moniter', 'Moniter'), ('lvs', 'LVS'), ('db', 'Database'), ('analysis', 'Analysis'), ('admin', 'Admin'), ('storge', 'Storge'), ('web', 'WEB'), ('email', 'Email'), ('mix', 'Mix')], max_length=32)),
                ('description', models.TextField()),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Admin')),
            ],
            options={
                'verbose_name': 'Host',
                'verbose_name_plural': 'Host',
            },
        ),
        migrations.CreateModel(
            name='MaintainLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintain_type', models.CharField(max_length=32)),
                ('hard_type', models.CharField(max_length=16)),
                ('time', models.DateTimeField()),
                ('operator', models.CharField(max_length=16)),
                ('note', models.TextField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Host')),
            ],
            options={
                'verbose_name': 'Maintain Log',
                'verbose_name_plural': 'Maintain Log',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('contact', models.CharField(max_length=32)),
                ('telphone', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
                ('is_valid', models.BooleanField(default=False)),
                ('customer_id', models.CharField(max_length=128)),
                ('create_time', models.DateField(auto_now=True)),
                ('groups', models.ManyToManyField(to='auth.Group')),
            ],
            options={
                'verbose_name': 'IDC',
                'verbose_name_plural': 'IDC',
            },
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('hosts', models.ManyToManyField(blank=True, related_name='groups', to='app.Host', verbose_name='Hosts')),
            ],
            options={
                'verbose_name': 'Host Group',
                'verbose_name_plural': 'Host Group',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.IDC'),
        ),
    ]
