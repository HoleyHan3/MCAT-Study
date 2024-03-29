import streamlit as st
import pandas as pd
#from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
#menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

st.title("Biology")
st.write("This section covers topics related to biology.")
st.write("Topics include molecular biology, cell biology, genetics, metabolism, and more.")

#col1, col2 = st.columns(2)

#with col1:
st.header('Biology', anchor = False , divider='blue')
st.subheader("Molecules:", anchor = False)
st.write("- Detailed explanations of key concepts.")
st.write("- Interactive diagrams and animations.")


# Define the main types of molecules, categories, and additional helpful info for MCAT
molecules_data = {
    "Molecule": [
        "Proteins", "Carbohydrates", "Lipids", "Nucleic Acids",
        "Enzymes", "Hormones", "Antibodies", "Neurotransmitters",
        "ATP", "Steroids", "Glycogen", "Cell Membrane",
        "Ribosomes", "Mitochondria", "Chlorophyll"
    ],
    "Category": [
        "Key Ones to Know", "Key Ones to Know", "Key Ones to Know", "Key Ones to Know",
        "Key Ones to Know", "Key Ones to Know", "Key Ones to Know", "Key Ones to Know",
        "Key Ones to Know", "Key Ones to Know", "Basic Structure", "Basic Structure",
        "Basic Structure", "Basic Structure", "Basic Structure"
    ],
    "Description": [
        "Large molecules composed of amino acids, serving various functions.",
        "Sugars, starches, and fibers found in foods, providing energy and structure.",
        "Diverse molecules including fats, oils, phospholipids, and cholesterol.",
        "DNA and RNA, storing and transmitting genetic information.",
        "Biological catalysts that speed up chemical reactions in living organisms.",
        "Signaling molecules that regulate various physiological processes in the body.",
        "Proteins produced by the immune system to identify and neutralize foreign substances.",
        "Chemical messengers that transmit signals across synapses in the nervous system.",
        "The primary energy currency of cells, used to power cellular processes.",
        "Lipids with a specific chemical structure, including hormones such as testosterone and estrogen.",
        "A polysaccharide that serves as a stored form of glucose in animals.",
        "The phospholipid bilayer that surrounds cells, regulating the passage of molecules and ions.",
        "Cellular structures responsible for protein synthesis.",
        "Organelles that generate energy through cellular respiration.",
        "The pigment in chloroplasts that absorbs light energy during photosynthesis."
    ],
    "Helpful_Info": [
        "Important for enzyme catalysis, structural support, immune defense, and cell signaling.",
        "Primary source of energy, essential for cell structure and function.",
        "Important for energy storage, cell membrane structure, and signaling molecules.",
        "Store and transmit genetic information, crucial for protein synthesis and cellular processes.",
        "Catalyze specific chemical reactions, increasing reaction rates without being consumed.",
        "Regulate physiological processes such as metabolism, growth, and reproduction.",
        "Identify and neutralize foreign substances such as bacteria and viruses.",
        "Regulate nerve impulses and synaptic transmission in the nervous system.",
        "Used to store and transfer energy within cells for various metabolic processes.",
        "Regulate metabolism, inflammation, immune response, and other physiological processes.",
        "Used as a fuel reserve and for energy storage in animals.",
        "Regulates the movement of substances in and out of the cell.",
        "Translate mRNA into proteins during protein synthesis.",
        "Generate ATP through cellular respiration, providing energy for cellular processes.",
        "Absorb light energy during photosynthesis to drive the conversion of carbon dioxide and water into glucose."
    ]
}

# Create a DataFrame from the dictionary
df_molecules = pd.DataFrame(molecules_data)

# Display the DataFrame
st.dataframe(df_molecules, hide_index=True)


# Display the flowchart using st.graphviz_chart
st.header("Cell Signaling Pathways")
st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Identify_Signaling_Molecules [label="Identify Signaling Molecules\n(hormones, neurotransmitters)"]
        Determine_Receptors [label="Determine Receptors\n(activation, signaling cascades)"]
        Trace_Downstream_Effects [label="Trace Downstream Effects\n(gene expression, protein synthesis)"]
        Consider_Feedback_Mechanisms [label="Consider Feedback Mechanisms\n(regulation)\n1. Positive Feedback: Amplifies Signal\n2. Negative Feedback: Dampens Signal"]
        
        Identify_Signaling_Molecules -> Determine_Receptors
        Determine_Receptors -> Trace_Downstream_Effects
        Trace_Downstream_Effects -> Consider_Feedback_Mechanisms
    }
