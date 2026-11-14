from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = '*^hihiedhcdijwd'

# Cấu hình kết nối MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = ( "mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
)

# Tắt cảnh báo theo dõi thay đổi dữ liệu
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 5
# Khởi tạo SQLAlchemy
db = SQLAlchemy(app=app)