# Generated by Django 2.2.1 on 2020-11-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201124_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Development_Programming', 'Development_Programming'), ('Security_Study', 'Security_Study'), ('Security_Wargame', 'Security_Wargame'), ('Other', 'Other'), ('Security_CTF', 'Security_CTF'), ('Development_Study', 'Development_Study')], default='none', max_length=100, null=True),
        ),
    ]
