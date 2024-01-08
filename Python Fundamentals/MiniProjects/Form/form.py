# NOT WORKING

def checkUID(id:str):
    if '_' not in id.split():    
        if id.isalpha():
            return True
    else:
        idlist = id.split()
        idlist.remove('_')
        if idlist.isalpha():
            return True
    return False
    
def checkPassword(pwd:str):
    if len(pwd)==8:
        count = 0
        nums = [1,2,3,4,5,6,7,8,9,0]
        specialChars = '[@_!#$%^&*()<>?/\|}{~:]'
        spCharList = [c for c in specialChars]
        pwdlist = pwd.split()
        for p in pwdlist:
            if str(p) in nums:
                count+=1
        for i in range(len(spCharList)-1):
            if spCharList[i] in pwdlist:
                count+=1
        if count>=2:
            return True
        else:
            return False
    else:
        return False  

def checkEmail(mail:str):
    if mail.endswith('.com') and mail.__contains__('@'):
        return True
    return False

def checkBranch(b:str, bl:list):
    if b.capitalize() in bl:
        return True
    if b.upper() in bl:
        return True
    return False

def checkPhone(phone:int):
    if len(phone)==10 and type(phone) == int:
        return True
    return False

def checkRating(rating:int):
    if rating in range(0,5):
        return True
    return False


form = {}
while True:
    user_id = input('Enter Username : ')
    if checkUID(user_id):
        form['User id'] = user_id
    else:
        print('Invalid User ID')
        continue
    
    password = input('Enter Password : ')
    if checkPassword(password):
        form['password'] = password
    else:
        print('Invalid Password')
        continue

    email = input('Enter Email : ')
    if checkEmail(email):
        form['email'] = email
    else:
        print('Invalid Email Id')
        continue
    
    branchlist = ['CS', 'IT', 'AI', 'IOT', 'Cyber', 'Blockchain']
    Branch = input(f'Enter Branch from {branchlist}: ')
    if checkBranch(Branch, branchlist):
        form['Branch'] = Branch
    else:
        print('Invalid Branch')
        continue

    phone_num = int(input('Enter Your Phone No. : '))
    if checkPhone(phone_num):
        form['Phone'] = phone_num
    else:
        print('Invalid Phone Number')
        continue
    
    comm_rating = int(input('Rate Trainer\'s Communication [0-5, 5 being highest] : '))
    if checkRating(comm_rating):
        form['Communication Rating to Trainer'] = comm_rating
    else:
        print('Invalid Communication Rating')
        continue
    
    content_rating = int(input('Rate Trainer\'s Content [0-5, 5 being highest] : '))
    if checkRating(content_rating):
        form['Content Rating to Trainer'] = content_rating
        break
    else:
        print('Invalid Content Rating')
        continue


for form_keys, form_values in form:
    print(form_keys, form_values)