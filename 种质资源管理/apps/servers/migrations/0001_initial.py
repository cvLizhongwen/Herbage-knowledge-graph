# Generated by Django 4.0.7 on 2022-09-06 12:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerHis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serverid', models.IntegerField(verbose_name='种子ID')),
                ('Gtype', models.CharField(max_length=20, verbose_name='种子类型')),
                ('Gke', models.CharField(blank=True, max_length=50, verbose_name='科中文名')),
                ('Gs', models.CharField(blank=True, max_length=50, verbose_name='属中文名')),
                ('Gz', models.CharField(blank=True, max_length=50, verbose_name='种中文名')),
                ('Gnumber', models.CharField(blank=True, max_length=50, verbose_name='种编号')),
                ('Gname', models.CharField(blank=True, max_length=50, verbose_name='种子中文名')),
                ('Gyear', models.CharField(blank=True, max_length=50, verbose_name='采集年份')),
                ('Gaddress', models.CharField(blank=True, max_length=50, verbose_name='采集地')),
                ('Gdrought', models.CharField(blank=True, max_length=50, verbose_name='抗旱性')),
                ('Gcold', models.CharField(blank=True, max_length=50, verbose_name='抗寒性')),
                ('Gsalt', models.CharField(blank=True, max_length=50, verbose_name='耐盐性')),
                ('Gfrost', models.CharField(blank=True, max_length=50, verbose_name='耐霜冻性')),
                ('Gheat', models.CharField(blank=True, max_length=50, verbose_name='耐热性')),
                ('Ginseck', models.CharField(blank=True, max_length=50, verbose_name='抗虫害性性')),
                ('Gdisease', models.CharField(blank=True, max_length=50, verbose_name='抗病性')),
                ('predisposingType', models.CharField(blank=True, max_length=50, verbose_name='易感病型')),
                ('rootType', models.CharField(blank=True, max_length=50, verbose_name='根系类型')),
                ('stem', models.CharField(blank=True, max_length=50, verbose_name='茎状')),
                ('understem', models.CharField(blank=True, max_length=50, verbose_name='地下茎')),
                ('leafType', models.CharField(blank=True, max_length=50, verbose_name='叶的类型')),
                ('phyllotaxis', models.CharField(blank=True, max_length=50, verbose_name='叶序')),
                ('vein', models.CharField(blank=True, max_length=50, verbose_name='脉序')),
                ('leafShape', models.CharField(blank=True, max_length=50, verbose_name='叶片形状')),
                ('anthotaxy', models.CharField(blank=True, max_length=50, verbose_name='花序')),
                ('fruitType', models.CharField(blank=True, max_length=50, verbose_name='果实类型')),
                ('ipaddress', models.CharField(blank=True, max_length=100, verbose_name='存放地址')),
                ('description', models.CharField(blank=True, max_length=50, verbose_name='相关信息描述')),
                ('zcnumber', models.CharField(blank=True, max_length=50, verbose_name='种子现存重量')),
                ('owner', models.CharField(max_length=20, verbose_name='管理人员')),
                ('undernet', models.CharField(max_length=10, verbose_name='所在状况')),
                ('comment', models.CharField(blank=True, max_length=300, verbose_name='备注')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '种质历史表',
                'verbose_name_plural': '种质历史表',
            },
        ),
        migrations.CreateModel(
            name='ServerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gtype', models.CharField(max_length=20, verbose_name='种质类型')),
            ],
            options={
                'verbose_name': '种质类型表',
                'verbose_name_plural': '种质类型表',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.CharField(blank=True, max_length=100, verbose_name='存放地址')),
                ('description', models.CharField(blank=True, max_length=50, verbose_name='相关信息描述')),
                ('Gke', models.CharField(blank=True, max_length=50, verbose_name='科中文名')),
                ('Gs', models.CharField(blank=True, max_length=50, verbose_name='属中文名')),
                ('Gz', models.CharField(blank=True, max_length=50, verbose_name='种中文名')),
                ('Gnumber', models.CharField(blank=True, max_length=50, verbose_name='种编号')),
                ('Gname', models.CharField(blank=True, max_length=50, verbose_name='种子中文名')),
                ('Gyear', models.CharField(blank=True, max_length=50, verbose_name='采集年份')),
                ('Gaddress', models.CharField(blank=True, max_length=50, verbose_name='采集地')),
                ('Gdrought', models.CharField(blank=True, max_length=50, verbose_name='抗旱性')),
                ('Gcold', models.CharField(blank=True, max_length=50, verbose_name='抗寒性')),
                ('Gsalt', models.CharField(blank=True, max_length=50, verbose_name='耐盐性')),
                ('Gfrost', models.CharField(blank=True, max_length=50, verbose_name='耐霜冻性')),
                ('Gheat', models.CharField(blank=True, max_length=50, verbose_name='耐热性')),
                ('Ginseck', models.CharField(blank=True, max_length=50, verbose_name='抗虫害性性')),
                ('Gdisease', models.CharField(blank=True, max_length=50, verbose_name='抗病性')),
                ('predisposingType', models.CharField(blank=True, max_length=50, verbose_name='易感病型')),
                ('rootType', models.CharField(blank=True, max_length=50, verbose_name='根系类型')),
                ('stem', models.CharField(blank=True, max_length=50, verbose_name='茎状')),
                ('understem', models.CharField(blank=True, max_length=50, verbose_name='地下茎')),
                ('leafType', models.CharField(blank=True, max_length=50, verbose_name='叶的类型')),
                ('phyllotaxis', models.CharField(blank=True, max_length=50, verbose_name='叶序')),
                ('vein', models.CharField(blank=True, max_length=50, verbose_name='脉序')),
                ('leafShape', models.CharField(blank=True, max_length=50, verbose_name='叶片形状')),
                ('anthotaxy', models.CharField(blank=True, max_length=50, verbose_name='花序')),
                ('fruitType', models.CharField(blank=True, max_length=50, verbose_name='果实类型')),
                ('zcnumber', models.CharField(blank=True, max_length=50, verbose_name='种子现存重量')),
                ('undernet', models.CharField(max_length=10, verbose_name='所在状况')),
                ('comment', models.CharField(blank=True, max_length=300, verbose_name='备注')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('Gtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servers.servertype')),
            ],
            options={
                'verbose_name': '种质表',
                'verbose_name_plural': '种质表',
            },
        ),
    ]
