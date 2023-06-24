from apps import db

class CustomerMaster(db.Model):
    __tablename__ = "customermaster"

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String())
    primary_contact_name = db.Column(db.String())
    secondary_contact_name = db.Column(db.String())
    email_id = db.Column(db.String())
    contact_number = db.Column(db.INT())
    pan_number = db.Column(db.String())
    gst_number = db.Column(db.String())
    address = db.Column(db.String())
    customer_country_name = db.Column(db.String())
    customer_state_name = db.Column(db.String())
    customer_city_name = db.Column(db.String())

    def __init__(self, customer_name, primary_contact_name, secondary_contact_name, email_id, contact_number, pan_number, gst_number,
                 address,customer_country_name,customer_state_name,customer_city_name):
        self.customer_name = customer_name
        self.primary_contact_name = primary_contact_name
        self.secondary_contact_name = secondary_contact_name
        self.email_id = email_id
        self.contact_number = contact_number
        self.pan_number = pan_number
        self.gst_number = gst_number
        self.address = address
        customer_country_name=customer_country_name
        customer_state_name=customer_state_name
        customer_city_name=customer_city_name

    def __repr__(self):
        return f"{self.customer_name}:{self.primary_contact_name}"

class AddOffer(db.Model):
    __tablename__ = "addoffer"

    id = db.Column(db.Integer, primary_key=True)
    customer_name_offer = db.Column(db.String())
    due_date_offer = db.Column(db.String())
    offer_type_offer = db.Column(db.String())
    quotation_number_offer = db.Column(db.String())
    marketing_person_offer = db.Column(db.String())
    currency_type_offer = db.Column(db.String())

    product_kit_offer_json = db.Column(db.String())

    grossAmount = db.Column(db.Float())
    discountType = db.Column(db.String())
    discountValue = db.Column(db.Float())
    assessableValue = db.Column(db.Float())
    pfPercentage = db.Column(db.Float())
    pfValue = db.Column(db.Float())
    freightValue = db.Column(db.Float())
    totalFreight = db.Column(db.Float())
    tcsPercentage = db.Column(db.Float())
    gstType = db.Column(db.String())
    tcsValue = db.Column(db.Float())
    gstPercentage = db.Column(db.Float())
    gstValue = db.Column(db.Float())
    roundOffType = db.Column(db.String())
    roundOffValue = db.Column(db.Float())
    grandTotal = db.Column(db.Float())

    subject_offer = db.Column(db.String())
    reference_offer = db.Column(db.String())
    description_offer = db.Column(db.String())
    footer_description_offer = db.Column(db.String())
    notes_offer = db.Column(db.String())
    price_basis_offer = db.Column(db.String())
    PandFcharges_offer = db.Column(db.String())
    igst_terms_offer = db.Column(db.String())
    hsn_code_offer = db.Column(db.String())
    payment_terms_offer = db.Column(db.String())
    delivery_terms_offer = db.Column(db.String())
    freight_terms_offer = db.Column(db.String())
    validity_terms_offer = db.Column(db.String())
    warrenty_terms_offer = db.Column(db.String())

    # contractReview Fields
    contract_review_Order_No = db.Column(db.String())
    contract_review_Order_Date = db.Column(db.String())
    contract_review_PO_Qty = db.Column(db.Integer())
    contract_review_Billing_Address = db.Column(db.String())
    contract_review_Delivery_Address_1 = db.Column(db.String())
    contract_review_Delivery_Address_2 = db.Column(db.String())
    contract_review_Delivery_Address_3 = db.Column(db.String())
    contract_review_Delivery_Address_4 = db.Column(db.String())
    contract_review_Delivery_Address_5 = db.Column(db.String())
    contract_review_Offer_No = db.Column(db.String())
    contract_review_Total_Cost = db.Column(db.Float())

    contract_review_price = db.Column(db.String())
    contract_review_price_1 = db.Column(db.String())
    contract_review_price_2 = db.Column(db.String())

    contract_review_packing_and_Forwarding = db.Column(db.String())
    contract_review_packing_and_Forwarding_1 = db.Column(db.String())
    contract_review_packing_and_Forwarding_2 = db.Column(db.String())

    contract_review_gst = db.Column(db.String())
    contract_review_gst_1 = db.Column(db.String())
    contract_review_gst_2 = db.Column(db.String())


    contract_review_delivery = db.Column(db.String())
    contract_review_delivery_1 = db.Column(db.String())
    contract_review_delivery_2 = db.Column(db.String())


    contract_review_warrantly = db.Column(db.String())
    contract_review_warrantly_1 = db.Column(db.String())
    contract_review_warrantly_2 = db.Column(db.String())


    contract_review_terms_of_pay = db.Column(db.String())
    contract_review_terms_of_pay_1 = db.Column(db.String())
    contract_review_terms_of_pay_2 = db.Column(db.String())


    contract_review_freight = db.Column(db.String())
    contract_review_freight_1 = db.Column(db.String())
    contract_review_freight_2 = db.Column(db.String())


    contract_review_preferred_transporter = db.Column(db.String())
    contract_review_preferred_transporter_1 = db.Column(db.String())
    contract_review_preferred_transporter_2 = db.Column(db.String())


    contract_review_contact_person = db.Column(db.String())
    contract_review_telephone_number = db.Column(db.String())
    contract_review_email_id = db.Column(db.String())
    contract_review_notes = db.Column(db.String())
    contract_review_approve = db.Column(db.INT())

    offer_conformation_number = db.Column(db.String())

    def __init__(self, customer_name_offer, due_date_offer, offer_type_offer, quotation_number_offer, marketing_person_offer,
             currency_type_offer, product_kit_offer_json,grossAmount,discountType,discountValue,assessableValue,pfPercentage,pfValue,
             freightValue,totalFreight,tcsPercentage,gstType,tcsValue,gstPercentage,gstValue,roundOffType,roundOffValue,grandTotal, subject_offer, reference_offer, description_offer,
             footer_description_offer, notes_offer, price_basis_offer, PandFcharges_offer, igst_terms_offer,
             hsn_code_offer, payment_terms_offer, delivery_terms_offer, freight_terms_offer, validity_terms_offer,
             warrenty_terms_offer, contract_review_Order_No, contract_review_Order_Date, contract_review_PO_Qty,
             contract_review_Billing_Address, contract_review_Delivery_Address_1, contract_review_Delivery_Address_2,
             contract_review_Delivery_Address_3, contract_review_Delivery_Address_4, contract_review_Delivery_Address_5,
             contract_review_Offer_No, contract_review_Total_Cost, contract_review_price,contract_review_price_1,contract_review_price_2,
             contract_review_packing_and_Forwarding, contract_review_packing_and_Forwarding_1,contract_review_packing_and_Forwarding_2,
             contract_review_gst,contract_review_gst_1,contract_review_gst_2,
             contract_review_delivery,contract_review_delivery_1,contract_review_delivery_2,
             contract_review_warrantly,contract_review_warrantly_1,contract_review_warrantly_2,
             contract_review_terms_of_pay,contract_review_terms_of_pay_1,contract_review_terms_of_pay_2,
             contract_review_freight,contract_review_freight_1,contract_review_freight_2,
             contract_review_preferred_transporter,
              contract_review_preferred_transporter_1,contract_review_preferred_transporter_2,
                contract_review_contact_person,
             contract_review_telephone_number, contract_review_email_id, contract_review_notes,
             contract_review_approve, offer_conformation_number):
        self.customer_name_offer = customer_name_offer
        self.due_date_offer = due_date_offer
        self.offer_type_offer = offer_type_offer
        self.quotation_number_offer = quotation_number_offer
        self.marketing_person_offer = marketing_person_offer
        self.currency_type_offer = currency_type_offer

        self.product_kit_offer_json = product_kit_offer_json

        self.grossAmount = grossAmount
        self.discountType = discountType
        self.discountValue = discountValue
        self.assessableValue = assessableValue
        self.pfPercentage = pfPercentage
        self.pfValue = pfValue
        self.freightValue = freightValue
        self.totalFreight = totalFreight
        self.tcsPercentage = tcsPercentage
        self.gstType = gstType
        self.tcsValue = tcsValue
        self.gstPercentage = gstPercentage
        self.gstValue = gstValue
        self.roundOffType = roundOffType
        self.roundOffValue = roundOffValue
        self.grandTotal = grandTotal

        self.subject_offer = subject_offer
        self.reference_offer = reference_offer
        self.description_offer = description_offer
        self.footer_description_offer = footer_description_offer
        self.notes_offer = notes_offer
        self.price_basis_offer = price_basis_offer

        self.PandFcharges_offer = PandFcharges_offer
        self.igst_terms_offer = igst_terms_offer
        self.hsn_code_offer = hsn_code_offer
        self.payment_terms_offer = payment_terms_offer
        self.delivery_terms_offer = delivery_terms_offer
        self.freight_terms_offer = freight_terms_offer
        self.validity_terms_offer = validity_terms_offer
        self.warrenty_terms_offer = warrenty_terms_offer

        # Set the values for the new fields
        self.contract_review_Order_No = contract_review_Order_No
        self.contract_review_Order_Date = contract_review_Order_Date
        self.contract_review_PO_Qty = contract_review_PO_Qty
        self.contract_review_Billing_Address = contract_review_Billing_Address
        self.contract_review_Delivery_Address_1 = contract_review_Delivery_Address_1
        self.contract_review_Delivery_Address_2 = contract_review_Delivery_Address_2
        self.contract_review_Delivery_Address_3 = contract_review_Delivery_Address_3
        self.contract_review_Delivery_Address_4 = contract_review_Delivery_Address_4
        self.contract_review_Delivery_Address_5 = contract_review_Delivery_Address_5
        self.contract_review_Offer_No = contract_review_Offer_No
        self.contract_review_Total_Cost = contract_review_Total_Cost

        self.contract_review_price = contract_review_price
        self.contract_review_price_1 = contract_review_price_1
        self.contract_review_price_2 = contract_review_price_2

        self.contract_review_packing_and_Forwarding = contract_review_packing_and_Forwarding
        self.contract_review_packing_and_Forwarding_1 = contract_review_packing_and_Forwarding_1
        self.contract_review_packing_and_Forwarding_2 = contract_review_packing_and_Forwarding_2

        self.contract_review_gst = contract_review_gst
        self.contract_review_gst_1 = contract_review_gst_1
        self.contract_review_gst_2 = contract_review_gst_2

        self.contract_review_delivery = contract_review_delivery
        self.contract_review_delivery_1 = contract_review_delivery_1
        self.contract_review_delivery_2 = contract_review_delivery_2


        self.contract_review_warrantly = contract_review_warrantly
        self.contract_review_warrantly_1 = contract_review_warrantly_1
        self.contract_review_warrantly_2 = contract_review_warrantly_2


        self.contract_review_terms_of_pay = contract_review_terms_of_pay
        self.contract_review_terms_of_pay_1 = contract_review_terms_of_pay_1
        self.contract_review_terms_of_pay_2 = contract_review_terms_of_pay_2


        self.contract_review_freight = contract_review_freight
        self.contract_review_freight_1 = contract_review_freight_1
        self.contract_review_freight_2 = contract_review_freight_2


        self.contract_review_preferred_transporter = contract_review_preferred_transporter
        self.contract_review_preferred_transporter_1 = contract_review_preferred_transporter_1
        self.contract_review_preferred_transporter_2 = contract_review_preferred_transporter_2


        self.contract_review_contact_person = contract_review_contact_person
        self.contract_review_telephone_number = contract_review_telephone_number
        self.contract_review_email_id = contract_review_email_id
        self.contract_review_notes = contract_review_notes
        self.contract_review_approve = contract_review_approve

        self.offer_conformation_number = offer_conformation_number
    def __repr__(self):
        return f"{self.id}:{self.customer_name_offer}"
        

