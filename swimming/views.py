from django.shortcuts import render, redirect

def index(request):
    education_data = {'classmates': [
            {
                'name': 'Белых Александра',
                'email': 'a.belykh@edu.hse.ru',
                'phone': '+7 (999) 123-45-67',
                'photo_placeholder': True
            },
            {
                'name': 'Бакирова Екатерина',
                'email': 'e.bakirova@edu.hse.ru',
                'phone': '+7 (999) 765-43-21',
                'photo_placeholder': True
            }
        ]

    }
    return render(request, 'index.html', {'education': education_data})

def about(request):
    return render(request, 'about.html')

def benefits(request):
    return render(request, 'benefits.html')

def styles(request):
    return render(request, 'styles.html')

def reasons(request):
    return render(request, 'reasons.html')

def education(request):
   
    education_data = {
        'program': {
            'title': 'Мировая экономика',
            'description': 'Образовательная программа «Мировая экономика» – это подготовка экспертов по международной торговле, финансам и анализу рынков. Программа сочетает фундаментальную экономическую теорию, изучение двух иностранных языков, анализ данных и проектную работу с упором на современные вызовы, включая цифровую экономику.'
        },
        'leader': {
            'name': 'Щербакова Алина Вячеславовна',
            'phone': '+7 (495) 772-95-90',
            'photo_placeholder': True
        },
        'manager': {
            'name': 'Заяц Елена Игоревна',
            'phone': '+7 (495) 772-95-90',
            'photo_placeholder': True
        },
        'classmates': [
            {
                'name': 'Белых Александра',
                'email': 'a.belykh@edu.hse.ru',
                'phone': '+7 (999) 123-45-67',
                'photo_placeholder': True
            },
            {
                'name': 'Бакирова Екатерина',
                'email': 'e.bakirova@edu.hse.ru',
                'phone': '+7 (999) 765-43-21',
                'photo_placeholder': True
            }
        ]
    }
    
    return render(request, 'education.html', {'education': education_data})

def calc_str_get(request):
    
    students_data = []
    str1_value = request.GET.get("str1", "")
    str2_value = request.GET.get("str2", "")
    
    if str1_value and str2_value:
        try:
            name = str1_value.split(' ')
            marks = str2_value.split(' ')
            
            
            for i in range(len(name)):
                if i < len(marks):
                    scores = marks[i].split('-')
                    total = 0
                    for s in scores:
                        total += int(s)
                    average = total/ len(scores)
                    students_data.append({'name': name[i], 'average': average})
                
                

        except ValueError:
            result_text = " Ошибка: неверные значения. Проверьте формат ввода."

    context = {
        'result': students_data,
        'str1': str1_value,  
        'str2': str2_value    
    }
    return render(request, 'task.html', context)




from .models import AboutMe, Staff, Classmate, Review
from .forms import ReviewForm
from django.db.models import Avg

def education_page(request):
    about = AboutMe.objects.first()
    staff = Staff.objects.all()
    classmates = Classmate.objects.all()

    reviews = Review.objects.all()

    sort = request.GET.get('sort')
    min_rating = request.GET.get('min_rating')

    if min_rating:
        reviews = reviews.filter(rating__gte=min_rating)

    if sort == 'rating':
        reviews = reviews.order_by('-rating')
    elif sort == 'date':
        reviews = reviews.order_by('-created_at')
    else:
        reviews = reviews.order_by('-created_at')

    avg_rating = Review.objects.aggregate(Avg('rating'))['rating__avg']
    reviews_count = Review.objects.count()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('swimming:education_page')
    else:
        form = ReviewForm()

    context = {
        'about': about,
        'staff': staff,
        'classmates': classmates,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1) if avg_rating else 0,
        'reviews_count': reviews_count,
        'form': form,
    }
    return render(request, 'education_page.html', context)


from .models import PageContent

def about_page(request):
    history = PageContent.objects.get(page_name='about_history')
    types = PageContent.objects.get(page_name='about_types')
    sources = PageContent.objects.get(page_name='about_sources')
    
    context = {
        'history': history,
        'types': types,
        'sources': sources,
    }
    return render(request, 'about.html', context)

def benefits_page(request):
    physical = PageContent.objects.get(page_name='benefits_physical')
    mental = PageContent.objects.get(page_name='benefits_mental')
    medical = PageContent.objects.get(page_name='benefits_medical')
    
    context = {
        'physical': physical,
        'mental': mental,
        'medical': medical,
    }
    return render(request, 'benefits.html', context)

def styles_page(request):
    table = PageContent.objects.get(page_name='styles_table')
    comparison = PageContent.objects.get(page_name='styles_comparison')
    
    context = {
        'table': table,
        'comparison': comparison,
    }
    return render(request, 'styles.html', context)

def reasons_page(request):
    reasons_list = PageContent.objects.get(page_name='reasons_list')
    details = PageContent.objects.get(page_name='reasons_details')
    
    # Преобразуем текст в список причин
    reasons_data = []
    lines = reasons_list.content.split('\n')
    for line in lines:
        if ':' in line:
            parts = line.split(':', 1)
            title = parts[0].strip()
            items = [item.strip() for item in parts[1].split(',')]
            reasons_data.append({'title': title, 'items': items})
    
    context = {
        'reasons_data': reasons_data,
        'details': details,
    }
    return render(request, 'reasons.html', context)

def index_page(request):
    michael = PageContent.objects.get(page_name='index_michael')
    competitions = PageContent.objects.get(page_name='index_competitions')
    facts = PageContent.objects.get(page_name='index_facts')
    
    context = {
        'michael': michael,
        'competitions': competitions,
        'facts': facts,
    }
    return render(request, 'index.html', context)


def content_list(request):
    pages = PageContent.objects.all()

    category = request.GET.get('category')
    sort = request.GET.get('sort')

    if category:
        pages = pages.filter(category=category)

    if sort == 'title':
        pages = pages.order_by('title')
    elif sort == 'date':
        pages = pages.order_by('-created_at')
    else:
        pages = pages.order_by('page_name')

    categories = PageContent.objects.values_list('category', flat=True).distinct()

    context = {
        'pages': pages,
        'categories': categories,
    }
    return render(request, 'content_list.html', context)