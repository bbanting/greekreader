from django.contrib import admin
from .models import HelpSet, Lexeme, Word, Root, Book, Collection, HelpImage, HelpSetAssignment



class HelpSetInline(admin.TabularInline):
    model = HelpSetAssignment
    extra = 1


class BookAdmin(admin.ModelAdmin):
    model = Book
    inlines = [HelpSetInline]


admin.site.register(HelpSet)
admin.site.register(Root)
admin.site.register(Lexeme)
admin.site.register(Word)
admin.site.register(HelpImage)
admin.site.register(Collection)
admin.site.register(Book, BookAdmin)