class OCModel(db.Model):
    __tablename__ = "OfferComfirmation"
    id = db.Column(db.Integer, primary_key=True)
    oc_date = db.Column(db.String())
    oc_number = db.Column(db.String())
    oc_customer_name = db.Column(db.String())
    oc_po_value = db.Column(db.String())
    oc_customer_type = db.Column(db.String())
    oc_po_number = db.Column(db.String())
    oc_po_date = db.Column(db.String())
    oc_quotation_no = db.Column(db.String())
    oc_dispatch_date = db.Column(db.String())
    oc_invoice_no = db.Column(db.String())
    oc_invoice_date= db.Column(db.String())
    oc_po_qty = db.Column(db.String())
    oc_remarks = db.Column(db.String())
    oc_confirmation_offer = db.Column(db.String())

    def __init__(self, oc_date,oc_number, oc_customer_name, oc_customer_type, oc_po_number, oc_po_date, oc_po_value, oc_quotation_no,
                 oc_invoice_no,oc_invoice_date, oc_po_qty,oc_dispatch_date,oc_remarks, oc_confirmation_offer):
        self.oc_date = oc_date
        self.oc_number = oc_number
        self.oc_customer_name = oc_customer_name
        self.oc_customer_type = oc_customer_type
        self.oc_po_number = oc_po_number
        self.oc_po_date = oc_po_date
        self.oc_po_value = oc_po_value
        self.oc_quotation_no = oc_quotation_no
        self.oc_invoice_no = oc_invoice_no
        self.oc_invoice_date = oc_invoice_date
        self.oc_po_qty = oc_po_qty
        self.oc_dispatch_date = oc_dispatch_date
        self.oc_remarks = oc_remarks
        self.oc_confirmation_offer = oc_confirmation_offer
        

    def __repr__(self):
        return f"{self.oc_number}:{self.oc_customer_name}"
    
