from apps import db

class UserModel(db.Model):
    __tablename__ = "use"

    id = db.Column(db.Integer, primary_key=True)
    usr_id = db.Column(db.String())
    usr_name = db.Column(db.String())
    usr_password = db.Column(db.String())
    usr_api_key = db.Column(db.String())
    usr_api_secret_key = db.Column(db.String())
    usr_totp_key = db.Column(db.String())
    usr_access_key = db.Column(db.String())
    usr_access_key_time = db.Column(db.String())
    usr_autologin_status = db.Column(db.String(80))
    usr_autologin = db.Column(db.String(80))
    usr_autoverify_status = db.Column(db.String(80))
    usr_autologout_status = db.Column(db.String(80))
    usr_aut_prem_to_sell_nifty = db.Column(db.String())
    usr_aut_prem_to_sell_bank = db.Column(db.String())
    usr_aut_stike_to_buy_nifty = db.Column(db.String())
    usr_aut_stike_to_buy_bank = db.Column(db.String())
    usr_man_odr_1buy_nifty = db.Column(db.String())
    usr_man_odr_2sell_nifty = db.Column(db.String())
    usr_man_odr_1buy_bank = db.Column(db.String())
    usr_man_odr_2sell_bank = db.Column(db.String())
    usr_funds_not_to_use = db.Column(db.String())
    usr_max_qty = db.Column(db.String())
    usr_disp_open_post = db.Column(db.String())
    usr_disp_net_day = db.Column(db.String())
    usr_disp_funds_avil = db.Column(db.String())

    def __init__(self, usr_id, usr_name, usr_password, usr_api_key, usr_api_secret_key, usr_totp_key, usr_access_key,
                 usr_access_key_time, usr_autologin_status, usr_autologin, usr_autoverify_status, usr_autologout_status,
                 usr_aut_prem_to_sell_nifty, usr_aut_prem_to_sell_bank, usr_aut_stike_to_buy_nifty, usr_aut_stike_to_buy_bank,
                 usr_man_odr_1buy_nifty, usr_man_odr_2sell_nifty, usr_man_odr_1buy_bank, usr_man_odr_2sell_bank,
                 usr_funds_not_to_use, usr_max_qty, usr_disp_open_post, usr_disp_net_day, usr_disp_funds_avil):
        self.usr_id = usr_id
        self.usr_name = usr_name
        self.usr_password = usr_password
        self.usr_api_key = usr_api_key
        self.usr_api_secret_key = usr_api_secret_key
        self.usr_totp_key = usr_totp_key
        self.usr_access_key = usr_access_key
        self.usr_access_key_time = usr_access_key_time
        self.usr_autologin_status = usr_autologin_status
        self.usr_autologin = usr_autologin
        self.usr_autoverify_status = usr_autoverify_status
        self.usr_autologout_status = usr_autologout_status
        self.usr_aut_prem_to_sell_nifty = usr_aut_prem_to_sell_nifty
        self.usr_aut_prem_to_sell_bank = usr_aut_prem_to_sell_bank
        self.usr_aut_stike_to_buy_nifty = usr_aut_stike_to_buy_nifty
        self.usr_aut_stike_to_buy_bank = usr_aut_stike_to_buy_bank
        self.usr_man_odr_1buy_nifty = usr_man_odr_1buy_nifty
        self.usr_man_odr_2sell_nifty = usr_man_odr_2sell_nifty
        self.usr_man_odr_1buy_bank = usr_man_odr_1buy_bank
        self.usr_man_odr_2sell_bank = usr_man_odr_2sell_bank
        self.usr_funds_not_to_use = usr_funds_not_to_use
        self.usr_max_qty = usr_max_qty
        self.usr_disp_open_post = usr_disp_open_post
        self.usr_disp_net_day = usr_disp_net_day
        self.usr_disp_funds_avil = usr_disp_funds_avil
        

    def __repr__(self):
        return f"{self.usr_id}:{self.usr_name}"



