from django.contrib import admin
from .models import Book, Member, BorrowRecord

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'total_copies', 'available_copies', 'publication_date')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('publication_date', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'isbn', 'publication_date', 'description')
        }),
        ('Inventory', {
            'fields': ('total_copies', 'available_copies')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'membership_id', 'email', 'status', 'join_date')
    search_fields = ('first_name', 'last_name', 'email', 'membership_id')
    list_filter = ('status', 'join_date')
    readonly_fields = ('join_date',)
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Membership Details', {
            'fields': ('membership_id', 'status', 'join_date')
        }),
    )
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = 'Member Name'


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('get_member_name', 'get_book_title', 'checkout_date', 'due_date', 'is_returned')
    search_fields = ('member__first_name', 'member__last_name', 'book__title')
    list_filter = ('is_returned', 'checkout_date', 'due_date')
    readonly_fields = ('checkout_date',)
    
    fieldsets = (
        ('Borrow Information', {
            'fields': ('book', 'member', 'checkout_date')
        }),
        ('Return Details', {
            'fields': ('due_date', 'return_date', 'is_returned')
        }),
    )
    
    def get_member_name(self, obj):
        return obj.member.get_full_name()
    get_member_name.short_description = 'Member'
    
    def get_book_title(self, obj):
        return obj.book.title
    get_book_title.short_description = 'Book'