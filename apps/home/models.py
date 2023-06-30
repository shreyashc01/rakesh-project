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

class AddOffer(db.Model):
    __tablename__ = "addoffer"

    id = db.Column(db.Integer, primary_key=True)
    customer_name_offer = db.Column(db.String())
    due_date_offer = db.Column(db.String())
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

    def __init__(self, customer_name_offer, due_date_offer, quotation_number_offer, marketing_person_offer,
             currency_type_offer, product_kit_offer_json,grossAmount,discountType,discountValue,assessableValue,pfPercentage,pfValue,
             freightValue,totalFreight,tcsPercentage,gstType,tcsValue,gstPercentage,gstValue,roundOffType,roundOffValue,grandTotal, subject_offer, reference_offer, description_offer,
             footer_description_offer, notes_offer, price_basis_offer, PandFcharges_offer, igst_terms_offer,
             hsn_code_offer, payment_terms_offer, delivery_terms_offer, freight_terms_offer, validity_terms_offer,
             warrenty_terms_offer):
        self.customer_name_offer = customer_name_offer
        self.due_date_offer = due_date_offer
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

    def __repr__(self):
        return f"{self.id}:{self.customer_name_offer}"
        

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

class BankDetails(db.Model):
    __tablename__ = "BankDetails"

    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String())
    supplier_role = db.Column(db.String())
    supplier_contact_no = db.Column(db.String())
    suppliers_gstin_number = db.Column(db.String())
    suppliers_pan_number = db.Column(db.String())
    suppliers_hsn_code = db.Column(db.String())
    suppliers_state_code = db.Column(db.String())
    suppliers_bank = db.Column(db.String())
    suppliers_account_no = db.Column(db.String())
    suppliers_ifsc_code = db.Column(db.String())
    nature_of_account = db.Column(db.String())

    def __init__(self, supplier_name,supplier_role, supplier_contact_no, suppliers_gstin_number, suppliers_pan_number, suppliers_hsn_code,
                 suppliers_state_code, suppliers_bank, suppliers_account_no,
                 suppliers_ifsc_code, nature_of_account):
        self.supplier_name = supplier_name
        self.supplier_role = supplier_role
        self.supplier_contact_no = supplier_contact_no
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
            supplier_name = "name",
            supplier_role = "role",
            supplier_contact_no = "contact no",
            suppliers_gstin_number="GSTN NUMBER",
            suppliers_pan_number="PAN NUMBER",
            suppliers_hsn_code="HSN NUMBER",
            suppliers_state_code="STATE CODE",
            suppliers_bank="SUPPLIER BANK",
            suppliers_account_no="ACCOUNT NUMBER",
            suppliers_ifsc_code="IFSC CODE",
            nature_of_account="ACCOUNT TYPE"
        )
        db.session.add(bank_detail)
        db.session.commit()

@db.event.listens_for(BankDetails.__table__, 'after_create')
def create_bank_details(*args, **kwargs):
    BankDetails.create_bank_details()

