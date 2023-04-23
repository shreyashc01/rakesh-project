import imp
import json
from re import U
from apps.home import blueprint
from flask import render_template, request, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps import db
from apps.home.models import UserModel
from apps.home.models import MainUser
from apps.home.models import ProductMaster
from apps.home.models import CustomerMaster


@blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html', segment='dashboard')


@blueprint.route('/offer-addoffer', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        user1 = ProductMaster.query.all()
        return render_template('home/add-offer.html',users=users,user1=user1,segment='offer-addoffer')
    if request.method == 'POST':
        # usr_id = request.form['usr_id']
        # usr_name = request.form['usr_name']
        # usr_password = request.form['usr_password']
        # usr_api_key = request.form['usr_api_key']
        # usr_api_secret_key = request.form['usr_api_secret_key']
        # usr_totp_key = request.form['usr_totp_key']
        # usr_access_key = ""
        # usr_access_key_time = ""
        # usr_autologin_status = request.form['usr_autologin_status']
        # usr_autoverify_status = ""
        # usr_autologin = ""
        # usr_autologout_status = ""
        # usr_aut_prem_to_sell_nifty = ""
        # usr_aut_prem_to_sell_bank = ""
        # usr_aut_stike_to_buy_nifty = ""
        # usr_aut_stike_to_buy_bank = ""
        # usr_man_odr_1buy_nifty = ""
        # usr_man_odr_2sell_nifty = ""
        # usr_man_odr_1buy_bank = ""
        # usr_man_odr_2sell_bank = ""
        # usr_funds_not_to_use = ""
        # usr_max_qty = ""
        # usr_disp_open_post = ""
        # usr_disp_net_day = ""
        # usr_disp_funds_avil = ""

        # # else we can create the user
        # user = UserModel(usr_id=usr_id,
        #     usr_name=usr_name,
        #     usr_password=usr_password,
        #     usr_api_key=usr_api_key,
        #     usr_api_secret_key=usr_api_secret_key,
        #     usr_totp_key=usr_totp_key,
        #     usr_access_key=usr_access_key,
        #     usr_access_key_time=usr_access_key_time,
        #     usr_autologin_status=usr_autologin_status,
        #     usr_autoverify_status=usr_autoverify_status,
        #     usr_autologin=usr_autologin,
        #     usr_autologout_status = usr_autologout_status,
        #     usr_aut_prem_to_sell_nifty = usr_aut_prem_to_sell_nifty,
        #     usr_aut_prem_to_sell_bank = usr_aut_prem_to_sell_bank,
        #     usr_aut_stike_to_buy_nifty = usr_aut_stike_to_buy_nifty,
        #     usr_aut_stike_to_buy_bank = usr_aut_stike_to_buy_bank,
        #     usr_man_odr_1buy_nifty = usr_man_odr_1buy_nifty,
        #     usr_man_odr_2sell_nifty =usr_man_odr_2sell_nifty,
        #     usr_man_odr_1buy_bank = usr_man_odr_1buy_bank,
        #     usr_man_odr_2sell_bank = usr_man_odr_2sell_bank,
        #     usr_funds_not_to_use = usr_funds_not_to_use,
        #     usr_max_qty = usr_max_qty,
        #     usr_disp_open_post =usr_disp_open_post,
        #     usr_disp_net_day = usr_disp_net_day,
        #     usr_disp_funds_avil = usr_disp_funds_avil )
        # db.session.add(user)
        # db.session.commit()
        return redirect('/offer-offerlist')


@blueprint.route('/add-kits', methods=['GET', 'POST'])
@login_required
def kit_add():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        user1 = ProductMaster.query.all()
        return render_template('home/add-kit.html',users=users,user1=user1)
    if request.method == 'POST':
        return redirect('/Kit-masters')

@blueprint.route('/add-user-login', methods=['GET', 'POST'])
@login_required
def add_user_login():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        user1 = ProductMaster.query.all()
        return render_template('home/add-user-login.html',users=users,user1=user1)
    if request.method == 'POST':
        return redirect('/User-masters')
    
@blueprint.route('/invoice-addinvoice', methods=['GET', 'POST'])
@login_required
def addinvoice():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        user1 = ProductMaster.query.all()
        return render_template('home/add-invoice.html',users=users,user1=user1,segment='add-invoice')

@blueprint.route('/invoice-invoiceslist', methods=['GET', 'POST'])
@login_required
def listinvoices():
    return render_template('home/invoices.html', segment='list-invoice')



@blueprint.route('/PO-addpo', methods=['GET', 'POST'])
@login_required
def addpo():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        user1 = ProductMaster.query.all()
        return render_template('home/add-purchaseorder.html',users=users,user1=user1,segment='add-purchaseorder')

@blueprint.route('/PO-POlist', methods=['GET', 'POST'])
@login_required
def listpo():
    return render_template('home/purchaseorder.html', segment='list-purchaseorder')

@blueprint.route('/BOM-List', methods=['GET', 'POST'])
@login_required
def BOM_List():
    return render_template('home/BOM-Lists.html', segment='BOM-List')

@blueprint.route('/Purchase-Order-Request', methods=['GET', 'POST'])
@login_required
def Add_PO_REQ():
    return render_template('home/ADD-PO-Request.html', segment='Purchase-Order-Request')

@blueprint.route('/Purchase-Order-Request-List', methods=['GET', 'POST'])
@login_required
def PO_REQ_LIST():
    return render_template('home/PO-Request-List.html', segment='Purchase-Order-Request-List')

@blueprint.route('/offer-offerlist', methods=['GET', 'POST'])
@login_required
def retrieve_list():
    # if MainUser.query.filter_by(id=1).first() == None:
    #     users = MainUser(
    #         main_usr_id = "main_usr_id",
    #         main_usr_name = "main_usr_name")
    #     db.session.add(users)
    #     db.session.commit()
    # if "main_usr_apply" in request.form:
        # all_users = UserModel.query.filter_by(usr_id=request.form.get('main_usr_select')).first()
        # main_user = MainUser.query.filter_by(id=1).first()
        # if all_users != None:
        #     main_user.main_usr_id = all_users.usr_id
        #     main_user.main_usr_name = all_users.usr_name
        #     db.session.commit()
    users = UserModel.query.all()
    main_user = MainUser.query.filter_by(id=1).first()
    return render_template('home/users.html', main_user= main_user, users=users, segment='offer-offerlist')



@blueprint.route('/<int:id>/editcustomer', methods=['GET', 'POST'])
@login_required
def update(id):
    user = CustomerMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        user.customer_name = request.form['customer_name']
        user.primary_contact_name = request.form['primary_contact_name']
        user.secondary_contact_name = request.form['secondary_contact_name']
        user.email_id = request.form['email_id']
        user.contact_number = request.form['contact_number']
        user.pan_number = request.form['pan_number']
        user.gst_number = request.form['gst_number']
        user.address = request.form['address']

        db.session.commit()
        return redirect('/Customer-masters')

    return render_template('home/updatecustomer.html', user=user, segment='Customer-masters')


@blueprint.route('/<int:id>/editproduct', methods=['GET', 'POST'])
@login_required
def update2(id):
    user = ProductMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        user.product_name = request.form['product_name']
        user.part_no = request.form['part_no']
        user.rack_no = request.form['rack_no']
        user.bin_no = request.form['bin_no']
        user.minimum_qty = request.form['minimum_qty']
        user.maximum_order = request.form['maximum_order']
        user.description = request.form['description']

        db.session.commit()
        return redirect('/Product-masters')

    return render_template('home/updateproduct.html', user=user, segment='Product-masters')


@blueprint.route('/Product-masters', methods=['GET', 'POST'])
@login_required
def product_masters():
    if request.method == 'GET':
        users = ProductMaster.query.all()
        return render_template('home/Product-masters.html',users=users, segment='Product-masters')
    if request.method == 'POST':
        product_name = request.form['product_name']
        part_no = request.form['part_no']
        rack_no = request.form['rack_no']
        bin_no = request.form['bin_no']
        minimum_qty = request.form['minimum_qty']
        maximum_order = request.form['maximum_order']
        description = request.form['description']
        offer = ProductMaster(product_name=product_name,
            part_no=part_no,
            rack_no=rack_no,
            bin_no=bin_no,
            minimum_qty=minimum_qty,
            maximum_order=maximum_order,
            description=description)
        
        db.session.add(offer)
        db.session.commit()
        return redirect('/Product-masters')

@blueprint.route('/Kit-masters')
@login_required
def kit_masters():
    users = UserModel.query.all()
    return render_template('home/Kit-masters.html', users=users, segment='Kit-masters')



@blueprint.route('/Customer-masters', methods=['GET', 'POST'])
@login_required
def Customer_masters():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        return render_template('home/Customer-masters.html',users=users, segment='Customer-masters')
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        primary_contact_name = request.form['primary_contact_name']
        secondary_contact_name = request.form['secondary_contact_name']
        email_id = request.form['email_id']
        contact_number = request.form['contact_number']
        pan_number = request.form['pan_number']
        gst_number = request.form['gst_number']
        address = request.form['address']
        offer = CustomerMaster(customer_name=customer_name,
            primary_contact_name=primary_contact_name,
            secondary_contact_name=secondary_contact_name,
            email_id=email_id,
            contact_number=contact_number,
            pan_number=pan_number,
            gst_number=gst_number,
            address=address)
        
        db.session.add(offer)
        db.session.commit()
        return redirect('/Customer-masters')


@blueprint.route('/Country-masters')
@login_required
def Country_masters():
    users = UserModel.query.all()
    return render_template('home/Country-masters.html', users=users, segment='Country-masters')


@blueprint.route('/State-masters')
@login_required
def State_masters():
    users = UserModel.query.all()
    return render_template('home/State-masters.html', users=users, segment='State-masters')

@blueprint.route('/City-masters')
@login_required
def City_masters():
    users = UserModel.query.all()
    return render_template('home/City-masters.html', users=users, segment='City-masters')

@blueprint.route('/Role-masters')
@login_required
def Role_masters():
    users = UserModel.query.all()
    return render_template('home/Role-masters.html', users=users, segment='Role-masters')

@blueprint.route('/User-masters')
@login_required
def user_masters():
    users = UserModel.query.all()
    return render_template('home/User-masters.html', users=users, segment='User-masters')

@blueprint.route('/BOM-Category-masters')
@login_required
def BOM_Category_masters():
    users = UserModel.query.all()
    return render_template('home/BOM-Category-masters.html', users=users, segment='BOM-Category-masters')


@blueprint.route('/BOM-masters')
@login_required
def BOM_masters():
    users = UserModel.query.all()
    return render_template('home/BOM-masters.html', users=users, segment='BOM-masters')

@blueprint.route('/Supplier-masters')
@login_required
def Supplier_masters():
    users = UserModel.query.all()
    return render_template('home/Supplier-masters.html', users=users, segment='Supplier-masters')

@blueprint.route('/Currency-masters')
@login_required
def Currency_masters():
    users = UserModel.query.all()
    return render_template('home/Currency-masters.html', users=users, segment='Currency-masters')


@blueprint.route('/Contract-Review-list')
@login_required
def Contract_Review_list():
    users = UserModel.query.all()
    return render_template('home/Contract-Review.html', users=users, segment='contractreview')

@blueprint.route('/OC-Register-list')
@login_required
def OC_Register_list():
    users = UserModel.query.all()
    return render_template('home/OC-Register-List.html', users=users, segment='OcRegister')

@blueprint.route('/BOM-Register-List')
@login_required
def BOM_Register_list():
    users = UserModel.query.all()
    return render_template('home/BOM-Register-List.html', users=users, segment='BOMRegister')

@blueprint.route('/Marketing-RegisterList')
@login_required
def Marketing_RegisterList():
    users = UserModel.query.all()
    return render_template('home/Marketing-Register-List.html', users=users, segment='MarketingRegisterList')


@blueprint.route('/Marketing-Register-Report')
@login_required
def Marketing_Register_Report():
    users = UserModel.query.all()
    return render_template('home/Marketing-Register-Report.html', users=users, segment='MarketingRegisterReport')


@blueprint.route('/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def profile(id):
    users = UserModel.query.filter_by(id=id).first()
    main_user = MainUser.query.filter_by(id=1).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.delete(main_user)
            db.session.commit()
            return redirect('/offer-offerlist')
    return render_template('home/delete.html')


@blueprint.route('/<int:id>/deletecustomer', methods=['GET', 'POST'])
@login_required
def delete1(id):
    users = CustomerMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/Customer-masters')
    return render_template('home/deletecustomer.html')


@blueprint.route('/<int:id>/deleteproduct', methods=['GET', 'POST'])
@login_required
def delete2(id):
    users = ProductMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/Product-masters')
    return render_template('home/deleteproduct.html')


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