''', use_container_width=True)

st.subheader("Biological Processes:", anchor = False)

# Define the Krebs cycle steps with products, side-products, reaction types, enzymes/coenzymes, and energy requirements
krebs_cycle_data = {
    "Step": [
        "Acetyl-CoA + Oxaloacetate → Citrate",
        "Citrate → Isocitrate",
        "Isocitrate → α-Ketoglutarate",
        "α-Ketoglutarate → Succinyl-CoA",
        "Succinyl-CoA → Succinate",
        "Succinate → Fumarate",
        "Fumarate → Malate",
        "Malate → Oxaloacetate"
    ],
    "Reaction Type": [
        "Condensation",
        "Isomerization",
        "Decarboxylation",
        "Decarboxylation",
        "Substrate-level phosphorylation",
        "Hydration",
        "Dehydration",
        "Reduction"
    ],
    "Enzyme/Coenzyme": [
        "Citrate synthase",
        "Aconitase",
        "Isocitrate dehydrogenase",
        "α-Ketoglutarate dehydrogenase complex (KGDHC)",
        "Succinyl-CoA synthetase",
        "Succinate dehydrogenase",
        "Fumarase",
        "Malate dehydrogenase"
    ],
    "Products/Side-Products": [
        "Citrate",
        "Isocitrate",
        "α-Ketoglutarate, CO2, NADH",
        "Succinyl-CoA, CO2, NADH",
        "Succinate, GTP",
        "Fumarate, FADH2",
        "Malate",
        "Oxaloacetate, NADH"
    ],
    "Energy Required": [
        "No",
        "No",
        "No",
        "Yes (NAD+ → NADH)",
        "Yes (GDP + Pi → GTP)",
        "No",
        "No",
        "Yes (NAD+ → NADH)"
    ]
}

# Create a DataFrame for the Krebs cycle
krebs_cycle_df = pd.DataFrame(krebs_cycle_data)

# Display the DataFrame using st.dataframe
st.dataframe(krebs_cycle_df, hide_index=True)

st.subheader("Anatomy & Physiology:", anchor = "A&P", divider='blue')

# Define the organ systems in the human body
organ_systems_data = {
    "Organ System": [
        "Integumentary System", "Skeletal System", "Muscular System", "Nervous System",
        "Endocrine System", "Cardiovascular System", "Lymphatic System", "Respiratory System",
        "Digestive System", "Urinary System", "Reproductive System"
    ],
    "Key Functions": [
        "Protection, temperature regulation, sensory reception",
        "Support, protection of internal organs, movement",
        "Movement, posture maintenance, heat generation",
        "Integration and coordination of body activities, sensory reception",
        "Hormone production, homeostasis regulation",
        "Nutrient and waste transport, immune response",
        "Immunity, fluid balance, fat absorption",
        "Gas exchange (oxygen and carbon dioxide), pH regulation",
        "Nutrient breakdown and absorption, waste elimination",
        "Blood filtration, electrolyte balance, waste removal",
        "Gamete production, hormone secretion, embryonic development"
    ],
    "Main Organs": [
        "Skin, hair, nails, sweat glands",
        "Bones, cartilage, ligaments, tendons",
        "Skeletal muscles, smooth muscles, cardiac muscle",
        "Brain, spinal cord, nerves, sensory organs",
        "Pituitary gland, thyroid gland, pancreas",
        "Heart, blood vessels, blood",
        "Lymph nodes, spleen, thymus gland",
        "Lungs, trachea, bronchi, diaphragm",
        "Mouth, esophagus, stomach, intestines",
        "Kidneys, ureters, bladder, urethra",
        "Testes, ovaries, uterus, fallopian tubes"
    ]
}

# Create a DataFrame from the dictionary
organ_systems_df = pd.DataFrame(organ_systems_data)

# Display the DataFrame using st.dataframe
st.dataframe(organ_systems_df, hide_index=True)

# Define the basic types of tissues
tissue_data = {
    "Tissue Type": [
        "Epithelial Tissue", "Connective Tissue", "Muscle Tissue", "Nervous Tissue"
    ],
    "Description": [
        "Covers body surfaces and lines cavities; involved in absorption, secretion, and protection; forms glands.",
        "Provides structural support, connects and cushions organs, stores energy, and transports substances.",
        "Contracts to produce movement in the body; includes skeletal, cardiac, and smooth muscle.",
        "Transmits electrical impulses and supports rapid communication between different parts of the body."
    ],
    "Key Features": [
        "Cells tightly packed with little extracellular matrix; avascular; classified by shape and layering.",
        "Abundant extracellular matrix composed of fibers (collagen, elastin) and ground substance; diverse cell types.",
        "Highly contractile cells with actin and myosin filaments; voluntary (skeletal) or involuntary (smooth, cardiac).",
        "Composed of neurons and neuroglia; neurons transmit signals, while neuroglia support and protect neurons."
    ],
    "Examples": [
        "Skin epithelium (epidermis), lining of digestive tract (intestinal epithelium), kidney tubules, glands (e.g., sweat glands).",
        "Bone, cartilage, adipose tissue, blood, tendons, ligaments, loose and dense connective tissue.",
        "Skeletal muscles (biceps, quadriceps), smooth muscles (intestinal muscles, blood vessels), cardiac muscle (heart).",
        "Brain, spinal cord, peripheral nerves, sensory receptors."
    ],
    "Locations": [
        "Skin, respiratory tract, gastrointestinal tract, genitourinary tract, glands (endocrine and exocrine).",
        "Throughout the body including bones, cartilage, blood, lymph, adipose tissue, tendons, ligaments, and organs.",
        "Attached to bones (skeletal muscle), walls of internal organs (smooth muscle), heart (cardiac muscle).",
        "Central nervous system (brain and spinal cord), peripheral nerves, sensory organs."
    ],
    "Key Processes/Characteristics": [
        "Protection, absorption, secretion, excretion, filtration, sensory reception.",
        "Support, protection, transportation, energy storage, immune response, insulation.",
        "Contraction, movement, posture maintenance, heat production, organ support.",
        "Electrical signaling, neurotransmission, integration of sensory information, motor control."
    ]
}

# Create a DataFrame from the dictionary
tissue_df = pd.DataFrame(tissue_data)

# Display the DataFrame using st.dataframe
st.dataframe(tissue_df, hide_index=True)

st.subheader("Immunology", anchor = "Immune", divider='blue')

st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Hematopoietic_Stem_Cell [label="Hematopoietic Stem Cell\n(Bone Marrow)\nCapable of self-renewal and differentiation into various blood cell lineages"]
        Common_Lymphoid_Progenitor [label="Common Lymphoid Progenitor\nGives rise to cells of lymphoid lineage\n- T cells (T lymphocytes)\n- B cells (B lymphocytes)\n- Natural Killer (NK) cells"]
        Common_Myeloid_Progenitor [label="Common Myeloid Progenitor\nDifferentiates into cells of myeloid lineage\n- Granulocytes (Neutrophils, Eosinophils, Basophils)\n- Monocytes\n- Dendritic Cells\n- Megakaryocytes"]
        Lymphoid_Lineage [label="Lymphoid Lineage\nIncludes mature lymphocytes responsible for adaptive immune responses"]
        Myeloid_Lineage [label="Myeloid Lineage\nComprises innate immune cells involved in immediate defense against pathogens"]
        
        Hematopoietic_Stem_Cell -> Common_Lymphoid_Progenitor
        Hematopoietic_Stem_Cell -> Common_Myeloid_Progenitor
        Common_Lymphoid_Progenitor -> Lymphoid_Lineage
        Common_Myeloid_Progenitor -> Myeloid_Lineage
    }
''', use_container_width=True)

