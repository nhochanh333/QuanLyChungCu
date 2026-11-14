import math
from flask import render_template , request

from eapp import app, dao
from eapp.models import Product


#mở HTML và trả về giao diện trình duyệt
#request lấy dữ liệu người dùng gửi lên server


# @app.route('/') đường dẫn URL của trang chủ
#Fask gọi hàm index
@app.route('/')
def index():
    # lấy count của product
    count = dao.counr_product()
    page_size = app.config['PAGE_SIZE']


    products = dao.load_products(kw=request.args.get('kw'),cate_id=request.args.get('category_id'),page=int(request.args.get('page',1)))

    # render_template() mở file index.html trong thư mục templates
    return render_template('index.html', products=products, page=math.ceil(count / page_size))
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
    # categories = [{
    #     'id': 1,
    #     'name': 'Mobile'
    # },
    #     {
    #         'id': 2,
    #         'name': 'Tablet'
    #     }
    #     , {
    #         'id': 3,
    #         'name': 'Laptop'
    #     }
    # ]
    return{
        'categories' : dao.load_categories()
    }

if __name__ == '__main__':
    with app.app_context():
        from eapp import admin
        # debug=True giúp tự động reload khi sửa code
        app.run(debug=True)
