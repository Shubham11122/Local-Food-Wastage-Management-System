# import streamlit as st

# from Modules import home
# from Modules import dashboard
# from Modules import browse_food
# from Modules import food_listings
# from Modules import claims
# from Modules import providers
# from Modules import receivers
# from Modules import analytics
# from Modules import sql_insights

# st.set_page_config(
#     page_title="Food Waste Management",
#     page_icon="🍱",
#     layout="wide"
# )

# # =====================
# # SIDEBAR
# # =====================

# with st.sidebar:

#     st.title("🍱 Food Waste")

#     page = st.radio(
#         "Navigation",
#         [
#             "🏠 Home",
#             "📊 Dashboard",
#             "🔍 Browse Food",
#             "🍱 Food Listings",
#             "📋 Claims",
#             "🏢 Providers",
#             "👥 Receivers",
#             "📈 Analytics",
#             "🧠 SQL Insights"
#         ]
#     )

# # =====================
# # ROUTING
# # =====================

# if page == "🏠 Home":
#     home.show()

# elif page == "📊 Dashboard":
#     dashboard.show()

# elif page == "🔍 Browse Food":
#     browse_food.show()

# elif page == "🍱 Food Listings":
#     food_listings.show()

# elif page == "📋 Claims":
#     claims.show()

# elif page == "🏢 Providers":
#     providers.show()

# elif page == "👥 Receivers":
#     receivers.show()

# elif page == "📈 Analytics":
#     analytics.show()

# elif page == "🧠 SQL Insights":
#     sql_insights.show()


import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine, text

# =============================================
# DATABASE CONNECTION
# =============================================

server = r"DESKTOP-BDSN4BM\SQLEXPRESS"
database = "local_food_management"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# =============================================
# PAGE CONFIG
# =============================================

st.set_page_config(
    page_title="Food Waste Management",
    page_icon="🍱",
    layout="wide"
)

# =============================================
# GLOBAL STYLES
# =============================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* ---- Base ---- */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f2027 0%, #1a3a2a 60%, #0f2027 100%);
    border-right: 1px solid #1e4d30;
}

[data-testid="stSidebar"] * {
    color: #e0f2e9 !important;
}

/* Sidebar title */
.sidebar-logo {
    text-align: center;
    padding: 18px 0 10px 0;
    font-size: 28px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #52e09c !important;
    border-bottom: 1px solid #1e4d30;
    margin-bottom: 18px;
}

.sidebar-logo span {
    display: block;
    font-size: 11px;
    font-weight: 400;
    letter-spacing: 2px;
    color: #6bbf8e !important;
    text-transform: uppercase;
    margin-top: 2px;
}

/* Nav buttons */
.nav-btn {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 16px;
    border-radius: 10px;
    cursor: pointer;
    margin-bottom: 4px;
    font-size: 14px;
    font-weight: 500;
    color: #a8d5b5 !important;
    transition: background 0.2s;
    border: none;
    background: transparent;
    width: 100%;
    text-align: left;
}

.nav-btn:hover {
    background: rgba(82,224,156,0.10);
    color: #52e09c !important;
}

.nav-btn.active {
    background: rgba(82,224,156,0.18);
    color: #52e09c !important;
    font-weight: 600;
    border-left: 3px solid #52e09c;
}

.nav-section-label {
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #4a8c66 !important;
    padding: 10px 16px 4px 16px;
    font-weight: 600;
}

/* ---- Main content ---- */
[data-testid="stAppViewContainer"] {
    background: #0d1117;
}

.block-container {
    padding-top: 28px !important;
    padding-bottom: 40px !important;
}

