from django.shortcuts import render
import pyrebase
# Create your views here.


config={
    "apiKey": "AIzaSyAq7-ziABaQCTxfeOlMIbv8jvfQk2B7lmQ",
    "authDomain": "pbl5-94125.firebaseapp.com",
    "databaseURL": "https://pbl5-94125-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "pbl5-94125",
    "storageBucket": "pbl5-94125.appspot.com",
    "messagingSenderId": "42461525472",
    "appId": "1:42461525472:web:e0519d8a1a0e0644f1e785",
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def index(request):
    name = database.child('Data').child('Name').get().val()
    cl =  database.child('Data').child('Class').get().val()
    phone = database.child('Data').child('Phone').get().val()
    return render(request, 'index.html', {
        "name": name,
        "class": cl,
        "phone": phone
    })
    
def loginSignUp(request):
    return render(request, "Login.html")

def postSignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('password')
    name = request.POST.get('username')
    role = request.POST.get('roles')
    print(role)
    print(name)
    try:
        
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        print("signed up !")
        result = database.child("Users").child(user['localId']).set({"email": email, "username": name, "role": role})

    except:
        return render(request, "Login.html")
    return render(request,"Login.html")


def postSignIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = authe.sign_in_with_email_and_password(email, password)
            print(user['localId'])
            userId = user['localId']
            # Nếu xác thực thành công, chuyển hướng đến trang chính
            username = database.child('Users').child(userId).child('username').get().val()
            role = database.child('Users').child(userId).child('role').get().val()
            print("Username:", username)
            print("role: ", role)
            context = {'username': username}
            if role=='teacher':
                return render(request, 'Home.html')
            else:
                return render(request, 'Profiles.html')
            
        except:
            # Nếu xác thực thất bại, trả về thông báo lỗi
            message = "Invalid email or password"
            return render(request, 'Login.html', {'message': message})
    else:
        return render(request, 'Login.html')
    

def logOut(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")