# Define the types of immune cells with detailed descriptions and additional categories
immune_cells_data = {
    "Cell Type": [
        "T lymphocytes (T cells)",
        "B lymphocytes (B cells)",
        "Natural killer (NK) cells",
        "Macrophages",
        "Neutrophils",
        "Eosinophils",
        "Basophils",
        "Dendritic cells",
        "Mast cells"
    ],
    "Description": [
        "Coordinate immune responses, kill infected cells, regulate immune reactions",
        "Produce antibodies, present antigens, regulate immune responses",
        "Destroy virus-infected cells and tumor cells",
        "Engulf and digest pathogens and cellular debris, present antigens",
        "Phagocytize pathogens, release antimicrobial substances",
        "Combat multicellular parasites, modulate allergic responses",
        "Release histamine and other mediators of inflammation",
        "Capture and present antigens to T cells, initiate adaptive immune responses",
        "Release histamine and other mediators of inflammation, contribute to allergic responses"
    ],
    "Recognition Mechanism": [
        "Recognize antigens presented by MHC molecules",
        "Bind antigens via B cell receptors (BCRs) and recognize by T cells",
        "Recognize altered or infected cells lacking MHC class I molecules",
        "Recognize pathogen-associated molecular patterns (PAMPs) and damage-associated molecular patterns (DAMPs)",
        "Recognize and phagocytize pathogens via pattern recognition receptors (PRRs)",
        "Recognize parasites and allergens, regulate immune responses",
        "Respond to allergens and release histamine",
        "Capture antigens in peripheral tissues and present to T cells in lymph nodes",
        "Recognize allergens and pathogens, release histamine and other mediators"
    ],
    "Development": [
        "Develop in the thymus",
        "Develop in the bone marrow",
        "Develop in bone marrow and mature in lymphoid tissues",
        "Derived from monocytes in bone marrow",
        "Develop in bone marrow",
        "Develop in bone marrow",
        "Develop in bone marrow",
        "Develop in bone marrow and differentiate in peripheral tissues",
        "Develop in bone marrow"
    ],
    "Lifespan": [
        "Long-lived, can persist for years",
        "Varies, some short-lived (days to weeks) and others long-lived (years)",
        "Variable, can persist for several days to weeks",
        "Variable, can persist from days to months",
        "Short-lived, typically hours to days",
        "Variable, can persist for days to weeks",
        "Short-lived, typically hours to days",
        "Variable, can persist for days to weeks",
        "Variable, can persist for days to weeks"
    ],
    "Movement": [
        "Circulate in blood and lymph, migrate to lymphoid organs and tissues",
        "Circulate in blood and lymph, migrate to lymphoid organs and tissues",
        "Circulate in blood and lymph, migrate to sites of infection or inflammation",
        "Reside in tissues throughout the body, migrate to sites of infection or inflammation",
        "Circulate in blood and migrate to sites of infection or inflammation",
        "Circulate in blood and migrate to sites of inflammation or allergic reactions",
        "Circulate in blood and migrate to sites of inflammation or allergic reactions",
        "Reside in peripheral tissues and migrate to lymphoid organs",
        "Reside in tissues throughout the body, migrate to sites of inflammation or allergic reactions"
    ]
}

