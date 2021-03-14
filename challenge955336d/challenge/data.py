"""Routines associated with the application data.
"""

courses = {}

def load_data():
    """Load the data from the json file.
    """
    attr = ['id','date_created','date_updated','description','discount_price','image_path','on_discount','price','title']

    temp_list = [[] for i in range(9)]

    # with open('course.json','r') as file:
    #   contents = file.read()

    with open('json/course.json','r') as file:
        contents = file.readlines()

    contents2 = contents[1:-1]

    '''
    # temp list implies this : 
    id= []
    date_created = []
    date_updated = []
    description = []
    discount_price = []
    image_path = []
    on_discount = []
    price = []
    title = []

    '''

    for i in contents2:
        i = i.strip()
        i = i.replace('"','')
        if len(i)>2:
            # first occurrence then stop splitting
            key ,value = i.split(':',1)
            value = value[:-1] # ignore the comma at end
            # print('key : ',key,'\nvalue:',value)
            if key==attr[0]:
                temp_list[0].append(int(value))
            if key==attr[1]:
                temp_list[1].append(value)

            if key==attr[2]:
                temp_list[2].append(value)
            if key==attr[3]:
                temp_list[3].append(value)

            if key==attr[4]:
                temp_list[4].append(value)
            if key==attr[5]:
                temp_list[5].append(value)

            if key==attr[6]:
                if value=='false':
                    temp_list[6].append(False)
                else:
                    temp_list[6].append(True)

            if key==attr[7]:
                temp_list[7].append(float(value))

            if key==attr[8]:
                temp_list[8].append(value)



        # if len(temp_list)==0:
        # else:
        # temp_list.append('keys:values')
    # print(i,type(i),len(i),'\n','--------------------------')
    # print('-'*100)

    # print('first 20 values')

    # c_dict = {}
    
    for i in range(len(temp_list[0])):
        # if i%20==0:
            # print('running for i=',i)
            # print('*'*73)

        new_dict = {}
        for attrs_index in range(len(attr)):
        # 0 to 9
            new_dict[attr[attrs_index]] = temp_list[attrs_index][i]

        courses[temp_list[0][i]] = new_dict
    
    # print('done')
    # print(c_dict.keys())
    # courses = c_dict
    # print('courses avaialble : ',courses.keys())

    pass


