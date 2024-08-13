from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.contrib.auth import authenticate
from django.contrib import messages
from django.utils import timezone
from datetime import date
from django.db.models import Q

# Create your views here.

def index(request):

    return render(request,"index.html")

def login(request):

    if request.POST:
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email,password=password)

        if user:
            if user.is_active:
                if user.is_superuser:
                    return redirect('/admin_home')
                elif user.usertype=="caters":
                    user = Caters_registration.objects.get(email=email)
                    if user.approved:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/caters_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')
                elif user.usertype=="restaurant":
                    user = Restauarant_registration.objects.get(email=email)
                    if user.approved:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/restaurant_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')
                elif user.usertype=="user":
                    user = User_registration.objects.get(email=email)
                    request.session["email"]=email
                    request.session["id"]=user.id
                    return redirect('/user_home')


    return render(request,"login.html")

def registration_users(request):

    if request.POST:
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']

        log=Login_table.objects.create_user(
            username=email,
            password=password,
            usertype="user"
        )
        log.save()

        user=User_registration.objects.create(
            name=name,
            contact=contact,
            email=email,
            login_id=log
            )
        user.save()

        messages.info(request,"Registration successful,you can login now")


    return render(request,"registration_users.html")


def registration_caters(request):

    if request.POST:
        owner_name=request.POST['owner_name']
        caters_name=request.POST['caters_name']
        address=request.POST['address']
        map_link=request.POST['map_link']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        caters_license=request.FILES['caters_license']
        id_proof=request.FILES['id_proof']
        cg_image=request.FILES['cg_image']
        ck_image=request.FILES['ck_image']

        log=Login_table.objects.create_user(
            username=email,
            password=password,
            usertype="caters"
        )
        log.save()

        caters=Caters_registration.objects.create(
            owner_name=owner_name,
            caters_name=caters_name,
            address=address,
            map_link=map_link,
            contact=contact,
            email=email,
            caters_license=caters_license,
            id_proof=id_proof,
            cg_image=cg_image,
            ck_image=ck_image,
            approved=False,
            login_id=log
        )
        caters.save()
        messages.info(request,"Registration successful,Wait admin approvel")

    return render(request,"registration_caters.html")


def registration_restaurants(request):

    if request.POST:
        owner_name=request.POST['owner_name']
        restaurant_name=request.POST['restaurant_name']
        location=request.POST['location']
        map_link=request.POST['map_link']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        opening_time=request.POST['opening_time']
        closing_time=request.POST['closing_time']
        restaurant_license=request.FILES['restaurant_license']
        id_proof=request.FILES['id_proof']
        r_image=request.FILES['r_image']
        rk_image=request.FILES['rk_image']

        log=Login_table.objects.create_user(
            username=email,
            password=password,
            usertype="restaurant"
        )
        log.save()

        restaurant=Restauarant_registration.objects.create(
            owner_name=owner_name,
            restaurant_name=restaurant_name,
            location=location,
            map_link=map_link,
            contact=contact,
            email=email,
            opening_time=opening_time,
            closing_time=closing_time,
            restaurant_license=restaurant_license,
            id_proof=id_proof,
            r_image=r_image,
            rk_image=rk_image,
            approved=False,
            login_id=log
        )
        restaurant.save()
        messages.info(request,"Registration successful,Wait admin approvel")   

    return render(request,"registration_restaurants.html")

########################## ADMIN ################################

def admin_home(request):
    
    amount=User_booking_food.objects.filter(payment_status=True)
    booking_food=User_booking_food.objects.filter(payment_status=True)
    food_added=Add_food_admin_to_user.objects.all()
    food_remaining=Add_food_admin.objects.all()

    total_amount=0
    total_bookings=0
    added_foods=0
    remaining_foods=0

    for p in amount:
        total_amount+=p.price 
    for b in booking_food:
        total_bookings+=b.quantity
    for a in food_added:
        added_foods+=a.quantity
    for f in food_remaining:
        remaining_foods+=f.quantity

    return render(request,"admin/admin_home.html",{
        "total_amount":total_amount,
        "total_bookings":total_bookings,
        "added_foods":added_foods,
        "remaining_foods":remaining_foods,
        })

