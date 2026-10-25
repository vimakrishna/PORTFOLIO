from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.

class AboutView(View):
    def get(self,request):
        data = {
            "ID":12,
            "FULL NAME":"Vimal krishna",
            "PROFESSIONAL TITLE":"FullStack Developer",
            "BIO":"Pyhton FullStack Developer with skills in coding",
            "DOB":"06-02-2004",
            "EMAIL":"vimalkrishna.tech@gmail.com",
            "CONTACT NUMBER":9037610037,
            "LOCATION":"Alappuzha",
            "GITHUB URL":"http//.124.0.8000",
            "LINKEDIN URL":"http//Linkedin"

        }
        return JsonResponse(data)

class educationView(View):
    def get(self,request):
        input = {
            "ID":10,
            "INSTITUTION":"ST.THOMAS COLLEGE",
            "DEGREE":"B.Tech",
            "UNIVERSITY":"KTU",
            "LOCATION":"KOCHI",
            "START YEAR":2022,
            "END YEAR":2026,
            "CGPA":7,
            "DESCRIPTION":"B.Tech in computer science"

        }
        return JsonResponse(input)

class projectView(View):
    def get(self,request):
        projects = [
    {
        "id": 1,
        "title": "Student Management System",
        "short_description": "A web application for managing student information and academic records.",
        "long_description": "A Django-based web application that allows users to add, view, update, and delete student details. The system helps manage student records in an organized way.",
        "technologies_used": ["Django", "Python", "HTML", "CSS", "MySQL"],
        "live_url": "https://student-management-demo.com",
        "linkedin_url": "https://linkedin.com/in/demo-student",
        "github_url": "https://github.com/demo/student-management",
        "imagelink": "https://images.example.com/student-management.jpg",
        "featured":True
    },

    {
        "id": 2,
        "title": "Online Food Ordering System",
        "short_description": "A web application for browsing food items and placing online orders.",
        "long_description": "An online food ordering platform developed using Django and Python. Users can view available food items, select products, add them to a cart, and place orders through a simple interface.",
        "technologies_used": ["Django", "Python", "JavaScript", "HTML", "CSS"],
        "live_url": "https://food-ordering-demo.com",
        "linkedin_url": "https://linkedin.com/in/demo-food",
        "github_url": "https://github.com/demo/food-ordering",
        "imagelink": "https://images.example.com/food-ordering.jpg",
        "featured":False
    },

    {
        "id": 3,
        "title": "Employee Management System",
        "short_description": "A system for managing employee details, departments, salaries, and joining information.",
        "long_description": "A Django-based employee management application designed to store and manage employee records. It provides features for adding, viewing, updating, and deleting employee information.",
        "technologies_used": ["Django", "Python", "MySQL", "HTML", "CSS"],
        "live_url": "https://employee-management-demo.com",
        "linkedin_url": "https://linkedin.com/in/demo-employee",
        "github_url": "https://github.com/demo/employee-management",
        "imagelink": "https://images.example.com/employee-management.jpg",
        "featured":True
    },

    {
        "id": 4,
        "title": "Vehicle Tracking System",
        "short_description": "A web application for monitoring vehicle information and tracking vehicle locations.",
        "long_description": "A vehicle tracking application developed using Django and Python. The system stores vehicle information and uses location data to display tracking details, helping users monitor vehicles efficiently.",
        "technologies_used": ["Django", "Python", "JavaScript", "API", "HTML", "CSS"],
        "live_url": "https://vehicle-tracking-demo.com",
        "linkedin_url": "https://linkedin.com/in/demo-vehicle",
        "github_url": "https://github.com/demo/vehicle-tracking",
        "imagelink": "https://images.example.com/vehicle-tracking.jpg",
        "featured":False 
    }
]
        return JsonResponse(projects,safe=False)

