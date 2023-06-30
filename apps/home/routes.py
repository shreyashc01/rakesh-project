import json
from apps.home import blueprint
from flask import render_template, request, redirect, jsonify, flash
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps import db
from apps.home.models import CustomerMaster,AddOffer,Invoices,BankDetails

@blueprint.route('/dashboard')
@login_required
def dashboard():
    # db.metadata.tables['Users'].drop(db.engine)
    return render_template('home/dashboard.html', segment='dashboard')

@blueprint.route('/offer-addoffer', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        details = BankDetails.query.filter_by(id=1).first()
        addOffer = AddOffer.query.all()
        Quatationnumber = len(addOffer) 
        Quatationnumber += 1
        return render_template('home/add-offer.html',details=details,users=users, offer_json=None,Quatationnumber=Quatationnumber, addOffer_database=None,segment='offer-addoffer')
    if request.method == 'POST':
        customer_name_offer = request.form['customer_name_offer']

        due_date_offer = request.form['due_date_offer']
        quotation_number_offer = request.form['quotation_number_offer']
        marketing_person_offer = request.form['marketing_Person_offer']
        currency_type_offer = request.form['currency_type_offer']
        product_kit_offer_json = ''
        product_kit_offer = []

        product_offers = request.form.getlist('product')
        quantity_list = request.form.getlist('quantity')
        unit_price_list = request.form.getlist('unit_price')
        uom_type_list = request.form.getlist('offer_uom')
        total_price_product_offer = request.form.getlist('totalPrice')

        product_kit_offer = []
        for i in range(len(product_offers)):
            product_offer = {
                'product_name': product_offers[i],
                'quantity': quantity_list[i],
                'unit_price': unit_price_list[i],
                'uom' : uom_type_list[i],
                'total_price': total_price_product_offer[i],
            }
            product_kit_offer.append(product_offer)

        product_kit_offer_json = json.dumps(product_kit_offer)

        grossAmount = request.form['offer_grossAmount']
        discountType = request.form['discountType']
        discountValue = request.form['offer_discountValue']
        assessableValue = request.form['offer_assessableValue']
        pfPercentage = request.form['offer_pfPercentage']
        pfValue = request.form['offer_pfValue']
        freightValue = request.form['offer_freightValue']
        totalFreight = request.form['offer_totalFreight']
        tcsPercentage = request.form['offer_tcsPercentage']
        gstType = request.form['offer_gstPercentage']
        tcsValue = request.form['offer_tcsValue']
        gstPercentage = request.form['offer_gstPercentage']
        gstValue = request.form['offer_gstValue']
        roundOffType = request.form['roundOffType']
        roundOffValue = request.form['offer_roundOffValue']
        grandTotal = request.form['offer_grandTotal']

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
            warrenty_terms_offer=warrenty_terms_offer
        )

        db.session.add(new_offer)
        db.session.commit()
        return redirect('/offer-offerlist')