# Create a DataFrame for the types of immune cells
immune_cells_df = pd.DataFrame(immune_cells_data)

# Apply formatting
immune_cells_df_styled = immune_cells_df.style.set_properties(**{'text-align': 'left'}).set_table_styles(
    [{'selector': 'th', 'props': [('text-align', 'left')]}]
)
# Display the DataFrame using st.dataframe
st.dataframe(immune_cells_df_styled, hide_index=True)


# Create a dictionary of data
immune_process_data = {
    "Immune Response Step": ["Recognition", "Activation", "Effector Phase", "Clearance", "Memory"],
    "Innate Immunity": [
        "PAMPs recognized by PRRs",
        "Inflammatory cytokines released",
        "Phagocytosis, NK cell killing, inflammation",
        "Removal of pathogens and debris",
        "None"
    ],
    "Adaptive Immunity": [
        "Antigens recognized by BCRs or TCRs",
        "Antigen presentation to T cells, T cell activation and clonal selection",
        "Cytotoxic T cells kill infected cells, B cells produce antibodies",
        "Antibody neutralization, complement activation",
        "Memory T and B cells generated"
    ],
    "Examples": [
        "Macrophages phagocytize bacteria, Dendritic cells capture and present antigens",
        "Macrophages release cytokines, DCs activate naive T cells",
        "Macrophages engulf pathogens, CTLs lyse virus-infected cells, Plasma cells secrete antibodies",
        "Antibodies neutralize toxins, Complement opsonizes pathogens for phagocytosis",
        "Memory B cells provide rapid secondary response upon reinfection"
    ]
}