/* ---- Page header ---- */
.page-header {
    background: linear-gradient(90deg, #0f2d1f, #163d28);
    border: 1px solid #1e4d30;
    border-radius: 14px;
    padding: 24px 30px;
    margin-bottom: 24px;
}

.page-header h1 {
    color: #52e09c !important;
    font-size: 26px !important;
    font-weight: 700 !important;
    margin: 0 0 4px 0 !important;
}

.page-header p {
    color: #6bbf8e !important;
    font-size: 14px !important;
    margin: 0 !important;
}

/* ---- KPI cards ---- */
[data-testid="metric-container"] {
    background: #111b14;
    border: 1px solid #1e4d30;
    border-radius: 12px;
    padding: 16px 20px !important;
}

[data-testid="stMetricValue"] {
    color: #52e09c !important;
    font-size: 28px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricLabel"] {
    color: #6bbf8e !important;
    font-size: 13px !important;
}

/* ---- Hero (home) ---- */
.hero-box {
    background: linear-gradient(120deg, #0a2a18 0%, #0f3d22 50%, #0a2a18 100%);
    border: 1px solid #1e4d30;
    border-radius: 18px;
    padding: 48px 40px;
    text-align: center;
    margin-bottom: 28px;
}

.hero-box h1 {
    color: #52e09c !important;
    font-size: 34px !important;
    font-weight: 700 !important;
    margin-bottom: 8px !important;
}

.hero-box p {
    color: #a8d5b5 !important;
    font-size: 16px !important;
    max-width: 600px;
    margin: 0 auto !important;
    line-height: 1.7;
}

/* ---- Feature cards ---- */
.feat-card {
    background: #111b14;
    border: 1px solid #1e4d30;
    border-radius: 14px;
    padding: 24px 20px;
    text-align: center;
    min-height: 160px;
}

.feat-card .icon { font-size: 32px; margin-bottom: 10px; }

.feat-card h4 {
    color: #52e09c !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    margin-bottom: 8px !important;
}

.feat-card p {
    color: #7aba96 !important;
    font-size: 13px !important;
    line-height: 1.6 !important;
}

/* ---- Footer ---- */
.footer-box {
    background: #0d1a11;
    border: 1px solid #1e4d30;
    border-radius: 12px;
    padding: 20px 26px;
    margin-top: 28px;
    color: #6bbf8e !important;
    font-size: 13px;
}

.footer-box b { color: #52e09c !important; }

/* ---- Dataframe ---- */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}

/* ---- Tabs ---- */
[data-testid="stTab"] {
    color: #6bbf8e !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #52e09c !important;
    border-bottom-color: #52e09c !important;
}

/* ---- Forms ---- */
[data-testid="stForm"] {
    background: #111b14;
    border: 1px solid #1e4d30;
    border-radius: 14px;
    padding: 20px !important;
}

/* ---- Divider ---- */
hr {
    border-color: #1e4d30 !important;
}

</style>
""", unsafe_allow_html=True)


# =============================================
# SIDEBAR
# =============================================

NAV_ITEMS = [
    ("🏠", "Home",          "OVERVIEW"),
    ("📊", "Dashboard",     "OVERVIEW"),
    ("🔍", "Browse Food",   "FOOD"),
    ("🍱", "Food Listings", "FOOD"),
    ("📋", "Claims",        "OPERATIONS"),
    ("🏢", "Providers",     "OPERATIONS"),
    ("👥", "Receivers",     "OPERATIONS"),
    ("📈", "Analytics",     "INSIGHTS"),
    ("🧠", "SQL Insights",  "INSIGHTS"),
]

if "page" not in st.session_state:
    st.session_state.page = "Home"

with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        🍱 FoodShare
        <span>Waste Management System</span>
    </div>
    """, unsafe_allow_html=True)

    current_section = None
    for icon, label, section in NAV_ITEMS:
        if section != current_section:
            st.markdown(
                f'<div class="nav-section-label">{section}</div>',
                unsafe_allow_html=True
            )
            current_section = section

        is_active = st.session_state.page == label
        btn_class = "nav-btn active" if is_active else "nav-btn"

        if st.button(
            f"{icon}  {label}",
            key=f"nav_{label}",
            use_container_width=True
        ):
            st.session_state.page = label
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="padding:12px 16px;border-top:1px solid #1e4d30;margin-top:8px;">
        <div style="color:#4a8c66;font-size:11px;letter-spacing:1px;
                    text-transform:uppercase;margin-bottom:6px;">Connected to</div>
        <div style="color:#52e09c;font-size:12px;font-weight:600;">
            🗄️ SQL Server (Local)
        </div>
        <div style="color:#4a8c66;font-size:11px;margin-top:2px;">
            local_food_management
        </div>
    </div>
    """, unsafe_allow_html=True)


page = st.session_state.page


# =============================================
# HELPER
# =============================================

def page_header(title, subtitle=""):
    st.markdown(f"""
    <div class="page-header">
        <h1>{title}</h1>
        {"<p>" + subtitle + "</p>" if subtitle else ""}
    </div>
    """, unsafe_allow_html=True)


# =============================================
# PAGE: HOME
# =============================================

def show_home():
    st.markdown("""
    <div class="hero-box">
        <h1>🍽️ Local Food Wastage Management</h1>
        <p>
            Connecting food providers — restaurants, supermarkets, grocery stores —
            with NGOs, shelters and communities in need.
            Smart redistribution to reduce waste and hunger.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📌 Project Overview")
    st.info("""
    Millions of meals are wasted every day while many people struggle to access food.

    This platform enables food listing, food claiming, claim tracking,
    and analytical reporting to reduce food wastage and connect communities.
    """)

    st.subheader("⚙️ How It Works")
    st.markdown("""
    **Provider → Food Listing → Receiver → Claim → Distribution**

    1. Food Providers list surplus food available for pickup.
    2. Receivers browse available food listings.
    3. Receivers claim food items they need.
    4. Claims are processed and tracked through the platform.
    5. Food gets redistributed instead of wasted.
    """)

    st.subheader("🚀 Core Modules")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="feat-card">
            <div class="icon">♻️</div>
            <h4>Reduce Food Waste</h4>
            <p>Prevent surplus food from being discarded by connecting providers with receivers.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feat-card">
            <div class="icon">🍲</div>
            <h4>Reduce Hunger</h4>
            <p>Help NGOs, shelters and individuals access available food resources in their city.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feat-card">
            <div class="icon">🚚</div>
            <h4>Improve Distribution</h4>
            <p>Create an efficient food redistribution network through digital tracking.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.subheader("🎯 Business Objectives")
    c1, c2 = st.columns(2)
    with c1:
        st.success("**Reduce Food Waste** — Identify and redistribute surplus food before it expires.")
    with c2:
        st.success("**Reduce Hunger** — Connect available food resources with communities in need.")

    st.markdown("""
    <div class="footer-box">
        <b>Tech Stack:</b> Python · SQL Server · Streamlit · Pandas · Plotly · SQLAlchemy
        &nbsp;&nbsp;|&nbsp;&nbsp;
        <b>Domain:</b> Food Management · Waste Reduction · Social Good
    </div>
    """, unsafe_allow_html=True)


# =============================================
# PAGE: DASHBOARD
# =============================================

@st.cache_data
def load_dashboard_data():
    providers = pd.read_sql("SELECT * FROM providers", engine)
    receivers = pd.read_sql("SELECT * FROM receivers", engine)
    food      = pd.read_sql("SELECT * FROM food_listings", engine)
    claims    = pd.read_sql("SELECT * FROM claims", engine)
    return providers, receivers, food, claims


def show_dashboard():
    page_header("📊 Dashboard", "Monitor food availability, provider contributions and claim activity.")

    providers, receivers, food, claims = load_dashboard_data()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🏢 Providers",     f"{len(providers):,}")
    c2.metric("🤝 Receivers",     f"{len(receivers):,}")
    c3.metric("🍱 Food Listings", f"{len(food):,}")
    c4.metric("📝 Claims",        f"{len(claims):,}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        claim_status = claims.groupby("status").size().reset_index(name="count")
        fig = px.pie(claim_status, names="status", values="count",
                     hole=0.5, title="Claims by Status",
                     color_discrete_sequence=px.colors.sequential.Greens_r)
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#a8d5b5")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        food_type = food.groupby("food_type")["quantity"].sum().reset_index()
        fig = px.bar(food_type, x="food_type", y="quantity",
                     title="Food Quantity by Type", color="food_type",
                     color_discrete_sequence=px.colors.sequential.Greens_r)
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#a8d5b5", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        if "provider_type" in food.columns:
            provider_type = food.groupby("provider_type")["quantity"].sum().reset_index()
            fig = px.bar(provider_type, x="provider_type", y="quantity",
                         color="provider_type", title="Food Quantity by Provider Type",
                         color_discrete_sequence=px.colors.sequential.Greens_r)
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                              font_color="#a8d5b5", showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        meal_type = food.groupby("meal_type").size().reset_index(name="count")
        fig = px.bar(meal_type, x="meal_type", y="count", color="meal_type",
                     title="Meal Type Distribution",
                     color_discrete_sequence=px.colors.sequential.Greens_r)
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#a8d5b5", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("📍 Top Locations by Available Food Quantity")
    location_df = (
        food.groupby("location")["quantity"]
        .sum().reset_index()
        .sort_values("quantity", ascending=False).head(10)
    )
    fig = px.bar(location_df, x="location", y="quantity", color="quantity",
                 title="Top 10 Locations",
                 color_continuous_scale="Greens")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      font_color="#a8d5b5")
    st.plotly_chart(fig, use_container_width=True)

    top_food     = food.groupby("food_type")["quantity"].sum().idxmax()
    top_provider = food.groupby("provider_type")["quantity"].sum().idxmax() if "provider_type" in food.columns else "N/A"

    st.info(f"""
    • Highest available food category: **{top_food}**
    • Largest contributing provider type: **{top_provider}**
    • Total food listings available: **{len(food):,}**
    • Total claims processed: **{len(claims):,}**
    """)


# =============================================
# PAGE: BROWSE FOOD
# =============================================

@st.cache_data
def load_browse_data():
    query = """
    SELECT
        f.food_id, f.food_name, f.quantity, f.expiry_date,
        f.location, f.food_type, f.meal_type,
        p.provider_id, p.name AS provider_name,
        p.type AS provider_type, p.address, p.city, p.contact
    FROM food_listings f
    INNER JOIN providers p ON f.provider_id = p.provider_id
    """
    return pd.read_sql(query, engine)


def show_browse_food():
    page_header("🔍 Browse Available Food", "Search and explore available food listings.")

    food_df = load_browse_data()

    st.subheader("🎯 Filter Listings")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        location_filter = st.selectbox("Location",
            ["All"] + sorted(food_df["location"].dropna().unique().tolist()))
    with col2:
        food_filter = st.selectbox("Food Type",
            ["All"] + sorted(food_df["food_type"].dropna().unique().tolist()))
    with col3:
        meal_filter = st.selectbox("Meal Type",
            ["All"] + sorted(food_df["meal_type"].dropna().unique().tolist()))
    with col4:
        provider_filter = st.selectbox("Provider",
            ["All"] + sorted(food_df["provider_name"].dropna().unique().tolist()))

    filtered_df = food_df.copy()
    if location_filter != "All":
        filtered_df = filtered_df[filtered_df["location"] == location_filter]
    if food_filter != "All":
        filtered_df = filtered_df[filtered_df["food_type"] == food_filter]
    if meal_filter != "All":
        filtered_df = filtered_df[filtered_df["meal_type"] == meal_filter]
    if provider_filter != "All":
        filtered_df = filtered_df[filtered_df["provider_name"] == provider_filter]

    st.success(f"Found **{len(filtered_df)}** listings — Total Quantity: **{filtered_df['quantity'].sum()}**")

    st.subheader("🍱 Available Food Listings")
    st.dataframe(
        filtered_df[["food_id","food_name","quantity","food_type",
                     "meal_type","location","provider_name","contact"]],
        use_container_width=True, hide_index=True
    )

    if len(filtered_df) > 0:
        st.divider()
        st.subheader("📦 Food & Provider Details")

        food_options = {
            f"{row.food_id} - {row.food_name}": row.food_id
            for _, row in filtered_df.iterrows()
        }
        selected_food = st.selectbox("Select Food Item", list(food_options.keys()))
        food_id       = food_options[selected_food]
        food_details  = filtered_df[filtered_df["food_id"] == food_id].iloc[0]

        c1, c2 = st.columns(2)
        with c1:
            st.info(f"""
**🍽️ Food Information**

**Name:** {food_details['food_name']}
**Quantity:** {food_details['quantity']}
**Food Type:** {food_details['food_type']}
**Meal Type:** {food_details['meal_type']}
**Expiry Date:** {food_details['expiry_date']}
""")
        with c2:
            st.success(f"""
**🏢 Provider Information**

**Provider:** {food_details['provider_name']}
**Type:** {food_details['provider_type']}
**City:** {food_details['city']}
**Contact:** {food_details['contact']}
**Address:** {food_details['address']}
""")


# =============================================
# PAGE: FOOD LISTINGS
# =============================================

@st.cache_data
def load_listings():
    return pd.read_sql("SELECT * FROM food_listings ORDER BY food_id", engine)

@st.cache_data
def load_providers_list():
    return pd.read_sql("SELECT provider_id, name FROM providers ORDER BY name", engine)


def show_food_listings():
    page_header("🍱 Food Listings Management", "Add, edit or remove food listings.")

    tab1, tab2, tab3, tab4 = st.tabs(["📖 All Listings", "➕ Add", "✏️ Edit", "🗑 Delete"])

    with tab1:
        listings_df = load_listings()
        st.metric("Total Listings", len(listings_df))
        st.dataframe(listings_df, use_container_width=True, hide_index=True)

    with tab2:
        providers_df   = load_providers_list()
        provider_options = {f"#{r.provider_id} — {r.name}": r.provider_id
                            for _, r in providers_df.iterrows()}

        with st.form("add_food_form"):
            food_name   = st.text_input("Food Name")
            quantity    = st.number_input("Quantity", min_value=1, value=10)
            expiry_date = st.date_input("Expiry Date")
            provider    = st.selectbox("Provider", list(provider_options.keys()))
            location    = st.text_input("Location (City)")
            food_type   = st.selectbox("Food Type", ["Vegetarian","Non-Vegetarian","Vegan"])
            meal_type   = st.selectbox("Meal Type", ["Breakfast","Lunch","Dinner","Snacks"])
            submit      = st.form_submit_button("➕ Add Listing")

        if submit:
            query = text("""
            INSERT INTO food_listings (food_name,quantity,expiry_date,provider_id,location,food_type,meal_type)
            VALUES (:food_name,:quantity,:expiry_date,:provider_id,:location,:food_type,:meal_type)
            """)
            with engine.begin() as conn:
                conn.execute(query, {
                    "food_name": food_name, "quantity": quantity,
                    "expiry_date": expiry_date,
                    "provider_id": provider_options[provider],
                    "location": location, "food_type": food_type, "meal_type": meal_type
                })
            st.cache_data.clear()
            st.success("Food Listing Added Successfully!")

    with tab3:
        listings_df  = load_listings()
        providers_df = load_providers_list()

        listing_options = {f"#{r.food_id} — {r.food_name}": r.food_id
                           for _, r in listings_df.iterrows()}
        selected_listing = st.selectbox("Select listing to edit", list(listing_options.keys()))
        selected_id      = listing_options[selected_listing]
        row              = listings_df[listings_df["food_id"] == selected_id].iloc[0]

        provider_options = {f"#{r.provider_id} — {r.name}": r.provider_id
                            for _, r in providers_df.iterrows()}
        provider_keys    = list(provider_options.keys())
        current_provider_index = next(
            (i for i, k in enumerate(provider_keys)
             if provider_options[k] == row["provider_id"]), 0
        )

        food_types  = ["Vegetarian","Non-Vegetarian","Vegan"]
        meal_types  = ["Breakfast","Lunch","Dinner","Snacks"]

        with st.form("edit_food_form"):
            food_name   = st.text_input("Food Name", value=row["food_name"])
            quantity    = st.number_input("Quantity", min_value=1, value=int(row["quantity"]))
            expiry_date = st.date_input("Expiry Date", value=pd.to_datetime(row["expiry_date"]))
            provider    = st.selectbox("Provider", provider_keys, index=current_provider_index)
            location    = st.text_input("Location (City)", value=row["location"])
            food_type   = st.selectbox("Food Type", food_types,
                                       index=food_types.index(row["food_type"]) if row["food_type"] in food_types else 0)
            meal_type   = st.selectbox("Meal Type", meal_types,
                                       index=meal_types.index(row["meal_type"]) if row["meal_type"] in meal_types else 0)
            update      = st.form_submit_button("💾 Save Changes")

        if update:
            query = text("""
            UPDATE food_listings
            SET food_name=:food_name, quantity=:quantity, expiry_date=:expiry_date,
                provider_id=:provider_id, location=:location,
                food_type=:food_type, meal_type=:meal_type
            WHERE food_id=:food_id
            """)
            with engine.begin() as conn:
                conn.execute(query, {
                    "food_name": food_name, "quantity": quantity,
                    "expiry_date": expiry_date,
                    "provider_id": provider_options[provider],
                    "location": location, "food_type": food_type,
                    "meal_type": meal_type, "food_id": selected_id
                })
            st.cache_data.clear()
            st.success("Food Listing Updated Successfully!")

    with tab4:
        listings_df     = load_listings()
        listing_options = {f"#{r.food_id} — {r.food_name}": r.food_id
                           for _, r in listings_df.iterrows()}
        selected_listing = st.selectbox("Select listing to delete", list(listing_options.keys()))
        delete_id        = listing_options[selected_listing]
        st.warning("This action cannot be undone.")

        if st.button("🗑 Delete Listing", use_container_width=True):
            query = text("DELETE FROM food_listings WHERE food_id=:food_id")
            with engine.begin() as conn:
                conn.execute(query, {"food_id": delete_id})
            st.cache_data.clear()
            st.success("Food Listing Deleted Successfully!")


# =============================================
# PAGE: CLAIMS
# =============================================

@st.cache_data
def load_claims():
    query = """
    SELECT c.claim_id, c.food_id, f.food_name, c.receiver_id,
           r.name AS receiver_name, c.status, c.timestamp
    FROM claims c
    INNER JOIN food_listings f ON c.food_id = f.food_id
    INNER JOIN receivers r ON c.receiver_id = r.receiver_id
    ORDER BY c.claim_id DESC
    """
    return pd.read_sql(query, engine)

@st.cache_data
def load_food_for_claims():
    return pd.read_sql("SELECT food_id, food_name FROM food_listings ORDER BY food_name", engine)

@st.cache_data
def load_receivers_for_claims():
    return pd.read_sql("SELECT receiver_id, name FROM receivers ORDER BY name", engine)


def show_claims():
    page_header("📋 Claims Center", "Manage food claims, update statuses and track distribution.")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📖 All Claims", "➕ Add Claim", "✏️ Update Status", "🗑 Delete"])

    with tab1:
        claims_df     = load_claims()
        status_filter = st.selectbox("Filter by Status", ["All","Pending","Completed","Cancelled"])
        filtered_df   = claims_df if status_filter == "All" else claims_df[claims_df["status"] == status_filter]
        st.metric("Total Claims", len(filtered_df))
        st.dataframe(
            filtered_df[["claim_id","food_name","receiver_name","status","timestamp"]],
            use_container_width=True, hide_index=True
        )

    with tab2:
        food_df     = load_food_for_claims()
        receiver_df = load_receivers_for_claims()

        food_options     = {f"#{r.food_id} — {r.food_name}": r.food_id for _, r in food_df.iterrows()}
        receiver_options = {f"#{r.receiver_id} — {r.name}": r.receiver_id for _, r in receiver_df.iterrows()}

        with st.form("add_claim_form"):
            selected_food     = st.selectbox("Food Item", list(food_options.keys()))
            selected_receiver = st.selectbox("Receiver", list(receiver_options.keys()))
            status            = st.selectbox("Status", ["Pending","Completed","Cancelled"])
            add_claim         = st.form_submit_button("➕ Add Claim")

        if add_claim:
            query = text("""
            INSERT INTO claims (food_id, receiver_id, status, timestamp)
            VALUES (:food_id, :receiver_id, :status, GETDATE())
            """)
            with engine.begin() as conn:
                conn.execute(query, {
                    "food_id": food_options[selected_food],
                    "receiver_id": receiver_options[selected_receiver],
                    "status": status
                })
            st.cache_data.clear()
            st.success("Claim Added Successfully!")

    with tab3:
        claims_df    = load_claims()
        claim_options = {
            f"#{r.claim_id} — {r.food_name} → {r.receiver_name}": r.claim_id
            for _, r in claims_df.iterrows()
        }
        selected_claim = st.selectbox("Select Claim", list(claim_options.keys()))
        claim_id       = claim_options[selected_claim]
        row            = claims_df[claims_df["claim_id"] == claim_id].iloc[0]
        status_list    = ["Pending","Completed","Cancelled"]
        current_index  = status_list.index(row["status"]) if row["status"] in status_list else 0

        with st.form("update_claim_form"):
            st.text_input("Food Item", value=row["food_name"], disabled=True)
            st.text_input("Receiver",  value=row["receiver_name"], disabled=True)
            status       = st.selectbox("Status", status_list, index=current_index)
            update_claim = st.form_submit_button("💾 Save Changes")

        if update_claim:
            query = text("UPDATE claims SET status=:status WHERE claim_id=:claim_id")
            with engine.begin() as conn:
                conn.execute(query, {"status": status, "claim_id": claim_id})
            st.cache_data.clear()
            st.success("Claim Updated Successfully!")

    with tab4:
        claims_df    = load_claims()
        claim_options = {
            f"#{r.claim_id} — {r.food_name} → {r.receiver_name}": r.claim_id
            for _, r in claims_df.iterrows()
        }
        selected_claim = st.selectbox("Select Claim To Delete", list(claim_options.keys()))
        delete_id      = claim_options[selected_claim]
        st.warning("This action cannot be undone.")

        if st.button("🗑 Delete Claim", use_container_width=True):
            query = text("DELETE FROM claims WHERE claim_id=:claim_id")
            with engine.begin() as conn:
                conn.execute(query, {"claim_id": delete_id})
            st.cache_data.clear()
            st.success("Claim Deleted Successfully!")


# =============================================
# PAGE: PROVIDERS
# =============================================

@st.cache_data
def load_providers():
    return pd.read_sql(
        "SELECT provider_id,name,type,address,city,contact FROM providers ORDER BY name",
        engine
    )


def show_providers():
    page_header("🏢 Providers Directory", "Manage food providers and donation partners.")

    providers_df = load_providers()

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Total Providers", len(providers_df))
    c2.metric("Restaurants",     len(providers_df[providers_df["type"]=="Restaurant"]))
    c3.metric("Grocery Stores",  len(providers_df[providers_df["type"]=="Grocery Store"]))
    c4.metric("Supermarkets",    len(providers_df[providers_df["type"]=="Supermarket"]))

    st.divider()

    tab1,tab2,tab3,tab4 = st.tabs(["📖 Directory","➕ Add","✏️ Edit","🗑 Delete"])

    with tab1:
        col1,col2,col3 = st.columns(3)
        city_filter     = col1.selectbox("City", ["All"]+sorted(providers_df["city"].dropna().unique().tolist()))
        type_filter     = col2.selectbox("Provider Type", ["All"]+sorted(providers_df["type"].dropna().unique().tolist()))
        search_provider = col3.text_input("Search Provider")

        filtered_df = providers_df.copy()
        if city_filter != "All":
            filtered_df = filtered_df[filtered_df["city"]==city_filter]
        if type_filter != "All":
            filtered_df = filtered_df[filtered_df["type"]==type_filter]
        if search_provider:
            filtered_df = filtered_df[filtered_df["name"].str.contains(search_provider, case=False, na=False)]

        st.metric("Providers Found", len(filtered_df))
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    with tab2:
        with st.form("add_provider"):
            name          = st.text_input("Provider Name")
            provider_type = st.selectbox("Provider Type", ["Restaurant","Grocery Store","Supermarket","Catering Service"])
            address       = st.text_area("Address")
            city          = st.text_input("City")
            contact       = st.text_input("Contact")
            submit        = st.form_submit_button("Add Provider")

        if submit:
            query = text("""
            INSERT INTO providers (name,type,address,city,contact)
            VALUES (:name,:type,:address,:city,:contact)
            """)
            with engine.begin() as conn:
                conn.execute(query, {"name":name,"type":provider_type,
                                     "address":address,"city":city,"contact":contact})
            st.cache_data.clear()
            st.success("Provider Added Successfully")

    with tab3:
        providers_df    = load_providers()
        provider_options = {f"#{r.provider_id} — {r.name}": r.provider_id
                            for _, r in providers_df.iterrows()}
        selected    = st.selectbox("Select Provider", list(provider_options.keys()))
        provider_id = provider_options[selected]
        row         = providers_df[providers_df["provider_id"]==provider_id].iloc[0]

        p_types = ["Restaurant","Grocery Store","Supermarket","Catering Service"]
        with st.form("edit_provider"):
            name          = st.text_input("Provider Name", value=row["name"])
            provider_type = st.selectbox("Provider Type", p_types,
                                         index=p_types.index(row["type"]) if row["type"] in p_types else 0)
            address       = st.text_area("Address", value=row["address"])
            city          = st.text_input("City", value=row["city"])
            contact       = st.text_input("Contact", value=row["contact"])
            update        = st.form_submit_button("Save Changes")

        if update:
            query = text("""
            UPDATE providers SET name=:name,type=:type,address=:address,city=:city,contact=:contact
            WHERE provider_id=:provider_id
            """)
            with engine.begin() as conn:
                conn.execute(query, {"name":name,"type":provider_type,"address":address,
                                     "city":city,"contact":contact,"provider_id":provider_id})
            st.cache_data.clear()
            st.success("Provider Updated Successfully")

    with tab4:
        providers_df    = load_providers()
        provider_options = {f"#{r.provider_id} — {r.name}": r.provider_id
                            for _, r in providers_df.iterrows()}
        selected  = st.selectbox("Select Provider To Delete", list(provider_options.keys()))
        delete_id = provider_options[selected]
        st.warning("This action cannot be undone.")

        if st.button("🗑 Delete Provider", use_container_width=True):
            try:
                query = text("DELETE FROM providers WHERE provider_id=:provider_id")
                with engine.begin() as conn:
                    conn.execute(query, {"provider_id": delete_id})
                st.cache_data.clear()
                st.success("Provider Deleted Successfully")
            except Exception:
                st.error("Provider has linked food listings. Delete or reassign those listings first.")


# =============================================
# PAGE: RECEIVERS
# =============================================

@st.cache_data
def load_receivers():
    return pd.read_sql(
        "SELECT receiver_id,name,type,city,contact FROM receivers ORDER BY name",
        engine
    )


def show_receivers():
    page_header("👥 Receivers Directory", "Manage NGOs, Shelters and Individuals receiving food.")

    receivers_df = load_receivers()

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Total Receivers", len(receivers_df))
    c2.metric("NGOs",        len(receivers_df[receivers_df["type"]=="NGO"]))
    c3.metric("Shelters",    len(receivers_df[receivers_df["type"]=="Shelter"]))
    c4.metric("Individuals", len(receivers_df[receivers_df["type"]=="Individual"]))

    st.divider()

    tab1,tab2,tab3,tab4 = st.tabs(["📖 Directory","➕ Add","✏️ Edit","🗑 Delete"])

    with tab1:
        col1,col2,col3 = st.columns(3)
        city_filter     = col1.selectbox("City", ["All"]+sorted(receivers_df["city"].dropna().unique().tolist()))
        type_filter     = col2.selectbox("Receiver Type", ["All"]+sorted(receivers_df["type"].dropna().unique().tolist()))
        search_receiver = col3.text_input("Search Receiver")

        filtered_df = receivers_df.copy()
        if city_filter != "All":
            filtered_df = filtered_df[filtered_df["city"]==city_filter]
        if type_filter != "All":
            filtered_df = filtered_df[filtered_df["type"]==type_filter]
        if search_receiver:
            filtered_df = filtered_df[filtered_df["name"].str.contains(search_receiver, case=False, na=False)]

        st.metric("Receivers Found", len(filtered_df))
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    with tab2:
        with st.form("add_receiver"):
            name          = st.text_input("Receiver Name")
            receiver_type = st.selectbox("Receiver Type", ["NGO","Shelter","Individual"])
            city          = st.text_input("City")
            contact       = st.text_input("Contact")
            submit        = st.form_submit_button("Add Receiver")

        if submit:
            query = text("""
            INSERT INTO receivers (name,type,city,contact)
            VALUES (:name,:type,:city,:contact)
            """)
            with engine.begin() as conn:
                conn.execute(query, {"name":name,"type":receiver_type,"city":city,"contact":contact})
            st.cache_data.clear()
            st.success("Receiver Added Successfully")

    with tab3:
        receivers_df    = load_receivers()
        receiver_options = {f"#{r.receiver_id} — {r.name}": r.receiver_id
                            for _, r in receivers_df.iterrows()}
        selected    = st.selectbox("Select Receiver", list(receiver_options.keys()))
        receiver_id = receiver_options[selected]
        row         = receivers_df[receivers_df["receiver_id"]==receiver_id].iloc[0]

        type_list     = ["NGO","Shelter","Individual"]
        current_index = type_list.index(row["type"]) if row["type"] in type_list else 0

        with st.form("edit_receiver"):
            name          = st.text_input("Receiver Name", value=row["name"])
            receiver_type = st.selectbox("Receiver Type", type_list, index=current_index)
            city          = st.text_input("City", value=row["city"])
            contact       = st.text_input("Contact", value=row["contact"])
            update        = st.form_submit_button("Save Changes")

        if update:
            query = text("""
            UPDATE receivers SET name=:name,type=:type,city=:city,contact=:contact
            WHERE receiver_id=:receiver_id
            """)
            with engine.begin() as conn:
                conn.execute(query, {"name":name,"type":receiver_type,
                                     "city":city,"contact":contact,"receiver_id":receiver_id})
            st.cache_data.clear()
            st.success("Receiver Updated Successfully")

    with tab4:
        receivers_df    = load_receivers()
        receiver_options = {f"#{r.receiver_id} — {r.name}": r.receiver_id
                            for _, r in receivers_df.iterrows()}
        selected  = st.selectbox("Select Receiver To Delete", list(receiver_options.keys()))
        delete_id = receiver_options[selected]
        st.warning("This action cannot be undone.")

        if st.button("🗑 Delete Receiver", use_container_width=True):
            try:
                query = text("DELETE FROM receivers WHERE receiver_id=:receiver_id")
                with engine.begin() as conn:
                    conn.execute(query, {"receiver_id": delete_id})
                st.cache_data.clear()
                st.success("Receiver Deleted Successfully")
            except Exception:
                st.error("Receiver has linked claims. Delete claims first.")


# =============================================
# PAGE: ANALYTICS
# =============================================

@st.cache_data
def load_analytics_data():
    food      = pd.read_sql("SELECT * FROM food_listings", engine)
    claims    = pd.read_sql("SELECT * FROM claims", engine)
    providers = pd.read_sql("SELECT * FROM providers", engine)
    receivers = pd.read_sql("SELECT * FROM receivers", engine)
    return food, claims, providers, receivers


def show_analytics():
    page_header("📈 Analytics & Insights", "Business insights for food distribution, providers, claims and receivers.")

    food_df, claims_df, providers_df, receivers_df = load_analytics_data()

    total_claims      = len(claims_df)
    completed_claims  = len(claims_df[claims_df["status"]=="Completed"])
    claim_success_rate = round(completed_claims / total_claims * 100, 2) if total_claims > 0 else 0

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("🍱 Food Listings",       f"{len(food_df):,}")
    c2.metric("📦 Quantity Available",  f"{int(food_df['quantity'].sum()):,}")
    c3.metric("📋 Total Claims",        f"{total_claims:,}")
    c4.metric("✅ Claim Success %",     f"{claim_success_rate}%")

    st.divider()

    # Food insights
    st.subheader("🍱 Food Insights")
    col1, col2 = st.columns(2)
    with col1:
        food_type_df = food_df.groupby("food_type").size().reset_index(name="Total Listings")
        fig = px.pie(food_type_df, names="food_type", values="Total Listings",
                     title="Food Type Distribution",
                     color_discrete_sequence=px.colors.sequential.Greens_r)
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#a8d5b5")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        meal_type_df = food_df.groupby("meal_type").size().reset_index(name="Total Listings")
        fig = px.bar(meal_type_df, x="meal_type", y="Total Listings",
                     title="Meal Type Distribution",
                     color_discrete_sequence=["#52e09c"])
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#a8d5b5")
        st.plotly_chart(fig, use_container_width=True)

    # Provider insights
    st.subheader("🏢 Provider Insights")
    provider_df = pd.read_sql("""
        SELECT TOP 10 p.name, SUM(f.quantity) AS TotalQuantity
        FROM food_listings f JOIN providers p ON f.provider_id=p.provider_id
        GROUP BY p.name ORDER BY TotalQuantity DESC
    """, engine)
    provider_type_df = pd.read_sql("""
        SELECT p.type, SUM(f.quantity) AS TotalQuantity
        FROM food_listings f JOIN providers p ON f.provider_id=p.provider_id
        GROUP BY p.type
    """, engine)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(provider_df, x="name", y="TotalQuantity",
                     title="Top Providers by Quantity",
                     color_discrete_sequence=["#52e09c"])
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#a8d5b5")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.pie(provider_type_df, names="type", values="TotalQuantity",
                     title="Provider Type Contribution",
                     color_discrete_sequence=px.colors.sequential.Greens_r)
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#a8d5b5")
        st.plotly_chart(fig, use_container_width=True)

    # Claims insights
    st.subheader("🤝 Claims Insights")
    claim_status_df = pd.read_sql("""
        SELECT status, COUNT(*) AS TotalClaims FROM claims GROUP BY status
    """, engine)
    claim_date_df = pd.read_sql("""
        SELECT CAST(timestamp AS DATE) AS ClaimDate, COUNT(*) AS TotalClaims
        FROM claims GROUP BY CAST(timestamp AS DATE) ORDER BY ClaimDate
    """, engine)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(claim_status_df, names="status", values="TotalClaims",
                     hole=0.5, title="Claim Status Breakdown",
                     color_discrete_sequence=px.colors.sequential.Greens_r)
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#a8d5b5")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.line(claim_date_df, x="ClaimDate", y="TotalClaims",
                      markers=True, title="Claims Over Time",
                      color_discrete_sequence=["#52e09c"])
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#a8d5b5")
        st.plotly_chart(fig, use_container_width=True)

    # Receiver insights
    st.subheader("👥 Receiver Insights")
    receiver_df = pd.read_sql("""
        SELECT TOP 10 r.name, COUNT(*) AS ClaimsReceived
        FROM claims c JOIN receivers r ON c.receiver_id=r.receiver_id
        GROUP BY r.name ORDER BY ClaimsReceived DESC
    """, engine)
    receiver_type_df = pd.read_sql("""
        SELECT type, COUNT(*) AS TotalReceivers FROM receivers GROUP BY type
    """, engine)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(receiver_df, x="name", y="ClaimsReceived",
                     title="Top Receivers",
                     color_discrete_sequence=["#52e09c"])
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#a8d5b5")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.pie(receiver_type_df, names="type", values="TotalReceivers",
                     title="Receiver Type Distribution",
                     color_discrete_sequence=px.colors.sequential.Greens_r)
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#a8d5b5")
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("📊 Database Summary")
    summary_df = pd.DataFrame({
        "Table":   ["Food Listings","Providers","Receivers","Claims"],
        "Records": [len(food_df), len(providers_df), len(receivers_df), len(claims_df)]
    })
    st.dataframe(summary_df, use_container_width=True, hide_index=True)


