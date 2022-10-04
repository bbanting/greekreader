from django.contrib import admin

from .models import (HelpSet, Lexeme, Word, Root, Book, Chapter, Collection, 
HelpImage, HelpSetAssignment, StudyGroup, Membership)


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1


class StudyGroupAdmin(admin.ModelAdmin):
    model = StudyGroup
    inlines = [MembershipInline]


class HelpSetAssignmentInline(admin.TabularInline):
    model = HelpSetAssignment
    extra = 1


class BookAdmin(admin.ModelAdmin):
    model = Book
    inlines = [HelpSetAssignmentInline]


admin.site.register(HelpSet)
admin.site.register(Root)
admin.site.register(Lexeme)
admin.site.register(Word)
admin.site.register(HelpImage)
admin.site.register(Collection)
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter)
admin.site.register(StudyGroup, StudyGroupAdmin)
