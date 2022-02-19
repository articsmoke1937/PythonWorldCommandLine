import json

class user:
    def __init__(self):
        self.user_cred=self.user_cred()

        self.user_attributes=self.user_attributes()

    def reveal(self):
        self.user_cred.message("This is the outer calling the inner class level 1")
    
    class user_cred():

        def message(self, msg):
            print('This is from the inner class')

        #Get Last user logged in
        def last_user(self,user_log_filename):
            with open(user_log_filename) as last_user_filename:
                global pname
                pname = json.load(last_user_filename)
            return pname

        #Define User File udpate function
        def add_user(self,user_file, key,v1,value):
            with open(user_file) as f:
                users_file_decoded=json.load(f)
                users_file_decoded[key][v1].append(value)
            json.dump(users_file_decoded, open(user_file, 'w'))

        def username_check(self,user_file,pname):
            with open(user_file) as open_user_file:
                username_check=json.load(open_user_file)
            if pname in username_check['first'][0]:
                user_in='y'
            else:
                user_in='n'
            return user_in

    class user_attributes():
        def user_int_get(self,user_file,pname):
            with open(user_file) as open_user_file:
                username_check=json.load(open_user_file)
            user_int=0
            new_user_int=-1
            for x in username_check['first'][0]:
                if x != pname:
                    user_int=user_int+1-1  
                else:
                    break
            for x in username_check['first'][0]:
                new_user_int=new_user_int+1  
                user_int=user_int+1-1
            return user_int, new_user_int

        def get_user_info(self,user_file,user_int):
            with open(user_file) as open_user_file:
                username_check=json.load(open_user_file)
                pname=username_check['first'][0][int(user_int)]
                city=username_check['city'][0][int(user_int)]
                age=username_check['age'][0][int(user_int)]
            return pname, city, age