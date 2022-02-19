import json

class user(object):
   
    def __init__(self,user_id,first,last,city,age):
        self.user_id=user_id
        self.first=first
        self.last=last
        self.city=city
        self.age=age
    
    def display_user_info(self):
        user_info=f'{self.user_id}\n{self.first}\n{self.last}\n{self.city}\n{self.age}'
        return user_info.title()
 #======================= =================
#User Creds
#========================================   
    #Get Last user logged in
    def last_user(user_log_filename):
        with open(user_log_filename) as last_user_filename:
            global pname
            pname = json.load(last_user_filename)
        return pname

    #Define User File udpate function
    def add_user(user_file, key,v1,value):
        with open(user_file) as f:
            users_file_decoded=json.load(f)
            users_file_decoded[key][v1].append(value)
        json.dump(users_file_decoded, open(user_file, 'w'))
    
    # def add_user_all(user_file, key,v1,value):
    #     for x in key:
    #         for y in value:
    #             with open(user_file) as f:
    #                 users_file_decoded=json.load(f)
    #                 users_file_decoded[x][v1].append(y)
    #             json.dump(users_file_decoded, open(user_file, 'w'))
    #             break
    
    #Check username in users file
    def username_check(user_file,pname):
        with open(user_file) as open_user_file:
            username_check=json.load(open_user_file)
        if pname in username_check['first'][0]:
            user_in='y'
        else:
            user_in='n'
        return user_in
#========================================
#User Attributes
#========================================
    #Get either user number or create number for new user
    def user_id_get(user_file,pname):
        with open(user_file) as open_user_file:
            username_check=json.load(open_user_file)
        user_id=-1
        new_user_id=0
        for x in username_check['first'][0]:
            if x != pname:
                user_id=int(user_id)+1
                new_user_id=int(user_id)+1 
            else:
                break
        user_id=int(user_id)+1
        # for x in username_check['first'][0]:
        # new_user_id=int(user_id)+1  
            # user_id=user_id+1
        return user_id, new_user_id
    
    #Get updated user information
    def get_user_info(user_file,user_id):
        with open(user_file) as open_user_file:
            username_check=json.load(open_user_file)
            user_id_get=username_check['user_id'][0][int(user_id)] 
            pname=username_check['first'][0][int(user_id)]
            lname=username_check['last'][0][int(user_id)]
            city=username_check['city'][0][int(user_id)]
            age=username_check['age'][0][int(user_id)]
        return user_id_get,pname,lname,city,age
    
    #Get information for new user
    def get_new_user_info(users_file,new_user_id,pname):
        prompt='> '
        user_id=new_user_id
        pname_same=pname
        print(f"What is your last name, {pname}? ")
        lname=input(prompt)
        lname=lname.capitalize()
        print(f"How old are you, {pname}? ")
        age = int(input(prompt))
        print("What City do you live in: ")
        city=input(prompt)
        city=city.capitalize()
        return user_id,pname_same,lname,city,age

#************************************************
# Admin User Maintenance
#************************************************
# def user_clear(user_file):
#     print(user_file)
#     with open(user_file) as open_user_file:
#         user_clear=json.load(open_user_file)
#     for x in user_clear['user_id'][0]:
#         if x != '':
#             del user_clear['user_id'][0]
#             del user_clear['first'][0]
#             del user_clear['last'][0]
#             del user_clear['city'][0]
#             del user_clear['age'][0]
#         json.dump(open_user_file, open(user_file, 'w'))
#         for x in user_clear['user_id'][0]:
#             print('delete')
#             print(x)   
                
#         else:
#             break


    def user_clear(user_file):
        print(user_file)
        with open(user_file) as open_user_file:
            user_clear = json.load(open_user_file)
        for key, value in user_clear['user_id'][0]:
            del user_clear[key][value]
            json.dump(open_user_file, open(user_file, 'w'))


        
   
