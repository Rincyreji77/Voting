from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login, user_details
from.models import state_master,district_master,place_master,voters_master,election_master
from.models import election_candidate_master,party_master ,election_booth_master ,election_booth_candidate_map
from.models import election_booth_file ,election_booth_duty_master ,election_booth_voter_map ,election_booth_vote

from datetime import datetime
from django.core.files.storage import FileSystemStorage
import os
from project.settings import BASE_DIR

def index(request):
    return render(request, './myapp/index.html')

def about(request):
    return render(request, './myapp/about.html')

def contact(request):
    return render(request, './myapp/contact.html')

################################# ADMIN #########################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1 style="color:black;font-size:20px;"> Invalid Uname or Password</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)

def admin_staff_user_add(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('password')
        u_type = 'staff'
        status='ok'
        ul = user_login(uname=uname,passwd=passwd,u_type=u_type,status=status)
        ul.save()
        context = {'msg':'Staff registered'}
        return render(request, 'myapp/admin_staff_user_add.html', context)

    else:
        return render(request, 'myapp/admin_staff_user_add.html')

def admin_staff_user_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = user_login.objects.get(id=int(id))
    nm.delete()

    nm_l = user_login.objects.filter(u_type='staff')
    context ={'staff_list':nm_l}
    return render(request,'myapp/admin_staff_user_view.html',context)

def admin_staff_user_view(request):
    nm_l = user_login.objects.filter(u_type='staff')
    context = {'staff_list': nm_l}
    return render(request, 'myapp/admin_staff_user_view.html', context)


def admin_state_master_add(request):
    if request.method == 'POST':
        state_name = request.POST.get('state_name')
        state_code = request.POST.get('state_code')
        l_s = state_master(state_name=state_name, state_code=state_code)
        l_s.save()
        context = {'msg': 'New state added'}
        return render(request, 'myapp/admin_state_master_add.html',context)

    else:
        return render(request, 'myapp/admin_state_master_add.html')

def admin_state_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    l_s = state_master.objects.get(id=int(id))
    l_s.delete()

    state_list = state_master.objects.all()
    context ={'state_list':state_list, 'msg':'State Deleted'}
    return render(request,'myapp/admin_state_master_view.html',context)

def admin_state_master_view(request):
    state_list = state_master.objects.all()
    context = {'state_list': state_list, 'msg': ''}
    return render(request, 'myapp/admin_state_master_view.html', context)


def admin_district_master_add(request):
    if request.method == 'POST':
        district_name = request.POST.get('district_name')
        district_code = request.POST.get('district_code')
        state_id = request.POST.get('state_id')
        l_s = district_master(district_name=district_name, district_code=district_code, state_id=int(state_id))
        l_s.save()
        context = {'msg': 'New district added', 'state_id':state_id }
        return render(request, 'myapp/admin_district_master_add.html',context)

    else:
        state_id = request.GET.get('state_id')
        context = {'msg': '', 'state_id': state_id}
        return render(request, 'myapp/admin_district_master_add.html',context)

def admin_district_master_delete(request):
    id = request.GET.get('id')

    print("id="+id)

    l_s = district_master.objects.get(id=int(id))
    l_s.delete()

    state_id = request.GET.get('state_id')
    district_list = district_master.objects.filter(state_id=int(state_id))
    state_list = state_master.objects.all()
    context ={'district_list':district_list, 'msg':'District Deleted', 'state_id':state_id,'state_list':state_list}
    return render(request,'myapp/admin_district_master_view.html',context)

def admin_district_master_view(request):
    state_id = request.GET.get('state_id')
    district_list = district_master.objects.filter(state_id=int(state_id))
    state_list = state_master.objects.all()
    context = {'district_list': district_list, 'msg': '', 'state_id': state_id, 'state_list':state_list}
    return render(request, 'myapp/admin_district_master_view.html', context)

def admin_place_master_add(request):
    if request.method == 'POST':
        place_name = request.POST.get('place_name')
        place_code = request.POST.get('place_code')
        place_type = request.POST.get('place_type')
        district_id = request.POST.get('district_id')
        l_s = place_master(place_name=place_name, place_code=place_code,
                              place_type=place_type, district_id=int(district_id))
        l_s.save()
        context = {'msg': 'New place added', 'district_id':district_id }
        return render(request, 'myapp/admin_place_master_add.html',context)

    else:
        district_id = request.GET.get('district_id')
        context = {'msg': '', 'district_id': district_id}
        return render(request, 'myapp/admin_place_master_add.html',context)

def admin_place_master_delete(request):
    id = request.GET.get('id')

    print("id="+id)

    l_s = place_master.objects.get(id=int(id))
    l_s.delete()

    district_id = request.GET.get('district_id')
    place_list = place_master.objects.filter(district_id=int(district_id))
    district_list = district_master.objects.all()
    context ={'district_list':district_list, 'msg':'Place Deleted',
              'district_id':district_id,'place_list':place_list}
    return render(request,'myapp/admin_place_master_view.html',context)

def admin_place_master_view(request):
    district_id = request.GET.get('district_id')
    place_list = place_master.objects.filter(district_id=int(district_id))
    district_list = district_master.objects.all()
    context = {'district_list': district_list, 'msg': '',
               'district_id': district_id, 'place_list': place_list}
    return render(request, 'myapp/admin_place_master_view.html', context)


def admin_election_master_add(request):
    if request.method == 'POST':
        election_name = request.POST.get('election_name')
        election_dt = request.POST.get('election_dt')
        election_remark = request.POST.get('election_remark')
        state_id = int(request.POST.get('state_id'))
        status='ok'
        data_obj = election_master(election_name=election_name, state_id=state_id,
                                   election_dt=election_dt, election_remark=election_remark,
                                   status=status)
        data_obj.save()
        state_list = state_master.objects.all()
        context = {'state_list': state_list ,'msg':'Record added'}
        return render(request, 'myapp/admin_election_master_add.html', context)
    else:
        state_list = state_master.objects.all()
        context = {'state_list': state_list, 'msg': ''}
        return render(request, 'myapp/admin_election_master_add.html', context)

def admin_election_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    lm = election_master.objects.get(id=int(id))
    lm.delete()

    state_id = request.GET.get('state_id')
    election_list = election_master.objects.all()
    state_list = state_master.objects.all()
    context = {'election_list':election_list,'state_list':state_list,'msg':'Record deleted','state_id':state_id}
    return render(request,'myapp/admin_election_master_view.html',context)

def admin_election_master_status(request):
    id = request.GET.get('id')
    status=request.GET.get('status')
    print("id="+id)
    lm = election_master.objects.get(id=int(id))
    lm.status=status
    lm.save()

    state_id = request.GET.get('state_id')
    election_list = election_master.objects.all()
    state_list = state_master.objects.all()
    context = {'election_list':election_list,'state_list':state_list,'msg':'Record '+status,'state_id':state_id}
    return render(request,'myapp/admin_election_master_view.html',context)

def admin_election_master_view(request):
    state_id = request.GET.get('state_id')
    election_list = election_master.objects.all()
    state_list = state_master.objects.all()
    context = {'election_list':election_list,'state_list':state_list,'msg':'','state_id':state_id}
    return render(request,'myapp/admin_election_master_view.html',context)

def admin_booth_master_add(request):
    if request.method == 'POST':
        booth_name = request.POST.get('booth_name')
        booth_no = request.POST.get('booth_no')
        addr1 = request.POST.get('addr1')
        addr2 = request.POST.get('addr2')
        addr3 = request.POST.get('addr3')
        addr4 = request.POST.get('addr4')
        pincode = request.POST.get('pincode')

        election_master_id = int(request.POST.get('election_master_id'))
        status='ok'
        data_obj = election_booth_master(booth_name=booth_name,
                                    election_master_id=election_master_id,
                                    booth_no=booth_no, addr1=addr1,addr2=addr2,
                                    addr3=addr3,addr4=int(addr4),pincode=pincode,
                                   status=status)
        data_obj.save()
        place_list = place_master.objects.all()
        context = {'msg':'Record added','election_master_id':election_master_id,'place_list':place_list}
        return render(request, 'myapp/admin_booth_master_add.html', context)
    else:
        election_master_id = int(request.GET.get('election_master_id'))
        place_list = place_master.objects.all()
        context = {'election_master_id': election_master_id, 'msg': '','place_list':place_list}
        return render(request, 'myapp/admin_booth_master_add.html', context)

def admin_booth_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    lm = election_booth_master.objects.get(id=int(id))
    lm.delete()

    election_master_id = int(request.GET.get('election_master_id'))
    booth_list = election_booth_master.objects.filter(election_master_id=election_master_id)
    place_list = place_master.objects.all()
    context = {'booth_list':booth_list,'election_master_id':election_master_id,
               'msg':'Record deleted','place_list':place_list}
    return render(request,'myapp/admin_booth_master_view.html',context)

def admin_booth_master_view(request):
    election_master_id = int(request.GET.get('election_master_id'))
    booth_list = election_booth_master.objects.filter(election_master_id=election_master_id)
    place_list = place_master.objects.all()
    context = {'booth_list': booth_list, 'election_master_id': election_master_id,
               'msg': '','place_list':place_list}
    return render(request, 'myapp/admin_booth_master_view.html', context)


def admin_booth_staff_master_add(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = ''#request.POST.get('booth_no')
        user_role = request.POST.get('user_role')


        election_booth_master_id = int(request.POST.get('election_booth_master_id'))
        status='ok'
        data_obj = election_booth_duty_master(uname=uname,
                                    election_booth_master_id=election_booth_master_id,
                                    passwd=passwd, user_role=user_role,
                                   status=status)
        data_obj.save()
        user_list = user_login.objects.filter(u_type='staff')
        context = {'msg':'Record added','election_booth_master_id':election_booth_master_id,'user_list':user_list}
        return render(request, 'myapp/admin_booth_staff_master_add.html', context)
    else:
        election_booth_master_id = int(request.GET.get('election_booth_master_id'))
        user_list = user_login.objects.filter(u_type='staff')
        context = {'election_booth_master_id': election_booth_master_id, 'msg': '','user_list':user_list}
        return render(request, 'myapp/admin_booth_staff_master_add.html', context)

def admin_booth_staff_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    lm = election_booth_duty_master.objects.get(id=int(id))
    lm.delete()

    election_booth_master_id = int(request.GET.get('election_booth_master_id'))
    staff_list = election_booth_duty_master.objects.filter(election_booth_master_id=election_booth_master_id)
    user_list = user_login.objects.filter(u_type='staff')
    context = {'staff_list':staff_list,'election_booth_master_id':election_booth_master_id,
               'msg':'Record deleted','user_list':user_list}
    return render(request,'myapp/admin_booth_staff_master_view.html',context)

def admin_booth_staff_master_view(request):
    election_booth_master_id = int(request.GET.get('election_booth_master_id'))
    staff_list = election_booth_duty_master.objects.filter(election_booth_master_id=election_booth_master_id)
    user_list = user_login.objects.filter (u_type='staff')
    context = {'staff_list': staff_list, 'election_booth_master_id': election_booth_master_id,
               'msg': '', 'user_list': user_list}
    return render(request, 'myapp/admin_booth_staff_master_view.html', context)


def admin_party_master_add(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        party_logo = fs.save(uploaded_file.name, uploaded_file)
        party_name = request.POST.get('party_name')
        party_remark = request.POST.get('party_remark')

#        dt = datetime.today().strftime('%Y-%m-%d')
#        tm = datetime.today().strftime('%H:%M:%S')
        status='ok'
        data_obj = party_master(party_remark=party_remark, party_logo=party_logo,
                              party_name=party_name, status=status)
        data_obj.save()
        context = {'msg':'Party uploaded'}
        return render(request, 'myapp/admin_party_master_add.html',context)
    else:
        context = {}
        return render(request, 'myapp/admin_party_master_add.html',context)


def admin_party_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    lm = party_master.objects.get(id=int(id))
    lm.delete()
    party_list = party_master.objects.all()
    context = {'party_list':party_list, 'msg': 'Party Deleted'}
    return render(request,'myapp/admin_party_master_view.html',context)

def admin_party_master_view(request):
    party_list = party_master.objects.all()
    context = {'party_list': party_list, 'msg': ''}
    return render(request, 'myapp/admin_party_master_view.html', context)

def admin_candidate_view(request):
    election_master_id = request.GET.get('election_master_id')
    candidate_list = election_candidate_master.objects.filter(election_master_id=int(election_master_id))
    party_list = party_master.objects.all()
    election_list = election_master.objects.all()
    place_list = place_master.objects.all()
    context = {'candidate_list':candidate_list,'type':'Candidate Details','place_list':place_list,
               'party_list':party_list,'election_list':election_list,'election_master_id':election_master_id}
    return render(request, './myapp/admin_candidate_view.html',context)


def admin_booth_candidate_master_view(request):
    election_booth_master_id = int(request.GET.get('election_booth_master_id'))
    booth_candidate_list = election_booth_candidate_map.objects.filter(
        election_booth_master_id=election_booth_master_id)
    booth = election_booth_master.objects.get(id=election_booth_master_id)
    candidate_list = election_candidate_master.objects.filter(place_id=booth.addr4)
    context = {'booth_candidate_list': booth_candidate_list, 'election_booth_master_id': election_booth_master_id,
               'msg': '', 'candidate_list': candidate_list}
    return render(request, 'myapp/admin_booth_candidate_master_view.html', context)

def admin_booth_voter_master_view(request):
    election_booth_master_id = int(request.GET.get('election_booth_master_id'))
    booth_voter_list = election_booth_voter_map.objects.filter(election_booth_master_id=election_booth_master_id)
    booth = election_booth_master.objects.get(id=election_booth_master_id)
    voter_list = voters_master.objects.filter(place_id=booth.addr4)
    context = {'booth_voter_list': booth_voter_list, 'election_booth_master_id': election_booth_master_id,
               'msg': '', 'voter_list': voter_list}
    return render(request, 'myapp/admin_booth_voter_master_view.html', context)

def admin_booth_candidate_vote_view(request):
    election_booth_master_id = int(request.GET.get('election_booth_master_id'))
    booth_candidate_list = election_booth_candidate_map.objects.filter(
        election_booth_master_id=election_booth_master_id)
    booth = election_booth_master.objects.get(id=election_booth_master_id)

    vote_l = election_booth_vote.objects.filter(election_booth_master_id=election_booth_master_id)
    vote_list = []
    c_vote = {}
    for bcl in booth_candidate_list:
        c_vote[bcl.election_candidate_master_id] = 0
    for vote in vote_l:
        cnt = c_vote.get(vote.election_candidate_master_id, 0)
        c_vote[vote.election_candidate_master_id]=cnt + 1
    print(c_vote)
    for key, value in c_vote.items():
        vote_list.append({'id':key,'vote':value})
        print(key, value)

    candidate_list = election_candidate_master.objects.filter(place_id=booth.addr4)
    context = {'booth_candidate_list': booth_candidate_list, 'election_booth_master_id': election_booth_master_id,
               'msg': '', 'candidate_list': candidate_list,'vote_list':vote_list}
    return render(request, 'myapp/admin_booth_candidate_vote_view.html', context)

def admin_election_result_view(request):
    election_master_id = request.GET.get('election_master_id')
    district_list = district_master.objects.all()
    candidate_list = election_candidate_master.objects.filter(election_master_id=int(election_master_id))
    party_list = party_master.objects.all()
    election_list = election_master.objects.all()
    place_list = place_master.objects.all()
    ################Vote Counting ################
    booth_list = election_booth_master.objects.filter(election_master_id=election_master_id)
    vote_list = []
    c_vote = {}
    for boot in booth_list:
        vote_l = election_booth_vote.objects.filter(election_booth_master_id=boot.id)
        booth_candidate_list = election_booth_candidate_map.objects.filter(
            election_booth_master_id=boot.id)
        for bcl in booth_candidate_list:
            c_vote[bcl.election_candidate_master_id] = c_vote.get(bcl.election_candidate_master_id, 0)
        for vote in vote_l:
            cnt = c_vote.get(vote.election_candidate_master_id, 0)
            c_vote[vote.election_candidate_master_id] = cnt + 1
        print(c_vote)
    for key, value in c_vote.items():
        vote_list.append({'id': key, 'vote': value})
        print(key, value)

    ################################################

    context = {'candidate_list':candidate_list,'type':'Election Result',
               'place_list':place_list,'district_list':district_list,
               'party_list':party_list,'election_list':election_list,
                'election_master_id':election_master_id,'vote_list':vote_list}
    return render(request, './myapp/admin_election_result_view.html',context)


from .models import general_info
from django.core.files.storage import FileSystemStorage

def admin_general_info_add(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)

        description = request.POST.get('description')
        g_type = request.POST.get('g_type')

        gi = general_info(description=description,g_type=g_type,path=path)
        gi.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/admin_general_info_add.html', context)
    else:
        return render(request, './myapp/admin_general_info_add.html')


def admin_general_info_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    id = request.GET.get('id')
    print('id = '+id)
    gi = general_info.objects.get(id=int(id))
    gi.delete()
    msg = 'Record Deleted'
    gi_l = general_info.objects.all()
    context = {'info_list': gi_l,'msg':msg}
    return render(request, './myapp/admin_general_info_view.html',context)

def admin_general_info_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    gi_l = general_info.objects.all()
    context = {'info_list':gi_l}
    return render(request, './myapp/admin_general_info_view.html',context)

#####################################STAFF #################################
def staff_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='staff')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/staff_home.html',context)
        else:
            context = {'msg': 'Invalid Uname or Password'}
            return render(request, 'myapp/staff_login.html',context)
    else:
        return render(request, 'myapp/staff_login.html')

def staff_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/staff_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def staff_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/staff_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/staff_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/staff_changepassword.html', context)
    else:
        return render(request, './myapp/staff_changepassword.html')



def staff_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return staff_login_check(request)
    else:
        return staff_login_check(request)

def staff_election_master_view(request):
    state_id = request.GET.get('state_id')
    election_list = election_master.objects.all()
    state_list = state_master.objects.all()
    context = {'election_list':election_list,'state_list':state_list,'msg':'','state_id':state_id}
    return render(request,'myapp/staff_election_master_view.html',context)

def staff_voter_add(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        candidate_pic = fs.save(uploaded_file.name, uploaded_file)

        voter_no = request.POST.get('voter_no')
        place_id = request.POST.get('place_id')

        fname = request.POST.get('fname')
        co_relation = request.POST.get('co_relation')

        co_name = request.POST.get('co_name')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr1 = request.POST.get('addr1')
        addr2 = request.POST.get('addr2')
        addr3 = request.POST.get('addr3')
        addr4 = request.POST.get('addr4')
        pincode = request.POST.get('pincode')
        email = request.POST.get('email')
        mobile = request.POST.get('contact')

        issue_dt = datetime.today().strftime('%Y-%m-%d')
        issue_tm = datetime.today().strftime('%H:%M:%S')
        status = "new"
        ud = voters_master(voter_no=voter_no,candidate_pic=candidate_pic,
                           fname=fname, lname=lname, co_name=co_name,
                           co_relation=co_relation, gender=gender, dob=dob,
                           addr4=addr4, addr1=addr1, addr2=addr2, addr3=addr3,
                           place_id=int(place_id), pincode=pincode, mobile=mobile,
                           email=email, issue_dt=issue_dt, issue_tm=issue_tm, status=status )
        ud.save()
        place_list = place_master.objects.all()
        context = {'msg': 'Voter Registered','place_list':place_list}
        return render(request, 'myapp/staff_voter_add.html',context)

    else:
        place_list = place_master.objects.all()
        context = {'msg': '', 'place_list': place_list}
        return render(request, 'myapp/staff_voter_add.html', context)


def staff_voter_view(request):
    voter_list = voters_master.objects.all()
    place_list = place_master.objects.all()
    context = {'voter_list':voter_list,'type':'Voter Details','place_list':place_list}
    return render(request, './myapp/staff_voter_view.html',context)

def staff_voter_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = voters_master.objects.get(id=int(id))
    nm.delete()
    voter_list = voters_master.objects.all()
    place_list = place_master.objects.all()
    context = {'voter_list': voter_list, 'type': 'Voter Details',
               'place_list': place_list,'msg':'Voter Deleted'}
    return render(request, './myapp/staff_voter_view.html', context)

def staff_voter_search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        voter_list = voters_master.objects.filter(voter_no__contains=query)
        place_list = place_master.objects.all()
        context = {'voter_list': voter_list, 'type': 'Voter Details',
                   'place_list': place_list, 'msg': ''}
        return render(request, './myapp/staff_voter_view.html', context)

    else:
        context = {}
        return render(request, './myapp/staff_voter_search.html', context)

def staff_candidate_add(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        uploaded_file1 = request.FILES['document1']
        candidate_pic = fs.save(uploaded_file1.name, uploaded_file1)

        uploaded_file2 = request.FILES['document2']
        candidate_logo = fs.save(uploaded_file2.name, uploaded_file2)
        place_id = request.POST.get('place_id')
        election_master_id = request.POST.get('election_master_id')
        party_master_id = request.POST.get('party_master_id')

        fname = request.POST.get('fname')
        co_relation = request.POST.get('co_relation')

        co_name = request.POST.get('co_name')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr1 = request.POST.get('addr1')
        addr2 = request.POST.get('addr2')
        addr3 = request.POST.get('addr3')
        addr4 = request.POST.get('addr4')
        pincode = request.POST.get('pincode')
        email = request.POST.get('email')
        mobile = request.POST.get('contact')

        issue_dt = datetime.today().strftime('%Y-%m-%d')
        issue_tm = datetime.today().strftime('%H:%M:%S')
        status = "new"
        ud = election_candidate_master(election_master_id=int(election_master_id),
                                       candidate_logo=candidate_logo,candidate_pic=candidate_pic,
                            fname=fname, lname=lname, co_name=co_name,
                            co_realtion=co_relation,place_id=place_id,
                            addr4=addr4, addr1=addr1, addr2=addr2, addr3=addr3,
                            party_master_id=int(party_master_id), pincode=pincode, mobile=mobile,
                            email=email, issue_dt=issue_dt, issue_tm=issue_tm, status=status )
        ud.save()
        place_list = place_master.objects.all()
        party_list = party_master.objects.all()
        context = {'msg': 'Candidate Registered','party_list':party_list,'place_list':place_list,
                   'election_master_id':election_master_id}
        return render(request, 'myapp/staff_candidate_add.html',context)

    else:
        place_list = place_master.objects.all()
        election_master_id = request.GET.get('election_master_id')
        party_list = party_master.objects.all()
        context = {'msg': '', 'party_list': party_list,'place_list':place_list,
                   'election_master_id': election_master_id}
        return render(request, 'myapp/staff_candidate_add.html', context)


def staff_candidate_view(request):
    election_master_id = request.GET.get('election_master_id')
    candidate_list = election_candidate_master.objects.filter(election_master_id=int(election_master_id))
    party_list = party_master.objects.all()
    election_list = election_master.objects.all()
    place_list = place_master.objects.all()
    context = {'candidate_list':candidate_list,'type':'Candidate Details','place_list':place_list,
               'party_list':party_list,'election_list':election_list,'election_master_id':election_master_id}
    return render(request, './myapp/staff_candidate_view.html',context)

def staff_candidate_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = election_candidate_master.objects.get(id=int(id))
    nm.delete()
    election_master_id = request.GET.get('election_master_id')
    candidate_list = election_candidate_master.objects.filter(election_master_id=int(election_master_id))
    party_list = party_master.objects.all()
    election_list = election_master.objects.all()
    place_list = place_master.objects.all()
    context = {'candidate_list': candidate_list, 'type': 'Candidate Details','place_list':place_list,
               'party_list': party_list, 'election_list': election_list, 'election_master_id': election_master_id}
    return render(request, './myapp/staff_candidate_view.html', context)


def staff_candidate_search(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        election_master_id = request.POST.get('election_master_id')
        candidate_list = election_candidate_master.objects.filter(election_master_id=int(election_master_id),
                                                                  fname__contains=fname,
                                                                  lname__contains=lname)
        party_list = party_master.objects.all()
        election_list = election_master.objects.all()
        place_list = place_master.objects.all()
        context = {'candidate_list': candidate_list, 'type': 'Candidate Details',
                   'party_list': party_list, 'election_list': election_list,'place_list':place_list,
                   'election_master_id': election_master_id}
        return render(request, './myapp/staff_candidate_view.html', context)

    else:
        election_list = election_master.objects.all()
        context = {'election_list':election_list}
        return render(request, './myapp/staff_candidate_search.html', context)

def staff_booth_master_view(request):
    election_master_id = int(request.GET.get('election_master_id'))
    user_name = request.session['user_name']
    duty_list = election_booth_duty_master.objects.filter(uname=user_name)
    booth_list = []
    for duty in duty_list:
        booth = election_booth_master.objects.get(id=duty.election_booth_master_id)
        booth_list.append(booth)
    place_list = place_master.objects.all()
    context = {'booth_list': booth_list, 'election_master_id': election_master_id,
               'msg': '','place_list':place_list}
    return render(request, 'myapp/staff_booth_master_view.html', context)

def staff_booth_candidate_master_add(request):
    if request.method == 'POST':
        election_candidate_master_id = request.POST.get('election_candidate_master_id')
        list_position = 0#request.POST.get('booth_no')
        election_booth_master_id = int(request.POST.get('election_booth_master_id'))

        status='ok'
        data_obj = election_booth_candidate_map(election_candidate_master_id=int(election_candidate_master_id),
                                    election_booth_master_id=election_booth_master_id,
                                    list_position=int(list_position),
                                   status=status)
        data_obj.save()
        booth = election_booth_master.objects.get(id=election_booth_master_id)
        candidate_list = election_candidate_master.objects.filter(place_id=booth.addr4)
        context = {'msg':'Record added','election_booth_master_id':election_booth_master_id,
                   'candidate_list':candidate_list}
        return render(request, 'myapp/staff_booth_candidate_master_add.html', context)
    else:
        election_booth_master_id = int(request.GET.get('election_booth_master_id'))
        booth = election_booth_master.objects.get(id=election_booth_master_id)
        candidate_list = election_candidate_master.objects.filter(place_id=booth.addr4)

        context = {'election_booth_master_id': election_booth_master_id, 'msg': '',
                   'candidate_list':candidate_list}
        return render(request, 'myapp/staff_booth_candidate_master_add.html', context)

def staff_booth_candidate_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    lm = election_booth_candidate_map.objects.get(id=int(id))
    lm.delete()

    election_booth_master_id = int(request.GET.get('election_booth_master_id'))
    booth_candidate_list = election_booth_candidate_map.objects.filter(election_booth_master_id=election_booth_master_id)
    booth = election_booth_master.objects.get(id=election_booth_master_id)
    candidate_list = election_candidate_master.objects.filter(place_id=booth.addr4)
    context = {'booth_candidate_list':booth_candidate_list,'election_booth_master_id':election_booth_master_id,
               'msg':'Record deleted','candidate_list':candidate_list}
    return render(request,'myapp/staff_booth_candidate_master_view.html',context)

def staff_booth_candidate_master_view(request):
    election_booth_master_id = int(request.GET.get('election_booth_master_id'))
    booth_candidate_list = election_booth_candidate_map.objects.filter(
        election_booth_master_id=election_booth_master_id)
    booth = election_booth_master.objects.get(id=election_booth_master_id)
    candidate_list = election_candidate_master.objects.filter(place_id=booth.addr4)
    context = {'booth_candidate_list': booth_candidate_list, 'election_booth_master_id': election_booth_master_id,
               'msg': '', 'candidate_list': candidate_list}
    return render(request, 'myapp/staff_booth_candidate_master_view.html', context)

def staff_booth_voter_master_add(request):
    if request.method == 'POST':
        voter_id = request.POST.get('voter_id')

        election_booth_master_id = int(request.POST.get('election_booth_master_id'))
        ebm = election_booth_master.objects.get(id=election_booth_master_id)
        master_id = ebm.election_master_id
        status='ok'
        data_obj = election_booth_voter_map(voter_id=int(voter_id),
                                    election_booth_master_id=election_booth_master_id,
                                    master_id=master_id,
                                   status=status)
        data_obj.save()
        booth = election_booth_master.objects.get(id=election_booth_master_id)
        voter_list = voters_master.objects.filter(place_id=booth.addr4)
        context = {'msg':'Record added','election_booth_master_id':election_booth_master_id,
                   'voter_list':voter_list}
        return render(request, 'myapp/staff_booth_voter_master_add.html', context)
    else:
        election_booth_master_id = int(request.GET.get('election_booth_master_id'))
        booth = election_booth_master.objects.get(id=election_booth_master_id)
        voter_list = voters_master.objects.filter(place_id=booth.addr4)

        context = {'election_booth_master_id': election_booth_master_id, 'msg': '',
                   'voter_list':voter_list}
        return render(request, 'myapp/staff_booth_voter_master_add.html', context)

def staff_booth_voter_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    lm = election_booth_voter_map.objects.get(id=int(id))
    lm.delete()

    election_booth_master_id = int(request.GET.get('election_booth_master_id'))
    booth_voter_list = election_booth_voter_map.objects.filter(election_booth_master_id=election_booth_master_id)
    booth = election_booth_master.objects.get(id=election_booth_master_id)
    voter_list = voters_master.objects.filter(place_id=booth.addr4)
    context = {'booth_voter_list':booth_voter_list,'election_booth_master_id':election_booth_master_id,
               'msg':'Record deleted','voter_list':voter_list}
    return render(request,'myapp/staff_booth_voter_master_view.html',context)

def staff_booth_voter_master_view(request):
    election_booth_master_id = int(request.GET.get('election_booth_master_id'))
    booth_voter_list = election_booth_voter_map.objects.filter(election_booth_master_id=election_booth_master_id)
    booth = election_booth_master.objects.get(id=election_booth_master_id)
    voter_list = voters_master.objects.filter(place_id=booth.addr4)
    context = {'booth_voter_list': booth_voter_list, 'election_booth_master_id': election_booth_master_id,
               'msg': '', 'voter_list': voter_list}
    return render(request, 'myapp/staff_booth_voter_master_view.html', context)

def staff_election_result_view(request):
    election_master_id = request.GET.get('election_master_id')
    e_obj = election_master.objects.get(id=election_master_id)
    if e_obj.status == 'publish':
        district_list = district_master.objects.all()
        candidate_list = election_candidate_master.objects.filter(election_master_id=int(election_master_id))
        party_list = party_master.objects.all()
        election_list = election_master.objects.all()
        place_list = place_master.objects.all()
        ################Vote Counting ################
        booth_list = election_booth_master.objects.filter(election_master_id=election_master_id)
        vote_list = []
        c_vote = {}
        for boot in booth_list:
            vote_l = election_booth_vote.objects.filter(election_booth_master_id=boot.id)
            booth_candidate_list = election_booth_candidate_map.objects.filter(
                election_booth_master_id=boot.id)
            for bcl in booth_candidate_list:
                c_vote[bcl.election_candidate_master_id] = c_vote.get(bcl.election_candidate_master_id, 0)
            for vote in vote_l:
                cnt = c_vote.get(vote.election_candidate_master_id, 0)
                c_vote[vote.election_candidate_master_id] = cnt + 1
            print(c_vote)
        for key, value in c_vote.items():
            vote_list.append({'id': key, 'vote': value})
            print(key, value)
        ################################################

        context = {'candidate_list':candidate_list,'type':'Election Result',
               'place_list':place_list,'district_list':district_list,
               'party_list':party_list,'election_list':election_list,
                'election_master_id':election_master_id,'vote_list':vote_list}
        return render(request, './myapp/staff_election_result_view.html',context)
    else:
        election_list = election_master.objects.all()
        state_list = state_master.objects.all()
        context = {'election_list': election_list, 'state_list': state_list, 'msg': 'Result Not Published'}
        return render(request, './myapp/staff_election_master_view.html', context)


def staff_general_info_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return user_login_check(request)

    gi_l = general_info.objects.all()
    context = {'info_list':gi_l}
    return render(request, './myapp/staff_general_info_view.html',context)


########################### USER ##############################
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = voters_master.objects.filter(voter_no=uname, email=passwd)
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].voter_no
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, age=age,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)


def user_election_master_view(request):
    state_id = request.GET.get('state_id')
    election_list = election_master.objects.all()
    state_list = state_master.objects.all()
    context = {'election_list':election_list,'state_list':state_list,'msg':'','state_id':state_id}
    return render(request,'myapp/user_election_master_view.html',context)

def user_booth_candidate_master_view(request):
    election_master_id = int(request.GET.get('election_master_id'))
    voter_id = int(request.session['user_id'])
    evm = election_booth_voter_map.objects.get(voter_id=voter_id,master_id=election_master_id)
    election_booth_master_id = evm.election_booth_master_id

    ebv = election_booth_vote.objects.filter(election_booth_master_id=election_booth_master_id,voters_id=voter_id)
    if len(ebv) != 0:
        context = {'msg': 'Vote Already Registered'}
        return render(request, 'myapp/user_messages.html', context)

    booth_candidate_list = election_booth_candidate_map.objects.filter(
        election_booth_master_id=election_booth_master_id)
    booth = election_booth_master.objects.get(id=election_booth_master_id)
    candidate_list = election_candidate_master.objects.filter(place_id=booth.addr4)
    context = {'booth_candidate_list': booth_candidate_list, 'election_booth_master_id': election_booth_master_id,
               'msg': '', 'candidate_list': candidate_list}
    return render(request, 'myapp/user_booth_candidate_master_view.html', context)


from .Blockchain import Blockchain
import os
def user_booth_candidate_master_vote(request):
    id = request.GET.get('id')
    voter_id = int(request.session['user_id'])
    election_booth_master_id = int(request.GET.get('election_booth_master_id'))
    lm = election_booth_candidate_map.objects.get(id=int(id))
    election_candidate_master_id = lm.election_candidate_master_id
    dt = datetime.today().strftime('%Y-%m-%d')
    tm = datetime.today().strftime('%H:%M:%S')
    status = 'voted'
    vote = election_booth_vote(election_booth_master_id=election_booth_master_id,
                                    voters_id=voter_id,
                                    election_candidate_master_id=election_candidate_master_id,
                                    dt=dt,tm=tm,status=status)
    vote.save()
    #####################Block Chain ####################
    file_path = os.path.join(BASE_DIR, f'myapp\\static\\myapp\\block\\{election_booth_master_id}.json')
    block_data = f'{election_booth_master_id}-{voter_id}-{election_candidate_master_id}-{dt}-{tm}'
    if os.path.exists(file_path):
        blockchain2 = Blockchain(fromFile=True)
        blockchain2.load_chain(file_path)
        blockchain2.add_new_transaction(block_data)
        blockchain2.mine()
        blockchain2.save_chain(file_path)
    else:
        blockchain = Blockchain(fromFile=False)
        blockchain.add_new_transaction(block_data)
        blockchain.mine()
        print(blockchain.get_chain())
        blockchain.save_chain(file_path)
    ########################################################
    context = {'msg':'Vote Registered'}
    return render(request,'myapp/user_messages.html',context)


def user_general_info_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return user_login_check(request)

    gi_l = general_info.objects.all()
    context = {'info_list':gi_l}
    return render(request, './myapp/user_general_info_view.html',context)

def user_election_result_view(request):
    election_master_id = request.GET.get('election_master_id')
    e_obj = election_master.objects.get(id=election_master_id)
    if e_obj.status == 'publish':
        district_list = district_master.objects.all()
        candidate_list = election_candidate_master.objects.filter(election_master_id=int(election_master_id))
        party_list = party_master.objects.all()
        election_list = election_master.objects.all()
        place_list = place_master.objects.all()
        ################Vote Counting ################
        booth_list = election_booth_master.objects.filter(election_master_id=election_master_id)
        vote_list = []
        c_vote = {}
        for boot in booth_list:
            vote_l = election_booth_vote.objects.filter(election_booth_master_id=boot.id)
            booth_candidate_list = election_booth_candidate_map.objects.filter(
                election_booth_master_id=boot.id)
            for bcl in booth_candidate_list:
                c_vote[bcl.election_candidate_master_id] = c_vote.get(bcl.election_candidate_master_id, 0)
            for vote in vote_l:
                cnt = c_vote.get(vote.election_candidate_master_id, 0)
                c_vote[vote.election_candidate_master_id] = cnt + 1
            print(c_vote)
        for key, value in c_vote.items():
            vote_list.append({'id': key, 'vote': value})
            print(key, value)
        ################################################

        context = {'candidate_list':candidate_list,'type':'Election Result',
               'place_list':place_list,'district_list':district_list,
               'party_list':party_list,'election_list':election_list,
                'election_master_id':election_master_id,'vote_list':vote_list}
        return render(request, './myapp/user_election_result_view.html',context)
    else:
        context = { 'msg': 'Result Not Published'}
        return render(request, './myapp/user_messages.html', context)
