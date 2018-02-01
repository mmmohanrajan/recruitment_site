from rest_framework import serializers
 
from api.v1.models import JobPost, Employee, Education, Experience

 
class JobPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = JobPost
		fields = ('title', 'key_skills', 'posted_by', 'experience', 'job_description', 'created_on')
		read_only_fields = ['posted_by']

class ExperienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Experience
		fields = ('experience', 'designation', 'company_name')


class EducationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Education
		fields = ('degree', 'university', 'year', 'percentage')


class EmployeeSerializer(serializers.ModelSerializer):
	experience = ExperienceSerializer(many=True)
	education = EducationSerializer(many=True)

	class Meta:
		model = Employee
		fields = ('name', 'sex', 'date_of_birth', 'phone_number', 'email', 'is_accepted', 'education', 'experience')
		read_only_fields = ['is_accepted']

	def create(self, validated_data) :
	    experiences_data = validated_data.pop('experience')
	    educations_data = validated_data.pop('education')
	    employee = Employee.objects.create(**validated_data)
	    for experience_data in experiences_data:
	    	Experience.objects.create(employee=employee, **experience_data)
	    for education_data in educations_data:
	    	Education.objects.create(employee=employee, **education_data)
	    return employee


