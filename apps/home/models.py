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
    quotation_number_offer = db.Column(db.Integer())
    marketing_person_offer = db.Column(db.String())
    currency_type_offer = db.Column(db.String())

    product_kit_offer_json = db.Column(db.String())
    # product_offers_json =  db.Column(db.String())
    # kit_description_offer = db.Column(db.String())
    # kit_number_offer = db.Column(db.String())
    # quantity_kit_offer = db.Column(db.Integer())
    # unit_price_kit_offer = db.Column(db.Float())
    # total_price_kit_offer = db.Column(db.Float())

    total_amount_offer = db.Column(db.Float())
    freight_offer = db.Column(db.Float())
    cgst_igst_type_offer = db.Column(db.String())
    pf_percentage_offer = db.Column(db.Float())
    gst_offer = db.Column(db.Float())
    grand_total_offer = db.Column(db.Float())

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

    def __init__(self, customer_name_offer, due_date_offer, offer_type_offer, quotation_number_offer, marketing_person_offer,
                 currency_type_offer, product_kit_offer_json, total_amount_offer, freight_offer, cgst_igst_type_offer,
                 pf_percentage_offer, gst_offer, grand_total_offer, subject_offer, reference_offer, description_offer,
                 footer_description_offer, notes_offer, price_basis_offer, PandFcharges_offer, igst_terms_offer,
                 hsn_code_offer, payment_terms_offer, delivery_terms_offer, freight_terms_offer, validity_terms_offer,
                 warrenty_terms_offer):
        self.customer_name_offer = customer_name_offer
        self.due_date_offer = due_date_offer
        self.offer_type_offer = offer_type_offer
        self.quotation_number_offer = quotation_number_offer
        self.marketing_person_offer = marketing_person_offer
        self.currency_type_offer = currency_type_offer

        self.product_kit_offer_json = product_kit_offer_json
        # self.product_offers_json = product_offers_json

        # self.kit_description_offer = kit_description_offer
        # self.kit_number_offer = kit_number_offer
        # self.quantity_kit_offer = quantity_kit_offer
        # self.unit_price_kit_offer = unit_price_kit_offer
        # self.total_price_kit_offer = total_price_kit_offer

        self.total_amount_offer = total_amount_offer
        self.freight_offer = freight_offer
        self.cgst_igst_type_offer = cgst_igst_type_offer
        self.pf_percentage_offer = pf_percentage_offer
        self.gst_offer = gst_offer
        self.grand_total_offer = grand_total_offer

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

    def __repr__(self):
        return f"{self.id}:{self.customer_name_offer}"
        

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
    bom_serial_no = db.Column(db.String())
    bom_category = db.Column(db.String())
    bom_product = db.Column(db.String())
    bom_quantity = db.Column(db.String())
    bom_uom = db.Column(db.String())

    def __init__(self, bom_description, bom_no, bom_model_no, bom_cls,bom_lube_points,
                 bom_type,bom_notes,bom_serial_no,bom_category,bom_product,bom_quantity, bom_uom):
        self.bom_description = bom_description
        self.bom_no = bom_no
        self.bom_model_no = bom_model_no
        self.bom_cls = bom_cls
        self.bom_lube_points = bom_lube_points
        self.bom_type = bom_type
        self.bom_notes = bom_notes
        self.bom_serial_no = bom_serial_no
        self.bom_category = bom_category
        self.bom_product = bom_product
        self.bom_quantity = bom_quantity
        self.bom_uom = bom_uom

    def __repr__(self):
        return f"{self.bom_description}:{self.bom_no}"