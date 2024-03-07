''' **********************************************************
Importing Libraries
***********************************************************'''
import random

''' **********************************************************
Defining Classes
***********************************************************'''

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        names = [grp.get_name() for grp in self.get_groups()]
        if group.get_name() not in names:
            self.groups.append(group)
        else:
            for grp in self.get_groups():
                if grp.get_name() == group.get_name():
                    for user in group.get_users():
                        if user not in grp.get_users():
                            grp.add_user(user)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
''' **********************************************************
Defining Functions
***********************************************************'''

def is_user_in_group(user, group, display=False):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True

    for grps in group.get_groups():
        if user in grps.get_users():
            if display:
                print(user + ' found!;', 'Group_Name:', grps.get_name(), '; Users:', grps.get_users())
            return True
    if display:
        print(user + ' not found')

    return False

''' **********************************************************
Running Code - Main
***********************************************************'''

if __name__ == "__main__":

    print('\n-------------------- UDACITY CASE --------------------\n')
        
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print('''Is {} in {}:'''.format(sub_child_user,
                        sub_child.get_name()),is_user_in_group("sub_child_user", sub_child))

    ## Add your own test cases: include at least three test cases
    ## and two of them must include edge cases, such as null, empty or very large values

    ## Test Case 1

    print('\n--------------------- TEST CASE 1  ---------------------\n')

    Groups = ['Group_'+str(n) for n in range(5)]
    Users =  ['User_'+str(n) for n in range(10)]
    Parent = Group('Parent')

    for i, grp in enumerate(Groups):
        grp_tmp = Group(grp)
        grp_tmp.add_user(Users[i])
        grp_tmp.add_user(Users[i+5])
        print('''Adding {} and {} to {}'''.format(Users[i], Users[i+5], grp))
        Parent.add_group(grp_tmp)
    print('Adding Created groups to parent group')

    print('\nResult:\n')
    
    for user in ['User_'+str(n) for n in range(15)]:
        _ = is_user_in_group(user, Parent, True)    


    print('\n--------------------- TEST CASE 2  ---------------------\n')

    Groups = ['Group_1', 'Group_1', 'Group_1', '', '']
    Users =  ['User_'+str(n) for n in range(2)]
    Users += ['User_1', 'User_2', '', '', '']
    Parent = Group('Parent')

    for i, grp in enumerate(Groups):
        grp_tmp = Group(grp)
        grp_tmp.add_user(Users[i])
        print('''Adding {} to {}'''.format(Users[i], grp))
        Parent.add_group(grp_tmp)
    print('Adding Created groups to parent group')

    print('\nResult:\n')

    for user in ['User_'+str(n) for n in range(4)]:
        _ = is_user_in_group(user, Parent, True)        


    print('\n--------------------- TEST CASE 3  ---------------------\n')

    print('''
    Creating 100 groups and adding 200 users, 2 users per created group. 
    It is expected for each group n to have user n and user n+100 as users,
    where n is an integer number between 0 and 100.''')

    Groups = ['Group_'+str(n) for n in range(100)]
    Users =  ['User_'+str(n) for n in range(200)]
    Parent = Group('Parent')

    print('\nResult: Looking for 5 randomly selected users\n')

    for i, grp in enumerate(Groups):
        grp_tmp = Group(grp)
        grp_tmp.add_user(Users[i])
        grp_tmp.add_user(Users[i+100])
        Parent.add_group(grp_tmp)

    for n in range(5):
        _ = is_user_in_group(Users[random.randint(0, len(Users))], Parent, True)
    
''' **********************************************************
END
***********************************************************'''
