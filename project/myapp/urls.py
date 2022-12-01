"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_staff_user_add', views.admin_staff_user_add, name='admin_staff_user_add'),
    path('admin_staff_user_view', views.admin_staff_user_view, name='admin_staff_user_view'),
    path('admin_staff_user_delete', views.admin_staff_user_delete, name='admin_staff_user_delete'),

    path('admin_state_master_add', views.admin_state_master_add, name='admin_state_master_add'),
    path('admin_state_master_view', views.admin_state_master_view, name='admin_state_master_view'),
    path('admin_state_master_delete', views.admin_state_master_delete, name='admin_state_master_delete'),

    path('admin_district_master_add', views.admin_district_master_add, name='admin_district_master_add'),
    path('admin_district_master_view', views.admin_district_master_view, name='admin_district_master_view'),
    path('admin_district_master_delete', views.admin_district_master_delete, name='admin_district_master_delete'),

    path('admin_place_master_add', views.admin_place_master_add, name='admin_place_master_add'),
    path('admin_place_master_view', views.admin_place_master_view, name='admin_place_master_view'),
    path('admin_place_master_delete', views.admin_place_master_delete, name='admin_place_master_delete'),

    path('admin_election_master_add', views.admin_election_master_add, name='admin_election_master_add'),
    path('admin_election_master_view', views.admin_election_master_view, name='admin_election_master_view'),
    path('admin_election_master_delete', views.admin_election_master_delete, name='admin_election_master_delete'),
    path('admin_election_master_status', views.admin_election_master_status, name='admin_election_master_status'),

    path('admin_booth_master_add', views.admin_booth_master_add, name='admin_booth_master_add'),
    path('admin_booth_master_view', views.admin_booth_master_view, name='admin_booth_master_view'),
    path('admin_booth_master_delete', views.admin_booth_master_delete, name='admin_booth_master_delete'),

    path('admin_booth_staff_master_add', views.admin_booth_staff_master_add, name='admin_booth_staff_master_add'),
    path('admin_booth_staff_master_view', views.admin_booth_staff_master_view, name='admin_booth_staff_master_view'),
    path('admin_booth_staff_master_delete', views.admin_booth_staff_master_delete, name='admin_booth_staff_master_delete'),

    path('admin_party_master_add', views.admin_party_master_add, name='admin_party_master_add'),
    path('admin_party_master_view', views.admin_party_master_view, name='admin_party_master_view'),
    path('admin_party_master_delete', views.admin_party_master_delete, name='admin_party_master_delete'),

    path('admin_candidate_view', views.admin_candidate_view, name='admin_candidate_view'),

    path('admin_booth_candidate_master_view', views.admin_booth_candidate_master_view, name='admin_booth_candidate_master_view'),
    path('admin_booth_candidate_vote_view', views.admin_booth_candidate_vote_view, name='admin_booth_candidate_vote_view'),

    path('admin_booth_voter_master_view', views.admin_booth_voter_master_view, name='admin_booth_voter_master_view'),

    path('admin_election_result_view', views.admin_election_result_view, name='admin_election_result_view'),

    path('admin_general_info_add', views.admin_general_info_add, name='admin_general_info_add'),
    path('admin_general_info_view', views.admin_general_info_view, name='admin_general_info_view'),
    path('admin_general_info_delete', views.admin_general_info_delete, name='admin_general_info_delete'),

    path('staff_login', views.staff_login_check, name='staff_login'),
    path('staff_logout', views.staff_logout, name='staff_logout'),
    path('staff_home', views.staff_home, name='staff_home'),
    path('staff_changepassword', views.staff_changepassword, name='staff_changepassword'),

    path('staff_election_master_view', views.staff_election_master_view, name='staff_election_master_view'),

    path('staff_voter_add', views.staff_voter_add, name='staff_voter_add'),
    path('staff_voter_delete', views.staff_voter_delete, name='staff_voter_delete'),
    path('staff_voter_view', views.staff_voter_view, name='staff_voter_view'),
    path('staff_voter_search', views.staff_voter_search, name='staff_voter_search'),

    path('staff_candidate_add', views.staff_candidate_add, name='staff_candidate_add'),
    path('staff_candidate_delete', views.staff_candidate_delete, name='staff_candidate_delete'),
    path('staff_candidate_view', views.staff_candidate_view, name='staff_candidate_view'),
    path('staff_candidate_search', views.staff_candidate_search, name='staff_candidate_search'),

    path('staff_booth_master_view', views.staff_booth_master_view, name='staff_booth_master_view'),

    path('staff_booth_candidate_master_add', views.staff_booth_candidate_master_add, name='staff_booth_candidate_master_add'),
    path('staff_booth_candidate_master_view', views.staff_booth_candidate_master_view, name='staff_booth_candidate_master_view'),
    path('staff_booth_candidate_master_delete', views.staff_booth_candidate_master_delete, name='staff_booth_candidate_master_delete'),

    path('staff_booth_voter_master_add', views.staff_booth_voter_master_add, name='staff_booth_voter_master_add'),
    path('staff_booth_voter_master_view', views.staff_booth_voter_master_view, name='staff_booth_voter_master_view'),
    path('staff_booth_voter_master_delete', views.staff_booth_voter_master_delete, name='staff_booth_voter_master_delete'),

    path('staff_election_result_view', views.staff_election_result_view, name='staff_election_result_view'),

    path('staff_general_info_view', views.staff_general_info_view, name='staff_general_info_view'),

    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('user_election_master_view', views.user_election_master_view, name='user_election_master_view'),
    path('user_booth_candidate_master_view', views.user_booth_candidate_master_view, name='user_booth_candidate_master_view'),
    path('user_booth_candidate_master_vote', views.user_booth_candidate_master_vote, name='user_booth_candidate_master_vote'),

    path('user_general_info_view', views.user_general_info_view, name='user_general_info_view'),
    path('user_election_result_view', views.user_election_result_view, name='user_election_result_view'),
]