def view_caters_requests(request):

    caters=Caters_registration.objects.all()

    return render(request,"admin/view_caters_requests.html",{"caters":caters})

def accept_caters(request):

    cid=request.GET.get('id')
    caters=Caters_registration.objects.get(id=cid)
    caters.approved=True
    caters.save()
    messages.info(request,"Request approved")

    return redirect('/view_caters_requests')

def reject_caters(request):

    cid=request.GET.get('id')
    caters=Caters_registration.objects.get(id=cid)
    caters.delete()
    log=Login_table.objects.get(username=caters.login_id)
    log.delete()
    messages.info(request,"Request rejected")

    return redirect('/view_caters_requests')

def view_restaurants_requests(request):

    restaurants=Restauarant_registration.objects.all()

    return render(request,"admin/view_restaurants_requests.html",{"restaurants":restaurants})

def accept_restaurants(request):
    rid=request.GET.get('id')
    restaurant=Restauarant_registration.objects.get(id=rid)
    restaurant.approved=True
    restaurant.save()

    messages.info(request,"Request accepted")
    return redirect('/view_restaurants_requests')

def reject_restaurants(request):

    rid=request.GET.get('id')
    restaurant=Restauarant_registration.objects.get(id=rid)
    restaurant.delete()
    log=Login_table.objects.get(username=restaurant.login_id)
    log.delete()
    messages.info(request,"Request rejected")

    return redirect('/view_restaurants_requests')


def view_caters(request):

    caters=Caters_registration.objects.filter(approved=True)

    return render(request,"admin/view_caters.html",{"caters":caters})

def delete_caters(request):

    cid=request.GET.get('id')
    caters=Caters_registration.objects.get(id=cid)
    caters.delete()
    log=Login_table.objects.get(username=caters.login_id)
    log.delete()

    messages.info(request,"Removed Successfully")
    return redirect('/view_caters')

def view_foods_admin(request):
    
    foods=Add_food_admin.objects.all()

    context = {
        'combined_foods': foods
    }

    return render(request, "admin/view_foods_admin.html", context)


