logo = "assets/logo.png"
import streamlit as st
st.markdown("""
    <style>
        /* Sidebar background */
        [data-testid="stSidebar"] {
            background-color: #1E1E2F;
        }

        /* Sidebar text */
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Main background */
        .main {
            background-color: #F5F6FA;
        }

        /* Titles */
        h1, h2, h3 {
            color: #1E1E2F;
        }

        /* Buttons */
        .stButton>button {
            background-color: #1E1E2F;
            color: white;
            border-radius: 5px;
            padding: 8px 20px;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

from modules.auth import register_company, login_company
from modules.employees import add_employee, get_employees, delete_employee
from modules.attendance import check_in, check_out, get_attendance
from modules.payroll import calculate_payroll, get_payroll, payroll_to_excel
from modules.reports import attendance_summary, payroll_summary, employee_statistics

# ---------------------- GLOBAL STYLING ----------------------
st.markdown("""
    <style>
        /* MAIN BACKGROUND */
        .main {
            background-color: #F7F8FC;
        }

        /* SIDEBAR */
        [data-testid="stSidebar"] {
            background-color: #0A0F1F;
        }

        /* SIDEBAR TEXT */
        [data-testid="stSidebar"] * {
            color: #D4AF37 !important;
        }

        /* TITLES */
        h1, h2, h3 {
            color: #0A0F1F;
        }

        /* METRIC CARDS */
        div[data-testid="metric-container"] {
            background-color: white;
            border: 1px solid #E0E0E0;
            padding: 20px;
            border-radius: 10px;
        }

        /* BUTTONS */
        .stButton>button {
            background-color: #0A0F1F;
            color: #D4AF37;
            border-radius: 6px;
            padding: 10px 20px;
            border: 1px solid #D4AF37;
            font-weight: bold;
        }

        .stButton>button:hover {
            background-color: #D4AF37;
            color: #0A0F1F;
            border: 1px solid #0A0F1F;
        }

        /* DIVIDER SPACING */
        .block-container {
            padding-top: 20px;
        }
   st.markdown("""
<style>

/* SIDEBAR MENU ITEMS */
[data-testid="stSidebar"] .css-1d391kg,
[data-testid="stSidebar"] .css-1n76uvr {
    color: #D4AF37 !important; /* Golden when active */
    font-weight: bold;
}

/* HOVER EFFECT */
[data-testid="stSidebar"] .css-1d391kg:hover,
[data-testid="stSidebar"] .css-1n76uvr:hover {
    color: #0A0F1F !important; /* Blue-Black on hover */
    background-color: #D4AF37 !important; /* Golden background */
    border-radius: 6px;
    padding-left: 10px;
    transition: 0.2s ease-in-out;
}

/* UNSELECTED MENU ITEMS */
[data-testid="stSidebar"] .css-1n76uvr {
    color: white !important; /* White when not active */
}

</style>
""", unsafe_allow_html=True)


/* HOVER EFFECT */
[data-testid="stSidebar"] .css-1d391kg:hover,
[data-testid="stSidebar"] .css-1n76uvr:hover {
    color: #0A0F1F !important; /* Blue-Black on hover */
    background-color: #D4AF37 !important; /* Golden background */
    border-radius: 6px;
    padding-left: 10px;
    transition: 0.2s ease-in-out;
}

/* UNSELECTED MENU ITEMS */
[data-testid="stSidebar"] .css-1n76uvr {
    color: white !important; /* White when not active */
}
/* CARD STYLE (Soft Rounded) */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
    margin-bottom: 20px;
    border: 1px solid #E5E5E5;
}

/* SECTION HEADER */
.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #0A0F1F;
    margin-bottom: 10px;
}

/* TABLE STYLING */
table {
    border-radius: 10px;
    overflow: hidden;
}

thead tr {
    background-color: #0A0F1F !important;
    color: #D4AF37 !important;
}

tbody tr:nth-child(even) {
    background-color: #F2F2F2 !important;
}


# ---------------------- SESSION STATE ----------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "company_id" not in st.session_state:
    st.session_state.company_id = None