@blueprint.route('/<int:id>/edit-addoffer', methods=['GET', 'POST'])
@login_required
def update_add_offer(id):
    addOffer_database = AddOffer.query.filter_by(id=id).first()
    details = BankDetails.query.filter_by(id=1).first()
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        offer_json = json.loads(addOffer_database.product_kit_offer_json)
    if request.method == 'POST':
        addOffer_database.customer_name_offer = request.form['customer_name_offer']
        addOffer_database.due_date_offer = request.form['due_date_offer']
        addOffer_database.quotation_number_offer = request.form['quotation_number_offer']
        addOffer_database.marketing_person_offer = request.form['marketing_Person_offer']
        addOffer_database.currency_type_offer = request.form['currency_type_offer']
        product_kit_offer_json = ''
        product_kit_offer = []
        product_offers = request.form.getlist('product')
        quantity_list = request.form.getlist('quantity')
        unit_price_list = request.form.getlist('unit_price')
        uom_type_list = request.form.getlist('offer_uom')
        total_price_product_offer = request.form.getlist('totalPrice')

        product_kit_offer = []
        for i in range(len(product_offers)):
            product_offer = {
                'product_name': product_offers[i],
                'quantity': quantity_list[i],
                'unit_price': unit_price_list[i],
                'uom' : uom_type_list[i],
                'total_price': total_price_product_offer[i],
            }
            product_kit_offer.append(product_offer)

        product_kit_offer_json = json.dumps(product_kit_offer)
        addOffer_database.product_kit_offer_json = product_kit_offer_json
        addOffer_database.grossAmount = request.form['offer_grossAmount']
        addOffer_database.discountType = request.form['discountType']
        addOffer_database.discountValue = request.form['offer_discountValue']
        addOffer_database.assessableValue = request.form['offer_assessableValue']
        addOffer_database.pfPercentage = request.form['offer_pfPercentage']
        addOffer_database.pfValue = request.form['offer_pfValue']
        addOffer_database.freightValue = request.form['offer_freightValue']
        addOffer_database.totalFreight = request.form['offer_totalFreight']
        addOffer_database.tcsPercentage = request.form['offer_tcsPercentage']
        addOffer_database.gstType = ""
        addOffer_database.tcsValue = request.form['offer_tcsValue']
        addOffer_database.gstPercentage = request.form['offer_gstPercentage']
        addOffer_database.gstValue = request.form['offer_gstValue']
        addOffer_database.roundOffType = request.form['roundOffType']
        addOffer_database.roundOffValue = request.form['offer_roundOffValue']
        addOffer_database.grandTotal = request.form['offer_grandTotal']

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
    return render_template('home/add-offer.html',details=details,users=users, Quatationnumber=0,offer_json=offer_json, addOffer_database=addOffer_database,segment='offer-offerlist')

@blueprint.route('/invoice-addinvoice', methods=['GET', 'POST'])
@login_required
def addinvoice():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        return render_template('home/add-invoice.html',users=users,segment='add-invoice')
    if request.method == 'POST':
        invoiceNo = request.form['invoiceNo']
        invoiceDate = request.form['invoiceDate']
        supplierCode = request.form['supplierCode']
        invoiceType = request.form['invoiceType']
        oc_name_change = request.form['oc_name_change']
        buyers_name = request.form['buyer_input']
        oc_number = request.form['main_oc_select']
        billingAddress1 = request.form['billingAddress1']
        billingAddress = request.form['billingAddress']
        buyersGSTIN = request.form['buyersGSTIN']
        buyersPAN = request.form['buyersPAN']
        buyersOrderNo = request.form['buyersOrderNo']
        buyersOrderDate = request.form['buyersOrderDate']
        buyersStateCode = request.form['buyersStateCode']
        placeOfSupply = request.form['placeOfSupply']
        transporterDetails = request.form['transporterDetails']
        exportFields = request.form['export_standard']
        paymentTerms = request.form['paymentTerms']
        kitSpare = request.form['kitSpare']
        product_kit_offer_json = ''
        product_kit_offer = []
        part_no = request.form.getlist('part_no')
        product = request.form.getlist('product')
        hsn_code = request.form.getlist('hsn_code')
        quantity = request.form.getlist('quantity')
        invoice_uom = request.form.getlist('invoice_uom')
        unit_price = request.form.getlist('unit_price')
        totalPrice = request.form.getlist('totalPrice')
        product_kit_offer = []
        for i in range(len(part_no)):
            product_offer = {
                'part_no': part_no[i],
                'product' : product[i],
                'hsn_code': hsn_code[i],
                'quantity': quantity[i],
                'invoice_uom' : invoice_uom[i],
                'unit_price': unit_price[i],
                'totalPrice': totalPrice[i]
            }
            product_kit_offer.append(product_offer)

        product_kit_offer_json = json.dumps(product_kit_offer)
        invoice_grossAmount = request.form['invoice_grossAmount']
        discountType = request.form['discountType']
        invoice_discountValue = request.form['invoice_discountValue']
        assessableValue = request.form['invoice_assessableValue']
        pfPercentage = request.form['invoice_pfPercentage']
        invoice_pfValue = request.form['invoice_pfValue']
        freightValue = request.form['invoice_freightValue']
        invoice_totalFreight = request.form['invoice_totalFreight']
        tcsPercentage = request.form['invoice_tcsPercentage']
        invoice_tcsValue = request.form['invoice_tcsValue']
        gstPercentage = request.form['invoice_gstPercentage']
        invoice_gstValue = request.form['invoice_gstValue']
        roundOffType = request.form['roundOffType']
        invoice_roundOffValue = request.form['invoice_roundOffValue']
        invoice_grandTotal = request.form['invoice_grandTotal']

        product_kit_Json = product_kit_offer_json

        new_invoice = Invoices(invoiceNo=invoiceNo, invoiceDate=invoiceDate, supplierCode=supplierCode,
                               invoiceType=invoiceType, oc_name_change=oc_name_change, buyers_name=buyers_name,
                               oc_number=oc_number, billingAddress1=billingAddress1, billingAddress=billingAddress,
                               buyersGSTIN=buyersGSTIN, buyersPAN=buyersPAN, buyersOrderNo=buyersOrderNo,
                               buyersOrderDate=buyersOrderDate, buyersStateCode=buyersStateCode,
                               placeOfSupply=placeOfSupply, transporterDetails=transporterDetails,
                               exportFields=exportFields, paymentTerms=paymentTerms, kitSpare=kitSpare,
                               invoice_grossAmount=invoice_grossAmount, discountType=discountType,
                               invoice_discountValue=invoice_discountValue, assessableValue=assessableValue,
                               pfPercentage=pfPercentage, invoice_pfValue=invoice_pfValue,
                               freightValue=freightValue, invoice_totalFreight=invoice_totalFreight,
                               tcsPercentage=tcsPercentage, invoice_tcsValue=invoice_tcsValue,
                               gstPercentage=gstPercentage, invoice_gstValue=invoice_gstValue,
                               roundOffType=roundOffType, invoice_roundOffValue=invoice_roundOffValue,
                               invoice_grandTotal=invoice_grandTotal, invoice_status=0,product_kit_Json=product_kit_Json)

        db.session.add(new_invoice)
        db.session.commit()
        return redirect('/invoice-invoiceslist')
    