class skillsView(View):
    def get(self,request):
        skills = [
    {
        "id": 1,
        "skill_name": "Python",
        "category": "Programming Language",
        "proficiency_level": "Advanced",
        "years_of_experience": 3
    },
    {
        "id": 2,
        "skill_name": "Django",
        "category": "Framework",
        "proficiency_level": "Intermediate",
        "years_of_experience": 2
    },
    {
        "id": 3,
        "skill_name": "MySQL",
        "category": "Database",
        "proficiency_level": "Intermediate",
        "years_of_experience": 2
    }
]
        return JsonResponse(skills,safe=False)

class experienceView(View):
    def get(self,request):
        experiences = [
    {
        "id": 1,
        "job_title": "Python Developer",
        "company_name": "Tech Solutions Pvt Ltd",
        "location": "Kochi, Kerala",
        "employment_type": "Full-time",
        "start_date": "2023-06-01",
        "end_date": "2024-05-31",
        "currently_working": False,
        "description": "Developed and maintained Python-based web applications using Django. Worked with databases, APIs, and backend development."
    },

    {
        "id": 2,
        "job_title": "Junior Web Developer",
        "company_name": "WebTech Solutions",
        "location": "Thiruvananthapuram, Kerala",
        "employment_type": "Full-time",
        "start_date": "2022-07-01",
        "end_date": "2023-05-31",
        "currently_working": False,
        "description": "Worked on web application development using HTML, CSS, JavaScript, and Python. Assisted in developing responsive web pages and backend features."
    },

    {
        "id": 3,
        "job_title": "Python Intern",
        "company_name": "CodeCraft Technologies",
        "location": "Kochi, Kerala",
        "employment_type": "Internship",
        "start_date": "2022-01-10",
        "end_date": "2022-06-30",
        "currently_working": False,
        "description": "Gained practical experience in Python programming, Django, MySQL, and REST API development while working on real-world projects."
    },

    {
        "id": 4,
        "job_title": "Software Developer",
        "company_name": "Innovative IT Solutions",
        "location": "Kochi, Kerala",
        "employment_type": "Full-time",
        "start_date": "2024-06-01",
        "end_date": None,
        "currently_working": True,
        "description": "Currently working on backend applications using Python and Django. Developing APIs, managing databases, and implementing new application features."
    }
]
        return JsonResponse(experiences,safe=False)

class certificateView(View):
    def get(self,request):
        certifications = [
    {
        "id": 1,
        "certification_name": "Python Programming Certification",
        "issued_organization": "Python Institute",
        "issued_date": "2024-03-15"
    },
    {
        "id": 2,
        "certification_name": "Django Web Development",
        "issued_organization": "Udemy",
        "issued_date": "2024-06-20"
    },
    {
        "id": 3,
        "certification_name": "SQL and Database Management",
        "issued_organization": "Great Learning",
        "issued_date": "2024-08-10"
    },
    {
        "id": 4,
        "certification_name": "Full Stack Web Development",
        "issued_organization": "Luminar Technolab",
        "issued_date": "2025-02-25"
    }
]
        return JsonResponse(certifications,safe=False)

class sevicesView(View):
    def get(self,request):
        services = [
    {
        "id": 1,
        "service_name": "Web Development",
        "description": "Development of responsive and user-friendly websites and web applications.",
        "technologies": ["HTML", "CSS", "JavaScript", "Python", "Django"]
    },
    {
        "id": 2,
        "service_name": "Backend Development",
        "description": "Development of secure and scalable backend applications and REST APIs.",
        "technologies": ["Python", "Django", "REST API", "MySQL"]
    },
    {
        "id": 3,
        "service_name": "Database Management",
        "description": "Designing, managing, and maintaining databases for web applications.",
        "technologies": ["MySQL", "SQL", "Django ORM"]
    },
    {
        "id": 4,
        "service_name": "Full Stack Development",
        "description": "Building complete web applications with frontend, backend, and database integration.",
        "technologies": ["Python", "Django", "HTML", "CSS", "JavaScript", "MySQL"]
    }
]
        return JsonResponse(services,safe=False)