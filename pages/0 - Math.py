import streamlit as st
import pandas as pd
#from modules.menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
#menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

st.title("Pre-req Math", anchor = False)
st.write("This section focuses on math.")

st.header("Pre-req Math:", anchor = False)

# Define the data for the DataFrame
math_df = {
        "Math Skill": ["Algebraic Manipulation", "Functions and Graphs", "Trigonometry", "Geometry",
                    "Statistics and Probability", "Calculus", "Data Interpretation", "Units and Conversions"],
        "Description": ["Ability to simplify expressions, solve equations, and factor polynomials.",
                    "Understanding of basic functions (linear, quadratic, exponential, logarithmic) and ability to interpret graphs.",
                    "Familiarity with trigonometric functions, identities, and solving trigonometric equations.",
                    "Knowledge of basic geometry concepts such as area, perimeter, volume, and geometric transformations.",
                    "Understanding of basic statistical concepts (mean, median, standard deviation, etc.) and probability calculations.",
                    "Basic understanding of differential and integral calculus concepts, including limits, derivatives, and integrals.",
                    "Analyzing and interpreting data presented in tables, graphs, and charts.",
                    "Proficiency in converting between different units of measurement and understanding dimensional analysis."],
        "Formula/Equation/Symbol": ["Quadratic formula: \(x = \frac{{-b ± \sqrt{{b^2 - 4ac}}}}{{2a}}\)\nBinomial theorem: \((a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k\)\nExponential properties: \(a^m \cdot a^n = a^{m+n}\), \(\frac{{a^m}}{{a^n}} = a^{m-n}\)",
                                 "Linear equation: \(y = mx + b\)\nQuadratic equation: \(ax^2 + bx + c = 0\)\nExponential function: \(y = ab^x\)",
                                 "Pythagorean theorem: \(a^2 + b^2 = c^2\)\nSine, cosine, tangent definitions: \(\sin \theta = \frac{{\text{{opposite}}}}{{\text{{hypotenuse}}}}\), \(\cos \theta = \frac{{\text{{adjacent}}}}{{\text{{hypotenuse}}}}\), \(\tan \theta = \frac{{\text{{opposite}}}}{{\text{{adjacent}}}}\)",
                                 "Area of a rectangle: \(A = lw\)\nArea of a triangle: \(A = \frac{1}{2}bh\)\nVolume of a cylinder: \(V = \pi r^2 h\)",
                                 "Mean: \(\bar{x} = \frac{{\sum x_i}}{{n}}\)\nStandard deviation: \(s = \sqrt{\frac{{\sum (x_i - \bar{x})^2}}{{n-1}}}\)\nProbability: \(P(E) = \frac{{\text{{number of favorable outcomes}}}}{{\text{{total number of outcomes}}}}\)",
                                 "Derivative: \(\frac{{df}}{{dx}}\)\nIntegral: \(\int f(x) \, dx\)",
                                 "None specific, but understanding graphs, charts, and tables is essential.",
                                 "None specific, but dimensional analysis is important."],
}


# Create a DataFrame
df_math = pd.DataFrame(math_df)

# Display the DataFrame using Streamlit
st.header("Math Skills for the MCAT")
st.dataframe(df_math)

st.subheader("Algebraic Equations for the MCAT")
st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Algebraic_Equation [label="Algebraic Equation\nMathematical expression\nrelating variables"]
        Linear_Equation [label="Linear Equation\nDegree of variables is 1\n(e.g., y = mx + b)"]
        Quadratic_Equation [label="Quadratic Equation\nDegree of variables is 2\n(e.g., ax^2 + bx + c = 0)"]
        Exponential_Equation [label="Exponential Equation\nVariable in exponent\n(e.g., y = ab^x)"]
        Logarithmic_Equation [label="Logarithmic Equation\nVariable in logarithm\n(e.g., log_b(x) = y)"]
        
        Algebraic_Equation -> Linear_Equation
        Algebraic_Equation -> Quadratic_Equation
        Algebraic_Equation -> Exponential_Equation
        Algebraic_Equation -> Logarithmic_Equation
    }
''', use_container_width=True)

st.subheader("Trigonometric Functions for the MCAT")
st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Trigonometric_Function [label="Trigonometric Function\nMathematical function of angle"]
        Sine_Function [label="Sine Function\nOpposite / Hypotenuse\n(sinθ)"]
        Cosine_Function [label="Cosine Function\nAdjacent / Hypotenuse\n(cosθ)"]
        Tangent_Function [label="Tangent Function\nOpposite / Adjacent\n(tanθ)"]
        Cosecant_Function [label="Cosecant Function\nReciprocal of Sine\n(cscθ = 1 / sinθ)"]
        Secant_Function [label="Secant Function\nReciprocal of Cosine\n(secθ = 1 / cosθ)"]
        Cotangent_Function [label="Cotangent Function\nReciprocal of Tangent\n(cotθ = 1 / tanθ)"]
        
        Trigonometric_Function -> Sine_Function
        Trigonometric_Function -> Cosine_Function
        Trigonometric_Function -> Tangent_Function
        Trigonometric_Function -> Cosecant_Function
        Trigonometric_Function -> Secant_Function
        Trigonometric_Function -> Cotangent_Function
    }
''', use_container_width=True)

st.subheader("Exponents and Logarithms for the MCAT")
st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Exponent_Function [label="Exponent Function\nRaises base to power"]
        Logarithm_Function [label="Logarithm Function\nInverse of exponent"]
        
        Exponent_Function -> Logarithm_Function [label="Inverse"]
        Logarithm_Function -> Exponent_Function [label="Inverse"]
    }
''', use_container_width=True)