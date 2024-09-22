from django.shortcuts import render


def index_view(request):
    context = {
        'skills': ['Python', 'JWT', 'REST', 'Django-REST', 'HTML', 'CSS', 'JavaScript', 'React'],
        'portfolio':[
                ['Tourist destinations', 
                    'The Tourist Destinations project is a web application aimed at showcasing various tourist spots,', 
                    'tour.jpeg', 
                    ['https://github.com/arshidathasli/tourist_destinations_project/', 
                        'http://13.201.37.227/']
                ],
                ['Bookhub', 
                    'The Book Hub project is a web application designed for managing books and user profiles in a library setting. I', 
                    'libarary.jpeg', 
                    ['https://github.com/arshidathasli/book_hub', 
                        'https://github.com/arshidathasli/book_hub_frontend', 
                        'https://youtu.be/yApVmDBWoxE'
                    ]
                ],
            ]
        }
    return render(request, 'index.html', context)