from .forms import input_beta
from django.shortcuts import render
from warehouse.models import warehouse
from order_temp.models import temporary_time_address, temporary_order
import datetime


def order(request):
    # FUNCTIONS
    def bill(shrink):
        shrinks_cost = shrink * 300
        if shrink < 6:
            delivery_cost = 100
        else:
            delivery_cost = 100 + (shrink - 5) * 10
        tax_cost = float((shrinks_cost + delivery_cost)) / 100 * 9
        temp_total = temporary_order(shr=shrinks_cost, deli=delivery_cost, tax=tax_cost)
        temp_total.save()

    def delivery_time_address(dd, sit, add):
        days = dd
        if sit == 2 and days < 14:
            days = 14
        temp_time = temporary_time_address(days=days, address=add)
        temp_time.save()

    # PARAMETERS & VARIABLES
    total = sc = dc = tc = dt = ad = ware = error = error2 = ''

    # MAIN OPERATION
    first = input_beta(request.POST or None)

    if first.is_valid():

        data = first.cleaned_data
        first = input_beta()
        ware = data['ware']
        address = data['address']
        date = data['date']
        shrinks = data['shrinks']
        ware_need = warehouse.objects.get(ware_name=ware)
        ware_ready = ware_need.ware_ready
        ware_semi = ware_need.ware_semi

        if shrinks > ware_ready:
            diff = shrinks - ware_ready
            if diff > ware_semi:
                error = "sorry! it's out of stock"
            else:
                bill(shrinks)
                situation = 2
                delivery_time_address(date, situation, address)
                if date < 14:
                    error2 = f'due to some issue your delivery date has been delayed for {14 - date} days'
        else:
            bill(shrinks)
            situation = 1
            delivery_time_address(date, situation, address)

        to = temporary_order.objects.last()  # to --> temporary order
        tt = temporary_time_address.objects.last()  # tt --> temporary time
        if to and tt:
            sc = to.shr
            dc = to.deli
            tc = to.tax
            total = sc + dc + tc
            dys = tt.days
            ad = tt.address
            now = datetime.date.today()
            dt = now + datetime.timedelta(days=dys)

    context = {
        'a': first,
        'error': error,
        'error2': error2,
        'sc': sc,
        'dc': dc,
        'tc': tc,
        'total': total,
        'dt': dt,
        'ad': ad,
        'ware': ware,
    }

    return render(request, 'orderpage.html', context)
