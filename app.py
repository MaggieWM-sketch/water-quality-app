"""Main Streamlit application file."""

import streamlit as st
import pandas as pd
import numpy as np
import warnings

from config.settings import PAGE_CONFIG, CUSTOM_CSS
from utils.model_loader import load_models
from utils.data_processing import predict_water_quality, assess_risk_factors
from components.ui_components import (
    render_sidebar_inputs, render_quick_test_buttons, 
    render_parameter_table, render_prediction_results, render_educational_content
)
from components.charts import (
    create_gauge_chart, create_parameter_radar_chart, create_feature_importance_chart
)

warnings.filterwarnings('ignore')


def main():
    """Main application function."""
    # Page configuration
    st.set_page_config(**PAGE_CONFIG)
    
    # Custom CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">💧 AI Water Quality Predictor</h1>', unsafe_allow_html=True)
    st.markdown("### 🎯 Supporting UN SDG 6: Clean Water and Sanitation")
    
    # Load models
    model, scaler, imputer, feature_names = load_models()
    
    if model is None:
        st.stop()
    
    # Sidebar inputs
    input_values = render_sidebar_inputs()
    render_quick_test_buttons()
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<h2 class="sub-header">📊 Current Parameters</h2>', unsafe_allow_html=True)
        render_parameter_table(input_values)
    
    with col2:
        st.markdown('<h2 class="sub-header">🔬 Prediction Results</h2>', unsafe_allow_html=True)
        
        # Make prediction
        input_array = np.array([input_values[param] for param in feature_names])
        prediction, probability = predict_water_quality(model, scaler, imputer, input_array)
        
        render_prediction_results(prediction, probability)
    
    # Visualizations
    if prediction is not None:
        st.markdown('<h2 class="sub-header">📈 Visualizations</h2>', unsafe_allow_html=True)
        
        viz_col1, viz_col2 = st.columns([1, 1])
        
        with viz_col1:
            gauge_fig = create_gauge_chart(probability, prediction)
            st.plotly_chart(gauge_fig, use_container_width=True)
        
        with viz_col2:
            radar_fig = create_parameter_radar_chart(input_values, feature_names)
            st.plotly_chart(radar_fig, use_container_width=True)
        
        # Feature importance
        importance_fig = create_feature_importance_chart(model, feature_names)
        if importance_fig:
            st.markdown('<h2 class="sub-header">🎯 Feature Importance</h2>', unsafe_allow_html=True)
            st.plotly_chart(importance_fig, use_container_width=True)
    
    # Risk Assessment
    st.markdown('<h2 class="sub-header">⚠️ Risk Assessment</h2>', unsafe_allow_html=True)
    risk_factors = assess_risk_factors(input_values)
    
    if risk_factors:
        st.warning("**Identified Risk Factors:**")
        for i, risk in enumerate(risk_factors, 1):
            st.write(f"{i}. {risk}")
    else:
        st.success("✅ No specific risk factors identified based on standard guidelines.")
    
    # Recommendations
    st.markdown('<h2 class="sub-header">💡 Recommendations</h2>', unsafe_allow_html=True)
    render_recommendations(prediction, risk_factors, input_values)
    
    # Educational content
    render_educational_content()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🔬 This tool is for educational purposes and preliminary assessment only.</p>
        <p>Always consult certified water testing laboratories for official water quality certification.</p>
        <p>Built with ❤️ for sustainable water management</p>
    </div>
    """, unsafe_allow_html=True)


def render_recommendations(prediction, risk_factors, input_values):
    """Render personalized recommendations based on prediction and risk factors."""
    
    if prediction == 0:  # Unsafe water
        st.error("🚨 **Immediate Actions Required:**")
        
        recommendations = [
            "🛑 **Do not consume this water** until proper treatment",
            "🔬 Get professional water testing from a certified laboratory",
            "💧 Use bottled water or properly treated water for drinking and cooking",
            "🏠 Consider installing appropriate water treatment systems"
        ]
        
        # Specific recommendations based on risk factors
        if any("pH" in risk for risk in risk_factors):
            if input_values['ph'] < 6.5:
                recommendations.append("🧪 **pH too low**: Consider lime treatment or pH adjustment systems")
            elif input_values['ph'] > 8.5:
                recommendations.append("🧪 **pH too high**: Consider acid neutralization systems")
        
        if any("Chloramines" in risk for risk in risk_factors):
            recommendations.append("☣️ **High chloramines**: Install activated carbon filtration")
        
        if any("Trihalomethanes" in risk for risk in risk_factors):
            recommendations.append("⚗️ **High trihalomethanes**: Use granular activated carbon or reverse osmosis")
        
        if any("Turbidity" in risk for risk in risk_factors):
            recommendations.append("🌊 **High turbidity**: Install sediment filtration and UV disinfection")
        
        if any("Solids" in risk for risk in risk_factors):
            recommendations.append("🧂 **High TDS**: Consider reverse osmosis or distillation systems")
        
        for rec in recommendations:
            st.write(f"• {rec}")
            
    else:  # Safe water
        st.success("✅ **Water appears safe for consumption**")
        
        maintenance_tips = [
            "🔄 **Regular monitoring**: Test water quality periodically",
            "🧽 **System maintenance**: Clean and maintain any existing filtration systems",
            "🏠 **Plumbing check**: Ensure pipes and storage tanks are clean",
            "📊 **Keep records**: Document water quality test results over time"
        ]
        
        # Additional tips based on parameter levels
        if input_values['Hardness'] > 300:
            maintenance_tips.append("🪨 **Water hardness**: Consider water softening for appliance longevity")
        
        if input_values['Chloramines'] > 2.0:
            maintenance_tips.append("💨 **Chloramine levels**: Let water sit or use carbon filtration to reduce taste/odor")
        
        st.write("**Maintenance Recommendations:**")
        for tip in maintenance_tips:
            st.write(f"• {tip}")
    
    # Treatment technology guide
    with st.expander("🛠️ Water Treatment Technologies Guide"):
        treatment_df = pd.DataFrame({
            'Contaminant': [
                'High/Low pH', 'Chloramines', 'Trihalomethanes', 'High TDS', 
                'Turbidity', 'Bacteria/Viruses', 'Heavy Metals', 'Bad Taste/Odor'
            ],
            'Primary Treatment': [
                'pH Adjustment Systems', 'Activated Carbon', 'Activated Carbon/RO', 
                'Reverse Osmosis', 'Sediment Filtration', 'UV Disinfection', 
                'Reverse Osmosis', 'Activated Carbon'
            ],
            'Alternative Treatment': [
                'Ion Exchange', 'Catalytic Carbon', 'Distillation', 
                'Distillation', 'Coagulation/Flocculation', 'Chlorination', 
                'Ion Exchange', 'Aeration'
            ],
            'Approximate Cost': [
                '$200-800', '$50-300', '$100-500', '$200-1000', 
                '$30-200', '$100-400', '$200-1000', '$50-300'
            ]
        })
        st.dataframe(treatment_df, use_container_width=True)


# Additional utility functions for enhanced functionality
def export_results(input_values, prediction, probability, risk_factors):
    """Export results to CSV format."""
    results_dict = input_values.copy()
    results_dict.update({
        'Prediction': 'Safe' if prediction == 1 else 'Unsafe',
        'Confidence': f"{max(probability)*100:.1f}%",
        'Safe_Probability': f"{probability[1]:.3f}",
        'Unsafe_Probability': f"{probability[0]:.3f}",
        'Risk_Factors_Count': len(risk_factors),
        'Risk_Factors': '; '.join(risk_factors) if risk_factors else 'None',
        'Timestamp': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    return pd.DataFrame([results_dict])


# Enhanced sidebar with export functionality
def render_enhanced_sidebar():
    """Render enhanced sidebar with additional features."""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📥 Export Results")
    
    if st.sidebar.button("📊 Export Current Results"):
        # This would be implemented with the actual prediction results
        st.sidebar.success("Results exported! (Feature would save CSV file)")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ℹ️ About This Tool")
    st.sidebar.info("""
    This AI-powered tool uses machine learning to predict water potability based on 9 key parameters. 
    
    **Model Performance:**
    - Accuracy: ~67%
    - Precision: ~66%
    - Recall: ~71%
    
    **Data Source:** 3276 water quality records with various physicochemical properties.
    """)


# Integration with the main function
if __name__ == "__main__":
    main()