class ProductMaster(db.Model):
    __tablename__ = "productmaster"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String())
    part_no = db.Column(db.INT())
    rack_no = db.Column(db.INT())
    bin_no = db.Column(db.INT())
    minimum_qty = db.Column(db.INT())
    maximum_order = db.Column(db.INT())
    product_hsn_no = db.Column(db.INT())
    description = db.Column(db.String())

    def __init__(self, product_name, part_no, rack_no, bin_no, minimum_qty, maximum_order, product_hsn_no,description):
        self.product_name = product_name
        self.part_no = part_no
        self.rack_no = rack_no
        self.bin_no = bin_no
        self.minimum_qty = minimum_qty
        self.maximum_order = maximum_order
        self.product_hsn_no = product_hsn_no
        self.description = description
        

    def __repr__(self):
        return f"{self.product_name}:{self.part_no}"


class Invoices(db.Model):
    __tablename__ = "InvoiceList"

    id = db.Column(db.Integer, primary_key=True)
    invoiceNo = db.Column(db.String())
    invoiceDate = db.Column(db.String())
    supplierCode = db.Column(db.String())
    invoiceType = db.Column(db.String())
    oc_name_change = db.Column(db.String())
    buyers_name = db.Column(db.String())
    oc_number = db.Column(db.String())
    billingAddress1 = db.Column(db.String())
    billingAddress = db.Column(db.String())
    buyersGSTIN = db.Column(db.String())
    buyersPAN = db.Column(db.String())
    buyersOrderNo = db.Column(db.String())
    buyersOrderDate = db.Column(db.String())
    buyersStateCode = db.Column(db.String())
    placeOfSupply = db.Column(db.String())
    transporterDetails = db.Column(db.String())
    exportFields = db.Column(db.String())
    paymentTerms = db.Column(db.String())
    kitSpare = db.Column(db.String())

    invoice_grossAmount = db.Column(db.Float)
    discountType = db.Column(db.String())
    invoice_discountValue = db.Column(db.Float)
    assessableValue = db.Column(db.Float)
    pfPercentage = db.Column(db.Float)
    invoice_pfValue = db.Column(db.Float)
    freightValue = db.Column(db.Float)
    invoice_totalFreight = db.Column(db.Float)
    tcsPercentage = db.Column(db.Float)
    invoice_tcsValue = db.Column(db.Float)
    gstPercentage = db.Column(db.Float)
    invoice_gstValue = db.Column(db.Float)
    roundOffType = db.Column(db.String())
    invoice_roundOffValue = db.Column(db.Float)
    invoice_grandTotal = db.Column(db.Float)
    invoice_status = db.Column(db.String())
    product_kit_Json = db.Column(db.String())

    def __init__(self, invoiceNo, invoiceDate, supplierCode, invoiceType, oc_name_change, buyers_name, oc_number,
                 billingAddress1, billingAddress, buyersGSTIN, buyersPAN, buyersOrderNo, buyersOrderDate,
                 buyersStateCode, placeOfSupply, transporterDetails, exportFields, paymentTerms, kitSpare,
                 invoice_grossAmount, discountType, invoice_discountValue, assessableValue, pfPercentage,
                 invoice_pfValue, freightValue, invoice_totalFreight, tcsPercentage, invoice_tcsValue,
                 gstPercentage, invoice_gstValue, roundOffType, invoice_roundOffValue, invoice_grandTotal,
                 invoice_status,product_kit_Json):
        self.invoiceNo = invoiceNo
        self.invoiceDate = invoiceDate
        self.supplierCode = supplierCode
        self.invoiceType = invoiceType
        self.oc_name_change = oc_name_change
        self.buyers_name = buyers_name
        self.oc_number = oc_number
        self.billingAddress1 = billingAddress1
        self.billingAddress = billingAddress
        self.buyersGSTIN = buyersGSTIN
        self.buyersPAN = buyersPAN
        self.buyersOrderNo = buyersOrderNo
        self.buyersOrderDate = buyersOrderDate
        self.buyersStateCode = buyersStateCode
        self.placeOfSupply = placeOfSupply
        self.transporterDetails = transporterDetails
        self.exportFields = exportFields
        self.paymentTerms = paymentTerms
        self.kitSpare = kitSpare
        self.invoice_grossAmount = invoice_grossAmount
        self.discountType = discountType
        self.invoice_discountValue = invoice_discountValue
        self.assessableValue = assessableValue
        self.pfPercentage = pfPercentage
        self.invoice_pfValue = invoice_pfValue
        self.freightValue = freightValue
        self.invoice_totalFreight = invoice_totalFreight
        self.tcsPercentage = tcsPercentage
        self.invoice_tcsValue = invoice_tcsValue
        self.gstPercentage = gstPercentage
        self.invoice_gstValue = invoice_gstValue
        self.roundOffType = roundOffType
        self.invoice_roundOffValue = invoice_roundOffValue
        self.invoice_grandTotal = invoice_grandTotal
        self.invoice_status = invoice_status
        self.product_kit_Json = product_kit_Json

    def __repr__(self):
        return f"{self.invoiceNo}:{self.invoiceDate}"

