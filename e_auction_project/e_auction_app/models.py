from datetime import datetime

from django.db import models

# Create your models here.


class UserInformation:
    user_id: int
    email: str

    def set_values(self, user_id, email):
        self.user_id = user_id
        self.email = email

    def get_values(self):
        value = {
            "user_id": self.user_id,
            "email": self.email
        }
        return value


class ProductDetails:
    user_email: str
    product_name: str
    product_detail: str
    min_bid_price: int
    end_time: datetime

    def set_value(self, user_email, product_name, product_detail, min_bid_price, end_time):
        self.user_email = user_email
        self.product_name = product_name
        self.product_detail = product_detail
        self.min_bid_price = min_bid_price
        self.end_time = end_time

    def get_value(self):
        value = {
            "user_email": self.user_email,
            "product_name": self.product_name,
            "product_detail": self.product_detail,
            "min_bid_price": self.min_bid_price,
            "end_time": self.end_time,
        }
        return value
