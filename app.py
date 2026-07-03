import streamlit as st
from streamlit_mermaid import mermaid

# Define the Mermaid diagram
mermaid_diagram = """
graph TD
    Start([Start]) --> DataPrep["1. Data Preparation"]
    
    %% Data Preparation Section
    DataPrep --> LoadData["Load Dataset"]
    LoadData --> CleanData["Data Cleaning"]
    CleanData --> MissingVals["Handle Missing Values"]
    CleanData --> Duplicates["Remove Duplicates"]
    CleanData --> Outliers["Handle Outliers"]
    
    %% Variable Definition
    MissingVals & Duplicates & Outliers --> Variables["2. Variable Definition"]
    
    Variables --> DemoVars["Demographic Variables"]
    Variables --> BehavVars["Behavioral Variables"]
    
    DemoVars --> Age["Age Groups"]
    DemoVars --> Income["Income Categories"]
    
    Age --> AgeGroups["• 18-25<br>• 26-35<br>• 36-50<br>• 50+"]
    Income --> IncomeGroups["• Low Income<br>• Medium Income<br>• High Income"]
    
    BehavVars --> Engagement["Engagement Levels"]
    BehavVars --> Purchase["Purchase Patterns"]
    
    Engagement --> EngageGroups["• Never Engaged<br>• Rarely Engaged<br>• Often Engaged"]
    Purchase --> PurchaseGroups["• Low Spender<br>• Moderate Spender<br>• High Spender"]
    
    %% Analysis
    AgeGroups & IncomeGroups & EngageGroups & PurchaseGroups --> Analysis["3. Analysis"]
    Analysis --> PivotTables["Create Pivot Tables"]
    PivotTables --> Segments["4. Define Segments"]
    
    %% Segments
    Segments --> Seg1["Segment 1: Young Professionals<br>• Age: 18-35<br>• Income: High<br>• Engagement: Often"]
    Segments --> Seg2["Segment 2: Wealthy Seniors<br>• Age: 50+<br>• Income: High<br>• Engagement: Rare"]
    Segments --> Seg3["Segment 3: Moderate Professionals<br>• Age: 36-50<br>• Income: Medium<br>• Engagement: Moderate"]
    Segments --> Seg4["Segment 4: Low-Income Retirees<br>• Age: 50+<br>• Income: Low<br>• Engagement: Never"]
    
    %% Visualization
    Seg1 & Seg2 & Seg3 & Seg4 --> Visualization["5. Visualization"]
    
    Visualization --> Chart1["Bar Charts:<br>Age & Income Distribution"]
    Visualization --> Chart2["Pie Chart:<br>Segment Distribution"]
    Visualization --> Chart3["Stacked Bar:<br>Engagement Levels"]
    Visualization --> Chart4["Box Plot:<br>Demographics"]
    
    %% Documentation and Presentation
    Chart1 & Chart2 & Chart3 & Chart4 --> Documentation["6. Documentation"]
    Documentation --> Characteristics["Define Characteristics"]
    Documentation --> Needs["Define Needs"]
    Documentation --> Strategy["Define Marketing Strategy"]
    
    Characteristics & Needs & Strategy --> Presentation["7. Create Presentation"]
    
    Presentation --> Slides["Final Slides:<br>• Title & Overview<br>• Methodology<br>• Segment Analysis<br>• Visualizations<br>• Recommendations<br>• Conclusion"]
    
    Slides --> End([End])
    
    %% Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px;
    classDef mainStep fill:#d4e6f1,stroke:#2874a6,stroke-width:3px;
    classDef subStep fill:#d4efdf,stroke:#27ae60,stroke-width:2px;
    classDef segment fill:#fdebd0,stroke:#f39c12,stroke-width:2px;
    classDef visualization fill:#ebdef0,stroke:#8e44ad,stroke-width:2px;
    classDef endpoint fill:#f2f3f4,stroke:#2c3e50,stroke-width:3px;
    
    class Start,End endpoint;
    class DataPrep,Variables,Analysis,Segments,Visualization,Documentation,Presentation mainStep;
    class LoadData,CleanData,MissingVals,Duplicates,Outliers,DemoVars,BehavVars,PivotTables subStep;
    class Seg1,Seg2,Seg3,Seg4 segment;
    class Chart1,Chart2,Chart3,Chart4 visualization;
"""

# Streamlit UI
st.title("Flowchart Visualization")
st.write("Below is the flowchart rendered using Mermaid.js:")

# Render the Mermaid diagram
mermaid(mermaid_diagram)
