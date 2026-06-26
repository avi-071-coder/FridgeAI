import gradio as gr
from collections import defaultdict

CATEGORIES = {
    "Vegetables": [
        "tomato","onion","potato","carrot","capsicum","brinjal",
        "patal","karela","lauki","bhindi","tinda","torai",
        "cabbage","beans","peas","palak","jackfruit"
    ],
    "Fruits": [
        "apple","banana","mango","guava","papaya","orange","grapes"
    ],
    "Grains": ["rice","atta"],
    "Dal": ["dal","moong dal","chana dal","rajma"],
    "Dairy": ["milk","curd","paneer","butter","cheese"],
    "Non-Veg": ["chicken","eggs","mutton"],
    "Spices": ["spices"],
    "Others": ["oil","salt","bread","cornflour","ketchup","cream","besan"]
}

RECIPES = [
{"name":"Aloo Sabji","time":15,"ingredients":["potato","spices","oil"]},
{"name":"Aloo Baingan","time":20,"ingredients":["potato","brinjal","spices","oil"]},
{"name":"Aloo Patal Sabji","time":20,"ingredients":["potato","patal","spices","oil"]},
{"name":"Bhindi Sabji","time":18,"ingredients":["bhindi","spices","oil"]},
{"name":"Karela Sabji","time":20,"ingredients":["karela","spices","oil"]},
{"name":"Lauki Sabji","time":18,"ingredients":["lauki","spices","oil"]},
{"name":"Torai Sabji","time":18,"ingredients":["torai","spices","oil"]},
{"name":"Tinda Sabji","time":20,"ingredients":["tinda","spices","oil"]},
{"name":"Cabbage Sabji","time":18,"ingredients":["cabbage","spices","oil"]},
{"name":"Beans Sabji","time":18,"ingredients":["beans","spices","oil"]},

{"name":"Aloo Bhujiya","time":15,"ingredients":["potato","spices","oil"]},
{"name":"Karela Bhujiya","time":18,"ingredients":["karela","spices","oil"]},
{"name":"Patal Bhujiya","time":18,"ingredients":["patal","spices","oil"]},
{"name":"Bhindi Bhujiya","time":15,"ingredients":["bhindi","spices","oil"]},

{"name":"Baingan Bharta","time":25,"ingredients":["brinjal","onion","tomato","spices","oil"]},
{"name":"Palak Paneer","time":25,"ingredients":["palak","paneer","onion","tomato","spices","oil"]},
{"name":"Paneer Butter Masala","time":30,"ingredients":["paneer","butter","tomato","cream","spices"]},
{"name":"Paneer Chilli","time":20,"ingredients":["paneer","capsicum","cornflour","ketchup","spices","oil"]},
{"name":"Mixed Veg Sabji","time":22,"ingredients":["vegetables","spices","oil"]},

{"name":"Kathal Sabji","time":30,"ingredients":["jackfruit","spices","oil"]},
{"name":"Kathal Masala","time":35,"ingredients":["jackfruit","onion","tomato","spices","oil"]},
{"name":"Kathal Pakora","time":20,"ingredients":["jackfruit","besan","spices","oil"]},

{"name":"Simple Dal","time":15,"ingredients":["dal","spices","oil"]},
{"name":"Dal Tadka","time":18,"ingredients":["dal","onion","spices","oil"]},
{"name":"Moong Dal Fry","time":15,"ingredients":["moong dal","spices","oil"]},
{"name":"Chana Dal Fry","time":20,"ingredients":["chana dal","onion","spices","oil"]},
{"name":"Rajma Masala","time":30,"ingredients":["rajma","onion","tomato","spices","oil"]},

{"name":"Jeera Rice","time":15,"ingredients":["rice","spices","oil"]},
{"name":"Veg Pulao","time":25,"ingredients":["rice","vegetables","spices","oil"]},
{"name":"Egg Fried Rice","time":18,"ingredients":["rice","eggs","oil","spices"]},
{"name":"Veg Fried Rice","time":20,"ingredients":["rice","vegetables","oil","spices"]},

{"name":"Chicken Curry","time":35,"ingredients":["chicken","onion","tomato","spices","oil"]},
{"name":"Chili Chicken","time":25,"ingredients":["chicken","capsicum","cornflour","ketchup","spices","oil"]},
{"name":"Egg Curry","time":20,"ingredients":["eggs","onion","tomato","spices","oil"]},
{"name":"Egg Bhurji","time":10,"ingredients":["eggs","onion","spices","oil"]},

{"name":"Mutton Curry","time":45,"ingredients":["mutton","onion","tomato","spices","oil"]},
{"name":"Mutton Masala","time":50,"ingredients":["mutton","onion","spices","oil"]},
{"name":"Mutton Fry","time":35,"ingredients":["mutton","spices","oil"]},

{"name":"Veg Omelette","time":10,"ingredients":["eggs","vegetables","spices"]},
{"name":"Paneer Bhurji","time":15,"ingredients":["paneer","onion","tomato","spices","oil"]},

{"name":"Fruit Shake","time":5,"ingredients":["milk","fruits"]},
{"name":"Fruit Lassi","time":5,"ingredients":["curd","fruits"]},
]

