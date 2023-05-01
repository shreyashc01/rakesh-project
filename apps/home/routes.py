import imp
import json
from re import U
from apps.home import blueprint
from flask import render_template, request, redirect, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps import db
from apps.home.models import OfferModel
from apps.home.models import CountryMaster
from apps.home.models import RoleMaster
from apps.home.models import BomCategoryMaster
from apps.home.models import StateMaster
from apps.home.models import CityMaster
from apps.home.models import KitMaster
from apps.home.models import ProductMaster
from apps.home.models import CustomerMaster
from apps.home.models import BomMaster
from apps.home.models import SupplierMaster
from apps.home.models import UserModel
from apps.home.models import CurrencyMaster


@blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html', segment='dashboard')

@blueprint.route('/get_kit_details', methods=['POST'])
@login_required
def get_kit_details():
    if request.method == 'POST':
        kit_description = request.form.get('kit_description')
        kit = KitMaster.query.filter_by(kit_description=kit_description).first()
        kit_no = kit.kit_no
        kit_products = kit.kit_products.replace(",", ",\n") 
        return jsonify({'kit_no': kit_no, 'kit_product': kit_products})


@blueprint.route('/offer-addoffer', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        user1 = ProductMaster.query.all()
        user2 = KitMaster.query.all()

        user2_json = json.dumps([{'kit_description': user.kit_description, 'kit_no': user.kit_no} for user in user2])
        print(user2_json)
        role_manager_offer = UserModel.query.all()
        currency_master_offer = CurrencyMaster.query.all()
        return render_template('home/add-offer.html',users=users,user1=user1,user2=user2,user2_json=user2_json,role_manager_offer=role_manager_offer,currency_master_offer=currency_master_offer,
                               segment='offer-addoffer')
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
        # user = OfferModel(usr_id=usr_id,
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
        users = KitMaster.query.all()
        return render_template('home/add-kit.html',users=users)
    if request.method == 'POST':
        kit_description = request.form['kit_description']
        kit_no = request.form['kit_no']
        hsn_code = request.form['hsn_code']
        lubricant_points = request.form['lubricant_points']
        kit_products_temp = request.form.getlist('kit_products')
        kit_products = ','.join(kit_products_temp)
        kit_master_add = KitMaster(kit_description=kit_description,
            kit_no=kit_no,
            hsn_code=hsn_code,
            lubricant_points=lubricant_points,
            kit_products = kit_products
            )
        
        db.session.add(kit_master_add)
        db.session.commit()
        return redirect('/Kit-masters')

@blueprint.route('/add-user-login', methods=['GET', 'POST'])
@login_required
def add_user_login():
    if request.method == 'GET':
        role_master = RoleMaster.query.all()
        user_master_login = UserModel.query.all()
        return render_template('home/add-user-login.html',role_master=role_master,user_master_login=user_master_login)
    if request.method == 'POST':
        user_first_name = request.form['user_first_name']
        user_last_name = request.form['user_last_name']
        user_contact_no =request.form['user_contact_no']
        user_email_id =request.form['user_email_id']
        user_name_master = request.form['user_name_master']
        password_master =request.form['password_master']
        confirm_password =request.form['confirm_password']
        user_role_master =request.form['user_role_master']
        user_reporting_person =request.form['user_reporting_person']

        user_master_add = UserModel(user_first_name = user_first_name,
            user_last_name = user_last_name,
            user_contact_no =user_contact_no,
            user_email_id =user_email_id,
            user_name_master=user_name_master,
            password_master =password_master,
            confirm_password =confirm_password,
            user_role_master =user_role_master,
            user_reporting_person =user_reporting_person
        )
        db.session.add(user_master_add)
        db.session.commit()
        return redirect('/User-masters')
        
    
@blueprint.route('/add-bom-master', methods=['GET', 'POST'])
@login_required
def add_bom_master():
    if request.method == 'GET':
        Bom_category = BomCategoryMaster.query.all()
        Product_category = ProductMaster.query.all()
        return render_template('home/add-bom-master.html',Bom_category=Bom_category,Product_category=Product_category)
    if request.method == 'POST':
        bom_description = request.form['bom_description']
        bom_no = request.form['bom_no']
        bom_model_no = request.form['bom_model_no']
        bom_cls = request.form['bom_cls']
        bom_lube_points = request.form['bom_lube_points']
        bom_type = request.form['bom_type']
        bom_notes = request.form['bom_notes']

        bom_serial_no_temp = request.form.getlist('bom_serial_no')
        bom_serial_no = ','.join(bom_serial_no_temp)
        bom_category_temp = request.form.getlist('bom_category')
        bom_category = ','.join(bom_category_temp)
        bom_product_temp = request.form.getlist('bom_product')
        bom_product = ','.join(bom_product_temp)
        bom_quantity_temp = request.form.getlist('bom_quantity')
        bom_quantity = ','.join(bom_quantity_temp)
        bom_uom_temp = request.form.getlist('bom_uom')
        bom_uom = ','.join(bom_uom_temp)

        bom_master = BomMaster(
            bom_description = bom_description,
        bom_no = bom_no,
        bom_model_no = bom_model_no,
        bom_cls = bom_cls,
        bom_lube_points = bom_lube_points,
        bom_type = bom_type,
        bom_notes = bom_notes,
        bom_serial_no = bom_serial_no,
        bom_category = bom_category,
        bom_product = bom_product,
        bom_quantity = bom_quantity,
        bom_uom = bom_uom
            )
        
        db.session.add(bom_master)
        db.session.commit()
        return redirect('/BOM-masters')
    
@blueprint.route('/add-supplier-master', methods=['GET', 'POST'])
@login_required
def add_supplier_master():
    if request.method == 'GET':
        Citymaster_main = CityMaster.query.all()
        return render_template('home/add-supplier.html',Citymaster_main=Citymaster_main)
    if request.method == 'POST':
        supplier_name = request.form['supplier_name']
        supplier_primary_contact =  request.form['supplier_primary_contact']
        supplier_secondary_contact =  request.form['supplier_secondary_contact']
        supplier_email_id =  request.form['supplier_email_id']
        supplier_contact_no =  request.form['supplier_contact_no']
        supplier_country =  request.form['supplier_country']
        supplier_state =  request.form['supplier_state']
        supplier_city =  request.form['supplier_city']
        supplier_address =  request.form['supplier_address']
        supplier_gst_no =  request.form['supplier_gst_no']
        supplier_pan =  request.form['supplier_pan']

        supplier_main = SupplierMaster(
            supplier_name = supplier_name,
            supplier_primary_contact = supplier_primary_contact,
            supplier_secondary_contact = supplier_secondary_contact,
            supplier_email_id = supplier_email_id,
            supplier_contact_no = supplier_contact_no,
            supplier_country = supplier_country,
            supplier_state = supplier_state,
            supplier_city = supplier_city,
            supplier_address = supplier_address,
            supplier_gst_no = supplier_gst_no,
            supplier_pan = supplier_pan
            )
        db.session.add(supplier_main)
        db.session.commit()
        return redirect('/Supplier-masters')
    
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
        users = SupplierMaster.query.all()
        user1 = CurrencyMaster.query.all()
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
        # all_users = OfferModel.query.filter_by(usr_id=request.form.get('main_usr_select')).first()
        # main_user = MainUser.query.filter_by(id=1).first()
        # if all_users != None:
        #     main_user.main_usr_id = all_users.usr_id
        #     main_user.main_usr_name = all_users.usr_name
        #     db.session.commit()
    users = OfferModel.query.all()
    return render_template('home/users.html', users=users, segment='offer-offerlist')



@blueprint.route('/<int:id>/editcustomer', methods=['GET', 'POST'])
@login_required
def update(id):
    user = CustomerMaster.query.filter_by(id=id).first()
    city_master = CityMaster.query.all()
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

    return render_template('home/updatecustomer.html', user=user,city_master=city_master, segment='Customer-masters')


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
        user.product_hsn_no = request.form['product_hsn_no']
        db.session.commit()
        return redirect('/Product-masters')

    return render_template('home/updateproduct.html', user=user, segment='Product-masters')


@blueprint.route('/<int:id>/editkit', methods=['GET', 'POST'])
@login_required
def update3(id):
    user = KitMaster.query.filter_by(id=id).first()
    values_list = user.kit_products.split(',')
    if request.method == 'POST':
        user.kit_description = request.form['kit_description']
        user.kit_no = request.form['kit_no']
        user.hsn_code = request.form['hsn_code']
        user.lubricant_points = request.form['lubricant_points']
        kit_products_temp = request.form.getlist('kit_products')
        user.kit_products = ','.join(kit_products_temp)
        db.session.commit()
        return redirect('/Kit-masters')

    return render_template('home/edit-kit.html', user=user,values_list=values_list, segment='Kit-masters')

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
        product_hsn_no = request.form['product_hsn_no']
        description = request.form['description']
        offer = ProductMaster(product_name=product_name,
            part_no=part_no,
            rack_no=rack_no,
            bin_no=bin_no,
            minimum_qty=minimum_qty,
            maximum_order=maximum_order,
            product_hsn_no=product_hsn_no,
            description=description)
        
        db.session.add(offer)
        db.session.commit()
        return redirect('/Product-masters')

@blueprint.route('/Kit-masters')
@login_required
def kit_masters():
    if request.method == 'GET':
        users = KitMaster.query.all()
        return render_template('home/Kit-masters.html', users=users, segment='Kit-masters')


@blueprint.route('/Customer-masters', methods=['GET', 'POST'])
@login_required
def Customer_masters():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        city_master = CityMaster.query.all()
        return render_template('home/Customer-masters.html',users=users,city_master=city_master, segment='Customer-masters')
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        primary_contact_name = request.form['primary_contact_name']
        secondary_contact_name = request.form['secondary_contact_name']
        email_id = request.form['email_id']
        contact_number = request.form['contact_number']
        pan_number = request.form['pan_number']
        gst_number = request.form['gst_number']
        address = request.form['address']
        customer_country_name = request.form['customer_country_name']
        customer_state_name = request.form['customer_state_name']
        customer_city_name = request.form['customer_city_name']
        offer = CustomerMaster(customer_name=customer_name,
            primary_contact_name=primary_contact_name,
            secondary_contact_name=secondary_contact_name,
            email_id=email_id,
            contact_number=contact_number,
            pan_number=pan_number,
            gst_number=gst_number,
            address=address,
            customer_country_name=customer_country_name,
            customer_state_name=customer_state_name,
            customer_city_name=customer_city_name
            )
        
        db.session.add(offer)
        db.session.commit()
        return redirect('/Customer-masters')


@blueprint.route('/Country-masters', methods=['GET', 'POST'])
@login_required
def Country_masters():
    if request.method == 'GET':
        users = CountryMaster.query.all()
        return render_template('home/Country-masters.html', users=users, segment='Country-masters')
    if request.method == 'POST':
        country_name_temp = request.form['country_name_temp']
        offer = CountryMaster(country_name_temp=country_name_temp)
        db.session.add(offer)
        db.session.commit()
        return redirect('/Country-masters')

@blueprint.route('/State-masters', methods=['GET', 'POST'])
@login_required
def State_masters():
    if request.method == 'GET':
        users = StateMaster.query.all()
        return render_template('home/State-masters.html', users=users, segment='State-masters')
    if request.method == 'POST':
        state_name_temp = request.form['state_name_temp']
        offer = StateMaster(state_name_temp=state_name_temp)
        db.session.add(offer)
        db.session.commit()
        return redirect('/State-masters')

@blueprint.route('/City-masters', methods=['GET', 'POST'])
@login_required
def City_masters():
    if request.method == 'GET':
        users = CityMaster.query.all()
        states = StateMaster.query.all()
        countries = CountryMaster.query.all()
        print(users,states,countries)
        return render_template('home/City-masters.html', len_country= len(countries), users=users, len_state=len(states), states=states, countries=countries,segment='City-masters')
    if request.method == 'POST':
        country_name = request.form['country_name']
        state_name = request.form['state_name']
        city_name = request.form['city_name']
        offer = CityMaster(country_name=country_name,state_name=state_name,city_name=city_name )
        db.session.add(offer)
        db.session.commit()
        return redirect('/City-masters')

@blueprint.route('/Role-masters', methods=['GET', 'POST'])
@login_required
def Role_masters():
    if request.method == 'GET':
        users = RoleMaster.query.all()
        return render_template('home/Role-masters.html', users=users, segment='Role-masters')
    if request.method == 'POST':
        role_name = request.form['role_name']
        offer = RoleMaster(role_name=role_name)
        db.session.add(offer)
        db.session.commit()
        return redirect('/Role-masters')
    
@blueprint.route('/User-masters', methods=['GET', 'POST'])
@login_required
def user_masters():
    if request.method == 'GET':
        users = UserModel.query.all()
        return render_template('home/User-masters.html', users=users, segment='User-masters')

@blueprint.route('/BOM-Category-masters', methods=['GET', 'POST'])
@login_required
def BOM_Category_masters():
    if request.method == 'GET':
        users = BomCategoryMaster.query.all()
        return render_template('home/BOM-Category-masters.html', users=users, segment='BOM-Category-masters')
    if request.method == 'POST':
        bom_category_name = request.form['bom_category_name']
        offer = BomCategoryMaster(bom_category_name=bom_category_name)
        db.session.add(offer)
        db.session.commit()
        return redirect('/BOM-Category-masters')

@blueprint.route('/BOM-masters', methods=['GET', 'POST'])
@login_required
def BOM_masters():
    if request.method == 'GET':
        BomMaster_main = BomMaster.query.all()
        return render_template('home/BOM-masters.html', BomMaster_main=BomMaster_main, segment='BOM-masters')

@blueprint.route('/Supplier-masters', methods=['GET', 'POST'])
@login_required
def Supplier_masters():
    if request.method == 'GET':
        users = SupplierMaster.query.all()
        return render_template('home/Supplier-masters.html', users=users, segment='Supplier-masters')

@blueprint.route('/Currency-masters', methods=['GET', 'POST'])
@login_required
def Currency_masters():
    if request.method == 'GET':
        users = CurrencyMaster.query.all()
        return render_template('home/Currency-masters.html', users=users, segment='Currency-masters')
    if request.method == 'POST':
        currency_name = request.form['currency_name']
        currency_model_add = CurrencyMaster(currency_name=currency_name)
        db.session.add(currency_model_add)
        db.session.commit()
        return redirect('/Currency-masters')

@blueprint.route('/Contract-Review-list', methods=['GET', 'POST'])
@login_required
def Contract_Review_list():
    if request.method == 'GET':
        users = OfferModel.query.all()
        return render_template('home/editcontract.html', users=users, segment='contractreview')

@blueprint.route('/OC-Register-list', methods=['GET', 'POST'])
@login_required
def OC_Register_list():
    if request.method == 'GET':
        users = OfferModel.query.all()
        return render_template('home/OC-Register-List.html', users=users, segment='OcRegister')

@blueprint.route('/BOM-Register-List', methods=['GET', 'POST'])
@login_required
def BOM_Register_list():
    if request.method == 'GET':
        users = OfferModel.query.all()
        return render_template('home/BOM-Register-List.html', users=users, segment='BOMRegister')

@blueprint.route('/Marketing-RegisterList', methods=['GET', 'POST'])
@login_required
def Marketing_RegisterList():
    if request.method == 'GET':
        users = OfferModel.query.all()
        return render_template('home/Marketing-Register-List.html', users=users, segment='MarketingRegisterList')


@blueprint.route('/Marketing-Register-Report', methods=['GET', 'POST'])
@login_required
def Marketing_Register_Report():
    if request.method == 'GET':
        users = OfferModel.query.all()
        return render_template('home/Marketing-Register-Report.html', users=users, segment='MarketingRegisterReport')


@blueprint.route('/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def profile(id):
    users = OfferModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
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

@blueprint.route('/<int:id>/deletekit', methods=['GET', 'POST'])
@login_required
def delete3(id):
    users = KitMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/Kit-masters')
    return render_template('home/delete-kit.html')

@blueprint.route('/<int:id>/deletecity', methods=['GET', 'POST'])
@login_required
def delete4(id):
    users = CityMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/City-masters')
    return render_template('home/delete-city.html')


@blueprint.route('/<int:id>/deletestate', methods=['GET', 'POST'])
@login_required
def delete5(id):
    users = StateMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/State-masters')
    return render_template('home/delete-state.html')

@blueprint.route('/<int:id>/deletecountry', methods=['GET', 'POST'])
@login_required
def delete6(id):
    users = CountryMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/Country-masters')
    return render_template('home/delete-country.html')

@blueprint.route('/<int:id>/deleterole', methods=['GET', 'POST'])
@login_required
def delete7(id):
    users = RoleMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/Role-masters')
    return render_template('home/delete-role.html')

@blueprint.route('/<int:id>/deletebomcategory', methods=['GET', 'POST'])
@login_required
def delete8(id):
    users = BomCategoryMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/BOM-Category-masters')
    return render_template('home/delete-category.html')

@blueprint.route('/<int:id>/deletecurrency', methods=['GET', 'POST'])
@login_required
def delete9(id):
    users = CurrencyMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/Currency-masters')
    return render_template('home/deletecurrency.html')

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
