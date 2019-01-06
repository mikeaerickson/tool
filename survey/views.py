from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Survey, Profile, Design
from funkyfun import myfunk
from decimal import *
import sys
import datetime


def home(request):
	surveys = Survey.objects.all()
	myfunk(surveys)
	return render(request, 'home.html', {'surveys': surveys})

def all_surveys(request):
    surveys = Survey.objects.all()
    return render(request, 'all_surveys.html', {'surveys': surveys})

@login_required
def user_profile(request,user):
	surveys = Survey.objects.filter(owner__username=user)
	return render(request, 'all_surveys.html', {'surveys': surveys})

@login_required
def new_survey(request):
	if request.method == 'POST':
		name = request.POST['name']
		description = request.POST['description']

		user = request.user  # TODO: get the currently logged in user

		topic = Survey.objects.create(
			name=name,
			description=description, 
			owner=user
		)
		pk = topic.pk
		return redirect('design_survey',pk=pk) 

	return render(request, 'new_survey.html')



@login_required
def survey_edit(request,user,pk): 
	survey = Survey.objects.get(pk=pk)
	design = Design.objects.get(in_survey=pk)

	if request.method == 'POST':
		survey.description = request.POST['description_input']
		design.num_alts = request.POST['num_alts_input']  
		design.num_qs = request.POST['num_qs_input']
		design.none_option = request.POST['none_option']
		design.att1_name = request.POST['att1_name_input']
		design.att2_name = request.POST['att2_name_input']
		design.att3_name = request.POST['att3_name_input']
		design.att4_name = request.POST['att4_name_input']
		design.att5_name = request.POST['att5_name_input']
		design.att6_name = request.POST['att6_name_input']
		design.att7_name = request.POST['att7_name_input']
		design.att8_name = request.POST['att8_name_input']
		design.att9_name = request.POST['att9_name_input']
		design.att10_name = request.POST['att10_name_input']

		design.att1_type = request.POST['att1_type_input']
		design.att2_type = request.POST['att2_type_input']
		design.att3_type = request.POST['att3_type_input']
		design.att4_type = request.POST['att4_type_input']
		design.att5_type = request.POST['att5_type_input']
		design.att6_type = request.POST['att6_type_input']
		design.att7_type = request.POST['att7_type_input']
		design.att8_type = request.POST['att8_type_input']
		design.att9_type = request.POST['att9_type_input']
		design.att10_type = request.POST['att10_type_input']



		design.save()
		survey.save()
		return redirect('user_profile', user=request.user)

	return render(request, 'survey_edit.html',{'survey':survey},{'design':design})

@login_required
def design_survey(request, pk):
	survey = Survey.objects.get(pk=pk)

	if request.method == 'POST':
		num_alts = int(request.POST['num_alt_input'])
		num_qs = int(request.POST['num_qs_input'])
		none_option = int(request.POST['none_option_input'])
		user = request.user  # TODO: get the currently logged in user
		topic = Design.objects.create(
			name=pk,
			num_alts=num_alts,  
			num_qs=num_qs,
			none_option=none_option,
			in_survey=survey      
		)

		return redirect('design_questions',pk=pk) 

	return render(request, 'design_survey.html',{'survey':survey})

@login_required
def design_questions(request, pk):
	survey = Survey.objects.get(pk=pk)
	design = Design.objects.get(in_survey=pk)

	if request.method == 'POST':
		design.att1_name = request.POST['att1_name_input']
		design.att2_name = request.POST['att2_name_input']
		design.att3_name = request.POST['att3_name_input']
		design.att4_name = request.POST['att4_name_input']
		design.att5_name = request.POST['att5_name_input']
		design.att6_name = request.POST['att6_name_input']
		design.att7_name = request.POST['att7_name_input']
		design.att8_name = request.POST['att8_name_input']
		design.att9_name = request.POST['att9_name_input']
		design.att10_name = request.POST['att10_name_input']

		design.att1_type = request.POST['att1_type_input']
		design.att2_type = request.POST['att2_type_input']
		design.att3_type = request.POST['att3_type_input']
		design.att4_type = request.POST['att4_type_input']
		design.att5_type = request.POST['att5_type_input']
		design.att6_type = request.POST['att6_type_input']
		design.att7_type = request.POST['att7_type_input']
		design.att8_type = request.POST['att8_type_input']
		design.att9_type = request.POST['att9_type_input']
		design.att10_type = request.POST['att10_type_input']

		request.POST=request.POST.copy()

		for item in request.POST:
			if request.POST[item] == '':
				request.POST[item] = Decimal(-1)
				print(request.POST[item])

		design.att1_values = [request.POST['att1v1_input'],request.POST['att1v2_input'], request.POST['att1v3_input'], request.POST['att1v4_input'], request.POST['att1v5_input'], request.POST['att1v6_input'], request.POST['att1v7_input']]

		design.att2_values = [request.POST['att2v1_input'], request.POST['att2v2_input'], request.POST['att2v3_input'], request.POST['att2v4_input'], request.POST['att2v5_input'], request.POST['att2v6_input'], request.POST['att2v7_input']]

		design.att3_values = [request.POST['att3v1_input'], request.POST['att3v2_input'], request.POST['att3v3_input'], request.POST['att3v4_input'], request.POST['att3v5_input'], request.POST['att3v6_input'], request.POST['att3v7_input']]

		design.att4_values = [request.POST['att4v1_input'],request.POST['att4v2_input'], request.POST['att4v3_input'], request.POST['att4v4_input'], request.POST['att4v5_input'], request.POST['att4v6_input'], request.POST['att4v7_input']]

		design.att5_values = [request.POST['att5v1_input'], request.POST['att5v2_input'], request.POST['att5v3_input'], request.POST['att5v4_input'], request.POST['att5v5_input'], request.POST['att5v6_input'], request.POST['att5v7_input']]

		design.att6_values = [request.POST['att6v1_input'], request.POST['att6v2_input'], request.POST['att6v3_input'], request.POST['att6v4_input'], request.POST['att6v5_input'], request.POST['att6v6_input'], request.POST['att6v7_input']]

		design.att7_values = [request.POST['att7v1_input'],request.POST['att7v2_input'], request.POST['att7v3_input'], request.POST['att7v4_input'], request.POST['att7v5_input'], request.POST['att7v6_input'], request.POST['att7v7_input']]

		design.att8_values = [request.POST['att8v1_input'], request.POST['att8v2_input'], request.POST['att8v3_input'], request.POST['att8v4_input'], request.POST['att8v5_input'], request.POST['att8v6_input'], request.POST['att8v7_input']]

		design.att9_values = [request.POST['att9v1_input'], request.POST['att9v2_input'], request.POST['att9v3_input'], request.POST['att9v4_input'], request.POST['att9v5_input'], request.POST['att9v6_input'], request.POST['att9v7_input']]

		design.att10_values = [request.POST['att10v1_input'],request.POST['att10v2_input'], request.POST['att10v3_input'], request.POST['att10v4_input'], request.POST['att10v5_input'], request.POST['att10v6_input'], request.POST['att10v7_input']]

		design.save()
		return redirect('design_profiles',pk=pk)
	return render(request, 'design_questions.html',{'survey':survey},{'design':design})

@login_required
def design_profiles(request, pk):
	survey = Survey.objects.get(pk=pk)
	design = Design.objects.get(in_survey=pk)
	print (design.att1_name)
	return render(request, 'design_profiles.html',{'survey':survey},{'design':design})
