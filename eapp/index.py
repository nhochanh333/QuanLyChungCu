from flask import render_template , request

from eapp import app


#mở HTML và trả về giao diện trình duyệt
#request lấy dữ liệu người dùng gửi lên server


# @app.route('/') đường dẫn URL của trang chủ
#Fask gọi hàm index
@app.route('/')
def index():

    products = [{"id": 1,
                 "name": "iPad Pro 2020",
                 "description": "Apple, 128GB, RAM: 6GB",
                 "price": 3700000,
                 "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                 "category_id": 2 },
                {"id": 2,
                 "name": "Laptop",
                 "description": "Apple, 128GB, RAM: 6GB",
                 "price": 37000000,
                 "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                 "category_id": 3 },
                {"id": 3,
                 "name": "Galaxy Note 10 Plus",
                 "description": "Samsung, 64GB, RAML: 6GB",
                 "price": 24000000,
                 "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                 "category_id": 1},
                {"id": 4,
                 "name": "iPad Pro 2020",
                 "description": "Apple, 128GB, RAM: 6GB",
                 "price": 37000000,
                 "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                 "category_id": 2 },
                {"id": 5,
                 "name": "iPad Pro 2020",
                 "description": "Apple, 128GB, RAM: 6GB", "price": 37000000,
                 "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                 "category_id": 2},
                {"id": 6,
                 "name": "Galaxy Note 10 Plus",
                 "description": "Samsung, 64GB, RAML: 6GB", "price": 24000000,
                 "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                 "category_id": 1},
                {"id": 7,
                 "name": "iPad Pro 2020",
                 "description": "Apple, 128GB, RAM: 6GB",
                 "price": 37000000,
                 "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                 "category_id": 2 },
                {"id": 8,
                 "name": "iPad Pro 2020",
                 "description": "Apple, 128GB, RAM: 6GB", "price": 37000000,
                 "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                 "category_id": 2},
                {"id": 9,
                 "name": "Galaxy Note 10 Plus",
                 "description": "Samsung, 64GB, RAML: 6GB", "price": 24000000,
                 "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                 "category_id": 1}
                ]


    # ==========================================
    # 3. CHỨC NĂNG TÌM KIẾM SẢN PHẨM
    # ==========================================
    # request.args.get('kw') lấy giá trị tham số kw từ URL
    # Ví dụ: http://127.0.0.1:5000/?kw=iPad
    # Khi đó kw = 'iPad'
    kw = request.args.get('kw')

    # Kiểm tra người dùng có nhập từ khóa tìm kiếm hay không
    if kw:
         products =[p for p in products
         if p['name'].find(kw) >= 0]


    # ==========================================
    # 4. CHỨC NĂNG LỌC THEO DANH MỤC
    # ==========================================

    cate_id = request.args.get('category_id')
    # Ví dụ: http://127.0.0.1:5000/?category_id=2
    # Khi đó cate_id = '2' (kiểu chuỗi String)
    if cate_id:
        products = [p for p in products
        if p['category_id'] == int(cate_id) ]


    # render_template() mở file index.html trong thư mục templates
    return render_template('index.html',products=products)
    # return render_template('index.html',categories=categories,products=products)


# đường dẫn login
@app.route('/login')
def login_view():
    return render_template('login.html')
@app.route('/register')
def register_view():
    return render_template('register.html')





# @app.context_processor
# - Đây là decorator của Flask.
# - Nó đăng ký một hàm để cung cấp dữ liệu dùng chung cho các template.
# - Khi Flask render một template, dữ liệu được trả về từ hàm này sẽ tự động được đưa vào context của template.
# Bạn có thể sử dụng categories trong:
# - index.html
# - login.html
# - register.html
# - Bất kỳ template nào được Flask render.
@app.context_processor
#tạo hàm dùng chung categories
def common_responses():
    categories = [{
        'id': 1,
        'name': 'Mobile'
    },
        {
            'id': 2,
            'name': 'Tablet'
        }
        , {
            'id': 3,
            'name': 'Laptop'
        }
    ]

    return{
        'categories' : categories
    }

if __name__ == '__main__':
    with app.app_context():
        # debug=True giúp tự động reload khi sửa code
        app.run(debug=True)
