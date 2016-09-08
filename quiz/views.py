from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
   		"name": "QUIZ 1",
	   	"description": "Hur bra kan du dina klassiker?"
	},
	{
		"quiz_number": 2,
   	   	"name": "QUIZ 2",
	   	"description": "Kan du dina lag?"
	},
	{
		"quiz_number": 3,
   	    	"name": "QUIZ 3",
	    	"description": "Hackerhistoria är viktigt, kan du den?"	},
]

# Create your views here.

def start(request):
	context = {
	"quizzes": quizzes,
	}
	return render(request, "quiz/start.html", context)

def quiz(request, quiz_number):
	context = {
	"quizzes": quizzes,
	"quiz":quizzes[int(quiz_number) - 1],
	"quiz_number": quiz_number,
	}

	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
	"quizzes": quizzes,
	"quiz":quizzes[int(quiz_number) - 1],
	"quiz_number": quiz_number,
	"question_number": question_number,
	"question": "Hur många bultar har bron?",
	"answer1": "12",
	"answer2": "66 400",
	"answer3": "7 428 954",



	}
	return render(request, "quiz/question.html", context)

def results(request, quiz_number):
	context = {
	"quizzes": quizzes,
	"correct": 12,
	"total": 20, 
	"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)