@blueprint.route('/invoice-invoiceslist', methods=['GET', 'POST'])
@login_required
def listinvoices():
    invoice = Invoices.query.all()
    return render_template('home/invoices.html', invoice=invoice,segment='list-invoice')

@blueprint.route('/PO-POlist', methods=['GET', 'POST'])
@login_required
def listpo():
    return render_template('home/purchaseorder.html', segment='list-purchaseorder')

@blueprint.route('/PO-addpo', methods=['GET', 'POST'])
@login_required
def addpo():
    if request.method == 'GET':
        return render_template('home/add-purchaseorder.html',segment='add-purchaseorder')

@blueprint.route('/offer-offerlist', methods=['GET', 'POST'])
@login_required
def retrieve_list():
    add_user = AddOffer.query.all()
    return render_template('home/users.html',add_user=add_user, segment='offer-offerlist')

@blueprint.route('/<int:id>/invoice_pdf', methods=['GET', 'POST'])
@login_required
def invoice_pdf(id):
    if request.method == 'GET':
        add_user = Invoices.query.filter_by(id=id).first()
        bank_details = BankDetails.query.filter_by(id=1).first()
        data = json.loads(add_user.product_kit_Json)
        html_rows = ""
        counter = 0
        html_rows = ""
        counter = 0
        for item in data:
            part_no = item['part_no']
            product = item['product']
            hsn_code = item['hsn_code']
            quantity = item['quantity']
            invoice_uom = item['invoice_uom']
            unit_price = item['unit_price']
            totalPrice = item['totalPrice']

            counter += 1
            if counter % 2 == 0:
                background_color = 'white'
            else:
                background_color = '#b18ae4'

            html_row = f"<tr style='background-color: {background_color};'><td style='border: 1px solid #ccc; text-align: center;'><span>{counter}</span></td><td style='border: 1px solid #ccc;'><span>{product}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{part_no}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{hsn_code}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{quantity}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{invoice_uom}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{unit_price}</span></td><td style='border: 1px solid #ccc; text-align: right;'><span>{totalPrice}</span></td></tr>"

            html_rows += html_row

        return render_template('home/pdf_add_invoice.html', bank_details=bank_details,add_user=add_user, html_rows=html_rows, segment='list-invoice')