class KitMaster(db.Model):
    __tablename__ = "kitmaster"

    id = db.Column(db.Integer, primary_key=True)
    kit_description = db.Column(db.String())
    kit_no = db.Column(db.INT())
    hsn_code = db.Column(db.Float())
    lubricant_points = db.Column(db.INT())
    kit_products = db.Column(db.String())

    def __init__(self, kit_description, kit_no, hsn_code, lubricant_points, kit_products):
        self.kit_description = kit_description
        self.kit_no = kit_no
        self.hsn_code = hsn_code
        self.lubricant_points = lubricant_points
        self.kit_products = kit_products
        

    def __repr__(self):
        return f"{self.kit_description}:{self.kit_no}"

class CountryMaster(db.Model):
    __tablename__ = "CountryMaster"

    id = db.Column(db.Integer, primary_key=True)
    country_name_temp = db.Column(db.String())

    def __init__(self, country_name_temp):
        self.country_name_temp = country_name_temp

    def __repr__(self):
        return self.country_name_temp

class StateMaster(db.Model):
    __tablename__ = "StateMaster"

    id = db.Column(db.Integer, primary_key=True)
    state_name_temp = db.Column(db.String())

    def __init__(self, state_name_temp):
        self.state_name_temp = state_name_temp
        

    def __repr__(self):
        return self.state_name_temp 

