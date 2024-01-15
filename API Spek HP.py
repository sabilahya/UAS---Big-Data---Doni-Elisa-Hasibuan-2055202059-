from flask import Flask, jsonify, request

app = Flask(__name__)

# Data spesifikasi beberapa ponsel
mobiles = [
    {
        "id" : 1,
        "brand": "Samsung",
        "model": "Galaxy S21",
        "release_year": 2021,
        "display": {
            "size": "6.2 inches",
            "resolution": "2400 x 1080 pixels",
            "type": "Dynamic AMOLED 2X"
        },
        "processor": "Exynos 2100 / Snapdragon 888",
        "ram": "8GB",
        "storage": "128GB / 256GB / 512GB",
        "camera": {
            "main": "12 MP (wide), 64 MP (telephoto), 12 MP (ultrawide)",
            "front": "10 MP"
        },
        "battery": "4000 mAh",
        "operating_system": "Android 11, One UI 3.1",
        "price": "$799"
    },
    {
        "id" : 2,
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "release_year": 2021,
        "display": {
            "size": "6.1 inches",
            "resolution": "1170 x 2532 pixels",
            "type": "Super Retina XDR OLED"
        },
        "processor": "Apple A15 Bionic",
        "ram": "6GB",
        "storage": "128GB / 256GB / 512GB / 1TB",
        "camera": {
            "main": "12 MP (wide), 12 MP (telephoto), 12 MP (ultrawide)",
            "front": "12 MP"
        },
        "battery": "3095 mAh",
        "operating_system": "iOS 15",
        "price": "$999"
    },
    {
        "id" : 3,
        "brand": "Xiaomi",
        "model": "Redmi Note 10",
        "release_year": 2021,
        "display": {
            "size": "6.43 inches",
            "resolution": "1080 x 2400 pixels",
            "type": "Super AMOLED"
        },
        "processor": "Snapdragon 678",
        "ram": "4GB / 6GB",
        "storage": "64GB / 128GB",
        "camera": {
            "main": "48 MP (wide), 8 MP (ultrawide), 2 MP (macro), 2 MP (depth)",
            "front": "13 MP"
        },
        "battery": "5000 mAh",
        "operating_system": "Android 11, MIUI 12",
        "price": "$199"
    },
    {
        "id" : 4,
        "brand": "Xiaomi",
        "model": "Mi 11 Lite",
        "release_year": 2022,
        "display": {
            "size": "6.55 inches",
            "resolution": "1080 x 2400 pixels",
            "type": "AMOLED"
        },
        "processor": "Snapdragon 732G",
        "ram": "6GB / 8GB",
        "storage": "64GB / 128GB",
        "camera": {
            "main": "64 MP (wide), 8 MP (ultrawide), 5 MP (macro)",
            "front": "16 MP"
        },
        "battery": "4250 mAh",
        "operating_system": "Android 11, MIUI 13",
        "price": "$199"
    },
    {
        "id" : 5,
        "brand": "OnePlus",
        "model": "OnePlus 9 Pro",
        "release_year": 2023,
        "display": {
            "size": "6.7 inches",
            "resolution": "1440 x 3216 pixels",
            "type": "Fluid AMOLED"
        },
        "processor": "Snapdragon 888",
        "ram": "8GB / 12GB",
        "storage": "128GB / 256GB",
        "camera": {
            "main": "48 MP (wide), 50 MP (ultrawide), 8 MP (macro)",
            "front": "16 MP"
        },
        "battery": "4500 mAh",
        "operating_system": "OxygenOS 11, Android 11",
        "price": "$599"
    },
    {
        "id" : 6,
        "brand": "Google",
        "model": "Google Pixel 6 Pro",
        "release_year": 2023,
        "display": {
            "size": "6.7 inches",
            "resolution": "1440 x 3120 pixels",
            "type": "OLED"
        },
        "processor": " Google Tensor",
        "ram": "12GB",
        "storage": "128GB / 256GB",
        "camera": {
            "main": "50 MP (wide), 12 MP (ultrawide), 48 MP (macro)",
            "front": "11 MP"
        },
        "battery": "5300 mAh",
        "operating_system": "Android 12",
        "price": "$699"
    },
    {
        "id" : 7,
        "brand": "Realme",
        "model": "Realme GT 5",
        "release_year": 2023,
        "display": {
            "size": "6.43 inches",
            "resolution": "1080 x 2400 pixels",
            "type": "Super AMOLED"
        },
        "processor": " Google Tensor",
        "ram": "12GB",
        "storage": "128GB / 256GB",
        "camera": {
            "main": "64 MP (wide), 8 MP (ultrawide), 2 MP (macro)",
            "front": "16 MP"
        },
        "battery": "4500 mAh",
        "operating_system": "Realme UI 2.0, Android 11",
        "price": "$599"
    },
    {
        "id" : 8,
        "brand": "Huawei",
        "model": "Huawei P40 Pro",
        "release_year": 2023,
        "display": {
            "size": "6.43 inches",
            "resolution": "1080 x 2400 pixels",
            "type": "OLED"
        },
        "processor": "HiSilicon Kirin 990",
        "ram": "8GB",
        "storage": "128GB / 256GB",
        "camera": {
            "main": "50 MP (wide), 40 MP (ultrawide), 12 MP (macro)",
            "front": "32 MP"
        },
        "battery": "4200 mAh",
        "operating_system": "EMUI 10.1, Android 10",
        "price": "$799"
    },
    {
        "id" : 9,
        "brand": "Vivo",
        "model": "Vivo X60 Pro+",
        "release_year": 2023,
        "display": {
            "size": "6.56 inches",
            "resolution": "1080 x 2376 pixels",
            "type": "AMOLED"
        },
        "processor": "Snapdragon 888",
        "ram": "8GB / 12GB",
        "storage": "128GB / 256GB",
        "camera": {
            "main": "50 MP (wide), 48 MP (ultrawide), 8 MP (macro)",
            "front": "32 MP"
        },
        "battery": "4200 mAh",
        "operating_system": "Funtouch OS 11.1, Android 11",
        "price": "$699"
    },
    {
        "id" : 10,
        "brand": "Asus",
        "model": "Asus ROG Phone 5",
        "release_year": 2023,
        "display": {
            "size": "6.78 inches",
            "resolution": "1080 x 2448 pixels",
            "type": "AMOLED"
        },
        "processor": "Snapdragon 888",
        "ram": "8GB / 12GB / 16GB",
        "storage": "128GB / 256GB",
        "camera": {
            "main": "64 MP (wide), 13 MP (ultrawide), 5 MP (macro)",
            "front": "24 MP"
        },
        "battery": "6000 mAh",
        "operating_system": "ROG UI, Android 11",
        "price": "$999"
    }
]