# Create a DataFrame
df_immune_process = pd.DataFrame(immune_process_data)

# Print the DataFrame with color coding for innate and adaptive immunity
st.dataframe(df_immune_process, hide_index=True)

# Define the data for the enhanced tables
ig_data = {
    "Immunoglobulin (Ig)": ["IgG", "IgM", "IgA", "IgE"],
    "Description": [
        "- Most abundant antibody in the bloodstream. Provides long-term immunity against bacterial and viral infections. Crosses the placenta to provide passive immunity to the fetus. Activates complement and enhances phagocytosis.",
        "- First antibody produced during the primary immune response. Exists mainly as a pentamer in the bloodstream. Effective at agglutination of pathogens and activation of the complement system.",
        "- Predominantly found in mucosal secretions such as saliva, tears, and breast milk. Provides defense against pathogens at mucosal surfaces. Acts as a first line of defense against infections in the respiratory, gastrointestinal, and genitourinary tracts.",
        "- Plays a key role in allergic reactions and defense against parasitic infections. Binds to mast cells and basophils, triggering the release of histamine and other mediators in response to allergens."
    ],
    "Key Cell Interactions": [
        "Interacts with macrophages, neutrophils, and NK cells.",
        "Binds to B cells and activates complement.",
        "Interacts with epithelial cells, neutrophils.",
        "Binds to mast cells and basophils."
    ],
    "Processes/Diseases": [
        "Opsonization, neutralization, passive immunity, autoimmune disorders",
        "Acute infections, autoimmune disorders, agglutination",
        "Mucosal immunity, respiratory infections, autoimmune disorders",
        "Allergic reactions, parasitic infections, asthma"
    ]
}

# Create a DataFrame for the enhanced tables
ig_df = pd.DataFrame(ig_data)

# Display the DataFrame using st.dataframe
st.dataframe(ig_df, hide_index=True)


# Define the Krebs cycle steps with products, side-products, reaction types, enzymes/coenzymes, and energy requirements
krebs_cycle_data = {
    "Step": [
        "Acetyl-CoA + Oxaloacetate → Citrate",
        "Citrate → Isocitrate",
        "Isocitrate → α-Ketoglutarate",
        "α-Ketoglutarate → Succinyl-CoA",
        "Succinyl-CoA → Succinate",
        "Succinate → Fumarate",
        "Fumarate → Malate",
        "Malate → Oxaloacetate"
    ],
    "Reaction Type": [
        "Condensation",
        "Isomerization",
        "Decarboxylation",
        "Decarboxylation",
        "Substrate-level phosphorylation",
        "Hydration",
        "Dehydration",
        "Reduction"
    ],
    "Enzyme/Coenzyme": [
        "Citrate synthase",
        "Aconitase",
        "Isocitrate dehydrogenase",
        "α-Ketoglutarate dehydrogenase complex (KGDHC)",
        "Succinyl-CoA synthetase",
        "Succinate dehydrogenase",
        "Fumarase",
        "Malate dehydrogenase"
    ],
    "Products/Side-Products": [
        "Citrate",
        "Isocitrate",
        "α-Ketoglutarate, CO2, NADH",
        "Succinyl-CoA, CO2, NADH",
        "Succinate, GTP",
        "Fumarate, FADH2",
        "Malate",
        "Oxaloacetate, NADH"
    ],
    "Energy Required": [
        "No",
        "No",
        "No",
        "Yes (NAD+ → NADH)",
        "Yes (GDP + Pi → GTP)",
        "No",
        "No",
        "Yes (NAD+ → NADH)"
    ]
}

# Create a DataFrame for the Krebs cycle
krebs_cycle_df = pd.DataFrame(krebs_cycle_data)

# Display the DataFrame using st.dataframe
st.dataframe(krebs_cycle_df, hide_index=True)

st.subheader("Cell Biology", anchor = "CellBio", divider='blue')