STORES = {
    "Blinkit": "https://blinkit.com/search?q=",
    "Zepto": "https://www.zeptonow.com/search/",
    "BigBasket": "https://www.bigbasket.com/search/?q=",
    "Flipkart": "https://www.flipkart.com/search?q="
}

def process(selected, custom):
    items = set(selected)
    items.update(["spices","oil"])

    if custom:
        items.update([i.strip().lower() for i in custom.split(",")])

    matched = []

    for r in RECIPES:
        have = sum(1 for i in r["ingredients"] if i in items)
        score = have / len(r["ingredients"])

        if score >= 0.7:
            matched.append((score, r))

    matched.sort(key=lambda x: (-x[0], x[1]["time"]))
    top = matched[:5]

    if not top:
        return "<div>No strong matches. Add more ingredients.</div>"

    recipe_html = ""
    missing_all = set()

    for score, r in top:
        missing = [i for i in r["ingredients"] if i not in items]
        missing_all.update(missing)

        recipe_html += f"""
        <div style="padding:14px;margin:10px 0;border-radius:10px;background:var(--block-background-fill);border:1px solid var(--border-color-primary);">
        <b>{r['name']}</b><br>
        Time: {r['time']} min | Match: {round(score*100)}%<br>
        Ingredients: {", ".join(r['ingredients'])}<br>
        Missing: {", ".join(missing) if missing else "None"}
        </div>
        """

    shop_html = ""
    for item in list(missing_all):
        shop_html += f"<b>{item}</b><br>"
        for s, link in STORES.items():
            shop_html += f'<a href="{link}{item}" target="_blank">{s}</a> '
        shop_html += "<br><br>"

    stock_html = "<div>Keep basics like onion, potato, rice, dal, milk for better coverage.</div>"

    return f"""
    <div style="display:flex;flex-direction:column;gap:16px;">

    <div style="padding:16px;border-radius:12px;background:var(--block-background-fill);border:1px solid var(--border-color-primary);">
    <b>Your Kitchen</b><br>
    {", ".join(items)}
    </div>

    <div style="padding:16px;border-radius:12px;background:var(--block-background-fill);border:1px solid var(--border-color-primary);">
    <b>Top Recipes</b>
    {recipe_html}
    </div>

    <div style="padding:16px;border-radius:12px;background:var(--block-background-fill);border:1px solid var(--border-color-primary);">
    <b>Buy Missing Items</b><br>
    {shop_html}
    </div>

    <div style="padding:16px;border-radius:12px;background:var(--block-background-fill);border:1px solid var(--border-color-primary);">
    <b>Smart Stock Suggestions</b><br>
    {stock_html}
    </div>

    </div>
    """

with gr.Blocks(title="FridgeAI", theme=gr.themes.Soft()) as demo:

    gr.Markdown("# FridgeAI")

    inputs = []

    for cat, items in CATEGORIES.items():
        with gr.Accordion(cat, open=False):
            cb = gr.CheckboxGroup(items)
            inputs.append(cb)

    custom = gr.Textbox(label="Add custom items")

    btn = gr.Button("Analyze")

    output = gr.HTML()

    def wrapper(*vals):
        selected = []
        for v in vals[:-1]:
            selected.extend(v)
        return process(selected, vals[-1])

    btn.click(wrapper, inputs=inputs + [custom], outputs=output)

demo.launch()