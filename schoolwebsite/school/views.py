from django.shortcuts import render

def home(request):
    students = ["Rahul", "Anita", "Suresh"]
    return render(request, 'home.html', {'students': students})


def result(request, name):
    results = {
        "Rahul": "Math: 85, Science: 90",
        "Anita": "Math: 92, Science: 95",
        "Suresh": "Math: 78, Science: 80"
    }

    student_result = results.get(name, "Result not found")

    return render(request, 'result.html', {
        'name': name,
        'result': student_result
    })