# Create a dictionary containing the organelle information
organelle_data = {
    "Organelle": ["Mitochondria", "Nucleus", "Endoplasmic Reticulum (ER)", "Golgi Apparatus", "Lysosomes", "Peroxisomes", "Endosomes", "Chloroplasts"],
    "Structure": ["Double membrane structure (outer and inner membranes)", "Surrounded by a double membrane (nuclear envelope)", "Rough ER (with ribosomes) and Smooth ER (without ribosomes)", "Flattened membranous sacs (cisternae)", "Membrane-bound vesicles containing digestive enzymes", "Single membrane-bound organelles with oxidative enzymes", "Membrane-bound vesicles involved in sorting and processing", "Double membrane structure containing thylakoids and stroma"],
    "Function": ["- Inner membrane highly folded into cristae surrounding the matrix \n - Responsible for ATP production through cellular respiration (glycolysis, citric acid cycle, oxidative phosphorylation) \n - Involved in apoptosis \n - Maternally inherited",
                 "- Houses genetic material (DNA) \n - Controls cellular activities \n - Site of transcription (mRNA synthesis) \n - Assembly of ribosomal subunits",
                 "- Rough ER: Protein synthesis and folding \n - Smooth ER: Lipid synthesis, detoxification, calcium ion storage",
                 "- Modifies, sorts, and packages proteins and lipids into vesicles for transport",
                 "- Break down cellular waste, foreign particles, and organelles through hydrolysis \n - Fuse with endocytic vesicles and autophagosomes for degradation",
                 "- Break down fatty acids, amino acids, detoxify harmful substances such as hydrogen peroxide",
                 "- Sort, process, and traffic endocytosed material \n - Mature into lysosomes or fuse with other organelles for material exchange",
                 "- Site of photosynthesis, converting light energy into chemical energy (ATP and sugars) \n - Contains chlorophyll for capturing light energy"],
    "High-Yield Facts": ["- Inner membrane subunits include complexes I (NADH dehydrogenase), II (succinate dehydrogenase), III (cytochrome bc1 complex), IV (cytochrome c oxidase), and V (ATP synthase). \n - The outer membrane contains porins, allowing the passage of small molecules. \n - Mitochondrial DNA encodes for a small number of essential proteins and RNA molecules.",
                         "- The nucleus is the control center of the cell, containing instructions for cellular activities encoded in DNA. \n - It communicates with the cytoplasm through nuclear pores. \n - The nucleolus contains subunits involved in ribosome assembly, such as ribosomal RNA (rRNA) and ribosomal proteins.",
                         "- Rough ER subunits include ribosomes attached to the membrane, involved in protein synthesis. \n - Smooth ER contains enzymes for lipid synthesis and detoxification, such as cytochrome P450 enzymes. \n - The rough ER synthesizes proteins that are destined for secretion or incorporation into the cell membrane.",
                         "- The Golgi apparatus consists of cis, medial, and trans cisternae, involved in sequential processing of proteins. \n - It adds carbohydrate groups to proteins (glycosylation). \n - Golgi subunits include enzymes like glycosyltransferases and phosphatases involved in protein modification.",
                         "- Lysosomes contain acidic hydrolases that work optimally at low pH. \n - They are involved in recycling cellular components through autophagy. \n - Lysosomes are involved in the degradation of cellular debris and foreign particles.",
                         "- Peroxisomes contain catalase, an enzyme that breaks down hydrogen peroxide into water and oxygen. \n - They are involved in lipid metabolism and detoxification. \n - Peroxisomes play a role in the oxidation of fatty acids and the synthesis of certain lipids.",
                         "- Endosomes are involved in the internalization and processing of cell surface receptors. \n - They play a role in signaling pathways and antigen presentation. \n - Endosomes mature into late endosomes or fuse with lysosomes for degradation.",
                         "- Chloroplasts are unique to plant cells and some protists. \n - They contain their own DNA and ribosomes, similar to mitochondria. \n - Thylakoid membranes contain chlorophyll and other pigments for light absorption during photosynthesis."]
}

# Create the DataFrame
organelle_df = pd.DataFrame(organelle_data)

# Display the DataFrame using st.dataframe
st.dataframe(organelle_df, hide_index=True)

