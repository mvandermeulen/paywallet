from .inventory import Inventory
from django.contrib import admin
from django.db.models import Count
import random
from django.utils.translation import gettext_lazy as _


class Dashboard(Inventory):
    class Meta:
        proxy = True
        verbose_name = _('Dashboard')
        verbose_name_plural = _('Dashboard')


class DashboardAdmin(admin.ModelAdmin):

    change_list_template = 'admin/cafe/dashboard.html'
    list_filter = ['cafe__name']

    def getRandomColor(self):
        letters = list('0123456789ABCDEF')
        color = '#'
        for i in range(6):
            f = random.randint(0, 15)
            color += letters[f]
        return color

    def get_product_count_based_on_stock(self, qs):
        labels = []
        data = []
        background_color = []
        #  Get product count based on stock whether it is in stock or out of stock

        in_stock_count = qs.filter(quantity__gt=5).count()
        labels.append('In Stock')
        data.append(in_stock_count)
        background_color.append(self.getRandomColor())

        low_stock_count = qs.filter(quantity__gt=0, quantity__lte=5).count()
        if (low_stock_count > 0):
            labels.append('Low Stock')
            data.append(low_stock_count)
            background_color.append(self.getRandomColor())

        oos_count = qs.filter(quantity=0).count()
        labels.append('OOS')
        data.append(oos_count)
        background_color.append(self.getRandomColor())

        return {
            'labels': labels,
            'datasets': [{'data': data,
                         'backgroundColor': background_color}]
        }

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
            response.context_data['get_product_count_based_on_stock'] = self.get_product_count_based_on_stock(
                qs)
        except (AttributeError, KeyError):
            return response
        return response
