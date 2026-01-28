# app/routes/main.py
from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.contact_agent import send_admin_notification, send_user_confirmation

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("home.html")


@main_bp.route("/about")
def about():
    return render_template("about_us.html")


@main_bp.route("/contact", methods=['GET', 'POST'])
def contact():
    try:
        print(0)
    except print(0):
        pass
    
    if request.method == 'POST':
        print(request.form)
        
        try:
            # Get form data
            name    = request.form['name'] #.data
            email   = request.form['email']    #.data
            company = request.form['company']  #.data or 'Not provided'
            service = request.form['service']  #.data or 'Not specified'
            message = request.form['message']  #.data
            
            # Get user IP address
            ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            
            print(ip_address, name, email, company, service, message)
            # Save to database (if using SQLAlchemy)
            """
            contact = Contact(
                name=name,
                email=email,
                company=company,
                service=service,
                message=message,
                ip_address=ip_address
            )
            db.session.add(contact)
            db.session.commit()
            """
            
            # Send email notification to admin
            send_admin_notification(ip_address, name, email, company, service, message)
            
            # Send confirmation email to user
            #send_user_confirmation(name, email)
            
            # Flash success message
            flash('Thank you for your message! We will get back to you within 24 hours.', 'success')
            
            # Redirect to contact page to prevent form resubmission
            return redirect(url_for('main.contact'))
        except Exception as e:
            # Log the error (use proper logging in production)
            print(f"Error processing contact form: {str(e)}")
            flash('There was an error submitting your message. Please try again or contact us directly.', 'error')
 
        
    return render_template("contact_us.html")