class CityMaster(db.Model):
    __tablename__ = "CityMaster"

    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String())
    state_name = db.Column(db.String())
    city_name = db.Column(db.String())

    def __init__(self, country_name, state_name, city_name):
        self.country_name = country_name
        self.state_name = state_name
        self.city_name = city_name

    def __repr__(self):
        return self.country_name

class RoleMaster(db.Model):
    __tablename__ = "RoleMaster"

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String())

    def __init__(self, role_name):
        self.role_name = role_name

    def __repr__(self):
        return f"{self.id}:{self.role_name}"

class BomCategoryMaster(db.Model):
    __tablename__ = "BomCategoryMaster"

    id = db.Column(db.Integer, primary_key=True)
    bom_category_name = db.Column(db.String())

    def __init__(self, bom_category_name):
        self.bom_category_name = bom_category_name

    def __repr__(self):
        return f"{self.bom_category_name}:{self.bom_category_name}"

class CurrencyMaster(db.Model):
    __tablename__ = "CurrencyMaster"

    id = db.Column(db.Integer, primary_key=True)
    currency_name = db.Column(db.String())

    def __init__(self, currency_name):
        self.currency_name = currency_name

    def __repr__(self):
        return f"{self.currency_name}:{self.currency_name}"

class UserModel(db.Model):
    __tablename__ = "UserModel"

    id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String())
    user_last_name = db.Column(db.String())
    user_contact_no = db.Column(db.String())
    user_email_id = db.Column(db.String())
    user_name_master = db.Column(db.String())
    password_master = db.Column(db.String())
    confirm_password = db.Column(db.String())
    user_role_master = db.Column(db.String())
    user_reporting_person = db.Column(db.String())


    def __init__(self, user_first_name,user_last_name,user_contact_no,user_email_id,user_name_master,password_master,confirm_password,user_role_master,user_reporting_person):
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_contact_no =user_contact_no
        self.user_email_id =user_email_id
        self.user_name_master = user_name_master
        self.password_master =password_master
        self.confirm_password =confirm_password
        self.user_role_master =user_role_master
        self.user_reporting_person =user_reporting_person

    def __repr__(self):
        return self.user_first_name
    