@blueprint.route('/<int:id>/offer_pdf', methods=['GET', 'POST'])
@login_required
def offer_pdf(id):
    if request.method == 'GET':
        add_user = AddOffer.query.filter_by(id=id).first()
        address_temp = CustomerMaster.query.filter_by(customer_name=add_user.customer_name_offer).first()
        addoffer_address = address_temp.address if address_temp.address else None
        Bank_detail = BankDetails.query.filter_by(id=1).first()
        Role = Bank_detail.supplier_role
        contact_no = Bank_detail.supplier_contact_no
        data = json.loads(add_user.product_kit_offer_json)
        html_rows = ""
        counter = 0

        for item in data:
            product_name = item['product_name']
            quantity = item['quantity']
            unit_price = item['unit_price']
            uom = item['uom']
            total_price = item['total_price']
            
            counter += 1
            if counter % 2 == 0:
                background_color = 'white'
            else:
                background_color = '#b18ae4'

            html_row = f"<tr style='background-color: {background_color};'><td style='border: 1px solid #ccc; text-align: center;'><span>{counter}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{product_name}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{uom}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{quantity}</span></td><td style='border: 1px solid #ccc; text-align: center;'><span>{unit_price}</span></td><td style='border: 1px solid #ccc; text-align: right;'><span>{total_price}</span></td></tr>"

            html_rows += html_row
        return render_template('home/pdf_add_offer.html',Role=Role,contact_no=contact_no,add_user=add_user,html_rows=html_rows,addoffer_address=addoffer_address,segment='offer-offerlist')

@blueprint.route('/<int:id>/editcustomer', methods=['GET', 'POST'])
@login_required
def update(id):
    user = CustomerMaster.query.filter_by(id=id).first()
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

    return render_template('home/updatecustomer.html', user=user, segment='Customer-masters')


@blueprint.route('/Customer-masters', methods=['GET', 'POST'])
@login_required
def Customer_masters():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        return render_template('home/Customer-masters.html',users=users, segment='Customer-masters')
    if request.method == 'POST':
        customer_name = request.form['customer_name'].strip()
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
            address=address
            )
        
        db.session.add(offer)
        db.session.commit()
        return redirect('/Customer-masters')

@blueprint.route('/Bank-details', methods=['GET', 'POST'])
@login_required
def Bank_master():
    if request.method == 'GET':
        bank_detail = BankDetails.query.filter_by(id=1).first()
        return render_template('home/Bank-master.html',segment='Bank-details',bank_detail=bank_detail)
    if request.method == 'POST':
        bank_detail = BankDetails.query.filter_by(id=1).first()
        bank_detail.supplier_name = request.form['supplier_name']
        bank_detail.supplier_role = request.form['supplier_role']
        bank_detail.supplier_contact_no = request.form['supplier_contact_no']
        bank_detail.suppliers_gstin_number = request.form['suppliers_gstin_number']
        bank_detail.suppliers_pan_number = request.form['suppliers_pan_number']
        bank_detail.suppliers_hsn_code = request.form['suppliers_hsn_code']
        bank_detail.suppliers_state_code = request.form['suppliers_state_code']
        bank_detail.suppliers_bank = request.form['suppliers_bank']
        bank_detail.suppliers_account_no = request.form['suppliers_account_no']
        bank_detail.suppliers_ifsc_code = request.form['suppliers_ifsc_code']
        bank_detail.nature_of_account = request.form['nature_of_account']
        db.session.commit()
        return redirect('/Bank-details')

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
