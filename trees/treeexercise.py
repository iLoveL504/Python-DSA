# Exercise 1
# Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree. As shown below,


class TreeNode:
    def __init__(self, **data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def print_tree(self, style=None, maxLevel=1000):
        #print(self.data)
        current_level = self.get_level()
        self.print_format(styled=style,level=current_level)
        for child in self.children:
            # print('current_level: ', current_level + 1)
            if current_level <= maxLevel - 1:
                child.print_tree(style, maxLevel)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level        
    
    def print_format(self, styled=None, level=0):
        if styled == 'position':
            print((level * 4 ) * ' ' + f'{'|__' if level!= 0 else ''}' + f'{self.data['position']}')
        elif styled == 'name':
            print((level * 4 ) * ' ' + f'{'|__' if level!= 0 else ''}' + f'{self.data['name']}')
        elif styled == 'complete':
            print((level * 4 ) * ' ' + f'{'|__' if level!= 0 else ''}' + f'{self.data['name']} ({self.data['position']})')
        else:
            print((level * 4 ) * ' ' + f'{'|__' if level!= 0 else ''}' + f'{self.data['name']}')


def build_company_tree():
    root = TreeNode(position='CEO',name='Nilupul')

    cto = TreeNode(position='CTO',name='Chinmay')
    infrastructure_head = TreeNode(position='Infrastucture Head',name='Vishwa')
    cloud_manager = TreeNode(position='Cloud Manager',name='Dhaval')
    app_manager = TreeNode(position='App Manager',name='Abhijit')
    application_head = TreeNode(position='Application Head',name='Aamir')

    cto.add_child(infrastructure_head)
    cto.add_child(application_head)

    infrastructure_head.add_child(app_manager)
    infrastructure_head.add_child(cloud_manager)

    hr_head = TreeNode(position='HR Head',name='Gels')
    recruitment_manager = TreeNode(position='Recruitment Manager',name='Peter')
    policy_manager = TreeNode(position='Policy Manager',name='Waqas')

    hr_head.add_child(recruitment_manager)
    hr_head.add_child(policy_manager)
    
    root.add_child(cto)
    root.add_child(hr_head)

    return root

def build_geography_tree():
    pass

if __name__ == "__main__":
    tree = build_company_tree()
    print('hello')
    print('=' * 5 + 'Original Style' + '=' * 5)
    tree.print_tree(style='complete')
    print('=' * 5 + 'Postion' + '=' * 5)
    tree.print_tree(style='position')
    print('=' * 5 + 'Name' + '=' * 5)
    tree.print_tree(style='name', maxLevel=1)
    
    # Exercise 2
    geography_tree = build_geography_tree()
    # Added a feature where it can only print up to a certain level

# =====Original Style=====
# Nilupul (CEO)
#     |__Chinmay (CTO)
#         |__Vishwa (Infrastucture Head)
#             |__Abhijit (App Manager)
#             |__Dhaval (Cloud Manager)
#         |__Aamir (Application Head)
#     |__Gels (HR Head)
#         |__Peter (Recruitment Manager)
#         |__Waqas (Policy Manager)
# =====Postion=====
# CEO
#     |__CTO
#         |__Infrastucture Head
#             |__App Manager
#             |__Cloud Manager
#         |__Application Head
#     |__HR Head
#         |__Recruitment Manager
#         |__Policy Manager
# =====Name=====
# Nilupul               # Here with a parameter of maxLevel = 1
#     |__Chinmay
#     |__Gels