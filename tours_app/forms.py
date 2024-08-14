from typing import Any
from django import forms
from django.forms import ModelForm
from .models import Tour, Type_Of_Tour, Profile


class Type_Tour(ModelForm):
    class Meta:
        model = Type_Of_Tour
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                    "placeholder": "name",
                }
            ),
        }


# Create a Tour form
class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = (
            "name",
            "duration",
            "maxGroupSize",
            "difficulty",
            "price",
            "start_location",
            "summary",
            "description",
            "type_tour",
            "imageCover",
        )
        labels = {
            "name": "",
            "duration": "",
            "maxGroupSize": "",
            "difficulty": "",
            "price": "",
            "start_location": "",
            "summary": "",
            "description": "",
            "type_tour": "",
            "imageCover": "",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "mb-5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-400 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    "placeholder": "name",
                }
            ),
            "duration": forms.TextInput(
                attrs={
                    "class": "mb-5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-400 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    "placeholder": "duration",
                }
            ),
            "maxGroupSize": forms.TextInput(
                attrs={
                    "class": "mb-5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-400 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    "placeholder": "maxGroupSize",
                }
            ),
            "difficulty": forms.TextInput(
                attrs={
                    "class": "mb-5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-400 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    "placeholder": "difficulty",
                }
            ),
            "price": forms.TextInput(
                attrs={
                    "class": "mb-5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-400 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    "placeholder": "price",
                }
            ),
            "start_location": forms.TextInput(
                attrs={
                    "class": "mb-5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-400 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    "placeholder": "start_location",
                }
            ),
            "summary": forms.TextInput(
                attrs={
                    "class": "mb-5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-400 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    "placeholder": "summary",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "mb-5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-400 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    "placeholder": "description",
                }
            ),
            "type_tour": forms.Select(
                attrs={
                    "class": "mb-5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-400 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    "placeholder": "Type_tour",
                }
            ),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("profile_pic",)
        labels = {
            "profile_pic": "",
        }
