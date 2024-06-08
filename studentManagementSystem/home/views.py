from django.shortcuts import render
from django.http import HttpResponse
from home.models import *


# Create your views here.
def home(request):
    # return HttpResponse("""<h1 style='background-color:red;color:yellow;'>Hey I am a Django Server....</h1>
    #                     <p>The urls.py file you just created is specific for the members application. We have to do some routing in the root directory my_tennis_club as well. This may seem complicated, but for now, just follow the instructions below.
    #                        There is a file called urls.py on the my_tennis_club folder, 
    #                        open that file and add the include module in the import statement, and also add a path() function 
    #                        in the urlpatterns[] list, with arguments that will route users that comes in via 127.0.0.1:8000/.</p>
    #                     <h2>We can add multiple tags also ..........like this......<hr>
    #                     <h3>this is not suitable way to create html and add css
    #                     because, html have lot of tags very complicated structure. so, to do this work easy and simple
    #                     we will create one folder named 'Template' and in that folder we will create <i>index.html</i> file.
    #                     (we will return actual html page from backend django server) so we will remove the httpResponse and instead of that we will use render() as below """)
    return render(request,"home/index.html")


def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is Success page</h1>")


def voting(request):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if(age>=18):
        return render(request,"home/voting.html")
    else:
        return HttpResponse("<h1 style='color:red;'>You Cannot Vote</h1>")
    

def studentRecord(request):
    students = [
        {"name":"karan","age":24},
        {"name":"ram","age":14},
        {"name":"shakshi","age":44},
        {"name":"harshali","age":25},
        {"name":"dharshan","age":32},
        {"name":"kiran","age":15}
    ]
    
    text = """
    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Facere molestiae 
    unde similique quo quos! Fugit laborum similique itaque ea, at a consequuntur quas praesentium 
    alias aliquid veritatis, sequi fuga in accusamus eius esse. Quos possimus minus repellendus adipisci enim. Unde facere 
    consequuntur tempora, tenetur aliquam laudantium itaque totam beatae asperiores quam ipsam accusamus nisi blanditiis soluta 
    vitae commodi minima nam corporis illum perferendis libero in pariatur sunt veritatis. Culpa, minima autem. Cum possimus dolore
    dicta quis quae omnis corporis vero ad sed sunt atque facere laborum nisi praesentium sint, repudiandae exercitationem nostrum deserunt 
    ullam distinctio quidem corrupti quisquam molestias voluptates!"""
    
    # now lets use in not in operators
    vegies =["tomato","potato","cabbage","capsicum","ladyFinger","fenugreek"]
    
    # for student in students:
    #     print(student)
    return render(request,"home/student-record.html", context={"student":students, "text":text, "vegitables":vegies})



# ---------------------------------------------------------------------------------------------------------
# redirect the pages but this is not effiecinet way that way we will see later and change the page title dynamically.............

def index(request):
    return render(request, "home/index.html", context = {'page':'view index'})


def viewStudent(request):
    students = [
        {"name":"karan","age":24},
        {"name":"ram","age":14},
        {"name":"shakshi","age":24},
        {"name":"harshali","age":25},
        {"name":"dharshan","age":32},
        {"name":"kiran","age":15}
    ]
    return render(request, "home/student-record.html", context = {'student':students, 'page':'view Student'})


def viewVoting(request):
    return render(request, "home/voting.html", context = {'page':' view voting'})


def displayData(request):
    stu = Student.objects.all().values()
    # print(stu)
    context = {"data":stu}
    return render(request, "home/practice.html",context)


def detailsMore(request,id):
    stu = Student.objects.get(id=id)
    context = {"detail":stu}
    return render(request, "home/practice2.html",context)

def main(request):
    return render(request,"home/main.html")

def handler404(request,exception):
    return render(request,"home/404.html",status=404)