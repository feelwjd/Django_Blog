from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(error_messages = {'required':"제목을 입력해주세요"}, label = "제목", max_length=128)
    body = forms.CharField(error_messages = {'required':"내용을 입력해주세요."}, label = "내용", widget = forms.Textarea)