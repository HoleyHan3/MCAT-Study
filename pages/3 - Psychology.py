import streamlit as st
import pandas as pd
#from modules.menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
#menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

st.title("Psychology", anchor = False)
st.write("This section covers topics related to psychology.")
st.write("Topics include social psychology, developmental psychology, personality, and more.")

st.header('Psychology', anchor = False, divider='gray')
st.subheader("Features:")
st.write("- Case studies for real-world application.")


with st.expander("**Psychology & Sociology Tricks**"):
    st.markdown("- **Freud's Psychosexual Stages**:  \n Sigmund Freud's stages - Oral, Anal, Phallic, Latency, Genital.")
    st.markdown("- **Kohlberg's Moral Development**:  \n Preconventional, Conventional, Postconventional.")


# Define the common concepts in psychology
psychology_data = {
    "Concept": [
        "Classical Conditioning", "Operant Conditioning", "Social Learning Theory",
        "Cognitive Dissonance", "Maslow's Hierarchy of Needs", "Erikson's Stages of Psychosocial Development",
        "Piaget's Stages of Cognitive Development", "Freud's Psychosexual Stages",
        "Kohlberg's Stages of Moral Development", "The Big Five Personality Traits"
    ],
    "Description": [
        "Learning process that occurs through associations between environmental stimuli and natural responses.",
        "Learning process that occurs through reinforcement and punishment of behaviors.",
        "Learning process that occurs through observation and imitation of others.",
        "Psychological discomfort caused by holding conflicting beliefs or attitudes.",
        "Hierarchy of human needs including physiological, safety, love/belonging, esteem, and self-actualization.",
        "Series of psychosocial stages that individuals pass through over their lifespan.",
        "Stages of cognitive development including sensorimotor, preoperational, concrete operational, and formal operational.",
        "Psychosexual stages of personality development including oral, anal, phallic, latency, and genital.",
        "Stages of moral reasoning including preconventional, conventional, and postconventional levels.",
        "Five broad dimensions of personality including openness, conscientiousness, extraversion, agreeableness, and neuroticism."
    ],
    "Key Figures": [
        "Ivan Pavlov", "B.F. Skinner", "Albert Bandura",
        "Leon Festinger", "Abraham Maslow", "Erik Erikson",
        "Jean Piaget", "Sigmund Freud", "Lawrence Kohlberg", "Various researchers"
    ]
}

# Create a DataFrame from the dictionary
psychology_df = pd.DataFrame(psychology_data)

# Display the DataFrame using st.dataframe
st.dataframe(psychology_df,hide_index=True)

st.subheader("Senses", divider='blue')

st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Light_Waves [label="Light Waves\nExternal visual stimulus\n- Range of visible light: 400-700 nanometers"]
        Cornea_Lens [label="Cornea & Lens\nFocus light onto retina\n- Cornea refracts light, lens fine-tunes focus"]
        Retina [label="Retina\nContains photoreceptors (rods and cones)\n- Rods: low-light vision\n- Cones: color vision"]
        Phototransduction [label="Phototransduction\nConversion of light into neural signals\n- Opsin proteins in photoreceptors initiate signal transduction"]
        Optic_Nerve [label="Optic Nerve\nTransmits neural signals to brain\n- Axons of retinal ganglion cells"]
        Visual_Cortex [label="Visual Cortex\nProcesses and interprets visual signals\n- Located in occipital lobe"]
        
        Light_Waves -> Cornea_Lens
        Cornea_Lens -> Retina
        Retina -> Phototransduction
        Phototransduction -> Optic_Nerve
        Optic_Nerve -> Visual_Cortex
    }
