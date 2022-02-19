from University.user_profile import user as up
import University.globals as globals

#Special admin window
def admin_menu(user_id,pname,lname,city,age):
    print(globals.border)
    print(globals.border)
    print('Admin Menu')  
    print(globals.border)
    print(globals.border)
    print('1. Clear out Users File\n2. User Info')
    answer=int(input(globals.prompt))
    if answer==1:
        up.user_clear(globals.users_file)
    elif answer==2:
        my_user=up(user_id,pname,lname,city,age)
        print(my_user.display_user_info())
