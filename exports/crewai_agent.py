from crewai import Agent

crispr_off_target_cleavage_predictor = Agent(
    role="Crispr Off Target Cleavage Predictor",
    goal="Deliver high-precision autonomous Crispr Off Target Cleavage Predictor operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
