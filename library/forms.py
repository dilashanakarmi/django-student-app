from django import forms
from .models import Book, Member, BorrowRecord

class BookForm(forms.ModelForm):
    publication_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Select the publication date'
    )
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publication_date', 'total_copies', 'available_copies', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '13-digit ISBN'}),
            'total_copies': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'available_copies': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Book description...'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        total = cleaned_data.get('total_copies')
        available = cleaned_data.get('available_copies')
        
        if total and available and available > total:
            raise forms.ValidationError('Available copies cannot exceed total copies!')
        
        return cleaned_data


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone', 'membership_id', 'status']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'membership_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Membership ID'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class BorrowRecordForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='When should the book be returned?'
    )
    
    class Meta:
        model = BorrowRecord
        fields = ['book', 'member', 'due_date', 'return_date', 'is_returned']
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'member': forms.Select(attrs={'class': 'form-control'}),
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'is_returned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }