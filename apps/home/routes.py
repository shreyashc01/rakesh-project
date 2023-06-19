import imp
import json
from re import U
from apps.home import blueprint
from flask import render_template, request, redirect, jsonify, flash
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps import db
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
from apps.home.models import AddOffer
from apps.home.models import OCModel
from apps.authentication.models import Users
import datetime

@blueprint.route('/dashboard')
@login_required
def dashboard():
    # db.metadata.tables['OfferComfirmation'].drop(db.engine)
    return render_template('home/dashboard.html', segment='dashboard')

@blueprint.route('/get_kit_details', methods=['POST'])
@login_required
def get_kit_details():
    if request.method == 'POST':
        kit_description = request.form.get('kit_description')
        kit = KitMaster.query.filter_by(kit_description=kit_description).first()
        kit_no = kit.kit_no
        data = json.loads(kit.kit_products)
        kit_names = [item['kit_name_master'] for item in data]
        return jsonify({'kit_no': kit_no, 'kit_product': kit_names})


@blueprint.route('/offer-addoffer', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        user1 = ProductMaster.query.all()
        user2 = KitMaster.query.all()
        addOffer = AddOffer.query.all()
        Quatationnumber = len(addOffer) 
        Quatationnumber += 1
        user2_json = json.dumps([{'kit_description': user.kit_description, 'kit_no': user.kit_no} for user in user2])
        role_manager_offer = UserModel.query.all()
        currency_master_offer = CurrencyMaster.query.all()
        return render_template('home/add-offer.html',users=users,user1=user1,user2=user2,user2_json=user2_json,role_manager_offer=role_manager_offer,
                               offer_json=None,currency_master_offer=currency_master_offer,Quatationnumber=Quatationnumber, addOffer_database=None,segment='offer-addoffer')
    if request.method == 'POST':
        customer_name_offer = request.form['customer_name_offer']

        address_temp = CustomerMaster.query.filter_by(customer_name=customer_name_offer).first()
        billing_address_temp = address_temp.address if address_temp.address else None

        due_date_offer = request.form['due_date_offer']
        offer_type_offer = request.form['offer_type_offer']
        quotation_number_offer = request.form['quotation_number_offer']
        marketing_person_offer = request.form['marketing_Person_offer']
        currency_type_offer = request.form['currency_type_offer']
        product_kit_offer_json = ''
        product_kit_offer = []
        if offer_type_offer == "Spares":
            product_offers = request.form.getlist('product_offer')
            quantity_list = request.form.getlist('quantity_product_offer')
            unit_price_list = request.form.getlist('unit_price_product_offer')
            uom_type_list = request.form.getlist('uom_type')
            total_price_product_offer = request.form.getlist('total')
            # json.loads(request.form.get('total_price_product_offer'))

            product_kit_offer = []
            for i in range(len(product_offers)):
                product_name = product_offers[i]
                product = ProductMaster.query.filter_by(product_name=product_name).first() 
                part_number = product.part_no if product else None
                product_offer = {
                    'product_name': product_name,
                    'part_number' : part_number,
                    'quantity': quantity_list[i],
                    'unit_price': unit_price_list[i],
                    'uom' : uom_type_list[i],
                    'total_price': total_price_product_offer[i],
                }
                product_kit_offer.append(product_offer)

            # Convert the list to JSON
            product_kit_offer_json = json.dumps(product_kit_offer)
        if offer_type_offer == "Kits":
            kit_description_offer = request.form.getlist('kit_description_offer')
            kit_number_offer = request.form.getlist('kit_number_offer')
            quantity_kit_offer = request.form.getlist('quantity_kit_offer')
            unit_price_kit_offer = request.form.getlist('unit_price_kit_offer')
            uom_type_list = request.form.getlist('uom_type')
            total_price_kit_offer = request.form.getlist('total')

            product_kit_offer = []
            for i in range(len(kit_description_offer)):
                kit_offer = {
                    'kit_name': kit_description_offer[i],
                    'part_number': kit_number_offer[i],
                    'quantity': quantity_kit_offer[i],
                    'unit_price': unit_price_kit_offer[i],
                    'uom' : uom_type_list[i],
                    'total_price': total_price_kit_offer[i],
                }
                product_kit_offer.append(kit_offer)

            # Convert the list to JSON
            product_kit_offer_json = json.dumps(product_kit_offer)

        # total_amount_offer = request.form['total_amount_offer']
        # freight_offer = request.form['freight_offer']
        # cgst_igst_type_offer = request.form['cgst_igst_type_offer']
        # pf_percentage_offer = request.form['pf_percentage_offer']
        # gst_offer = request.form['gst_offer']
        # grand_total_offer = request.form['grand_total_offer']
        grossAmount = request.form['grossAmount']
        discountType = request.form['discountType']
        discountValue = request.form['discountValue']
        assessableValue = request.form['assessableValue']
        pfPercentage = request.form['pfPercentage']
        pfValue = request.form['pfValue']
        freightValue = request.form['freightValue']
        totalFreight = request.form['totalFreight']
        tcsPercentage = request.form['tcsPercentage']
        gstType = request.form['gstType']
        tcsValue = request.form['tcsValue']
        gstPercentage = request.form['gstPercentage']
        gstValue = request.form['gstValue']
        roundOffType = request.form['roundOffType']
        roundOffValue = request.form['roundOffValue']
        grandTotal = request.form['grandTotal']

        subject_offer = request.form['subject_offer']
        reference_offer = request.form['reference_offer']
        description_offer = request.form['description_offer']
        footer_description_offer = request.form['footer_description_offer']
        notes_offer = request.form['notes_offer']

        price_basis_offer = request.form['price_basis_offer']
        PandFcharges_offer = request.form['PandFcharges_offer']
        igst_terms_offer = request.form['igst_terms_offer']
        hsn_code_offer = request.form['hsn_code_offer']
        payment_terms_offer = request.form['payment_terms_offer']
        delivery_terms_offer = request.form['delivery_terms_offer']
        freight_terms_offer = request.form['freight_terms_offer']
        validity_terms_offer = request.form['validity_terms_offer']
        warrenty_terms_offer = request.form['warrenty_terms_offer']
        
        new_offer = AddOffer(
            customer_name_offer=customer_name_offer,
            due_date_offer=due_date_offer,
            offer_type_offer=offer_type_offer,
            quotation_number_offer=quotation_number_offer,
            marketing_person_offer=marketing_person_offer,
            currency_type_offer=currency_type_offer,
            product_kit_offer_json=product_kit_offer_json,
            grossAmount = grossAmount,
            discountType = discountType,
            discountValue = discountValue,
            assessableValue = assessableValue,
            pfPercentage = pfPercentage,
            pfValue = pfValue,
            freightValue = freightValue,
            totalFreight = totalFreight,
            tcsPercentage = tcsPercentage,
            gstType = gstType,
            tcsValue = tcsValue,
            gstPercentage = gstPercentage,
            gstValue = gstValue,
            roundOffType = roundOffType,
            roundOffValue = roundOffValue,
            grandTotal = grandTotal,
            subject_offer=subject_offer,
            reference_offer=reference_offer,
            description_offer=description_offer,
            footer_description_offer=footer_description_offer,
            notes_offer=notes_offer,
            price_basis_offer=price_basis_offer,
            PandFcharges_offer=PandFcharges_offer,
            igst_terms_offer=igst_terms_offer,
            hsn_code_offer=hsn_code_offer,
            payment_terms_offer=payment_terms_offer,
            delivery_terms_offer=delivery_terms_offer,
            freight_terms_offer=freight_terms_offer,
            validity_terms_offer=validity_terms_offer,
            warrenty_terms_offer=warrenty_terms_offer,

            contract_review_Order_No='', 
            contract_review_Order_Date='',
            contract_review_PO_Qty=0,
            contract_review_Billing_Address=billing_address_temp,
            contract_review_Delivery_Address_1=billing_address_temp,
            contract_review_Delivery_Address_2='',
            contract_review_Delivery_Address_3='',
            contract_review_Delivery_Address_4='',
            contract_review_Delivery_Address_5='',
            contract_review_Offer_No='',
            contract_review_Total_Cost=grandTotal,

            contract_review_price=grossAmount,
            contract_review_price_1='',
            contract_review_price_2='',

            contract_review_packing_and_Forwarding=PandFcharges_offer,
            contract_review_packing_and_Forwarding_1='',
            contract_review_packing_and_Forwarding_2='',

            contract_review_gst=igst_terms_offer,
            contract_review_gst_1='',
            contract_review_gst_2='',


            contract_review_delivery=delivery_terms_offer,
            contract_review_delivery_1='',
            contract_review_delivery_2='',


            contract_review_warrantly=warrenty_terms_offer,
            contract_review_warrantly_1='',
            contract_review_warrantly_2='',


            contract_review_terms_of_pay=payment_terms_offer,
            contract_review_terms_of_pay_1='',
            contract_review_terms_of_pay_2='',


            contract_review_freight=freight_terms_offer,
            contract_review_freight_1='',
            contract_review_freight_2='',


            contract_review_preferred_transporter='',
            contract_review_preferred_transporter_1='',
            contract_review_preferred_transporter_2='',


            contract_review_contact_person='',
            contract_review_telephone_number='',
            contract_review_email_id='',
            contract_review_notes='',
            contract_review_approve=0,

            offer_conformation_number = ''
        )

        db.session.add(new_offer)
        db.session.commit()
        return redirect('/offer-offerlist')

@blueprint.route('/<int:id>/edit-addoffer', methods=['GET', 'POST'])
@login_required
def update_add_offer(id):
    addOffer_database = AddOffer.query.filter_by(id=id).first()
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        user1 = ProductMaster.query.all()
        user2 = KitMaster.query.all()
        # addOffer_database = AddOffer.query.filter_by(id=id).first()
        offer_json = json.loads(addOffer_database.product_kit_offer_json)
        # print(offer_json['kit_name'])
        user2_json = json.dumps([{'kit_description': user.kit_description, 'kit_no': user.kit_no} for user in user2])
        role_manager_offer = UserModel.query.all()
        currency_master_offer = CurrencyMaster.query.all()
    if request.method == 'POST':
        addOffer_database.customer_name_offer = request.form['customer_name_offer']

        address_temp = CustomerMaster.query.filter_by(customer_name=addOffer_database.customer_name_offer).first()
        billing_address_temp = address_temp.address if address_temp.address else None

        addOffer_database.due_date_offer = request.form['due_date_offer']
        addOffer_database.offer_type_offer = request.form['offer_type_offer']
        addOffer_database.quotation_number_offer = request.form['quotation_number_offer']
        addOffer_database.marketing_person_offer = request.form['marketing_Person_offer']
        addOffer_database.currency_type_offer = request.form['currency_type_offer']
        product_kit_offer_json = ''
        product_kit_offer = []
        if addOffer_database.offer_type_offer == "Spares":
            print(addOffer_database.offer_type_offer)
            product_offers = request.form.getlist('product_offer')
            quantity_list = request.form.getlist('quantity_product_offer')
            unit_price_list = request.form.getlist('unit_price_product_offer')
            uom_type_list = request.form.getlist('uom_type')
            total_price_product_offer = request.form.getlist('total')
            print(product_offers,quantity_list,unit_price_list,uom_type_list,total_price_product_offer)
            product_kit_offer = []
            for i in range(len(product_offers)):
                product_name = product_offers[i]
                product = ProductMaster.query.filter_by(product_name=product_name).first() 
                part_number = product.part_no if product else None
                product_offer = {
                    'product_name': product_name,
                    'part_number' : part_number,
                    'quantity': quantity_list[i],
                    'unit_price': unit_price_list[i],
                    'uom' : uom_type_list[i],
                    'total_price': total_price_product_offer[i],
                }
                product_kit_offer.append(product_offer)

            # Convert the list to JSON
            product_kit_offer_json = json.dumps(product_kit_offer)
        if addOffer_database.offer_type_offer == "Kits":
            kit_description_offer = request.form.getlist('kit_description_offer')
            kit_number_offer = request.form.getlist('kit_number_offer')
            quantity_kit_offer = request.form.getlist('quantity_kit_offer')
            unit_price_kit_offer = request.form.getlist('unit_price_kit_offer')
            uom_type_list = request.form.getlist('uom_type')
            total_price_kit_offer = request.form.getlist('total')

            product_kit_offer = []
            for i in range(len(kit_description_offer)):
                kit_offer = {
                    'kit_name': kit_description_offer[i],
                    'part_number': kit_number_offer[i],
                    'quantity': quantity_kit_offer[i],
                    'unit_price': unit_price_kit_offer[i],
                    'uom' : uom_type_list[i],
                    'total_price': total_price_kit_offer[i],
                }
                product_kit_offer.append(kit_offer)

            product_kit_offer_json = json.dumps(product_kit_offer)
        print(product_kit_offer_json)
        addOffer_database.product_kit_offer_json = product_kit_offer_json
        addOffer_database.grossAmount = request.form['grossAmount']
        addOffer_database.discountType = request.form['discountType']
        addOffer_database.discountValue = request.form['discountValue']
        addOffer_database.assessableValue = request.form['assessableValue']
        addOffer_database.pfPercentage = request.form['pfPercentage']
        addOffer_database.pfValue = request.form['pfValue']
        addOffer_database.freightValue = request.form['freightValue']
        addOffer_database.totalFreight = request.form['totalFreight']
        addOffer_database.tcsPercentage = request.form['tcsPercentage']
        addOffer_database.gstType = request.form['gstType']
        addOffer_database.tcsValue = request.form['tcsValue']
        addOffer_database.gstPercentage = request.form['gstPercentage']
        addOffer_database.gstValue = request.form['gstValue']
        addOffer_database.roundOffType = request.form['roundOffType']
        addOffer_database.roundOffValue = request.form['roundOffValue']
        addOffer_database.grandTotal = request.form['grandTotal']

        addOffer_database.subject_offer = request.form['subject_offer']
        addOffer_database.reference_offer = request.form['reference_offer']
        addOffer_database.description_offer = request.form['description_offer']
        addOffer_database.footer_description_offer = request.form['footer_description_offer']
        addOffer_database.notes_offer = request.form['notes_offer']

        addOffer_database.price_basis_offer = request.form['price_basis_offer']
        addOffer_database.PandFcharges_offer = request.form['PandFcharges_offer']
        addOffer_database.igst_terms_offer = request.form['igst_terms_offer']
        addOffer_database.hsn_code_offer = request.form['hsn_code_offer']
        addOffer_database.payment_terms_offer = request.form['payment_terms_offer']
        addOffer_database.delivery_terms_offer = request.form['delivery_terms_offer']
        addOffer_database.freight_terms_offer = request.form['freight_terms_offer']
        addOffer_database.validity_terms_offer = request.form['validity_terms_offer']
        addOffer_database.warrenty_terms_offer = request.form['warrenty_terms_offer']
        db.session.commit()
        return redirect('/offer-offerlist')
    return render_template('home/add-offer.html',users=users,user1=user1,user2=user2,user2_json=user2_json,role_manager_offer=role_manager_offer,
                               Quatationnumber=0,offer_json=offer_json,currency_master_offer=currency_master_offer, addOffer_database=addOffer_database,segment='offer-offerlist')

@blueprint.route('/add-kits', methods=['GET', 'POST'])
@login_required
def kit_add():
    if request.method == 'GET':
        users = KitMaster.query.all()
        return render_template('home/add-kit.html',users=users, segment="Kit-masters")
    if request.method == 'POST':
        kit_description = request.form['kit_description']
        kit_no = request.form['kit_no']
        hsn_code = request.form['hsn_code']
        lubricant_points = request.form['lubricant_points']
        kit_products_temp = request.form.getlist('kit_products')

        add_kit_master = []
        for i in range(len(kit_products_temp)):
            Kit_offer = {
                'kit_name_master': kit_products_temp[i]
            }
            add_kit_master.append(Kit_offer)
        
        kit_products = json.dumps(add_kit_master)
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
        data = Users.query.all()
        return render_template('home/add-user-login.html',role_master=role_master,user_master_login=user_master_login, users=None, segment='User-masters')
    if request.method == 'POST':
        user_first_name = request.form['user_first_name'].strip()
        user_last_name = request.form['user_last_name']
        user_contact_no =request.form['user_contact_no']
        user_email_id =request.form['user_email_id']
        user_name_master = request.form['user_name_master']
        password_master =request.form['password_master']
        confirm_password =request.form['confirm_password']
        user_role_master =request.form['user_role_master']
        user_reporting_person =request.form['user_reporting_person']

        password_data = Users(
            username = user_name_master,
            email = user_email_id,
            password = password_master
        )
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

        db.session.add(password_data)
        db.session.add(user_master_add)
        db.session.commit()
        return redirect('/User-masters')
        
@blueprint.route('/<int:id>/edit-user-login', methods=['GET', 'POST'])
@login_required
def updateuserlogin(id):
    users = UserModel.query.filter_by(id=id).first()
    role_master = RoleMaster.query.all()
    user_master_login = UserModel.query.all()
    if request.method == 'POST':
        users.user_first_name = request.form['user_first_name'].strip()
        users.user_last_name = request.form['user_last_name']
        users.user_contact_no = request.form['user_contact_no']
        users.user_email_id = request.form['user_email_id']
        users.user_name_master = request.form['user_name_master']
        users.password_master = request.form['password_master']
        users.confirm_password = request.form['confirm_password']
        users.user_role_master = request.form['user_role_master']
        users.user_reporting_person = request.form['user_reporting_person']

        db.session.commit()
        return redirect('/User-masters')

    return render_template('home/add-user-login.html',role_master=role_master,user_master_login=user_master_login, users=users, segment='User-masters')

@blueprint.route('/add-bom-master', methods=['GET', 'POST'])
@login_required
def add_bom_master():
    if request.method == 'GET':
        Bom_category = BomCategoryMaster.query.all()
        Product_category = ProductMaster.query.all()
        return render_template('home/add-bom-master.html',bom_temp_data=None,bom_database=None,Bom_category=Bom_category,Product_category=Product_category, segment='BOM-masters')
    if request.method == 'POST':
        bom_description = request.form['bom_description'].strip()
        bom_no = request.form['bom_no']
        bom_model_no = request.form['bom_model_no']
        bom_cls = request.form['bom_cls']
        bom_lube_points = request.form['bom_lube_points']
        bom_type = request.form['bom_type']
        bom_notes = request.form['bom_notes']
        
        bom_serial_no_temp = request.form.getlist('bom_serial_no')
        bom_category_temp = request.form.getlist('bom_category')
        bom_product_temp = request.form.getlist('bom_product')
        bom_quantity_temp = request.form.getlist('bom_quantity')
        bom_uom_temp = request.form.getlist('bom_uom')

        bom_data = {
            'bom_serial_no': bom_serial_no_temp,
            'bom_category': bom_category_temp,
            'bom_product': bom_product_temp,
            'bom_quantity': bom_quantity_temp,
            'bom_uom': bom_uom_temp
        }
        bom_data = json.dumps(bom_data)
        bom_master = BomMaster(
                bom_description = bom_description,
                bom_no = bom_no,
                bom_model_no = bom_model_no,
                bom_cls = bom_cls,
                bom_lube_points = bom_lube_points,
                bom_type = bom_type,
                bom_notes = bom_notes,
                bom_data=bom_data
            )
        
        db.session.add(bom_master)
        db.session.commit()
        return redirect('/BOM-masters')

@blueprint.route('/<int:id>/edit-bom-master', methods=['GET', 'POST'])
@login_required
def updatebom_master(id):
    bom_database = BomMaster.query.filter_by(id=id).first()
    bom_temp_data = json.loads(bom_database.bom_data)
    Bom_category = BomCategoryMaster.query.all()
    Product_category = ProductMaster.query.all()

    if request.method == 'POST':
        bom_database.bom_description = request.form['bom_description'].strip()
        bom_database.bom_no = request.form['bom_no']
        bom_database.bom_model_no = request.form['bom_model_no']
        bom_database.bom_cls = request.form['bom_cls']
        bom_database.bom_lube_points = request.form['bom_lube_points']
        bom_database.bom_type = request.form['bom_type']
        bom_database.bom_notes = request.form['bom_notes']

        bom_serial_no_temp = request.form.getlist('bom_serial_no')
        bom_category_temp = request.form.getlist('bom_category')
        bom_product_temp = request.form.getlist('bom_product')
        bom_quantity_temp = request.form.getlist('bom_quantity')
        bom_uom_temp = request.form.getlist('bom_uom')

        bom_data_temp = {
            'bom_serial_no': bom_serial_no_temp,
            'bom_category': bom_category_temp,
            'bom_product': bom_product_temp,
            'bom_quantity': bom_quantity_temp,
            'bom_uom': bom_uom_temp
        }
        bom_database.bom_data = json.dumps(bom_data_temp)
        
        db.session.commit()
        return redirect('/BOM-masters')

    return render_template('home/add-bom-master.html',Bom_category=Bom_category,Product_category=Product_category,bom_temp_data=bom_temp_data, bom_database=bom_database, segment='User-masters')

@blueprint.route('/add-supplier-master', methods=['GET', 'POST'])
@login_required
def add_supplier_master():
    if request.method == 'GET':
        Citymaster_main = CityMaster.query.all()
        State_masters = StateMaster.query.all()
        Country_master = CountryMaster.query.all()
        return render_template('home/add-supplier.html',State_masters=State_masters,Country_master=Country_master,users=None,Citymaster_main=Citymaster_main, segment='Supplier-masters')
    if request.method == 'POST':
        supplier_name = request.form['supplier_name'].strip()
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


@blueprint.route('/<int:id>/edit-supplier-master', methods=['GET', 'POST'])
@login_required
def updatesupplier(id):
    users = SupplierMaster.query.filter_by(id=id).first()
    Citymaster_main = CityMaster.query.all()
    State_masters = StateMaster.query.all()
    Country_master = CountryMaster.query.all()
    if request.method == 'POST':
        users.supplier_name = request.form['supplier_name'].strip()
        users.supplier_primary_contact = request.form['supplier_primary_contact']
        users.supplier_secondary_contact = request.form['supplier_secondary_contact']
        users.supplier_email_id = request.form['supplier_email_id']
        users.supplier_contact_no = request.form['supplier_contact_no']
        users.supplier_country = request.form['supplier_country']
        users.supplier_state = request.form['supplier_state']
        users.supplier_city = request.form['supplier_city']
        users.supplier_address = request.form['supplier_address']
        users.supplier_gst_no = request.form['supplier_gst_no']
        users.supplier_pan = request.form['supplier_pan']


        db.session.commit()
        return redirect('/Supplier-masters')

    return render_template('home/add-supplier.html',State_masters=State_masters,Country_master=Country_master,Citymaster_main=Citymaster_main,users=users, segment='Supplier-masters')


@blueprint.route('/invoice-addinvoice', methods=['GET', 'POST'])
@login_required
def addinvoice():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        user1 = ProductMaster.query.all()
        oc_list = OCModel.query.all()
        currency_user_invoice = CurrencyMaster.query.all()
        return render_template('home/add-invoice.html',oc_list=oc_list,users=users,user1=user1,currency_user_invoice=currency_user_invoice,segment='add-invoice')

@blueprint.route('/invoice-invoiceslist', methods=['GET', 'POST'])
@login_required
def listinvoices():
    return render_template('home/invoices.html', segment='list-invoice')



@blueprint.route('/PO-addpo', methods=['GET', 'POST'])
@login_required
def addpo():
    if request.method == 'GET':
        users = SupplierMaster.query.all()
        users_product = ProductMaster.query.all()
        user1 = CurrencyMaster.query.all()
        bom_PO = BomMaster.query.all()
        return render_template('home/add-purchaseorder.html',bom_PO=bom_PO,users=users,user1=user1,users_product=users_product,segment='add-purchaseorder')

@blueprint.route('/PO-POlist', methods=['GET', 'POST'])
@login_required
def listpo():
    return render_template('home/purchaseorder.html', segment='list-purchaseorder')

@blueprint.route('/BOM-List', methods=['GET', 'POST'])
@login_required
def BOM_List():
    return render_template('home/BOM-Lists.html', segment='BOM-List-purchaseorder')

@blueprint.route('/Purchase-Order-Request', methods=['GET', 'POST'])
@login_required
def Add_PO_REQ():
    return render_template('home/ADD-PO-Request.html', segment='purchaseorder-Request')

@blueprint.route('/Purchase-Order-Request-List', methods=['GET', 'POST'])
@login_required
def PO_REQ_LIST():
    return render_template('home/PO-Request-List.html', segment='Request-List-purchaseorder')

@blueprint.route('/offer-offerlist', methods=['GET', 'POST'])
@login_required
def retrieve_list():
    add_user = AddOffer.query.all()

    return render_template('home/users.html',add_user=add_user, segment='offer-offerlist')

@blueprint.route('/<int:id>/offer_pdf', methods=['GET', 'POST'])
@login_required
def offer_pdf(id):
    if request.method == 'GET':
        add_user = AddOffer.query.filter_by(id=id).first()
        role_phone_temp = UserModel.query.filter_by(user_first_name=add_user.marketing_person_offer).first()
  
        try:
            addoffer_Role = role_phone_temp.user_role_master
            addoffer_Phonenumber = role_phone_temp.user_contact_no
        except AttributeError:
            flash("The user's role is not available. User may have been deleted.", "warning")
            print("AttributeError")
            addoffer_Role = None
            addoffer_Phonenumber = None

        address_temp = CustomerMaster.query.filter_by(customer_name=add_user.customer_name_offer).first()
        addoffer_address = address_temp.address if address_temp.address else None
        
        data = json.loads(add_user.product_kit_offer_json)
        html_rows = ""
        counter = 0

        if add_user.offer_type_offer == "Spares":
            for item in data:
                product_name = item['product_name']
                part_number = item['part_number']
                quantity = item['quantity']
                unit_price = item['unit_price']
                total_price = item['total_price']
                counter += 1
                if counter % 2 == 0:
                    background_color = 'white'
                else:
                    background_color = 'lightblue'

                html_row = f"<tr style='background-color: {background_color};'><td style='border: 1px solid #ccc; text-align: center;'><span>{counter}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{product_name}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{part_number}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{quantity}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{unit_price}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{total_price}</span></td></tr>"

                html_rows += html_row
            return render_template('home/pdf_add_offer.html',add_user=add_user,html_rows=html_rows,addoffer_address=addoffer_address,addoffer_Role=addoffer_Role,
                                    addoffer_Phonenumber=addoffer_Phonenumber,segment='offer-offerlist')
        else:
            for item in data:
                kit_name = item['kit_name']
                kit_number = item['part_number']
                quantity = item['quantity']
                unit_price = item['unit_price']
                total_price = item['total_price']
                counter += 1

                kit_name_lines = kit_name.replace('\r\n', '\n').split('\n')
                kit_name_html = "<br>".join([f"&bull;&nbsp;{line}" if i > 0 else f"<strong>{line}</strong>" for i, line in enumerate(kit_name_lines)])
                if counter % 2 == 0:
                    background_color = 'white'
                else:
                    background_color = 'lightblue'

                html_row = f"<tr style='background-color: {background_color};'><td style='border: 1px solid #ccc; text-align: center;'><span>{counter}</span></td><td style='border: 1px solid #ccc;'><span>{kit_name_html}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{kit_number}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{quantity}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{unit_price}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{total_price}</span></td></tr>"

                html_rows += html_row
            return render_template('home/pdf_add_offer.html',add_user=add_user,html_rows=html_rows,addoffer_address=addoffer_address,addoffer_Role=addoffer_Role,
                                    addoffer_Phonenumber=addoffer_Phonenumber, segment='offer-offerlist')

@blueprint.route('/<int:id>/editcustomer', methods=['GET', 'POST'])
@login_required
def update(id):
    user = CustomerMaster.query.filter_by(id=id).first()
    city_master = CityMaster.query.all()
    if request.method == 'POST':
        user.customer_name = request.form['customer_name'].strip()
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
    values_list = json.loads(user.kit_products)

    if request.method == 'POST':
        user.kit_description = request.form['kit_description']
        user.kit_no = request.form['kit_no']
        user.hsn_code = request.form['hsn_code']
        user.lubricant_points = request.form['lubricant_points']
        kit_products_temp = request.form.getlist('kit_products')

        add_kit_master = []
        for i in range(len(kit_products_temp)):
            Kit_offer = {
                'kit_name_master': kit_products_temp[i]
            }
            add_kit_master.append(Kit_offer)
        
        user.kit_products = json.dumps(add_kit_master)
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
        state_masters = StateMaster.query.all()
        country_master = CountryMaster.query.all()

        return render_template('home/Customer-masters.html',users=users,city_master=city_master,state_masters=state_masters,
                               country_master=country_master, segment='Customer-masters')
    if request.method == 'POST':
        customer_name = request.form['customer_name'].strip()
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
        add_user_contractReview = AddOffer.query.all()
        return render_template('home/Contract-Review.html', add_user_contractReview=add_user_contractReview,segment='contractreview')


@blueprint.route('/<int:id>/edit_oc_register', methods=['GET', 'POST'])
@login_required
def edit_oc_register(id):
    add_user_contractReview = OCModel.query.filter_by(id=id).first()
    oc_confirmation_offer = add_user_contractReview.oc_confirmation_offer

    if oc_confirmation_offer:
        oc_temp_data = json.loads(oc_confirmation_offer)
    else:
        # Handle the case when oc_confirmation_offer is empty
        oc_temp_data = {}  # Set oc_temp_data to an empty dictionary or any default value
    print(oc_temp_data)
    print(oc_confirmation_offer)
    odoffer_database = AddOffer.query.filter_by(id=id).first()
    if request.method == 'POST':
        add_oc_confo = OCModel.query.filter_by(id=id).first()
        current_date = datetime.datetime.now().date()
        add_oc_confo.oc_date = current_date
        add_oc_confo.oc_customer_name = request.form['oc_customer_name']
        add_oc_confo.oc_po_value = request.form['oc_po_value']
        add_oc_confo.oc_customer_type = request.form['oc_customer_type']
        add_oc_confo.oc_po_number = request.form['oc_po_number']
        add_oc_confo.oc_po_date = request.form['oc_po_date']
        add_oc_confo.oc_dispatch_date = request.form['oc_dispatch_date']
        add_oc_confo.oc_po_qty = request.form['oc_po_qty']
        add_oc_confo.oc_remarks = request.form['oc_remarks']

        oc_confirmation_json = ''
        oc_confirmation_list = []
        # print(add_user_contractReview.oc_customer_type)
        if add_oc_confo.oc_customer_type == "Kits":
            oc_kit_type = request.form.getlist('oc_kit_type')
            oc_equipment = request.form.getlist('oc_equipment')
            oc_qty = request.form.getlist('oc_qty')
            oc_invoice_value = request.form.getlist('oc_invoice_value')
            oc_po_value = request.form.getlist('oc_po_value')
            oc_machine = request.form.getlist('oc_machine')
            oc_remark = request.form.getlist('oc_remark')

            oc_confirmation_list = []
            for i in range(len(oc_kit_type)):
                kit_offer = {
                    'oc_kit_type': oc_kit_type[i],
                    'oc_equipment': oc_equipment[i],
                    'oc_qty': oc_qty[i],
                    'oc_invoice_value': oc_invoice_value[i],
                    'oc_po_value' : oc_po_value[i],
                    'oc_machine': oc_machine[i],
                    'oc_remark': oc_remark[i]
                }
                oc_confirmation_list.append(kit_offer)
            print(oc_confirmation_list)
            # Convert the list to JSON
            oc_confirmation_json = json.dumps(oc_confirmation_list)
        add_oc_confo.oc_confirmation_offer = oc_confirmation_json
        db.session.commit()
        return redirect('/OC-Register-List')
    return render_template('home/editocfile.html', oc_temp_data=oc_temp_data,odoffer_database=odoffer_database,add_user_contractReview=add_user_contractReview, segment='OcRegister')
        
@blueprint.route('/<int:id>/edit_contractoffer', methods=['GET', 'POST'])
@login_required
def edit_contractoffer(id):
    add_user_contractReview = AddOffer.query.filter_by(id=id).first()
    if request.method == 'POST':
        # Get the values from request.form.get and assign them to the variables
        add_user_contractReview.contract_review_Order_No = request.form['contract_review_Order_No']
        add_user_contractReview.contract_review_Order_Date = request.form['contract_review_Order_Date']
        add_user_contractReview.contract_review_PO_Qty = request.form['contract_review_PO_Qty']
        add_user_contractReview.contract_review_Billing_Address = request.form['contract_review_Billing_Address']
        add_user_contractReview.contract_review_Delivery_Address_1 = request.form['contract_review_Delivery_Address_1']
        add_user_contractReview.contract_review_Delivery_Address_2 = request.form['contract_review_Delivery_Address_2']
        add_user_contractReview.contract_review_Delivery_Address_3 = request.form['contract_review_Delivery_Address_3']
        add_user_contractReview.contract_review_Delivery_Address_4 = request.form['contract_review_Delivery_Address_4']
        add_user_contractReview.contract_review_Delivery_Address_5 = request.form['contract_review_Delivery_Address_5']
        add_user_contractReview.contract_review_Offer_No = request.form['contract_review_Offer_No']
        add_user_contractReview.contract_review_Total_Cost = request.form['contract_review_Total_Cost']

        add_user_contractReview.contract_review_price = request.form['contract_review_price']
        add_user_contractReview.contract_review_price_1 = request.form['contract_review_price_1']
        add_user_contractReview.contract_review_price_2 = request.form['contract_review_price_2']

        add_user_contractReview.contract_review_packing_and_Forwarding = request.form['contract_review_packing_and_Forwarding']
        add_user_contractReview.contract_review_packing_and_Forwarding_1 = request.form['contract_review_packing_and_Forwarding_1']
        add_user_contractReview.contract_review_packing_and_Forwarding_2  = request.form['contract_review_packing_and_Forwarding_2']

        add_user_contractReview.contract_review_gst = request.form['contract_review_gst']
        add_user_contractReview.contract_review_gst_1 = request.form['contract_review_gst_1']
        add_user_contractReview.contract_review_gst_2 = request.form['contract_review_gst_2']

        add_user_contractReview.contract_review_delivery = request.form['contract_review_delivery']
        add_user_contractReview.contract_review_delivery_1 = request.form['contract_review_delivery_1']
        add_user_contractReview.contract_review_delivery_2 = request.form['contract_review_delivery_2']


        add_user_contractReview.contract_review_warrantly = request.form['contract_review_warrantly']
        add_user_contractReview.contract_review_warrantly_1 = request.form['contract_review_warrantly_1']
        add_user_contractReview.contract_review_warrantly_2 = request.form['contract_review_warrantly_2']


        add_user_contractReview.contract_review_terms_of_pay = request.form['contract_review_terms_of_pay']
        add_user_contractReview.contract_review_terms_of_pay_1 = request.form['contract_review_terms_of_pay_1']
        add_user_contractReview.contract_review_terms_of_pay_2 = request.form['contract_review_terms_of_pay_2']


        add_user_contractReview.contract_review_freight = request.form['contract_review_freight']
        add_user_contractReview.contract_review_freight_1 = request.form['contract_review_freight_1']
        add_user_contractReview.contract_review_freight_2 = request.form['contract_review_freight_2']


        add_user_contractReview.contract_review_preferred_transporter = request.form['contract_review_preferred_transporter']
        add_user_contractReview.contract_review_preferred_transporter_1 = request.form['contract_review_preferred_transporter_1']
        add_user_contractReview.contract_review_preferred_transporter_2 = request.form['contract_review_preferred_transporter_2']

        
        add_user_contractReview.contract_review_contact_person = request.form['contract_review_contact_person']
        add_user_contractReview.contract_review_telephone_number = request.form['contract_review_telephone_number']
        add_user_contractReview.contract_review_email_id = request.form['contract_review_email_id']
        
        add_user_contractReview.contract_review_notes = request.form['contract_review_notes']
        if 'contract_review_approve' in request.form:
            checkbox_value = '1'
            add_user_contractReview.contract_review_approve = checkbox_value
        else:
            checkbox_value = '0'
            add_user_contractReview.contract_review_approve = checkbox_value
        if add_user_contractReview.contract_review_approve == "1":
            oc_model_len = OCModel.query.all()
            Offer_confirmation_Number = len(oc_model_len)+1000
            Offer_confirmation_Number += 1

            current_date = datetime.datetime.now()
            current_year = str(current_date.year)[-2:]
            next_year = str(current_date.year + 1)[-2:]
            original_value = Offer_confirmation_Number
            updated_value = f"ORN/OC/{original_value}/{current_year}-{next_year}"
            add_user_contractReview.offer_conformation_number = updated_value
            
            oc_date = ""
            oc_number = updated_value
            oc_customer_name = add_user_contractReview.customer_name_offer
            oc_po_value = ""
            oc_customer_type = add_user_contractReview.offer_type_offer
            oc_po_number = ""

            oc_po_date = add_user_contractReview.contract_review_Order_Date
            oc_quotation_no = add_user_contractReview.quotation_number_offer
            oc_dispatch_date = ""
            oc_invoice_no = ""
            oc_invoice_date= ""
            oc_po_qty = add_user_contractReview.contract_review_PO_Qty
            oc_remarks = ""
            oc_confirmation_offer = ""

            add_oc = OCModel(
                oc_date = oc_date,
                oc_number = oc_number,
                oc_customer_name = oc_customer_name,
                oc_po_value = oc_po_value,
                oc_customer_type = oc_customer_type,
                oc_po_number = oc_po_number,
                oc_po_date = oc_po_date,
                oc_quotation_no = oc_quotation_no,
                oc_dispatch_date = oc_dispatch_date,
                oc_invoice_no = oc_invoice_no,
                oc_invoice_date= oc_invoice_date,
                oc_po_qty = oc_po_qty,
                oc_remarks = oc_remarks,
                oc_confirmation_offer = oc_confirmation_offer
            )

            db.session.add(add_oc)
            db.session.commit()

        db.session.commit()

        return redirect('/Contract-Review-list')

    return render_template('home/editcontract.html', add_user_contractReview=add_user_contractReview, segment='contractreview')

@blueprint.route('/OC-Register-list', methods=['GET', 'POST'])
@login_required
def OC_Register_list():
    if request.method == 'GET':
        users = OCModel.query.all()
        return render_template('home/OC-Register-List.html', users=users,segment='OcRegister')

@blueprint.route('/BOM-Register-List', methods=['GET', 'POST'])
@login_required
def BOM_Register_list():
    if request.method == 'GET':
        return render_template('home/BOM-Register-List.html', segment='BOMRegister')

@blueprint.route('/Marketing-RegisterList', methods=['GET', 'POST'])
@login_required
def Marketing_RegisterList():
    if request.method == 'GET':
        return render_template('home/Marketing-Register-List.html', segment='MarketingRegisterList')


@blueprint.route('/Marketing-Register-Report', methods=['GET', 'POST'])
@login_required
def Marketing_Register_Report():
    if request.method == 'GET':
        return render_template('home/Marketing-Register-Report.html',  segment='MarketingRegisterReport')



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


@blueprint.route('/<int:id>/delete-bom-master', methods=['GET', 'POST'])
@login_required
def delete_bom(id):
    users = BomMaster.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/BOM-masters')
    return render_template('home/delete_bom_master.html')

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
        segment = get_segment(request)
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
