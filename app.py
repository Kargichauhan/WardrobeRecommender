import streamlit as st
from WardrobeRecommender import WardrobeRecommender
from PIL import Image
import io
import base64

def set_custom_style():
    st.markdown("""
    <style>
        /* Global styles */
        .main {
            background-color: #ffffff;
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .stApp {
            background: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Header styles */
        h1 {
            color: #1a1a1a;
            font-size: 2.5rem !important;
            font-weight: 800 !important;
            text-align: center;
            margin-bottom: 1rem;
            letter-spacing: -0.5px;
            background: linear-gradient(120deg, #1a1a1a 0%, #4a4a4a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            color: #666666;
            font-size: 1.1rem;
            text-align: center;
            max-width: 600px;
            margin: 0 auto 2rem;
            line-height: 1.6;
        }
        
        /* Sidebar styles */
        [data-testid="stSidebar"] {
            background-color: #f8f9fa;
            padding: 2rem;
            border-right: 1px solid #e9ecef;
        }
        [data-testid="stSidebar"] .block-container {
            padding-top: 2rem;
        }
        [data-testid="stSidebar"] h2 {
            color: #1a1a1a;
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
        }
        [data-testid="stSidebar"] h3 {
            color: #4a4a4a;
            font-size: 1rem;
            font-weight: 600;
            margin: 1.5rem 0 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #e9ecef;
        }
        
        /* Input styles */
        .stSelectbox > div > div,
        .stMultiSelect > div > div {
            background-color: white;
            border-radius: 8px;
            border: 1px solid #e9ecef;
            padding: 0.5rem;
            transition: all 0.2s ease;
        }
        .stSelectbox > div > div:hover,
        .stMultiSelect > div > div:hover {
            border-color: #1a1a1a;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .stSelectbox label,
        .stMultiSelect label {
            color: #1a1a1a;
            font-weight: 500;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }
        
        /* Button styles */
        .stButton > button {
            width: 100%;
            background: linear-gradient(120deg, #1a1a1a 0%, #4a4a4a 100%);
            color: white;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        
        /* Recommendation card styles */
        .recommendation-card {
            background: white;
            border-radius: 16px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            border: 1px solid #e9ecef;
            transition: all 0.3s ease;
        }
        .recommendation-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.1);
        }
        .recommendation-card img {
            border-radius: 12px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .recommendation-card img:hover {
            transform: scale(1.02);
        }
        .recommendation-card h3 {
            color: #1a1a1a;
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            letter-spacing: -0.3px;
        }
        .recommendation-card p {
            color: #666666;
            font-size: 0.9rem;
            line-height: 1.5;
            margin-bottom: 0.75rem;
        }
        .price-tag {
            background: linear-gradient(120deg, #1a1a1a 0%, #4a4a4a 100%);
            color: white;
            font-weight: 600;
            font-size: 1rem;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            display: inline-block;
            margin-top: 1rem;
        }
        
        /* Item details styles */
        .item-details {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1rem;
        }
        .item-name {
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 0.5rem;
        }
        .item-category {
            color: #666666;
            font-style: italic;
            margin-bottom: 0.25rem;
        }
        .item-price {
            color: #1a1a1a;
            font-weight: 500;
            margin-bottom: 0.25rem;
        }
        .shop-button {
            display: inline-block;
            background: #1a1a1a;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            text-decoration: none;
            font-size: 0.9rem;
            margin-top: 0.5rem;
            transition: all 0.2s ease;
        }
        .shop-button:hover {
            background: #4a4a4a;
            transform: translateY(-1px);
        }
    </style>
    """, unsafe_allow_html=True)

