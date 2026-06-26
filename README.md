# FridgeAI

## Overview

FridgeAI is a smart kitchen assistant that helps users decide what to cook based on the ingredients they already have at home. Users select available items from categorized lists or add custom inputs, and the system analyzes possible recipes that can be prepared with minimal additional purchases. It also suggests missing ingredients and provides direct links to purchase them from popular online grocery platforms.

## Features

* Ingredient selection organized by categories such as vegetables, fruits, grains, dairy, and non-vegetarian items
* Custom ingredient input for flexibility
* Intelligent recipe matching based on available ingredients
* Displays top 5 recipes sorted by match percentage and cooking time
* Highlights missing ingredients required for each recipe
* Provides direct purchase links for missing items from multiple online stores
* Suggests essential items to keep stocked in the kitchen

## How It Works

The system takes user-selected ingredients and compares them against a predefined recipe dataset. Each recipe is scored based on how many required ingredients are already available. Recipes with at least 70 percent ingredient match are considered valid. The top results are then sorted and displayed along with missing items. Additional suggestions help users maintain a well-stocked kitchen.

## Requirements

* Python 3.8 or higher
* Gradio library

### requirements.txt

```
gradio>=4.0.0
```

## Installation and Setup

1. Clone the repository:

   ```
   git clone <your-repo-link>
   cd <project-folder>
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   python app.py
   ```

4. Open the local URL provided in the terminal to access the interface.

## Usage

* Select available ingredients from the categorized lists
* Optionally add custom ingredients
* Click the "Analyze" button
* View recommended recipes, missing ingredients, and purchase links

## Limitations

* Recipe dataset is static and limited to predefined entries
* Ingredient matching is rule-based and does not consider quantities
* Assumes certain items like spices and oil are always available
* Does not provide detailed cooking instructions
* No real-time pricing or availability comparison across stores
* No user personalization or dietary preference handling

## Conclusion

FridgeAI simplifies everyday cooking decisions by bridging the gap between available ingredients and actionable meal ideas. It is designed as a practical tool for households to reduce food waste, save time, and plan meals efficiently.
