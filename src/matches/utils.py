# from decimal import Decimal
# from django.contrib.auth import get_user_model

# from getfeedback.models import UserAnswer

# User = get_user_model()




# def get_points(user_a, user_b):
# 	a_answers = UserAnswer.objects.filter(user=user_a)[0]
# 	b_answers = UserAnswer.objects.filter(user=user_b)[0]
# 	a_total_awarded = 0

# 	if a_answers.project.id == b_answers.project.id:
# 		a_pref = a_answers.their_answer
# 		b_answer = b_answers.my_answer
# 		if a_pref == b_answer:
# 			a_total_awarded += a_answers.their_points
# 			print "%s has awarded %s points to %s" %(user_a, a_total_awarded ,user_b)


# get_points(ryanpower,johnlennon)









# def get_match(user_a, user_b):
# 	user_a_answers = UserAnswer.objects.filter(user=user_a)[0]
# 	user_b_answers = UserAnswer.objects.filter(user=user_b)[0]

# 	if user_a_answers.project.id == user_b_answers.project.id:
# 		user_a_answer = user_a_answers.my_answer
# 		user_a_pref = user_a_answers.their_answer
# 		user_b_answer = user_b_answers.my_answer
# 		user_b_pref = user_b_answers.their_answer

# 		user_a_total_awarded = 0
# 		user_b_total_awarded = 0

# 		if user_a_answer == user_b_pref:
# 			user_b_total_awarded += user_b_answers.their_points
# 			print "%s fits with %s's preference" %(user_a_answers.username, user_b_answers.username)

# 		if user_a_pref == user_b_answer:
# 			user_a_total_awarded += user_a_answers.their_points
# 			print "%s fits with %s's preference" %(user_a_answers.username, user_b_answers.username)
			
# 		if user_a_answer == user_b_pref and user_a_pref == user_b_answer:
# 			print "this is an ideal answer for both"
# 		print user_a_total_awarded, user_b_total_awarded


# get_match(ryanpower,johnlennon)








