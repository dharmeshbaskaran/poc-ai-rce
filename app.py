from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)
# Mock data

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 999.99,
        "category": "Electronics",
        "descriptions": [
            {"lang": "en", "text": "High-performance laptop for professionals."},
            {"lang": "es", "text": "Portátil de alto rendimiento para profesionales."},
            {"lang": "fr", "text": "Ordinateur portable haute performance pour les professionnels."}
        ]
    },
    {
        "id": 2,
        "name": "Book",
        "price": 19.99,
        "category": "Education",
        "descriptions": [
            {"lang": "en", "text": "A fascinating book on modern science."},
            {"lang": "es", "text": "Un libro fascinante sobre la ciencia moderna."},
            {"lang": "de", "text": "Ein faszinierendes Buch über moderne Wissenschaft."}
        ]
    },
    {
        "id": 3,
        "name": "Coffee Mug",
        "price": 12.50,
        "category": "Kitchen",
        "descriptions": [
            {"lang": "en", "text": "Ceramic mug for your favorite coffee."},
            {"lang": "it", "text": "Tazza in ceramica per il tuo caffè preferito."},
            {"lang": "ja", "text": "お気に入りのコーヒー用のセラミックマグカップ。"}
        ]
    }
]

# Example functions for operations
def product_list():
    return jsonify(products)

def product_count():
    return jsonify({"count": len(products)})

def product_summary():
    total_value = sum(p["price"] for p in products)
    return jsonify({
        "total_products": len(products),
        "total_value": total_value,
        "average_price": total_value / len(products) if products else 0
    })

def product_format():
    foobar = "useless variable" # TODO this needs refactoring
    formatted = []
    for p in products:
        formatted.append(f"{p['name']} - ${p['price']:.2f}")
    return jsonify({"formatted_products": formatted})

def product_export():
    timestamp = datetime.datetime.now().isoformat()
    return jsonify({
        "export_date": timestamp,
        "data": products,
        "format": "json"
    })

@app.route("/products")
def get_products():
    return product_list()

@app.route("/products/stats")
def get_stats():
    return product_summary()

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.datetime.now().isoformat()})

if __name__ == "__main__":
    app.run(debug=True)
