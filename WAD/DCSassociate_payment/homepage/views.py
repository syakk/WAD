from django.shortcuts import render, redirect
from homepage.models import Associate, Student, Payment, Affair
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
# Create your views here.

# HTML, urls, views kena link

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            associate = Associate.objects.get(username=username, password=password)
            return redirect('studentList')  # redirect to student list page
        except Associate.DoesNotExist:
            message = 'Incorrect username or password'
            return render(request, 'login.html', {'message': message})

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        a_associate_studentID = request.POST['id']
        u_username = request.POST['username']
        p_password = request.POST['password']
        n_name = request.POST['name']
        associate_members = Associate.objects.all()
        find = False
        for search in associate_members:
            if search.associate_studentID == a_associate_studentID:
                find = True
                break
        if find:
            msg = "This associate member already exists"
        else:
            data = Associate(associate_studentID=a_associate_studentID, username=u_username, password=p_password, name=n_name)
            data.save()
            msg = "User successfully registered"
            return HttpResponseRedirect(reverse('login'))
    else:
        msg = ''
    dict = {'message': msg}
    return render(request, "signup.html", dict)

def newStudent(request):
    if request.method == 'POST':
        studentID = request.POST['studentID']
        studentName = request.POST['studentName']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        course_code = request.POST['course_code']
        payment_status = request.POST['payment_status']
        student_data = Student.objects.all()
        find = False
        for search in student_data:
            if search.studentID == studentID:
                find = True
                break
        if find:
            msg = "This student data already exists"
        else:
            data = Student(studentID=studentID, studentName=studentName, email=email, phone_number=phone_number, course_code=course_code, payment_status=payment_status)
            data.save()
            msg = "Student data is successfully keyed in"
            return HttpResponseRedirect(reverse('studentList'))
    else:
        msg = ''
    dict = {'message': msg}
    return render(request,"newStudent.html")

def studentList(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'studentList.html', context)

def update_student(request, studentID):
    students = Student.objects.get(studentID=studentID)
    dict = {
        'students': students
    }
    return render(request, "update_student.html", dict)

def save_update_student(request, studentID):
    studentName = request.POST['studentName']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    course_code = request.POST['course_code']
    payment_status = request.POST['payment_status']
    students = Student.objects.get(studentID=studentID)
    students.studentName = studentName
    students.email = email
    students.phone_number = phone_number
    students.course_code = course_code
    students.payment_status = payment_status
    students.save()
    return HttpResponseRedirect(reverse("studentList"))

def delete_student(request, studentID):
    students = Student.objects.get(studentID=studentID)
    students.delete()
    return HttpResponseRedirect(reverse('studentList'))

def newPayment(request):
    if request.method == 'POST':
        paymentID = request.POST['paymentID']
        studentID = request.POST['studentID']
        payment_amount = request.POST['payment_amount']
        payment_date = request.POST['payment_date']
        payment_data = Payment.objects.all()
        find = False
        for search in payment_data:
            if search.paymentID == paymentID:
                find = True
                break
        if find:
            msg = "This payment data already exists"
        else:
            data = Payment(paymentID=paymentID, studentID=studentID, payment_amount=payment_amount, payment_date=payment_date)
            data.save()
            msg = "Payment data is successfully keyed in"
            return HttpResponseRedirect(reverse('paymentList'))
    else:
        msg = ''
    dict = {'message': msg}
    return render(request,"newPayment.html")

def paymentList(request):
    payment = Payment.objects.all()
    context = {'payment': payment}
    return render(request, 'paymentList.html', context)

def update_payment(request, paymentID):
    payment = Payment.objects.get(paymentID=paymentID)
    dict = {
        'payment': payment
    }
    return render(request, "update_payment.html", dict)

def save_update_payment(request, paymentID):
    studentID = request.POST['studentID']
    payment_amount = request.POST['payment_amount']
    payment_date = request.POST['payment_date']
    payment = Payment.objects.get(paymentID=paymentID)
    payment.studentID = studentID
    payment.payment_amount = payment_amount
    payment.payment_date = payment_date
    payment.save()
    return HttpResponseRedirect(reverse("paymentList"))

def delete_payment(request, paymentID):
    payment = Payment.objects.get(paymentID=paymentID)
    payment.delete()
    return HttpResponseRedirect(reverse('paymentList'))

def newEvent(request):
    if request.method == 'POST':
        affair_id = request.POST['affair_id']
        eventName = request.POST['eventName']
        eventDate = request.POST['eventDate']
        eventDescription = request.POST['eventDescription']
        event_data = Affair.objects.all()
        find = False
        for search in event_data:
            if search.affair_id == affair_id:
                find = True
                break
        if find:
            msg = "This affair data already exists"
        else:
            data = Affair(affair_id=affair_id, eventName=eventName, eventDate=eventDate, eventDescription=eventDescription)
            data.save()
            msg = "Affair data is successfully keyed in"
            return HttpResponseRedirect(reverse('eventList'))
    else:
        msg = ''
    dict = {'message': msg}
    return render(request,"newEvent.html")

def eventList(request):
    event = Affair.objects.all()
    context = {'event': event}
    return render(request, 'eventList.html', context)

def update_event(request, affair_id):
    event = affair_id.objects.get(affair_id=affair_id)
    dict = {
        'event': event
    }
    return render(request, "update_event.html", dict)

def save_update_event(request, affair_id):
    eventName = request.POST['eventName']
    eventDate = request.POST['eventDate']
    eventDescription = request.POST['eventDescription']
    event = Affair.objects.get(affair_id=affair_id)
    event.eventName = eventName
    event.eventDate = eventDate
    event.eventDescription = eventDescription
    event.save()
    return HttpResponseRedirect(reverse("eventList"))

def delete_event(request, affair_id):
    event = Affair.objects.get(affair_id=affair_id)
    event.delete()
    return HttpResponseRedirect(reverse('eventList'))