class commonconfig(db.Model):
    __tablename__ = "commonconfig"

    id = db.Column(db.Integer, primary_key=True)
    cmn_fetch_autoexpiry = db.Column(db.String(80))
    cmn_expiry = db.Column(db.String(80))
    cmn_autoswitch_premium_nifty = db.Column(db.String(80))
    cmn_autoswitch_premium_bank = db.Column(db.String(80))
    cmn_max_qty_trade_nifty = db.Column(db.String(80))
    cmn_max_qty_trade_bank = db.Column(db.String(80))
    cmn_round_nifty = db.Column(db.String(80))
    cmn_round_bank = db.Column(db.String(80))
    cmn_max_strike_prices_nifty = db.Column(db.String(80))
    cmn_max_strike_prices_bank = db.Column(db.String(80))
    cmn_set_strike = db.Column(db.String(80))

    def __init__(self, cmn_fetch_autoexpiry, cmn_expiry, cmn_autoswitch_premium_nifty, cmn_autoswitch_premium_bank,cmn_max_qty_trade_nifty, 
    cmn_max_qty_trade_bank,cmn_round_nifty,cmn_round_bank, 
        cmn_max_strike_prices_nifty,cmn_max_strike_prices_bank, cmn_set_strike,):
        self.cmn_fetch_autoexpiry = cmn_fetch_autoexpiry
        self.cmn_expiry = cmn_expiry
        self.cmn_autoswitch_premium_nifty = cmn_autoswitch_premium_nifty
        self.cmn_autoswitch_premium_bank = cmn_autoswitch_premium_bank
        self.cmn_max_qty_trade_nifty = cmn_max_qty_trade_nifty
        self.cmn_max_qty_trade_bank = cmn_max_qty_trade_bank
        self.cmn_round_nifty = cmn_round_nifty
        self.cmn_round_bank = cmn_round_bank
        self.cmn_max_strike_prices_nifty = cmn_max_strike_prices_nifty
        self.cmn_max_strike_prices_bank = cmn_max_strike_prices_bank
        self.cmn_set_strike = cmn_set_strike
        

    def __repr__(self):
        return f"{self.cmn_fetch_autoexpiry}:{self.cmn_expiry}"


class MainUser(db.Model):
    __tablename__ = "mainuser"

    id = db.Column(db.Integer, primary_key=True)
    main_usr_id = db.Column(db.String())
    main_usr_name = db.Column(db.String())


    def __init__(self, main_usr_id, main_usr_name):
        self.main_usr_id = main_usr_id
        self.main_usr_name = main_usr_name
    def __repr__(self):
        return f"{self.main_usr_id}:{self.main_usr_name}"

class ManualUser(db.Model):
    __tablename__ = "manualuser"

    id = db.Column(db.Integer, primary_key=True)
    man_opt_usr_id = db.Column(db.String())
    man_opt_nam = db.Column(db.String())
    man_opt_expiry = db.Column(db.String())
    man_opt_mis_nrml = db.Column(db.String())
    man_opt_buy_1_ord = db.Column(db.INT())
    man_opt_sell_2_ord = db.Column(db.INT())
    man_opt_buy_PECE = db.Column(db.INT())
    man_opt_sell_PECE = db.Column(db.INT())
    man_opt_qty_buy = db.Column(db.INT())
    man_opt_qty_sell = db.Column(db.INT())
    man_opt_nif_banknif = db.Column(db.String())
    man_usr_id = db.Column(db.String())
    man_name = db.Column(db.String())
    man_symb = db.Column(db.String())
    man_qty = db.Column(db.INT())
    man_buysell = db.Column(db.String())
    man_mis_nrml = db.Column(db.String())

    def __init__(self, man_opt_usr_id, man_opt_nam, man_opt_expiry, man_opt_mis_nrml, man_opt_buy_1_ord,
    man_opt_sell_2_ord, man_opt_buy_PECE, man_opt_sell_PECE, man_opt_qty_buy, man_opt_qty_sell, man_opt_nif_banknif,
    man_usr_id, man_name, man_symb,man_qty, man_buysell, man_mis_nrml ):
        self.man_opt_usr_id = man_opt_usr_id
        self.man_opt_nam = man_opt_nam
        self.man_opt_expiry = man_opt_expiry
        self.man_opt_mis_nrml = man_opt_mis_nrml
        self.man_opt_buy_1_ord = man_opt_buy_1_ord
        self.man_opt_sell_2_ord = man_opt_sell_2_ord
        self.man_opt_buy_PECE = man_opt_buy_PECE
        self.man_opt_sell_PECE = man_opt_sell_PECE
        self.man_opt_qty_buy = man_opt_qty_buy
        self.man_opt_qty_sell = man_opt_qty_sell
        self.man_opt_nif_banknif = man_opt_nif_banknif
        self.man_usr_id = man_usr_id
        self.man_name = man_name
        self.man_symb = man_symb
        self.man_qty = man_qty
        self.man_buysell = man_buysell
        self.man_mis_nrml = man_mis_nrml

    def __repr__(self):
        return f"{self.man_opt_usr_id}:{self.man_opt_nam}"

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