# =============================================
# PAGE: SQL INSIGHTS
# =============================================

def show_sql_insights():
    page_header("🧠 SQL Insights & Trends", "Run SQL business queries directly against the database.")

    queries = {
        "Food Providers & Receivers": {
            "Q1. How many food providers and receivers are there in each city?": """
                SELECT COALESCE(p.city,r.city) AS City,
                       COUNT(DISTINCT p.provider_id) AS Providers,
                       COUNT(DISTINCT r.receiver_id) AS Receivers
                FROM providers p FULL OUTER JOIN receivers r ON p.city=r.city
                GROUP BY COALESCE(p.city,r.city) ORDER BY City""",

            "Q2. Provider Type Contributing Most Food": """
                SELECT provider_type, SUM(quantity) AS total_food
                FROM food_listings GROUP BY provider_type ORDER BY total_food DESC""",

            "Q3. What Are The Most Claimed Food Items": """
                SELECT f.food_name, COUNT(c.claim_id) AS total_claims
                FROM food_listings f JOIN claims c ON f.food_id=c.food_id
                GROUP BY f.food_name ORDER BY total_claims DESC""",
        },
        "Food Listings": {
            "Q4. Which City Has The Highest Food Demand": """
                SELECT r.city, COUNT(c.claim_id) AS total_claims
                FROM receivers r JOIN claims c ON r.receiver_id=c.receiver_id
                GROUP BY r.city ORDER BY total_claims DESC""",

            "Q5. Food Type Most In Demand": """
                SELECT f.food_type, COUNT(c.claim_id) AS total_claims
                FROM food_listings f JOIN claims c ON f.food_id=c.food_id
                GROUP BY f.food_type ORDER BY total_claims DESC""",

            "Q6. Meal Type Most In Demand": """
                SELECT f.meal_type, COUNT(c.claim_id) AS total_claims
                FROM food_listings f JOIN claims c ON f.food_id=c.food_id
                GROUP BY f.meal_type ORDER BY total_claims DESC""",
        },
        "Claims Analysis": {
            "Q7. Claim Status Percentage": """
                SELECT status,
                       ROUND(COUNT(*)*100.0/SUM(COUNT(*)) OVER(),2) AS percentage
                FROM claims GROUP BY status""",

            "Q8. Claim Status Distribution": """
                SELECT status, COUNT(*) AS total_claims FROM claims GROUP BY status""",
        },
        "Business Intelligence": {
            "Q9. Top 10 Providers By Quantity": """
                SELECT TOP 10 p.name, SUM(f.quantity) AS total_quantity
                FROM food_listings f JOIN providers p ON f.provider_id=p.provider_id
                GROUP BY p.name ORDER BY total_quantity DESC""",

            "Q10. Top 10 Receivers By Claims": """
                SELECT TOP 10 r.name, COUNT(c.claim_id) AS total_claims
                FROM receivers r JOIN claims c ON r.receiver_id=c.receiver_id
                GROUP BY r.name ORDER BY total_claims DESC""",
        }
    }

    section = st.selectbox("Select Section", list(queries.keys()))

    for i, (question, sql) in enumerate(queries[section].items()):
        with st.expander(question):
            st.code(sql.strip(), language="sql")
            if st.button("▶ Run Query", key=f"query_{i}"):
                try:
                    df = pd.read_sql(sql, engine)
                    st.success(f"{len(df)} rows returned")
                    st.dataframe(df, use_container_width=True)
                except Exception as e:
                    st.error(str(e))

    st.divider()
    st.subheader("🎯 Project Conclusion")
    st.success("""
    The Food Waste Management System demonstrates how data analytics and operational management
    can work together to reduce food waste and improve food redistribution efficiency.

    By combining SQL Server, Python, Streamlit, and business intelligence techniques,
    the platform enables providers, receivers, and administrators to make informed decisions
    and maximize social impact.
    """)


# =============================================
# ROUTER
# =============================================

if page == "Home":
    show_home()
elif page == "Dashboard":
    show_dashboard()
elif page == "Browse Food":
    show_browse_food()
elif page == "Food Listings":
    show_food_listings()
elif page == "Claims":
    show_claims()
elif page == "Providers":
    show_providers()
elif page == "Receivers":
    show_receivers()
elif page == "Analytics":
    show_analytics()
elif page == "SQL Insights":
    show_sql_insights()