# ---------------------- LOGIN PAGE ----------------------
def show_login():
    st.markdown("<h1 style='text-align:center; color:#1E1E2F;'>Welcome Back</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:gray;'>Login to your company dashboard</p>", unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        company = login_company(email, password)
        if company:
            st.session_state.logged_in = True
            st.session_state.company_id = company.company_id
            st.success("Login successful")
        else:
            st.error("Invalid email or password")


# ---------------------- SIGNUP PAGE ----------------------
def show_signup():
    st.markdown("<h1 style='text-align:center; color:#1E1E2F;'>Create Your Company Account</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:gray;'>Register your business to get started</p>", unsafe_allow_html=True)

    company_name = st.text_input("Company Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        register_company(company_name, email, password)
        st.success("Account created successfully. You can now log in.")


# ---------------------- EMPLOYEE PAGE ----------------------
def employee_page():
    st.title("Employee Management")

    st.subheader("Add New Employee")
    full_name = st.text_input("Full Name")
    position = st.text_input("Position")
    department = st.text_input("Department")
    salary = st.number_input("Salary", min_value=0.0)

    if st.button("Add Employee"):
        add_employee(st.session_state.company_id, full_name, position, department, salary)
        st.success("Employee added successfully")

    st.subheader("Employee List")
    employees = get_employees(st.session_state.company_id)

    for emp in employees:
        st.write(f"**{emp.full_name}** — {emp.position} — {emp.department} — Salary: {emp.salary}")
        if st.button(f"Delete {emp.employee_id}"):
            delete_employee(emp.employee_id)
            st.warning("Employee deleted")
            st.experimental_rerun()


# ---------------------- ATTENDANCE PAGE ----------------------
def attendance_page():
    st.title("Attendance System")

    employees = get_employees(st.session_state.company_id)
    emp_names = {e.full_name: e.employee_id for e in employees}

    st.subheader("Record Attendance")
    selected_emp = st.selectbox("Select Employee", list(emp_names.keys()))

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Check In"):
            msg = check_in(emp_names[selected_emp])
            st.info(msg)

    with col2:
        if st.button("Check Out"):
            msg = check_out(emp_names[selected_emp])
            st.info(msg)

    st.subheader("Attendance Records")
    records = get_attendance(st.session_state.company_id)

    for r in records:
        st.write(
            f"Employee ID: {r.employee_id} | Date: {r.date} | "
            f"Check-in: {r.check_in} | Check-out: {r.check_out} | "
            f"Hours: {r.hours_worked} | OT: {r.overtime_hours}"
        )


# ---------------------- PAYROLL PAGE ----------------------
def payroll_page():
    st.title("Payroll System")

    month = st.selectbox("Select Month", list(range(1, 13)))
    year = st.number_input("Year", min_value=2020, max_value=2100, value=2026)

    employees = get_employees(st.session_state.company_id)
    emp_names = {e.full_name: e.employee_id for e in employees}

    st.subheader("Generate Payroll for Employee")
    selected_emp = st.selectbox("Employee", list(emp_names.keys()))

    if st.button("Generate Payroll"):
        calculate_payroll(emp_names[selected_emp], month, year)
        st.success(f"Payroll generated for {selected_emp}")

    st.subheader("Payroll Records")
    records = get_payroll(st.session_state.company_id, month, year)

    for r in records:
        st.write(
            f"Employee ID: {r.employee_id} | Net Salary: {r.net_salary} | "
            f"OT Pay: {r.overtime_pay} | Base: {r.base_salary}"
        )

    if st.button("Export to Excel"):
        df = payroll_to_excel(records)
        st.download_button("Download Payroll Excel", df.to_csv(), "payroll.csv")


def dashboard_page():
    st.title("Dashboard")

    # Subscription info
    status, days_left = get_subscription_status(st.session_state.company_id)

    if status == "trial":
        st.info(f"Trial: {days_left} days left")
    elif status == "active":
        st.success(f"Subscription Active — {days_left} days remaining")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Company Overview</div>", unsafe_allow_html=True)

    employees = db.query(Employee).filter_by(company_id=st.session_state.company_id).count()
    attendance = db.query(Attendance).filter_by(company_id=st.session_state.company_id).count()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Employees", employees)

    with col2:
        st.metric("Attendance Records", attendance)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Quick Actions</div>", unsafe_allow_html=True)

    st.button("Add Employee")
    st.button("Record Attendance")

    st.markdown("</div>", unsafe_allow_html=True)

    # Stats
    employees = db.query(Employee).filter_by(company_id=st.session_state.company_id).count()
    attendance = db.query(Attendance).filter_by(company_id=st.session_state.company_id).count()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Employees", employees)

    with col2:
        st.metric("Attendance Records", attendance)

    st.markdown("---")

    st.subheader("Quick Actions")
    st.button("Add Employee")
    st.button("Record Attendance")

def payment_page():
    st.title("Subscription Payment")

    st.subheader("Manual Payment (Bank Transfer / Cash)")

    st.write("Bank Name: Emirates NBD")
    st.write("Account Number: 1234567890")
    st.write("Account Name: Elias Tech Solutions")
    st.write("IBAN: AE12 3456 7890 1234 5678 90")

    st.markdown("---")

    st.subheader("Upload Payment Receipt")
    receipt = st.file_uploader("Upload receipt (jpg, png, pdf)", type=["jpg", "png", "jpeg", "pdf"])

    if receipt:
        st.success("Receipt uploaded! Admin will verify and activate your subscription.")

    st.markdown("---")

    st.subheader("Payment History")
    payments = db.query(Payment).filter_by(company_id=st.session_state.company_id).all()

    for p in payments:
        st.write(f"{p.payment_date} — {p.amount} {p.currency} — {p.payment_method}")
def admin_page():
    st.title("ADMIN PANEL")

    # ----- ADMIN PASSWORD -----
    password = st.text_input("Enter admin password", type="password")

    if password != "Alexans35@#$":
        st.error("Access denied")
        return

    st.warning("This page is for the system owner only.")

    # ----------- VIEW ALL COMPANIES -----------
    st.subheader("All Companies")
    companies = db.query(Company).all()

    for c in companies:
        st.write(f"ID: {c.company_id} | {c.company_name} | {c.email}")

    st.markdown("---")

    # ----------- VIEW SUBSCRIPTIONS -----------
    st.subheader("Subscriptions")
    subs = db.query(Subscription).all()

    for s in subs:
        st.write(
            f"Company {s.company_id} | Status: {s.status} | "
            f"Start: {s.start_date} | End: {s.end_date}"
        )

    st.markdown("---")

    # ----------- MANUAL PAYMENT APPROVAL -----------
    st.subheader("Approve Manual Payments")

    payments = db.query(Payment).filter_by(payment_method="manual").all()

    for p in payments:
        st.write(
            f"Payment ID: {p.payment_id} | Company: {p.company_id} | "
            f"Amount: {p.amount} | Date: {p.payment_date}"
        )

        if st.button(f"Approve Payment {p.payment_id}"):
    sub = db.query(Subscription).filter_by(company_id=p.company_id).first()

    today = datetime.now().date()

    # If expired, reset start date
    if sub.end_date < today:
        sub.start_date = today
        sub.end_date = today + timedelta(days=30)
    else:
        sub.end_date = sub.end_date + timedelta(days=30)

    sub.status = "active"
    db.commit()
    st.success("Subscription extended!")




# ---------------------- SIDEBAR MENU ----------------------
st.sidebar.image("assets/logo.png", width=180)
st.sidebar.markdown("### Payroll & Attendance System")

if not st.session_state.logged_in:
    menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])
else:
st.sidebar.image(logo, use_column_width=True)
st.sidebar.markdown("---")
    menu = st.sidebar.selectbox("Menu", ["Dashboard", "Employees", "Attendance", "Payroll"])


# ---------------------- PAGE ROUTING ----------------------
query_params = st.experimental_get_query_params()

# Admin hidden URL
if "admin" in query_params:
    admin_page()
    st.stop()

if not st.session_state.logged_in:
    if menu == "Login":
        show_login()
    else:
        show_signup()
else:
    # Check subscription status
    status, days_left = get_subscription_status(st.session_state.company_id)

    if status == "expired":
        st.error("Your subscription has expired.")
        st.info("Please go to the Payment page to renew your subscription.")
        payment_page()
	st.stop()
    else:
        if status == "trial":
            st.warning(f"Trial period: {days_left} days left")

        if menu == "Dashboard":
            dashboard_page()
        elif menu == "Employees":
            employee_page()
        elif menu == "Attendance":
            attendance_page()
        elif menu == "Payroll":
            payroll_page()
        elif menu == "Payment":
            payment_page()
	