def main():
    set_custom_style()
    
    # User profile section with modern styling
    st.sidebar.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <h3 style='color: #1a1a1a; font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem;'>Your Style Profile</h3>
            <div style='width: 50px; height: 2px; background: linear-gradient(120deg, #1a1a1a 0%, #4a4a4a 100%); margin: 0 auto 1rem;'></div>
        </div>
    """, unsafe_allow_html=True)
    
    # Add name input with custom styling
    st.sidebar.markdown("""
        <style>
            .stTextInput > label {
                font-size: 0.9rem;
                color: #666666;
                font-weight: 500;
            }
            .stTextInput > div > div > input {
                background-color: white;
                border: 1px solid #e9ecef;
                padding: 0.5rem 1rem;
                border-radius: 8px;
                font-size: 1rem;
                transition: all 0.2s ease;
            }
            .stTextInput > div > div > input:focus {
                border-color: #1a1a1a;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }
        </style>
    """, unsafe_allow_html=True)
    
    user_name = st.sidebar.text_input(
        "Your Name",
        placeholder="Enter your name",
        help="We'll use this to personalize your recommendations",
        key="user_name"
    )
    
    if user_name:
        st.sidebar.markdown(f"""
            <div style='text-align: center; margin-bottom: 1rem;'>
                <p style='color: #1a1a1a; font-size: 1.1rem; font-weight: 500; margin: 0;'>Welcome, {user_name}! 👋</p>
                <p style='color: #666666; font-size: 0.9rem; margin-top: 0.5rem;'>Let's find your perfect style</p>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.sidebar.file_uploader(
        "Upload your photo",
        type=["jpg", "jpeg", "png"],
        help="Add a profile photo to personalize your experience"
    )
    
    if uploaded_file is not None:
        try:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            # Resize image to a reasonable size
            max_size = (150, 150)
            image.thumbnail(max_size, Image.LANCZOS)
            # Convert to bytes for display
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            img_b64 = base64.b64encode(img_byte_arr).decode()
            
            st.sidebar.markdown(f"""
                <div style='text-align: center; margin: 1rem 0;'>
                    <div style='width: 150px; height: 150px; margin: 0 auto; border-radius: 50%; overflow: hidden; border: 3px solid #1a1a1a; box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: all 0.3s ease;'
                         onmouseover='this.style.transform="scale(1.05)"; this.style.boxShadow="0 8px 16px rgba(0,0,0,0.2)"'
                         onmouseout='this.style.transform="scale(1)"; this.style.boxShadow="0 4px 8px rgba(0,0,0,0.1)"'>
                        <img src='data:image/png;base64,{img_b64}' style='width: 100%; height: 100%; object-fit: cover;'>
                    </div>
                    <p style='color: #666666; font-size: 0.9rem; margin-top: 0.5rem;'>Add your picture</p>
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.sidebar.error("Error processing image. Please try another image.")
    else:
        # Display default profile icon
        st.sidebar.markdown("""
            <div style='text-align: center; margin: 1rem 0;'>
                <div style='width: 150px; height: 150px; margin: 0 auto; border-radius: 50%; background: linear-gradient(120deg, #f8f9fa 0%, #e9ecef 100%); display: flex; align-items: center; justify-content: center; border: 3px solid #1a1a1a; box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: all 0.3s ease;'
                     onmouseover='this.style.transform="scale(1.05)"; this.style.boxShadow="0 8px 16px rgba(0,0,0,0.2)"'
                     onmouseout='this.style.transform="scale(1)"; this.style.boxShadow="0 4px 8px rgba(0,0,0,0.1)"'>
                    <svg width='60' height='60' viewBox='0 0 24 24' fill='none' stroke='#666666' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>
                        <path d='M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2'></path>
                        <circle cx='12' cy='7' r='4'></circle>
                    </svg>
                </div>
                <p style='color: #666666; font-size: 0.9rem; margin-top: 0.5rem;'>Add Your Photo</p>
                <div style='margin-top: 0.5rem;'>
                    <span style='background: linear-gradient(120deg, #1a1a1a 0%, #4a4a4a 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 0.8rem;'>Click or drag an image</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # App header with animation
    st.markdown("""
        <div style='text-align: center; padding: 2rem 0; animation: fadeIn 1s ease-out;'>
            <h1>Stylish AI Wardrobe</h1>
            <div style='width: 50px; height: 3px; background: linear-gradient(120deg, #1a1a1a 0%, #4a4a4a 100%); margin: 1rem auto;'></div>
            <p class='subtitle'>Discover your perfect style with AI-powered outfit recommendations</p>
        </div>
        <style>
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize the recommender
    recommender = WardrobeRecommender()

    # Sidebar for user inputs
    st.sidebar.markdown("<h2>Style Preferences</h2>", unsafe_allow_html=True)
    
    # Occasion selection
    occasion = st.sidebar.selectbox(
        "What's the occasion?",
        ["Wedding", "Business Meeting", "Casual Outing", "Party", "Date Night"],
        key="occasion_select"
    )

    # Budget input
    budget = st.sidebar.number_input(
        "Budget Range ($)",
        min_value=50.0,
        max_value=1000.0,
        value=200.0,
        step=50.0,
        key="budget_input",
        help="Maximum budget for the entire outfit"
    )

    # Color preferences
    st.sidebar.markdown("### Color Palette")
    color_preference = st.sidebar.multiselect(
        "Select your preferred colors",
        ["Black", "White", "Blue", "Red", "Green", "Pink", "Purple", "Yellow"],
        default=["Black", "Blue"],
        key="color_select"
    )

    # Style preferences
    st.sidebar.markdown("### Style Aesthetic")
    style_preference = st.sidebar.multiselect(
        "Choose your style vibe",
        ["Casual", "Formal", "Professional", "Trendy", "Classic", "Elegant", "Comfortable"],
        default=["Casual", "Comfortable"],
        key="style_select"
    )

    # Get recommendations button
    if st.sidebar.button("Generate Outfits", key="get_recommendations"):
        with st.spinner("Curating your personalized outfits..."):
            preferences = {
                "colors": color_preference,
                "styles": style_preference
            }

            # Get recommendations
            recommendations = recommender.get_outfit_recommendations(
                style_profile=None,
                occasion=occasion,
                budget=budget,
                preferences=preferences,
                num_recommendations=3
            )

            # Display recommendations
            st.markdown(f"<h2>Curated Looks for {occasion}</h2>", unsafe_allow_html=True)
            
            for i, outfit in enumerate(recommendations, 1):
                st.markdown(f"""
                    <div class='recommendation-card'>
                        <h3>Look {i} - Curated Outfit</h3>
                        <div class='price-tag'>Total Budget: ${outfit['total_price']:.2f}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Create columns for each item in the outfit
                cols = st.columns(len(outfit['items']))
                
                for j, (col, item) in enumerate(zip(cols, outfit['items'])):
                    with col:
                        if 'image_data' in item and item['image_data']:
                            st.image(item['image_data'], key=f"image_{i}_{j}")
                        st.markdown(f"""
                            <div class='item-details'>
                                <div class='item-name'>{item['name']}</div>
                                <div class='item-category'>{item['category'].title()}</div>
                                <div class='item-price'>${item['price']:.2f}</div>
                                <div style='color: #666666;'>Color: {item['color']}</div>
                                {f"<a href='{item['purchase_link']}' target='_blank' class='shop-button'>Shop Now</a>" if item['purchase_link'] else ''}
                            </div>
                        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
