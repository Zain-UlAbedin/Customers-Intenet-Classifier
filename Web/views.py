from django.shortcuts import render
from django.contrib import messages
from .models import User, File, File_data
from django.shortcuts import redirect
from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from django.utils.encoding import force_text
from django.template.response import TemplateResponse
from django.conf import settings, os
import re
from . import Naive_Bayes, Insights
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import magic


# Create your views here.


def home(request):
    return render(request, 'Web/home.html')


def About(request):
    return render(request, 'Web/About Us.html')


def Contact(request):
    return render(request, 'Web/Contact Us.html')


def Log_in(request):
    if request.session.has_key('User_Email'):
        return redirect('http://127.0.0.1:8000/User_DashBoard/')
    else:
        return render(request, 'Web/Login.html')


def User_DashBoard(request):
    if request.session.has_key('User_Email'):
        em = request.session['User_Email']
        if User.objects.filter(Email=em):
            user = User.objects.get(Email=em)
            First_name = user.First_Name
            U_id = user.id
            U_files = File.objects.filter(User_id=U_id)
            context = {'Name': First_name, 'Files': U_files}
            return render(request, 'Web/UserDashBoard.html', context)
    else:
        return redirect('http://127.0.0.1:8000/Login/')


def Create_User(request):
    if request.method == 'POST':
        context = {'Error': ""}
        user = User()
        user.First_Name = request.POST.get('Fname')
        user.Email = request.POST.get('email')
        user.Password = request.POST.get('Pass')
        em = request.POST.get('email')
        if User.objects.filter(Email=em):
            context = {'Error': "This Email already Exists"}
            return render(request, 'Web/home.html', context)

        user.save()
        return render(request, 'Web/home.html', context)


def Log_User(request):
    if request.method == 'POST':
        logMail = request.POST.get('Log_email')
        logPass = request.POST.get('Log_pass')
        if User.objects.filter(Email=logMail) & User.objects.filter(Password=logPass):
            request.session['User_Email'] = logMail
            return redirect('http://127.0.0.1:8000/User_DashBoard/')
        else:
            messages.error(request, 'Invalid Email or Password')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def logout(request):
    try:
        del request.session['User_Email']
    except:
        pass
    return redirect('http://127.0.0.1:8000')


def File_Upload(request):
    if request.method == 'POST':
        em = request.session['User_Email']
        user = User.objects.get(Email=em)
        Name = request.FILES['filed1']
        #file = File.objects.get(User_id=user.id)
        #filetype = magic.from_buffer(Name.read(), mime=True)
        # print(filetype)
        # if not "xlsx" in filetype:
        #   messages.error(request, 'Wrong File Format, please select xlsx format file')
        #  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        Name.name = force_text(Name.name).strip().replace(' ', '_')
        Name.name = re.sub(r'(?u)[^-\w.]', '', Name.name)
        FSize = (Name.size) / 1000000
        # fill = File(File_Name=request.FILES['filed1'])
        User_files = File.objects.filter(User_id=user.id)
        for file in User_files:
            if file.File_Name == Name.name:
                messages.error(request, 'File Already Exists With Same Name')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

       # if File.objects.filter(User_id=user.id):
        #    if File.objects.filter(File_Name=Name.name):
        #        messages.error(request, 'File Already Exists With Same Name')
         #       return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        #File_Stored_loc = settings.MEDIA_ROOT + '\static\Files/'
        # if os.path.isfile(File_Stored_loc + Name.name):
        # Naive_Bayes.Labling_Reviews(Name)
        Upfile = File(File_Path=request.FILES['filed1'])
        Upfile.File_Name = Name.name
        Upfile.User_id = user.id
        Upfile.File_Size = FSize
        Upfile.Lable = False
        Upfile.save()
        return redirect('http://127.0.0.1:8000/User_DashBoard/')

    return redirect('http://127.0.0.1:8000/User_DashBoard/')


def Insight(request, Path):

    if File.objects.filter(File_Path=Path):
        file = File.objects.get(File_Path=Path)
        if(file.Lable == False):
            Name = str(file.File_Path)
            Name = Name.replace('static/Files/', '')
            complain, recommend, query, others, appreciation = Naive_Bayes.Labling_Reviews(Name)

            file_data = File_data()
            file_data.File_Name = Path
            file_data.Complain = complain
            file_data.Recommend = recommend
            file_data.Query = query
            file_data.Appreciation = appreciation
            file_data.Others = others
            file.Lable = True
            file_data.save()
            file.save()
            context = {'Path': Path}
            return render(request, 'Web/Insights.html', context)
        else:
            context = {'Path': Path}
            return render(request, 'Web/Insights.html', context)


def Statistics(request):
    return render(request, 'Web/Insights.html')


def Donut_Chart(request, Path):
    File = File_data.objects.get(File_Name=Path)
    DonutChart = Insights.donutplot(File.Complain, File.Recommend, File.Query, File.Appreciation, File.Others)
    canvas = FigureCanvas(DonutChart)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response


def Bar_Chart(request, Path):

    File = File_data.objects.get(File_Name=Path)
    BarChart = Insights.BarGraph(File.Complain, File.Recommend, File.Query, File.Appreciation, File.Others)
    canvas = FigureCanvas(BarChart)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response


# tree map will traverse all files and show its Data based on complaints

def TreeMap(request, Path):
    em = request.session['User_Email']
    user = User.objects.get(Email=em)
    U_files = File.objects.filter(User_id=user.id)
    FName = []
    Complain = []
    for file in U_files:
        if File_data.objects.filter(File_Name=file.File_Path):
            Data_file = File_data.objects.get(File_Name=file.File_Path)
            FName.append(file.File_Name)
            Complain.append(Data_file.Complain)

    Tree_Map = Insights.TreeMap(FName, Complain)
    canvas = FigureCanvas(Tree_Map.figure)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response


def Word_Cloud(request, Path):
    file = File.objects.get(File_Path=Path)
    Name = str(file.File_Path)
    Name = Name.replace('static/Files/', '')
    wordcloud = Insights.WordCloud(Name)

    canvas = FigureCanvas(wordcloud)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response


def media(request, path):
    print(path)
