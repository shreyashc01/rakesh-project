from apps import db

class UserModel(db.Model):
    __tablename__ = "use"

    id = db.Column(db.Integer, primary_key=True)
    quation_no = db.Column(db.String())
    customer_name_offer = db.Column(db.String())
    adress_name_offer = db.Column(db.String())
    due_date = db.Column(db.String())
    offer_type = db.Column(db.String())
    reference_no = db.Column(db.String())
    marketing_person = db.Column(db.String())
    currency_type = db.Column(db.String())
    total_cost = db.Column(db.String())
    pfpercent = db.Column(db.String(80))
    freight = db.Column(db.String(80))
    gst = db.Column(db.String(80))
    grand_total = db.Column(db.String(80))

    Subject = db.Column(db.String())
    reference = db.Column(db.String())
    description = db.Column(db.String())
    footer_description = db.Column(db.String())
    notes = db.Column(db.String())

    price_basis = db.Column(db.String())
    pfcharges = db.Column(db.String())
    igst = db.Column(db.String())
    hsn_code = db.Column(db.String())
    payment_terms = db.Column(db.String())
    delivery = db.Column(db.String())
    freight_tc = db.Column(db.String())
    validity = db.Column(db.String())
    warrantly = db.Column(db.String())

    def __init__(self, quation_no, customer_name_offer,adress_name_offer, due_date, offer_type, reference_no, marketing_person, currency_type,
                 total_cost, pfpercent, freight, gst, grand_total,
                 Subject, reference, description, footer_description,
                 notes, price_basis, pfcharges, igst,
                 hsn_code, payment_terms, delivery, freight_tc, validity,warrantly):
        self.quation_no = quation_no
        self.customer_name_offer = customer_name_offer
        self.adress_name_offer = adress_name_offer
        self.due_date = due_date
        self.offer_type = offer_type
        self.reference_no = reference_no
        self.marketing_person = marketing_person
        self.currency_type = currency_type
        self.total_cost = total_cost
        self.pfpercent = pfpercent
        self.freight = freight
        self.gst = gst
        self.grand_total = grand_total
        self.Subject = Subject
        self.reference = reference
        self.description = description
        self.footer_description = footer_description
        self.notes = notes
        self.price_basis = price_basis
        self.pfcharges = pfcharges
        self.igst = igst
        self.hsn_code = hsn_code
        self.payment_terms = payment_terms
        self.delivery = delivery
        self.freight_tc = freight_tc
        self.validity = validity
        self.warrantly = warrantly
        

    def __repr__(self):
        return f"{self.quation_no}:{self.customer_name_offer}"



class MainUser(db.Model):
    __tablename__ = "mainuser"

    id = db.Column(db.Integer, primary_key=True)
    product_offer = db.Column(db.String())
    UOM_offer = db.Column(db.String())
    quantity_offer = db.Column(db.String())
    unit_price_offer = db.Column(db.String())
    total_price_offer = db.Column(db.String())
 

    def __init__(self, product_offer, UOM_offer, quantity_offer,unit_price_offer, total_price_offer):
        self.product_offer = product_offer
        self.UOM_offer = UOM_offer
        self.quantity_offer = quantity_offer
        self.unit_price_offer = unit_price_offer
        self.total_price_offer = total_price_offer

    def __repr__(self):
        return f"{self.product_offer}:{self.UOM_offer}"

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

    def __init__(self, customer_name, primary_contact_name, secondary_contact_name, email_id, contact_number, pan_number, gst_number,
                 address):
        self.customer_name = customer_name
        self.primary_contact_name = primary_contact_name
        self.secondary_contact_name = secondary_contact_name
        self.email_id = email_id
        self.contact_number = contact_number
        self.pan_number = pan_number
        self.gst_number = gst_number
        self.address = address
        

    def __repr__(self):
        return f"{self.customer_name}:{self.primary_contact_name}"


class ProductMaster(db.Model):
    __tablename__ = "productmaster"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String())
    part_no = db.Column(db.INT())
    rack_no = db.Column(db.INT())
    bin_no = db.Column(db.INT())
    minimum_qty = db.Column(db.INT())
    maximum_order = db.Column(db.INT())
    description = db.Column(db.String())

    def __init__(self, product_name, part_no, rack_no, bin_no, minimum_qty, maximum_order, description):
        self.product_name = product_name
        self.part_no = part_no
        self.rack_no = rack_no
        self.bin_no = bin_no
        self.minimum_qty = minimum_qty
        self.maximum_order = maximum_order
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
        return f"{self.country_name_temp}:{self.country_name_temp}"

class StateMaster(db.Model):
    __tablename__ = "StateMaster"

    id = db.Column(db.Integer, primary_key=True)
    state_name_temp = db.Column(db.String())

    def __init__(self, state_name_temp):
        self.state_name_temp = state_name_temp
        

    def __repr__(self):
        return f"{self.state_name_temp}:{self.state_name_temp}"

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
        return f"{self.country_name}:{self.state_name}"

class RoleMaster(db.Model):
    __tablename__ = "RoleMaster"

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String())

    def __init__(self, role_name):
        self.role_name = role_name

    def __repr__(self):
        return f"{self.role_name}:{self.role_name}"

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

class SupplierMaster(db.Model):
    __tablename__ = "CurrencyMaster"

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
    __tablename__ = "CurrencyMaster"

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