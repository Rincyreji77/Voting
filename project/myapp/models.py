from django.db import models

# Create your models here.
# 1. user_login - id, user_id, uname, passwd, u_type, status
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id}- {self.uname}'

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname


# 2. state_master - id, state_name, state_code
class state_master(models.Model):
    # id
    state_name = models.CharField(max_length=150)
    state_code = models.CharField(max_length=25)

# 3. district_master - id, district_name, district_code, state_id
class district_master(models.Model):
    #id
    district_name = models.CharField(max_length=150)
    district_code = models.CharField(max_length=25)
    state_id = models.IntegerField()

# 4. place_master - id, place_name, place_code, place_type, district_id
class place_master(models.Model):
    #id
    place_name = models.CharField(max_length=150)
    place_code = models.CharField(max_length=25)
    place_type = models.CharField(max_length=25)
    district_id = models.IntegerField()

#5. voters_master -  id, voter_no, fname, lname, co_name, co_relation, gender, dob, addr1, addr2, addr3, addr4, pincode, place_id, mobile, email, issue_dt, issue_tm, status
class voters_master(models.Model):
    #id
    voter_no = models.CharField(max_length=50)
    candidate_pic = models.CharField(max_length=150)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    co_name = models.CharField(max_length=150)
    co_relation = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=15)
    addr1 = models.CharField(max_length=150)
    addr2 = models.CharField(max_length=150)
    addr3 = models.CharField(max_length=150)
    addr4 = models.CharField(max_length=150)
    pincode = models.CharField(max_length=15)
    place_id = models.IntegerField()
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    issue_dt = models.CharField(max_length=15)
    issue_tm = models.CharField(max_length=15)
    status = models.CharField(max_length=10)

# 6. election_master - id, election_name, state_id,election_dt, election_remark, status
class election_master(models.Model):
    # id
    election_name = models.CharField(max_length=150)
    state_id = models.IntegerField()
    election_dt = models.CharField(max_length=15)
    election_remark = models.CharField(max_length=150)
    status = models.CharField(max_length=10)

# 7. election_candidate_master - id, election_master_id, fname, lname, co_name, co_realtion, addr1, addr2, addr3, addr4, pincode, email, mobile, party_master_id, candidate_logo, candidate_pic, issue_dt, issue_tm, status
class election_candidate_master(models.Model):
    #id
    election_master_id = models.IntegerField()
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    co_name = models.CharField(max_length=150)
    co_realtion = models.CharField(max_length=150)
    addr1 = models.CharField(max_length=150)
    addr2 = models.CharField(max_length=150)
    addr3 = models.CharField(max_length=150)
    addr4 = models.CharField(max_length=150)
    pincode = models.CharField(max_length=10)
    email = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15)
    party_master_id = models.IntegerField()
    place_id = models.IntegerField()
    candidate_logo = models.CharField(max_length=150)
    candidate_pic = models.CharField(max_length=150)
    issue_dt = models.CharField(max_length=15)
    issue_tm = models.CharField(max_length=15)
    status = models.CharField(max_length=10)

# 8. party_master - id, party_name, party_logo, party_remark, status
class party_master(models.Model):
    # id
    party_name = models.CharField(max_length=150)
    party_logo = models.CharField(max_length=150)
    party_remark = models.CharField(max_length=150)
    status = models.CharField(max_length=150)

# 9. election_booth_master - id, election_master_id, booth_name, booth_no, addr1, addr2, addr3, addr4, pincode, status
class election_booth_master(models.Model):
    # id
    election_master_id = models.IntegerField()
    booth_name = models.CharField(max_length=150)
    booth_no = models.CharField(max_length=50)
    addr1 = models.CharField(max_length=150)
    addr2 = models.CharField(max_length=150)
    addr3 = models.CharField(max_length=150)
    addr4 = models.IntegerField()
    pincode = models.CharField(max_length=15)
    status = models.CharField(max_length=10)

# 10. election_booth_candidate_map - id, election_booth_master_id, election_candidate_master_id, list_position, status
class election_booth_candidate_map(models.Model):
    # id
    election_booth_master_id = models.IntegerField()
    election_candidate_master_id = models.IntegerField()
    list_position = models.IntegerField()
    status = models.CharField(max_length=10)

# 11. election_booth_file - id, election_booth_master_id, file_name, dt, tm, status
class election_booth_file(models.Model):
    # id
    election_booth_master_id = models.IntegerField()
    file_name = models.CharField(max_length=150)
    dt = models.CharField(max_length=15)
    tm = models.CharField(max_length=15)
    status = models.CharField(max_length=10)

# 12. election_booth_duty_master - id, election_booth_master_id, uname, passwd, user_role, status
class election_booth_duty_master(models.Model):
    # id
    election_booth_master_id = models.IntegerField()
    uname = models.CharField(max_length=150)
    passwd = models.CharField(max_length=150)
    user_role = models.CharField(max_length=15)
    status = models.CharField(max_length=10)

# 13. election_booth_voter_map - id, election_booth_master_id, master_id,voter_id, status
class election_booth_voter_map(models.Model):
    # id
    election_booth_master_id = models.IntegerField()
    master_id = models.IntegerField()
    voter_id = models.IntegerField()
    status = models.CharField(max_length=10)

# 14. election_booth_vote - id, election_booth_master_id,voters_id, election_candidate_master_id, dt, tm, status
class election_booth_vote(models.Model):
    # id
    election_booth_master_id = models.IntegerField()
    voters_id = models.IntegerField()
    election_candidate_master_id =models.IntegerField()
    dt = models.CharField(max_length=15)
    tm = models.CharField(max_length=15)
    status = models.CharField(max_length=15)

class general_info(models.Model):
    description = models.CharField(max_length=1500)
    g_type = models.CharField(max_length=150)
    path = models.CharField(max_length=250)