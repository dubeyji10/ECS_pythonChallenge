"""Routes for the course resource.
"""

from run import app
from flask import request
from http import HTTPStatus
import data
import json
from flask import render_template
from flask import Flask, request, jsonify

@app.route('/hello/')
@app.route('/hello/<name>')
def hello2(name=None):
    return render_template('hello.html', name=name)


@app.route("/course/<int:id>", methods=['GET'])
def get_course(id):

    """Get a course by id.

    :param int id: The record id.
    :return: A single course (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE
    # course = data.courses[id]
    try:
        c = {'data': data.courses[id]}
        return jsonify(c)

    except KeyError:
        return jsonify({'message':'Course {} does not exist'.format(str(id))})
    else:
        return jsonify({'message':'Course {} does not exist'.format(str(id))})
    # c = {'data': data.courses[id]}

    # print('return json of this : \n\n',c)
    # print('-'*55)

    # return {'message':'try sending a json dump'}
    # return json.dumps(c)
    return jsonify(c)


@app.route("/course", methods=['GET'])
def get_courses():
    """Get a page of courses, optionally filtered by title words (a list of
    words separated by commas".

    Query parameters: page-number, page-size, title-words
    If not present, we use defaults of page-number=1, page-size=10

    :return: A page of courses (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE
    # if request.args.get('page_size'):
    if request.args.get('page-size'):
        page_size =request.args.get('page-size')
        print('got value from user')
         # use default value repalce 'None'
    else:
        page_size = 5
        print('using default value')

    required_data = {}
    # required_data = {list(data.courses.keys())[0] : data.courses[list(data.courses.keys())[0]]}

    '''
    i didn't get what you meant by page_count page_number record_count
    '''
    page_count = None
    page_number = None
    record_count = None
    
    required_data = {list(data.courses.keys())[i] : data.courses[list(data.courses.keys())[i]] for i in range(int(page_size))}
    # print(required_data)
        # return jsonify({'page_size': page_size})
    
        
    return jsonify({'data': required_data,'metadata':{
            'page_count':page_count,
            'page_number':page_number,
            'page_size':page_size,
            'record_count' : record_count,
                }})

@app.route("/course", methods=['POST'])
def create_course():
    """Create a course.
    :return: The course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE

	# get the element with name 'name'
    id = request.form['id']
    print('id : ',id)
    title = request.form['title']
    print('title : ',title)
    image_path = request.form['image_path']
    description = request.form['description']
    # pass the name to the result.html template
 
    result_dict = {
    "id":int(id),
    "date_created":"2020-07-04 01:02:49",
    "date_updated":"2021-01-31 15:07:20",
    "description":description,
    "discount_price":3,
    "image_path":image_path,
    "on_discount":True,
    "price":30,
    "title":title
    }
    # print('writing to json ')

    # with open('sample_entry.json', 'w') as jsonfile:
    #     json.dump(result_dict, jsonfile)


    # line_to_be_added = '''{\n'''
    # for keys in result_dict.keys():
    #     line_to_be_added += '''"{}":"{}",\n'''.format(keys,result_dict[keys])
    # line_to_be_added += '''\n}'''

    # print('added : ',line_to_be_added)   
    # print('written data to sample_entry.json ')


    print('written data to course.json ')

    tempR = ''',\n'''+ str(json.dumps(result_dict, indent=4,sort_keys=True))
    tempR += "\n]" # since ] is at end of json
    print(tempR,'\n_________________\n', type(tempR))
    with open('./json/course.json', 'r') as jsonfile:
        lines = jsonfile.readlines()

    print('reached last line')
    print(' add json data before ]')
    print('lastline L before : ',lines[-1])
    lines[-1] = tempR
    print('-'*50)
    print('lastline L now : ',lines[-1])

    with open('./json/course.json', 'w') as jsonfile:
        jsonfile.writelines(lines)
    
    return render_template('data.html', courseID= id , courseTitle = title,courseDes = description,CourseImage_path = image_path)
    

# @app.route('/form/',methods = ['GET','POST'])
# def send():
#     if request.method == 'POST':
#         age = request.form['age']
#         return render_template('data.html',age=age)
#         print('at data.html')
#     print('at update.html')
#     return render_template('update.html')

'''

doing update own way 

'''

@app.route('/update2/<int:id>', methods=["GET", "POST"])
def update(id):
    old_id = None
    if request.method == 'GET':
        print('get form working for POST METHOD')
        print('-----------------------------------------')
        current_data= data.courses[id]
        print(current_data)
        print('-----------------------------------------')
        old_id = id
        return render_template('update.html', data_Dict = current_data)
    else:
        print('POST method working')
        # yourarg = request.args.get('argname')
        courseID = request.form['id']
        courseTitle = request.form['title']
        courseImage_path = request.form['image_path']
        courseDesc = request.form['description']
        coursePrice = request.form['price']
        courseOnDiscount = request.form['on_discount']
        courseDiscPrice = request.form['discounted_price']
        courseDateCreated = request.form['date_created']
        courseDateModified = request.form['date_updated']

        result_d = {
        'id':courseID,
        'title':courseTitle,
        'price':coursePrice,
        'description':courseDesc,
        'date_created':courseDateCreated,
        'date_modified':courseDateModified,
        'image_path':courseImage_path,
        'on_discount':courseOnDiscount,
        'discounted_price':courseDiscPrice
        }
        print(result_d)
        
        return jsonify(result_d)


@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    """Update a a course.
    :param int id: The record id.
    :return: The updated course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    # YOUR CODE HERE


@app.route("/Deletecourse/<int:id>")
def delete_course(id):
    """Delete a course
    :return: A confirmation message (see the challenge notes for examples)
    """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE
    # c = {'data': data.courses[id]}

    # data.courses.pop(id)
    try:
        print('deleted : ',data.courses.pop(id))
        return jsonify({'message':'deleted entry for course with id = {}'.format(str(id))})

    except KeyError:
        return jsonify({'message':'Course {} does not exist'.format(str(id))})
    else:
        return jsonify({'message':'Course {} does not exist'.format(str(id))})
    # c = {'data': data.courses[id]}

    # print('return json of this : \n\n',c)
    # print('-'*55)

    # return {'message':'try sending a json dump'}
    # return json.dumps(c)




# original

# @app.route("/course/<int:id>", methods=['DELETE'])
# def delete_course(id):
#     """Delete a course
#     :return: A confirmation message (see the challenge notes for examples)
#     """
#     """
#     -------------------------------------------------------------------------
#     Challenge notes:
#     -------------------------------------------------------------------------
#     None
#     """
#     # YOUR CODE HERE
#     # c = {'data': data.courses[id]}

#     print('deleted : ',data.courses.pop(id))
#     print('popped from dictionary')
#     return {'message':'it deletes record from dictionary not from json file'}

@app.route("/message")
def hello():

    print('_for debugging_')
    c = data.courses[100]
    print('-'*50)
    print(type(c))
    # print(c.keys())
    print(c)
    print('-'*50)
    return {'message':'HELLO'}
    # YOUR CODE HERE





@app.route("/createCourse")
def index():
    # open the index.html page
    return render_template('index.html')

# when the result url hit with a post request, show result function
@app.route('/courseCreated', methods = ['POST'])
def result():
	# get the element with name 'name'
    id = request.form['id']
    print('id : ',id)
    title = request.form['title']
    print('title : ',title)
    image_path = request.form['image_path']
    description = request.form['description']
    # pass the name to the result.html template
 
    result_dict = {
    "id":int(id),
    "date_created":"2020-07-04 01:02:49",
    "date_updated":"2021-01-31 15:07:20",
    "description":description,
    "discount_price":3,
    "image_path":image_path,
    "on_discount":True,
    "price":30,
    "title":title
    }
    # print('writing to json ')

    # with open('sample_entry.json', 'w') as jsonfile:
    #     json.dump(result_dict, jsonfile)


    # line_to_be_added = '''{\n'''
    # for keys in result_dict.keys():
    #     line_to_be_added += '''"{}":"{}",\n'''.format(keys,result_dict[keys])
    # line_to_be_added += '''\n}'''

    # print('added : ',line_to_be_added)   
    # print('written data to sample_entry.json ')


    print('written data to course.json ')

    tempR = ''',\n'''+ str(json.dumps(result_dict, indent=4,sort_keys=True))
    tempR += "\n]" # since ] is at end of json
    print(tempR,'\n_________________\n', type(tempR))
    with open('./json/course.json', 'r') as jsonfile:
        lines = jsonfile.readlines()

    print('reached last line')
    print(' add json data before ]')
    print('lastline L before : ',lines[-1])
    lines[-1] = tempR
    print('-'*50)
    print('lastline L now : ',lines[-1])

    with open('./json/course.json', 'w') as jsonfile:
        jsonfile.writelines(lines)
    
    return render_template('data.html', courseID= id , courseTitle = title,courseDes = description,CourseImage_path = image_path)
    

# @app.route('/form/',methods = ['GET','POST'])
# def send():
#     if request.method == 'POST':
#         age = request.form['age']
#         return render_template('data.html',age=age)
#         print('at data.html')
#     print('at update.html')
#     return render_template('update.html')