class SupplierMaster(db.Model):
    __tablename__ = "SupplierMaster"

    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String())
    supplier_primary_contact = db.Column(db.String())
    supplier_secondary_contact = db.Column(db.String())
    supplier_email_id = db.Column(db.String())
    supplier_contact_no = db.Column(db.String())
    supplier_country = db.Column(db.String())
    supplier_state = db.Column(db.String())
    supplier_city = db.Column(db.String())
    supplier_address = db.Column(db.String())
    supplier_gst_no = db.Column(db.String())
    supplier_pan = db.Column(db.String())

    def __init__(self, supplier_name, supplier_primary_contact, supplier_secondary_contact, supplier_email_id,supplier_contact_no,
                 supplier_country,supplier_state,supplier_city,supplier_address,supplier_gst_no,supplier_pan):
        self.supplier_name = supplier_name
        self.supplier_primary_contact = supplier_primary_contact
        self.supplier_secondary_contact = supplier_secondary_contact
        self.supplier_email_id = supplier_email_id
        self.supplier_contact_no = supplier_contact_no
        self.supplier_country = supplier_country
        self.supplier_state = supplier_state
        self.supplier_city = supplier_city
        self.supplier_address = supplier_address
        self.supplier_gst_no = supplier_gst_no
        self.supplier_pan = supplier_pan


    def __repr__(self):
        return f"{self.supplier_name}:{self.supplier_primary_contact}"
    
class BomMaster(db.Model):
    __tablename__ = "BomMaster"

    id = db.Column(db.Integer, primary_key=True)
    bom_description = db.Column(db.String())
    bom_no = db.Column(db.INT())
    bom_model_no = db.Column(db.String())
    bom_cls = db.Column(db.String())
    bom_lube_points = db.Column(db.String())
    bom_type = db.Column(db.String())
    bom_notes = db.Column(db.String())
    bom_data = db.Column(db.String())

    def __init__(self, bom_description, bom_no, bom_model_no, bom_cls,bom_lube_points,
                 bom_type,bom_notes,bom_data):
        self.bom_description = bom_description
        self.bom_no = bom_no
        self.bom_model_no = bom_model_no
        self.bom_cls = bom_cls
        self.bom_lube_points = bom_lube_points
        self.bom_type = bom_type
        self.bom_notes = bom_notes
        self.bom_data = bom_data

    def __repr__(self):
        return f"{self.bom_description}:{self.bom_no}"


class BankDetails(db.Model):
    __tablename__ = "BankDetails"

    id = db.Column(db.Integer, primary_key=True)
    suppliers_gstin_number = db.Column(db.String())
    suppliers_pan_number = db.Column(db.String())
    suppliers_hsn_code = db.Column(db.String())
    suppliers_state_code = db.Column(db.String())
    suppliers_bank = db.Column(db.String())
    suppliers_account_no = db.Column(db.String())
    suppliers_ifsc_code = db.Column(db.String())
    nature_of_account = db.Column(db.String())

    def __init__(self, suppliers_gstin_number, suppliers_pan_number, suppliers_hsn_code,
                 suppliers_state_code, suppliers_bank, suppliers_account_no,
                 suppliers_ifsc_code, nature_of_account):
        self.suppliers_gstin_number = suppliers_gstin_number
        self.suppliers_pan_number = suppliers_pan_number
        self.suppliers_hsn_code = suppliers_hsn_code
        self.suppliers_state_code = suppliers_state_code
        self.suppliers_bank = suppliers_bank
        self.suppliers_account_no = suppliers_account_no
        self.suppliers_ifsc_code = suppliers_ifsc_code
        self.nature_of_account = nature_of_account

    def __repr__(self):
        return f"<BankDetails {self.id}>"

    @classmethod
    def create_bank_details(cls):
        bank_detail = cls(
            suppliers_gstin_number="29AADCF1488R1ZT",
            suppliers_pan_number="AADCF1488R",
            suppliers_hsn_code="84798999",
            suppliers_state_code="29",
            suppliers_bank="BANK OF BARODA - JALAHALLI BRANCH",
            suppliers_account_no="89550200001031",
            suppliers_ifsc_code="BARB0VJJAHA (5th Digit is Zero)",
            nature_of_account="CURRENT ACCOUNT"
        )
        db.session.add(bank_detail)
        db.session.commit()

@db.event.listens_for(BankDetails.__table__, 'after_create')
def create_bank_details(*args, **kwargs):
    BankDetails.create_bank_details()

