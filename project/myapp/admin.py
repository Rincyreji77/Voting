from django.contrib import admin

# Register your models here.
from .models import user_login, user_details
from.models import state_master,district_master,place_master,voters_master,election_master
from.models import election_candidate_master,party_master ,election_booth_master ,election_booth_candidate_map
from.models import election_booth_file ,election_booth_duty_master ,election_booth_voter_map ,election_booth_vote


admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(state_master)
admin.site.register(district_master)
admin.site.register(place_master)
admin.site.register(voters_master)
admin.site.register(election_master)
admin.site.register(election_candidate_master)
admin.site.register(party_master)
admin.site.register(election_booth_master)
admin.site.register(election_booth_candidate_map)
admin.site.register(election_booth_file)
admin.site.register(election_booth_duty_master)
admin.site.register(election_booth_voter_map)
admin.site.register(election_booth_vote)