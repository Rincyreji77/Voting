# Generated by Django 3.2.7 on 2021-10-04 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_user_details_kcno'),
    ]

    operations = [
        migrations.CreateModel(
            name='district_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=150)),
                ('district_code', models.CharField(max_length=25)),
                ('state_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='election_booth_candidate_map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_booth_master_id', models.IntegerField()),
                ('election_candidate_master_id', models.IntegerField()),
                ('list_position', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='election_booth_duty_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_booth_master_id', models.IntegerField()),
                ('uname', models.CharField(max_length=150)),
                ('passwd', models.CharField(max_length=150)),
                ('user_role', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='election_booth_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_booth_master_id', models.IntegerField()),
                ('file_name', models.CharField(max_length=150)),
                ('dt', models.CharField(max_length=15)),
                ('tm', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='election_booth_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_master_id', models.IntegerField()),
                ('booth_name', models.CharField(max_length=150)),
                ('booth_no', models.CharField(max_length=50)),
                ('addr1', models.CharField(max_length=150)),
                ('addr2', models.CharField(max_length=150)),
                ('addr3', models.CharField(max_length=150)),
                ('addr4', models.CharField(max_length=150)),
                ('pincode', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='election_booth_vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_booth_master_id', models.IntegerField()),
                ('voters_id', models.IntegerField()),
                ('election_candidate_master_id', models.IntegerField()),
                ('dt', models.CharField(max_length=15)),
                ('tm', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='election_booth_voter_map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_booth_master_id', models.IntegerField()),
                ('master_id', models.IntegerField()),
                ('voter_id', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='election_candidate_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_master_id', models.IntegerField()),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('co_name', models.CharField(max_length=150)),
                ('co_realtion', models.CharField(max_length=150)),
                ('addr1', models.CharField(max_length=150)),
                ('addr2', models.CharField(max_length=150)),
                ('addr3', models.CharField(max_length=150)),
                ('addr4', models.CharField(max_length=150)),
                ('pincode', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=15)),
                ('party_master_id', models.IntegerField()),
                ('candidate_logo', models.CharField(max_length=150)),
                ('candidate_pic', models.CharField(max_length=150)),
                ('issue_dt', models.CharField(max_length=15)),
                ('issue_tm', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='election_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_name', models.CharField(max_length=150)),
                ('state_id', models.IntegerField()),
                ('election_dt', models.CharField(max_length=15)),
                ('election_remark', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='party_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=150)),
                ('party_logo', models.CharField(max_length=150)),
                ('party_remark', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='place_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=150)),
                ('place_code', models.CharField(max_length=25)),
                ('place_type', models.CharField(max_length=25)),
                ('district_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='state_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=150)),
                ('state_code', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='voters_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_no', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('co_name', models.CharField(max_length=150)),
                ('co_relation', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=15)),
                ('addr1', models.CharField(max_length=150)),
                ('addr2', models.CharField(max_length=150)),
                ('addr3', models.CharField(max_length=150)),
                ('addr4', models.CharField(max_length=150)),
                ('pincode', models.CharField(max_length=15)),
                ('place_id', models.IntegerField()),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=150)),
                ('issue_dt', models.CharField(max_length=15)),
                ('issue_tm', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='user_login',
            name='status',
            field=models.CharField(default='ok', max_length=10),
            preserve_default=False,
        ),
    ]
