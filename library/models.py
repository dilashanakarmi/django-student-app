from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Member(models.Model):
    MEMBERSHIP_STATUS = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    membership_id = models.CharField(max_length=20, unique=True)
    join_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=MEMBERSHIP_STATUS, default='active')
    
    class Meta:
        ordering = ['first_name', 'last_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.membership_id})"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_records')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrow_records')
    checkout_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-checkout_date']
    
    def __str__(self):
        return f"{self.member.get_full_name()} borrowed {self.book.title}"