# Define the key topics in cell biology with additional categories and suggestions
cell_biology_data = {
    "Topic": [
        "Cell Structure", "Cell Membrane", "Cell Organelles", "Cell Nucleus",
        "Cell Cycle", "Cell Signaling", "Cell Metabolism", "Cellular Transport",
        "Cellular Respiration", "Photosynthesis", "Cellular Reproduction"
    ],
    "Key Functions": [
        "Organization and components of a cell",
        "Regulation of molecular traffic in and out of the cell",
        "Specialized compartments performing specific functions",
        "Storage and processing of genetic information",
        "Regulation of cell growth and division",
        "Communication between cells and their environment",
        "Biochemical processes supporting cell growth, maintenance, and reproduction",
        "Movement of ions and molecules across cell membranes",
        "Conversion of biochemical energy into ATP",
        "Conversion of light energy into chemical energy",
        "Generation of new cells for growth, repair, and reproduction"
    ],
    "Key Characteristics": [
        "Cytoplasm, cytoskeleton, and cell membrane organization",
        "Lipid bilayer structure, selective permeability, and receptor proteins",
        "Endoplasmic reticulum, Golgi apparatus, mitochondria, etc.",
        "Nuclear envelope, chromatin, nucleolus, etc.",
        "Interphase, mitosis, cytokinesis, checkpoints, etc.",
        "Hormones, neurotransmitters, second messengers, etc.",
        "Glycolysis, Krebs cycle, oxidative phosphorylation, etc.",
        "Diffusion, osmosis, facilitated diffusion, active transport, etc.",
        "Glycolysis, Krebs cycle, electron transport chain, etc.",
        "Light-dependent reactions, Calvin cycle, etc.",
        "Mitosis, meiosis, cell growth, DNA replication, etc."
    ],
    "Key Processes": [
        "Cellular organization, maintenance, and reproduction",
        "Regulation of molecular traffic and signal transduction",
        "Specialized functions within the cell",
        "Storage, processing, and expression of genetic information",
        "Regulation of cell growth, division, and reproduction",
        "Communication and response to external stimuli",
        "Energy production, utilization, and storage",
        "Movement of ions, molecules, and particles",
        "Oxidation of glucose and other molecules",
        "Conversion of light energy into chemical energy",
        "Generation of new cells for growth, repair, and reproduction"
    ],
    "Key Examples": [
        "Cytoskeleton, plasma membrane, organelles",
        "Phospholipids, cholesterol, integral proteins",
        "Endoplasmic reticulum, mitochondria, lysosomes",
        "Nuclear envelope, chromatin, nucleolus",
        "Interphase, prophase, metaphase, anaphase",
        "Hormones, growth factors, neurotransmitters",
        "Glycolysis, Krebs cycle, ATP synthesis",
        "Diffusion of oxygen, active transport of ions",
        "Glycolysis, Krebs cycle, electron transport chain",
        "Thylakoid membrane, stroma, chlorophyll",
        "Mitosis in somatic cells, meiosis in germ cells"
    ]
}

# Create a DataFrame from the dictionary
cell_biology_df = pd.DataFrame(cell_biology_data)

# Display the DataFrame using st.dataframe
st.dataframe(cell_biology_df, hide_index=True)

st.subheader("Genetics", anchor = "Genetics", divider='blue')

# Define the key topics in genetics with concepts for MCAT problem-solving
genetics_data = {
    "Topic": [
        "DNA Structure", "DNA Replication", "Gene Expression", "Genetic Variation",
        "Mendelian Genetics", "Non-Mendelian Genetics", "Chromosomal Abnormalities", "Population Genetics",
        "Genetic Engineering", "Genomics", "Epigenetics"
    ],
    "Key Concepts for Problem-Solving": [
        "Understanding the double helix structure and base pairing rules (A-T, G-C)",
        "Identifying the enzymes involved and steps in DNA replication",
        "Analyzing transcription factors, RNA processing, and translation mechanisms",
        "Calculating allele frequencies, understanding genetic drift, and Hardy-Weinberg equilibrium",
        "Applying Punnett squares, test crosses, and probability calculations",
        "Solving dihybrid and trihybrid crosses, understanding sex-linked inheritance",
        "Interpreting karyotypes, recognizing chromosomal aberrations and their implications",
        "Understanding allele frequencies, genetic markers, and evolutionary forces",
        "Utilizing recombinant DNA techniques, CRISPR-Cas9, and gene expression systems",
        "Analyzing genomic data, identifying genes, and regulatory elements",
        "Understanding epigenetic modifications, gene regulation, and environmental influences"
    ]
}

# Create a DataFrame from the dictionary
genetics_df = pd.DataFrame(genetics_data)

# Display the DataFrame using st.dataframe
st.dataframe(genetics_df, hide_index=True)

