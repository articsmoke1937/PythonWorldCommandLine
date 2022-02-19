import json
from University.user_profile import user as up
import University.globals as g

checkin='start'
def user_validation(user_log,pname):
    userconfirm=1
    checkin='start'
    while checkin!='complete':
        if user_log=='y':
            while userconfirm < 3:
                if user_log=='y':
                    print(f'Are you {pname}?\n1. Yes\n2. No')
                    userconfirm=int(input(g.prompt))
                    if userconfirm==1:
                        user_id=up.user_id_get(g.users_file,pname)[0]
                        user_id,pname,lname,city,age=up.get_user_info(g.users_file,user_id)
                        print(user_id,'test1')##test
                        print(g.border)
                        print(f"Welcome back, {pname} from {city}")
                        userconfirm=3
                        checkin='complete'
                        userrecognized=True
                        break
                    elif userconfirm==2:
                        userrecognized=False
                        user_log='n'
                    break
                else:
                    break
        else:
            userrecognized=False
            print('Please tell me with whom I have the pleasure to speak.')
            print("What is your first name: ")
            pname=input(g.prompt)
            pname=pname.capitalize()
            user_log=up.username_check(g.users_file,pname)
            if user_log=='n':
                # print(user_id)
                user_id=up.user_id_get(g.users_file,pname)[1]
                print(user_id)
                print("You are a new user and we will need to get you set up")
                # up.add_user(users_file,'user_id',0,int(int(new_user_id)+1))       
                # up.add_user(users_file,'first',0,pname)
                with open(g.user_log_filename,'w') as f:
                    json.dump(pname,f)
                user_id,pname,lname,city,age=up.get_new_user_info(g.users_file,user_id,pname)
                dogage=age*8
                print(f'\n{g.border}')
                print(f"Well it is very nice to meet you {pname}.")
                print(f"Did you know that you age in dog years is {dogage}?")
                print(f'{g.border}\nYou have also been added to the Users list')
                print(g.border)
                # userconfirm==2+1
                checkin='complete'
                userrecognized==True
                up.add_user(g.users_file,'user_id',0,user_id)       
                up.add_user(g.users_file,'first',0,pname)
                up.add_user(g.users_file,'last',0,lname)
                up.add_user(g.users_file,'city',0,city)
                up.add_user(g.users_file,'age',0,age)
            elif user_log=='y':
                # print(user_id)
                user_id=up.user_id_get(g.users_file,pname)[0]
                print(user_id)
                user_id,pname,lname,city,age=up.get_user_info(g.users_file,user_id)
                print(user_id,pname,lname,city,age)
                with open(g.user_log_filename,'w') as f:
                    json.dump(pname,f)
                print(g.border)
                print(f'Ohhhh, you have been here before {pname}!')
                print(f'Welcome back!! I hope {city} is treating you well!')
                # userconfirm==2+1
                checkin='complete'
            else:
                break
   
    return(userrecognized,user_id)
