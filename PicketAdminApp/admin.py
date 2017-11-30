from django.contrib import admin
from .models import Place, Picket, Spot, Task
from .models import Person


class PicketAdmin(admin.ModelAdmin):
    #list_display = ['title', 'status']
    #ordering = ['title']
    actions = ['offer_a_job', 'parse_place_list', 'parse_person_list']

    def offer_a_job(self, request, queryset):
        person_list = Person.objects.all()
        id_list = []
        for p in person_list:
            id_list.append(p.telegram_id)
        #survey_of_picketers(id_list)
        #self.message_user(request, 'Список согласившихся: '+str(id_list))
    offer_a_job.short_description = "Выслать приглашение на работу"

    def parse_person_list(self, request, queryset):
        for picket in queryset:
            import pandas as pd
            df = pd.read_excel(picket.person_list)
            rows = []
            for i in range(0, len(df)):
                row = {}
                for k in df.keys():
                    row[k] = df[k][i]
                    rows.append(row)

            for row in rows:
                Person.objects.get_or_create(telegram_id=row['telegram_id'],
                                            name = row['name'],
                                             surname = row['surname'],
                                             patronymic = row['patronymic'],
                                             station = row['station'])
        self.message_user(request, 'Пикетчики: ' + str(Person.objects.all()))

    parse_person_list.short_description = "Добавить новых пикетчиков из файла"


    def parse_place_list(self,request, queryset):
        return_str = ''
        for picket in queryset:
            import pandas as pd
            df = pd.read_excel(picket.place_list)
            rows = []
            picket.places = []
            for i in range(0,len(df)):
                row = {}
                for k in df.keys():
                    row[k] = df[k][i]
                rows.append(row)

            for row in rows:
                new_place = Place.objects.get_or_create(latitude = row['latitude'],
                                        longitude=row['longitude'],
                                        shortname = row['shortname'],
                                        metro=row['metro'],
                                        description=row['description'])
                #Spot.objects.get_or_create(picket = picket,
                                            #place = new_place)
                if new_place[1] == True:
                    picket.places.append(new_place[0])

        return_str = ", ".join(str(x) for x in picket.places)
        self.message_user(request, 'Места: ' + return_str)
    parse_place_list.short_description = "Добавить места пикета из файла"

admin.site.register(Picket, PicketAdmin)
admin.site.register(Person)
admin.site.register(Place)
#admin.site.register(Picket)
admin.site.register(Spot)
admin.site.register(Task)