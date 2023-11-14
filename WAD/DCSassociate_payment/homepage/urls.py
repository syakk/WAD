from django.urls import path
from .import views

urlpatterns = [
    #urls for Associate
    path("",views.login, name="login"),
    path("sign_up",views.signup, name="signup"),

    #urls for Student
    path("studentList",views.studentList, name="studentList"),
    path("newStudent",views.newStudent, name="newStudent" ),
    path("update_student/<studentID>",views.update_student, name="update_student"),
    path("update_student/save_update_student/<studentID>",views.save_update_student, name="save_update_student"),    
    path("delete_student/<studentID>",views.delete_student, name="delete_student"),

    #urls for Payment
    path("paymentList",views.paymentList, name="paymentList"),
    path("newPayment",views.newPayment, name="newPayment"),
    path("update_payment/<paymentID>",views.update_payment, name="update_payment"),
    path("update_payment/save_update_payment/<paymentID>",views.save_update_payment, name="save_update_payment"),    
    path("delete_payment/<paymentID>",views.delete_payment, name="delete_payment"),

    #urls for Affair
    path("eventList",views.eventList, name="eventList"),
    path("newEvent",views.newEvent, name="newEvent"),
    path("update_event/<affair_id>",views.update_event, name="update_event"),
    path("update_event/save_update_event/<affair_id>",views.save_update_event, name="save_update_event"),    
    path("delete_event/<affair_id>",views.delete_event, name="delete_event"),
]