''', use_container_width=True)


st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Sound_Waves [label="Sound Waves\nExternal auditory stimulus\n- Frequency range: 20 Hz to 20 kHz"]
        Ear_Structures [label="Ear Structures\nOuter, middle, and inner ear\n- Middle ear contains ossicles (hammer, anvil, stirrup)"]
        Cochlea [label="Cochlea\nContains hair cells for sound detection\n- Basilar membrane vibrates, hair cells convert motion to electrical signals"]
        Auditory_Transduction [label="Auditory Transduction\nConversion of sound into neural signals\n- Hair cells release neurotransmitters to auditory nerve"]
        Auditory_Nerve [label="Auditory Nerve\nTransmits neural signals to brain\n- Auditory nerve fibers synapse in cochlear nucleus"]
        Auditory_Cortex [label="Auditory Cortex\nProcesses and interprets auditory signals\n- Located in temporal lobe"]
        
        Sound_Waves -> Ear_Structures
        Ear_Structures -> Cochlea
        Cochlea -> Auditory_Transduction
        Auditory_Transduction -> Auditory_Nerve
        Auditory_Nerve -> Auditory_Cortex
    }
''', use_container_width=True)

st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Tastants [label="Tastants\nChemical compounds in food\n- Five basic tastes: sweet, sour, salty, bitter, umami"]
        Taste_Buds [label="Taste Buds\nContain taste receptors\n- Papillae on tongue house taste buds"]
        Taste_Transduction [label="Taste Transduction\nActivation of taste receptors\n- Taste receptors are G-protein coupled"]
        Gustatory_Nerve [label="Gustatory Nerve\nTransmits neural signals to brain\n- Glossopharyngeal nerve (CN IX) and facial nerve (CN VII)"]
        Gustatory_Cortex [label="Gustatory Cortex\nProcesses and interprets taste signals\n- Located in insula and frontal operculum"]
        
        Tastants -> Taste_Buds
        Taste_Buds -> Taste_Transduction
        Taste_Transduction -> Gustatory_Nerve
        Gustatory_Nerve -> Gustatory_Cortex
    }
''', use_container_width=True)

st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Odorants [label="Odorants\nAirborne chemical molecules\n- Thousands of odorants can be detected"]
        Olfactory_Epithelium [label="Olfactory Epithelium\nContains olfactory receptors\n- Located in nasal cavity"]
        Olfactory_Transduction [label="Olfactory Transduction\nBinding of odorants to receptors\n- Olfactory receptors are G-protein coupled"]
        Olfactory_Nerve [label="Olfactory Nerve\nTransmits neural signals to brain\n- Axons form olfactory bulb synapses"]
        Olfactory_Bulb [label="Olfactory Bulb\nInitial processing of olfactory signals\n- Separates into glomeruli for odor discrimination"]
        Olfactory_Cortex [label="Olfactory Cortex\nProcesses and interprets olfactory signals\n- Located in temporal lobe (piriform cortex)"]
        
        Odorants -> Olfactory_Epithelium
        Olfactory_Epithelium -> Olfactory_Transduction
        Olfactory_Transduction -> Olfactory_Nerve
        Olfactory_Nerve -> Olfactory_Bulb
        Olfactory_Bulb -> Olfactory_Cortex
    }
''', use_container_width=True)

st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Tactile_Stimulus [label="Tactile Stimulus\nPhysical contact with objects\n- Includes pressure, vibration, temperature"]
        Skin_Structures [label="Skin Structures\nContains various sensory receptors\n- Mechanoreceptors, thermoreceptors, nociceptors"]
        Tactile_Transduction [label="Tactile Transduction\nActivation of tactile receptors\n- Receptors respond to specific stimuli types"]
        Somatosensory_Nerve [label="Somatosensory Nerve\nTransmits neural signals to brain\n- Axons travel via dorsal root ganglia"]
        Somatosensory_Cortex [label="Somatosensory Cortex\nProcesses and interprets tactile signals\n- Located in parietal lobe"]
        
        Tactile_Stimulus -> Skin_Structures
        Skin_Structures -> Tactile_Transduction
        Tactile_Transduction -> Somatosensory_Nerve
        Somatosensory_Nerve -> Somatosensory_Cortex
    }
''', use_container_width=True)