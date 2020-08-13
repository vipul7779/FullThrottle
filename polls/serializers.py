# from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer, ReadOnlyField
# from polls.models import Date, Member_Details, Member

# class DateSerializer(serializers.ModelSerializer):
#     # category_name = serializers.RelatedField(source='category', read_only=True)

#     class Meta:
#         model = Date 
#         fields = "__all__"

# class MemberDetailsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Member_Details 
#         fields = "__all__"

# class MemberSerializer(serializers.ModelSerializer):
#     x = serializers.ReadOnlyField(source='activity_periods.start_time')

#     class Meta:
#         model = Member 
#         fields = "__all__"