# Endpoint untuk mendapatkan semua data ponsel
@app.route('/api/mobiles', methods=['GET'])
def get_all_mobiles():
    return jsonify(mobiles)

# Endpoint untuk menambahkan data spesifikasi ponsel
@app.route('/api/mobiles', methods=['POST'])
def add_mobile():
    global mobiles
    new_mobile = request.json  # Mendapatkan data baru dari body permintaan JSON
    # Mendapatkan ID terbesar dan menambahkan 1 untuk membuat ID baru
    new_mobile_id = max([mobile.get('id', 0) for mobile in mobiles]) + 1
    new_mobile['id'] = new_mobile_id  # Menambahkan ID baru ke data ponsel baru
    mobiles.append(new_mobile)  # Menambahkan data ponsel baru ke dalam daftar
    return jsonify(new_mobile), 201  # Memberikan respons dengan data yang telah ditambahkan

# Endpoint untuk mengedit data spesifikasi ponsel berdasarkan ID
@app.route('/api/mobiles/<int:mobile_id>', methods=['PUT'])
def update_mobile(mobile_id):
    global mobiles
    mobile = next((m for m in mobiles if m['id'] == mobile_id), None)
    if mobile:
        data = request.json  # Mendapatkan data baru dari body permintaan JSON
        # Mengupdate data spesifikasi ponsel
        mobile.update(data)
        return jsonify({'message': f'Mobile with ID {mobile_id} has been updated'}), 200
    else:
        return jsonify({'message': f'Mobile with ID {mobile_id} not found'}), 404

# Endpoint untuk mendapatkan spesifikasi ponsel berdasarkan merek
@app.route('/api/mobiles/<brand>', methods=['GET'])
def get_mobiles_by_brand(brand):
    brand_mobiles = [mobile for mobile in mobiles if mobile['brand'].lower() == brand.lower()]
    if len(brand_mobiles) > 0:
        return jsonify({'mobiles': brand_mobiles})
    else:
        return jsonify({'error': 'Ponsel tidak ditemukan'}), 404
    
# Endpoint untuk menghapus data spesifikasi ponsel berdasarkan ID
@app.route('/api/mobiles/<int:mobile_id>', methods=['DELETE'])
def delete_mobile(mobile_id):
    global mobiles
    mobile_ids = [mobile['id'] for mobile in mobiles]
    if mobile_id in mobile_ids:
        mobiles = [mobile for mobile in mobiles if mobile['id'] != mobile_id]
        return jsonify({'message': f'Mobile with ID {mobile_id} has been deleted'}), 200
    else:
        return jsonify({'message': f'Mobile with ID {mobile_id} not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)