def upload_food_admin(request):
    fid = request.GET.get('id')
    food = get_object_or_404(Add_food_admin, id=fid)

    if request.method == 'POST':
        # Get POST data
        food_name = request.POST.get('food_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        food_image = request.FILES.get('food_image')

        # Validate inputs
        if not food_name or not price or not quantity or not food_image:
            messages.error(request, "All fields are required.")
            return render(request, 'admin/upload_food_admin.html', {"food": food})

        # Convert and validate quantity and price
        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            messages.error(request, "Invalid price or quantity.")
            return render(request, 'admin/upload_food_admin.html', {"food": food})

        # Check if there is enough quantity
        if quantity > food.quantity:
            messages.error(request, "Not enough quantity available.")
            return render(request, 'admin/upload_food_admin.html', {"food": food})

        # Reduce quantity from the main food record
        food.quantity -= quantity
        food.save()

        # Create a new food record for the user
        food_user = Add_food_admin_to_user.objects.create(
            food_name=food_name,
            price=price,
            quantity=quantity,
            uploaded_time=timezone.now(),
            food_image=food_image,
            admin_food_id=food
        )
        food_user.save()

        messages.success(request, "Food added successfully.")
        return redirect('/view_foods_admin')

    return render(request, 'admin/upload_food_admin.html', {"food": food})

def view_bookings_users_admin(request):

    bookings=User_booking_food.objects.filter(payment_status=True)

    return render(request,"admin/view_bookings_user.html",{"bookings":bookings})
################# admin and restaurant #######################

def view_restaurants(request):

    restaurants=Restauarant_registration.objects.filter(approved=True)

    return render(request,"admin/view_restaurants.html",{"restaurants":restaurants})

def delete_restaurants(request):

    rid=request.GET.get('id')
    restaurants=Restauarant_registration.objects.get(id=rid)
    restaurants.delete()
    log=Login_table.objects.get(username=restaurants.login_id)
    log.delete()

    messages.info(request,"Removed Successfully")
    return redirect('/view_restaurants')

def view_users(request):

    users=User_registration.objects.all()

    return render(request,"admin/view_users.html",{"users":users})

def delete_users(request):

    uid=request.GET.get('id')
    users=User_registration.objects.get(id=uid)
    users.delete()
    log=Login_table.objects.get(username=users.login_id)
    log.delete()

    messages.info(request,"Removed Successfully")
    return redirect('/view_users')

def view_restaurant_requests_admin(request):

    foods=Add_food_restaurants.objects.all() 

    return render(request,"admin/restaurant_food_requests.html",{"foods":foods})

def accept_restaurant_food_request(request):
    fid=request.GET.get('id')
    food=Add_food_restaurants.objects.get(id=fid)
    food.accepted='Accepted'

    food.admin_accept_time=timezone.now()
    food.save()
    messages.info(request,"Accepted Sucessfully")

    return redirect('/view_restaurant_requests_admin')

def reject_restaurant_food_request(request):
    fid=request.GET.get('id')
    food=Add_food_restaurants.objects.get(id=fid)
    food.accepted='Rejected'
    food.admin_accept_time=timezone.now()
    food.save()

    messages.info(request,"Rejected Sucessfully")

    return redirect('/view_restaurant_requests_admin')

def payment_restaurant_food(request):
    fid=request.GET.get('id')
    food=Add_food_restaurants.objects.get(id=fid)
    # print(food.restaurant_id.restaurant_name)

    return render(request,"admin/payment_restaurant_food.html",{"food":food})

def payment_confirm_restaurant_food(request):
    id=request.GET.get('id')
    food=Add_food_restaurants.objects.get(id=id)
    food.payment_status=True
    food.save()
    booking=Booking_restaurant_food.objects.create(
        payment_status=True,
        booked_date=timezone.now(),
        restaurant_food_id=food
    )
    booking.save()
    messages.info(request,"Payment Sucessfull")

    return redirect('/view_restaurant_requests_admin')

def view_bookings_admin_restaurants(request):
    booking=Booking_restaurant_food.objects.all()

    return render(request,'admin/view_bookings_restuarant.html',{"booking":booking})

#################### admin and caters ###################

def view_caters_requests_admin(request):

    foods=Add_food_caters.objects.all() 

    return render(request,"admin/caters_food_requests.html",{"foods":foods})

def accept_caters_food_request(request):
    fid=request.GET.get('id')
    food=Add_food_caters.objects.get(id=fid)
    food.accepted='Accepted'
    food.admin_accept_time=timezone.now()
    food.save()
    messages.info(request,"Accepted Sucessfully")

    return redirect('/view_caters_requests_admin')

def reject_caters_food_request(request):
    fid=request.GET.get('id')
    food=Add_food_caters.objects.get(id=fid)
    food.accepted='Rejected'
    food.admin_accept_time=timezone.now()
    food.save()

    messages.info(request,"Rejected Sucessfully")

    return redirect('/view_caters_requests_admin')


def payment_caters_food(request):
    fid=request.GET.get('id')
    food=Add_food_caters.objects.get(id=fid)

    return render(request,"admin/payment_caters_food.html",{"food":food})

def payment_confirm_caters_food(request):
    id=request.GET.get('id')
    food=Add_food_caters.objects.get(id=id)
    food.payment_status=True
    food.save()
    booking=Booking_caters_food.objects.create(
        payment_status=True,
        booked_date=timezone.now(),
        caters_food_id=food
    )
    booking.save()
    messages.info(request,"Payment Sucessfull")

    return redirect('/view_caters_requests_admin')


def view_bookings_admin_caters(request):
    booking=Booking_caters_food.objects.all()

    return render(request,'admin/view_bookings_caters.html',{"booking":booking})

############# admin and caters #################

def add_food_admin_restaurant(request):
    
    fid=request.GET.get('id')
    restuarant_food=Add_food_restaurants.objects.get(id=fid)
    a=Booking_restaurant_food.objects.get(restaurant_food_id=fid)
    a.admin_uploaded=True
    a.save()

    admin_food=Add_food_admin.objects.create(
        
        food_name=restuarant_food.food_name,
        price=restuarant_food.price,
        quantity=restuarant_food.quantity,
        food_image=restuarant_food.food_image,
        uploaded_time=timezone.now()
    )
    admin_food.save()

    messages.info(request,"Added successfully")

    return redirect('/view_bookings_admin_restaurants')

def add_food_admin_caters(request):
    
    fid=request.GET.get('id')
    caters_food=Add_food_caters.objects.get(id=fid)
    a=Booking_caters_food.objects.get(caters_food_id=fid)
    a.admin_uploaded=True
    a.save()

    admin_food=Add_food_admin.objects.create(
        
        food_name=caters_food.food_name,
        price=caters_food.price,
        quantity=caters_food.quantity,
        food_image=caters_food.food_image,
        uploaded_time=timezone.now()
    )
    admin_food.save()
    messages.info(request,"Added successfully")

    return redirect('/view_bookings_admin_caters')

########################## CATERS ###############################

def caters_home(request):
    id=request.session['id']
    caters=Caters_registration.objects.get(id=id)

    amount=Add_food_caters.objects.filter(payment_status=True)
    sell=Add_food_caters.objects.filter(payment_status=True)
   
    total_amount=0
    total_sell=0

    for p in amount:
        total_amount+=p.total_price 
    for s in sell:
        total_sell+=s.quantity

    return render(request,"caters/caters_home.html",{
        "caters":caters,
        "total_amount":total_amount,
        "total_sell":total_sell
        })

def sell_food_caters(request):
    id=request.session['id']
    caters_id=Caters_registration.objects.get(id=id)

    if request.POST:
        food_name=request.POST['food_name']
        price=request.POST['price']
        quantity=request.POST['quantity']
        food_image=request.FILES['food_image']
        
        total_price=int(price)*int(quantity)

        caters=Add_food_caters.objects.create(
            food_name=food_name,
            price=price,
            quantity=quantity,
            total_price=total_price,
            food_image=food_image,
            uploaded_time=timezone.now(),
            accepted='Pending',
            caters_id=caters_id
        )
        caters.save()
        messages.info(request,"Added successfully, wait for admin approvel ")

    return render(request,'caters/sell_food_caters.html')

def view_food_uploads_caters(request):
    id=request.session['id']
    caters_id=Caters_registration.objects.get(id=id)
    foods=Add_food_caters.objects.filter(caters_id=caters_id)

    return render(request,"caters/view_food_uploads_caters.html",{"foods":foods})


def cancel_food_caters(request):
    fid=request.GET.get('id')
    food=Add_food_caters.objects.get(id=fid)
    food.delete()
    messages.info(request,"Successfully removed")

    return redirect('/view_food_uploads_caters')

def view_bookings_food_caters(request):

    booking=Booking_caters_food.objects.all()

    return render(request,"caters/view_bookings_caters.html",{"booking":booking})



######################### RESTAURANTS ###########################

def restaurant_home(request):

    id=request.session['id']
    restaurant=Restauarant_registration.objects.get(id=id)

    amount=Add_food_restaurants.objects.filter(payment_status=True)
    sell=Add_food_restaurants.objects.filter(payment_status=True)
   
    total_amount=0
    total_sell=0

    for p in amount:
        total_amount+=p.total_price 
    for s in sell:
        total_sell+=s.quantity
  

    return render(request,"restaurant/restaurant_home.html",{
        "restaurant":restaurant,
        "total_amount":total_amount,
        "total_sell":total_sell,
        })

def sell_food_restaurants(request):
    id=request.session['id']
    restaurant_id=Restauarant_registration.objects.get(id=id)

    if request.POST:
        food_name=request.POST['food_name']
        price=request.POST['price']
        quantity=request.POST['quantity']
        food_image=request.FILES['food_image']
        
        total_price=int(price)*int(quantity)

        restaurant=Add_food_restaurants.objects.create(
            food_name=food_name,
            price=price,
            quantity=quantity,
            total_price=total_price,
            food_image=food_image,
            uploaded_time=timezone.now(),
            accepted='Pending',
            restaurant_id=restaurant_id
        )
        restaurant.save()
        messages.info(request,"Added successfully, wait for admin approvel ")

    return render(request,'restaurant/sell_food_restaurants.html')

def view_food_uploads_restaurants(request):
    id=request.session['id']
    restaurant_id=Restauarant_registration.objects.get(id=id)
    foods=Add_food_restaurants.objects.filter(restaurant_id=restaurant_id)

    return render(request,"restaurant/view_food_uploads_restaurants.html",{"foods":foods})


def cancel_food_restaurant(request):
    fid=request.GET.get('id')
    food=Add_food_restaurants.objects.get(id=fid)
    food.delete()
    messages.info(request,"Successfully removed")

    return redirect('/view_food_uploads_restaurants')


def view_bookings_food_restaurants(request):
        
    booking=Booking_restaurant_food.objects.all()

    return render(request,"restaurant/view_bookings_food_restaurants.html",{"booking":booking})


########################### USER ##############################


def user_home(request):
    id=request.session['id']
    user=User_registration.objects.get(id=id)
    foods=Add_food_admin_to_user.objects.all()

    return render(request,"user/user_home.html",{
        "foods":foods,
        "user":user})

def check_out_user(request):
    fid = request.GET.get('id')
    food = Add_food_admin_to_user.objects.get(id=fid)
    id = request.session['id']
    user = User_registration.objects.get(id=id)

    if request.POST:
        name = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        quantity = request.POST['quantity']
        
        # Convert quantity to integer
        quantity_int = int(quantity)
        
        # Check if the requested quantity is available
        if quantity_int > food.quantity:
            # Display an alert message if quantity exceeds available stock
            return render(request, "user/check_out_user.html", {
                'food': food,
                'error_message': 'Requested quantity exceeds available stock.'
            })
        
        booking = User_booking_food.objects.create(
            user_id=user,
            food_id=food,
            name=name,
            address=address,
            contact=contact,
            quantity=quantity_int,
            price=int(food.price) * quantity_int
        )

        booking.save()

        food.quantity -= quantity_int
        food.save()

        return redirect(f'/book_food_user?id={booking.id}')
    
    return render(request, "user/check_out_user.html", {'food': food})


def book_food_user(request):
    bid=request.GET.get('id')
    booking=User_booking_food.objects.get(id=bid)

    return render(request, "user/book_food_user.html",{"booking":booking})


def payment_page_user(request):

    bid=request.GET.get('id')
    booking=User_booking_food.objects.get(id=bid)
    booking.payment_status=True
    booking.booked_on=timezone.now()
    booking.save()
    # print(booking.price)

    if request.POST:
        pass
        return redirect('/view_bookings_user')
    messages.info(request,'Booking Confirmed')

    return render(request,"user/payment_page_user.html",{"booking":booking})

def view_bookings_user(request):

    bookings=User_booking_food.objects.all()


    return render(request,"user/view_bookings_user.html",{"bookings":bookings})

def add_feedbacks_user(request):
    bid=request.GET.get('id')
    booking=User_booking_food.objects.get(id=bid)
    id=request.session['id']
    user=User_registration.objects.get(id=id)

    if request.POST:
        feedback=request.POST['feedback']
        rating=request.POST['rating']

        feed=User_feedbacks.objects.create(
            feedback=feedback,
            rating=rating,
            booking_id=booking,
            user_id=user,
            date=timezone.now()
        )
        feed.save()
        messages.info(request,"Feedback send successfully")
        return redirect('/view_feedbacks_user')

    return render(request,"user/add_feedbacks_user.html")

def view_feedbacks_user(request):

    feedbacks=User_feedbacks.objects.all()

    return render(request,"user/view_feedbacks_user.html",{"feedbacks":feedbacks})

def view_foods_user(request):

    foods=Add_food_admin_to_user.objects.all()

    return render(request,"user/view_foods_user.html",{"foods":foods})

def search_foods(request):
   
    if request.method=="POST":
        searched=request.POST['searched']
        foods = Add_food_admin_to_user.objects.filter(Q(food_name__icontains=searched))


        return render(request,"user/search_food_user.html",{"searched":searched,"foods":foods})
    
    else:

        return render(request,"user/search_food_user.html")
