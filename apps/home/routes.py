import imp
import json
from re import U
from apps.home import blueprint
from flask import render_template, request, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps import db
from apps.home.forms import CreateUserForm
from apps.home.models import UserModel
from apps.home.models import commonconfig
from apps.home.models import MainUser
from apps.home.models import ProductMaster
from apps.home.models import CustomerMaster
from apps.home.models import ManualUser


@blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html', segment='dashboard')


@blueprint.route('/offer-addoffer', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        users = CustomerMaster.query.all()
        return render_template('home/add-offer.html',users=users,segment='offer-addoffer')
    if request.method == 'POST':
        usr_id = request.form['usr_id']
        usr_name = request.form['usr_name']
        usr_password = request.form['usr_password']
        usr_api_key = request.form['usr_api_key']
        usr_api_secret_key = request.form['usr_api_secret_key']
        usr_totp_key = request.form['usr_totp_key']
        usr_access_key = ""
        usr_access_key_time = ""
        usr_autologin_status = request.form['usr_autologin_status']
        usr_autoverify_status = ""
        usr_autologin = ""
        usr_autologout_status = ""
        usr_aut_prem_to_sell_nifty = ""
        usr_aut_prem_to_sell_bank = ""
        usr_aut_stike_to_buy_nifty = ""
        usr_aut_stike_to_buy_bank = ""
        usr_man_odr_1buy_nifty = ""
        usr_man_odr_2sell_nifty = ""
        usr_man_odr_1buy_bank = ""
        usr_man_odr_2sell_bank = ""
        usr_funds_not_to_use = ""
        usr_max_qty = ""
        usr_disp_open_post = ""
        usr_disp_net_day = ""
        usr_disp_funds_avil = ""

        # else we can create the user
        user = UserModel(usr_id=usr_id,
            usr_name=usr_name,
            usr_password=usr_password,
            usr_api_key=usr_api_key,
            usr_api_secret_key=usr_api_secret_key,
            usr_totp_key=usr_totp_key,
            usr_access_key=usr_access_key,
            usr_access_key_time=usr_access_key_time,
            usr_autologin_status=usr_autologin_status,
            usr_autoverify_status=usr_autoverify_status,
            usr_autologin=usr_autologin,
            usr_autologout_status = usr_autologout_status,
            usr_aut_prem_to_sell_nifty = usr_aut_prem_to_sell_nifty,
            usr_aut_prem_to_sell_bank = usr_aut_prem_to_sell_bank,
            usr_aut_stike_to_buy_nifty = usr_aut_stike_to_buy_nifty,
            usr_aut_stike_to_buy_bank = usr_aut_stike_to_buy_bank,
            usr_man_odr_1buy_nifty = usr_man_odr_1buy_nifty,
            usr_man_odr_2sell_nifty =usr_man_odr_2sell_nifty,
            usr_man_odr_1buy_bank = usr_man_odr_1buy_bank,
            usr_man_odr_2sell_bank = usr_man_odr_2sell_bank,
            usr_funds_not_to_use = usr_funds_not_to_use,
            usr_max_qty = usr_max_qty,
            usr_disp_open_post =usr_disp_open_post,
            usr_disp_net_day = usr_disp_net_day,
            usr_disp_funds_avil = usr_disp_funds_avil )
        db.session.add(user)
        db.session.commit()
        return redirect('/offer-offerlist')


@blueprint.route('/offer-offerlist', methods=['GET', 'POST'])
@login_required
def retrieve_list():
    if MainUser.query.filter_by(id=1).first() == None:
        users = MainUser(
            main_usr_id = "main_usr_id",
            main_usr_name = "main_usr_name")
        db.session.add(users)
        db.session.commit()
    if "main_usr_apply" in request.form:
        all_users = UserModel.query.filter_by(usr_id=request.form.get('main_usr_select')).first()
        main_user = MainUser.query.filter_by(id=1).first()
        if all_users != None:
            main_user.main_usr_id = all_users.usr_id
            main_user.main_usr_name = all_users.usr_name
            db.session.commit()
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


@blueprint.route('/configs-common', methods=['GET', 'POST'])
@login_required
def config():
    if request.method == 'GET': 
        user = commonconfig.query.all()
        if commonconfig.query.filter_by(id=1).first() == None:
            cmn_fetch_autoexpiry = "cmn_fetch_autoexpiry"
            cmn_expiry = "cmn_expiry"
            cmn_autoswitch_premium_nifty = "cmn_autoswitch_premium_nifty"
            cmn_autoswitch_premium_bank = "cmn_autoswitch_premium_bank"
            cmn_max_qty_trade_nifty =  "cmn_max_qty_trade_nifty"
            cmn_max_qty_trade_bank =  "cmn_max_qty_trade_bank"
            cmn_round_nifty = "cmn_round_nifty"
            cmn_round_bank = "cmn_round_bank"
            cmn_max_strike_prices_nifty = "cmn_max_strike_prices_nifty"
            cmn_max_strike_prices_bank = "cmn_max_strike_prices_bank"
            cmn_set_strike = "cmn_set_strike"


            users = commonconfig(
            cmn_fetch_autoexpiry = cmn_fetch_autoexpiry,
            cmn_expiry = cmn_expiry,
            cmn_autoswitch_premium_nifty = cmn_autoswitch_premium_nifty,
            cmn_autoswitch_premium_bank = cmn_autoswitch_premium_bank,
            cmn_max_qty_trade_nifty =  cmn_max_qty_trade_nifty,
            cmn_max_qty_trade_bank =  cmn_max_qty_trade_bank,
            cmn_round_nifty = cmn_round_nifty,
            cmn_round_bank = cmn_round_bank,
            cmn_max_strike_prices_nifty = cmn_max_strike_prices_nifty,
            cmn_max_strike_prices_bank = cmn_max_strike_prices_bank,
            cmn_set_strike = cmn_set_strike
            )
            db.session.add(users)
            db.session.commit()
        return render_template('home/common-configs.html', users=user, segment='configs-common')
    if request.method == 'POST':
        users5 = commonconfig.query.filter_by(id=1).first()

        if "btn_cmn_fetch_autoexpiry_at_autologin_apply" in request.form:
            users5.cmn_fetch_autoexpiry = request.form['cmn_fetch_autoexpiry']
        if "btn_cmn_expiry_apply" in request.form:
            users5.cmn_expiry = request.form['cmn_expiry']
        if "btn_cmn_autoswitch_premium_apply" in request.form:
            users5.cmn_autoswitch_premium_nifty = request.form['cmn_autoswitch_premium_nifty']
            users5.cmn_autoswitch_premium_bank = request.form['cmn_autoswitch_premium_bank']
        if "btn_cmn_max_qty_trade_apply" in request.form:
            users5.cmn_max_qty_trade_nifty =  request.form['cmn_max_qty_trade_nifty']
            users5.cmn_max_qty_trade_bank =  request.form['cmn_max_qty_trade_bank']
        if "btn_cmn_round_max_strike_prices_apply" in request.form:
            users5.cmn_round_nifty =  request.form['cmn_round_nifty']
            users5.cmn_round_bank =  request.form['cmn_round_bank']
            users5.cmn_max_strike_prices_nifty =  request.form['cmn_max_strike_prices_nifty']
            users5.cmn_max_strike_prices_bank =  request.form['cmn_max_strike_prices_bank']


        db.session.commit()   
        return redirect('/configs-common')

    

@blueprint.route('/configs-users', methods=['GET', 'POST'])
@login_required
def running_config():
    if request.method == 'GET':
        users = UserModel.query.all()
        data = commonconfig.query.filter_by(id=1).first()
        return render_template('home/user-configs.html', data=data.cmn_set_strike, users=users, segment='configs-users')
    if request.method == 'POST':
        if "btn_usr_aut_apply" in request.form:
            users5 = UserModel.query.filter_by(usr_id=request.form['btn_usr_aut_apply']).first()
            users5.usr_aut_prem_to_sell_nifty = request.form['usr_aut_prem_to_sell_nifty'+str(users5.usr_id)]
            users5.usr_aut_prem_to_sell_bank = request.form['usr_aut_prem_to_sell_bank'+str(users5.usr_id)]
            users5.usr_aut_stike_to_buy_nifty = request.form['usr_aut_stike_to_buy_nifty'+str(users5.usr_id)]
            users5.usr_aut_stike_to_buy_bank =  request.form['usr_aut_stike_to_buy_bank'+str(users5.usr_id)]
            db.session.commit()   
        if "btn_usr_man_apply" in request.form:
            users5 = UserModel.query.filter_by(usr_id=request.form['btn_usr_man_apply']).first()
            users5.usr_man_odr_1buy_nifty = request.form['usr_man_odr_1buy_nifty'+str(users5.usr_id)]
            users5.usr_man_odr_2sell_nifty = request.form['usr_man_odr_2sell_nifty'+str(users5.usr_id)]
            users5.usr_man_odr_1buy_bank = request.form['usr_man_odr_1buy_bank'+str(users5.usr_id)]
            users5.usr_man_odr_2sell_bank =  request.form['usr_man_odr_2sell_bank'+str(users5.usr_id)]
            db.session.commit()  
        if "btn_usr_oth_apply" in request.form:
            users5 = UserModel.query.filter_by(usr_id=request.form['btn_usr_oth_apply']).first()
            users5.usr_funds_not_to_use = request.form['usr_funds_not_to_use'+str(users5.usr_id)]
            users5.usr_max_qty = request.form['usr_max_qty'+str(users5.usr_id)]
            db.session.commit()  
        if "btn_cmn_set_strike_apply" in request.form:
            users5 = commonconfig.query.filter_by(id=1).first()
            users5.cmn_set_strike = request.form['cmn_set_strike']
            db.session.commit()  
        if "btn_usr_aut_apply_all" in request.form:
            users = UserModel.query.all()
            for i in range(1, len(users)+1):
                users5 = UserModel.query.filter_by(id=i).first()
                users5.usr_aut_prem_to_sell_nifty = request.form['usr_aut_prem_to_sell_nifty'+str(users5.usr_id)]
                users5.usr_aut_prem_to_sell_bank = request.form['usr_aut_prem_to_sell_bank'+str(users5.usr_id)]
                users5.usr_aut_stike_to_buy_nifty = request.form['usr_aut_stike_to_buy_nifty'+str(users5.usr_id)]
                users5.usr_aut_stike_to_buy_bank =  request.form['usr_aut_stike_to_buy_bank'+str(users5.usr_id)]
                db.session.commit()  
                
        if "btn_usr_man_apply_all" in request.form:
            users = UserModel.query.all()
            for i in range(1, len(users)+1):
                users5 = UserModel.query.filter_by(id=i).first()
                users5.usr_man_odr_1buy_nifty = request.form['usr_man_odr_1buy_nifty'+str(users5.usr_id)]
                users5.usr_man_odr_2sell_nifty = request.form['usr_man_odr_2sell_nifty'+str(users5.usr_id)]
                users5.usr_man_odr_1buy_bank = request.form['usr_man_odr_1buy_bank'+str(users5.usr_id)]
                users5.usr_man_odr_2sell_bank =  request.form['usr_man_odr_2sell_bank'+str(users5.usr_id)]
                db.session.commit()

        if "btn_usr_oth_apply_all" in request.form:
            users = UserModel.query.all()
            for i in range(1, len(users)+1):
                users5 = UserModel.query.filter_by(id=i).first()
                users5.usr_funds_not_to_use = request.form['usr_funds_not_to_use'+str(users5.usr_id)]
                users5.usr_max_qty = request.form['usr_max_qty'+str(users5.usr_id)]
                db.session.commit() 

        return redirect('/configs-users')


@blueprint.route('/trade-close')
@login_required
def switch():
    users = UserModel.query.all()
    return render_template('home/close-trade.html', users=users, segment='trade-close')


@blueprint.route('/trade-manual', methods=['GET', 'POST'])
@login_required
def close():
    if request.method == 'GET':
        users = UserModel.query.all()
        manualuser = ManualUser.query.filter_by(id=1).first()
        return render_template('home/manual-trade.html', users=users, manualuser=manualuser,  segment='trade-manual')

    if request.method == 'POST':
        if ManualUser.query.filter_by(id=1).first() == None:
            users = ManualUser(
                man_opt_usr_id = "man_opt_usr_id",
                man_opt_nam = "man_opt_nam",
                man_opt_expiry = "man_opt_expiry",
                man_opt_mis_nrml = "man_opt_mis_nrml",
                man_opt_buy_1_ord = "man_opt_buy_1_ord",
                man_opt_sell_2_ord = "man_opt_sell_2_ord",
                man_opt_buy_PECE = "man_opt_buy_PECE",
                man_opt_sell_PECE = "man_opt_sell_PECE",
                man_opt_qty_buy = "man_opt_qty_buy",
                man_opt_qty_sell = "man_opt_qty_sell",
                man_opt_nif_banknif = "man_opt_nif_banknif",
                man_usr_id = "man_usr_id",
                man_name = "man_name",
                man_symb = "man_symb",
                man_qty = "man_qty",
                man_buysell = "man_buysell",
                man_mis_nrml = "man_mis_nrml"
    )
            db.session.add(users)
            db.session.commit()
        if "man_opt_drpdwn_apply" in request.form:
            all_users = UserModel.query.filter_by(usr_id=request.form.get('man_opt_drpdwn')).first()
            manualuser = ManualUser.query.filter_by(id=1).first()
            if all_users != None:
                manualuser.man_opt_usr_id = all_users.usr_id
                manualuser.man_opt_nam = all_users.usr_name
                db.session.commit()
        if "man_drpdwn_apply" in request.form:
            all_users = UserModel.query.filter_by(usr_id=request.form.get('man_drpdwn')).first()
            manualuser = ManualUser.query.filter_by(id=1).first()
            if all_users != None:
                manualuser.man_usr_id = all_users.usr_id
                manualuser.man_name = all_users.usr_name
                db.session.commit()
        if "btn_man_opt_apply" in request.form:
            manualuser = ManualUser.query.filter_by(id=1).first()
            manualuser.man_opt_expiry = request.form['man_opt_expiry']
            manualuser.man_opt_nif_banknif = request.form['man_opt_nif_banknif']
            manualuser.man_opt_mis_nrml = request.form['man_opt_mis_nrml']
            manualuser.man_opt_buy_1_ord = request.form['man_opt_buy_1_ord']
            manualuser.man_opt_buy_PECE = request.form['man_opt_buy_PECE']
            manualuser.man_opt_qty_buy = request.form['man_opt_qty_buy']
            manualuser.man_opt_sell_2_ord = request.form['man_opt_sell_2_ord']
            manualuser.man_opt_sell_PECE = request.form['man_opt_sell_PECE']
            manualuser.man_opt_qty_sell = request.form['man_opt_qty_sell']
            db.session.commit()  
        if "btn_man_apply" in request.form:
            manualuser = ManualUser.query.filter_by(id=1).first()
            manualuser.man_symb = request.form['man_symb']
            manualuser.man_qty = request.form['man_qty']
            manualuser.man_buysell = request.form['man_buysell']
            manualuser.man_mis_nrml = request.form['man_mis_nrml']
            db.session.commit() 
        if "man_opt_select_all_user" in request.form:
            manualuser = ManualUser.query.filter_by(id=1).first()
            manualuser.man_opt_usr_id = "ALL"
            manualuser.man_opt_nam = "ALL"
            db.session.commit() 
        if "man_select_all_user" in request.form:
            manualuser = ManualUser.query.filter_by(id=1).first()
            manualuser.man_usr_id = "ALL"
            manualuser.man_name = "ALL"
            db.session.commit() 
        if "btn_man_opt_plc_odr" in request.form:
            manualuser = ManualUser.query.filter_by(id=1).first()
            print("Details")
            print(manualuser.man_opt_expiry)
            print(manualuser.man_opt_nif_banknif)
            print(manualuser.man_opt_mis_nrml)
            print(manualuser.man_opt_buy_1_ord)
            print(manualuser.man_opt_buy_PECE)
            print(manualuser.man_opt_qty_buy)
            print(manualuser.man_opt_sell_2_ord)
            print(manualuser.man_opt_sell_PECE)
            print(manualuser.man_opt_qty_sell)
        if "btn_man_plc_odr" in request.form:
            manualuser = ManualUser.query.filter_by(id=1).first()
            print("Details")
            print(manualuser.man_usr_id)
            print(manualuser.man_name)
            print(manualuser.man_symb)
            print(manualuser.man_qty)
            print(manualuser.man_buysell)
            print(manualuser.man_mis_nrml)
        return redirect('/trade-manual')

@blueprint.route('/print_data', methods=['POST'])
@login_required
def print_data():
    userinfo=request.get_json()
    print()
    print()
    print(userinfo)
    print()
    print()
    return str(userinfo)


@blueprint.route('/trade-switch')
@login_required
def balance():
    users = UserModel.query.all()
    return render_template('home/switch-trade.html', users=users, segment='trade-switch')


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
