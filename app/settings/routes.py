from flask import (flash, redirect, url_for, render_template, request,
                   current_app)
from flask_login import current_user, login_required
from flask_wtf.csrf import CSRFError


from app.settings import bp
from app.models import Approved_Sender, User, update_user_last_action, Event
from app.settings.forms import AddApprovedSenderForm
from app.auth.forms import UpdateAccountForm, UpdatePasswordForm, UpdateEmailForm
from app.settings.email import send_email_verification
from app import db

from datetime import datetime, timedelta


# ############################### #
# ##     Account settings      ## #
# ############################### #

@bp.route('/settings/account', methods=['GET', 'POST'])
@login_required
@bp.errorhandler(CSRFError)
def settings_account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        print('something')
        flash('Settings updated!', 'success')
        name = form.firstname.data
        username = form.username.data

        current_user.firstname = name
        current_user.username = username
        db.session.commit()


    u = {
        'username': current_user.username if current_user.username else current_user.email,
        'name': current_user.firstname if current_user.firstname else None,
        'email': current_user.email
    }
    print(u)

    # return render_template('settings.html',form=form, senders=approved_senders)
    return render_template('settings/settings_account.html', form=form, u=u)


@bp.route('/settings/account/password', methods=['GET', 'POST'])
@login_required
@bp.errorhandler(CSRFError)
def update_password():
    form = UpdatePasswordForm()
    pw = False
    if current_user.password_hash:
        pw = True

    if form.validate_on_submit():
        new = form.new_password.data
        if pw:
            curr = form.current_password.data
            if current_user.check_password(curr):
                current_user.set_password(new)
            else:
                flash('Current password is incorrect', 'error')
                #return redirect(url_for('settings.update_password'))
                return render_template('settings/settings_password.html', form=form, pw=pw)
        else:
            current_user.set_password(new) 
        
        flash('Password Set!', 'success')
        db.session.commit() 

        return redirect(url_for('settings.settings_account'))
    
    return render_template('settings/settings_password.html', form=form, pw=pw)

@bp.route('/settings/account/email', methods=['GET', 'POST'])
@login_required
@bp.errorhandler(CSRFError)
def update_email():
    form = UpdateEmailForm()
    
    if form.validate_on_submit():
        if form.validate_on_submit():
            send_email_verification(current_user, form.email.data)
            flash('Please check your email for a verification link', 'success')

        # return redirect(url_for('settings.update_email'))
    
    return render_template('settings/settings_account_email.html', form=form)


@bp.route('/settings/verify_email/<token>/<email>', methods=['GET', 'POST'])
def verify_email(token, email):
    user = User.verify_reset_password_token(token)
    if user:
        if user.username == user.email:
            user.username = email
        user.email = email
        db.session.commit()
        flash('Your email has been updated!', 'success')
        return redirect(url_for('settings.settings_account'))




# ############################# #
# ##     email settings      ## #
# ############################# #

@bp.route('/settings/content', methods=['GET', 'POST'])
@login_required
@bp.errorhandler(CSRFError)
def settings_content():
    approved_senders = Approved_Sender.query.filter_by(user_id=current_user.id
                                                       ).all()
    form = AddApprovedSenderForm()

    if form.validate_on_submit():
        email = form.email.data
        update_user_last_action('added approved sender')
        print('adding approved sender:')
        print(email)
        email = email.lower()
        print(email)
        e = Approved_Sender(user_id=current_user.id, email=email)
        db.session.add(e)

        ev = Event(user_id=current_user.id, name='added approved sender', date=datetime.utcnow())
        db.session.add(ev)

        db.session.commit()
        approved_senders = Approved_Sender.query.filter_by(user_id=current_user.id
                                                       ).all()

        # return redirect(url_for('settings.settings_content'))
        
    # return render_template('settings.html',form=form, senders=approved_senders)
    return render_template('settings/settings_content.html',form=form, senders=approved_senders)

@bp.route('/enable-add-by-email', methods=['POST'])
@login_required
@bp.errorhandler(CSRFError)
def enable_add_by_email():
    current_user.set_lurnby_email()
    update_user_last_action('enabled add by email')
    e = Approved_Sender(user_id=current_user.id, email=current_user.email)
    db.session.add(e)
    ev = Event(user_id=current_user.id, name='enabled add by email', date=datetime.utcnow())
    db.session.add(ev)
    
    db.session.commit()

    return '', 200