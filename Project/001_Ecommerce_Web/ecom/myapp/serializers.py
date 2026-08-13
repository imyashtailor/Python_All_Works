from django.contrib.auth.models import User
from rest_framework import serializers
from myapp.models import *


from .models import (
    Category,
    Product,
    ProductImage,
    Address,
    Wishlist,
    Cart,
    CartItem,
    Coupon,
    Order,
    OrderItem,
    Payment,
    Review,
    ReturnRequest,
    Notification,
)


# ============================================================
# USER
# ============================================================

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        user.save()
        return user


# ============================================================
# CATEGORY
# ============================================================

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "image",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


# ============================================================
# PRODUCT IMAGE
# ============================================================

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = [
            "id",
            "product",
            "image",
            "alt_text",
        ]
        read_only_fields = ["id"]


# ============================================================
# PRODUCT
# ============================================================

class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    final_price = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        read_only=True
    )

    is_in_stock = serializers.BooleanField(
        read_only=True
    )

    images = ProductImageSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "category_name",
            "name",
            "slug",
            "description",
            "price",
            "discount_price",
            "final_price",
            "brand",
            "sku",
            "stock",
            "image",
            "images",
            "specifications",
            "is_active",
            "is_featured",
            "is_in_stock",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "final_price",
            "is_in_stock",
            "created_at",
            "updated_at",
        ]


# ============================================================
# ADDRESS
# ============================================================

class AddressSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Address
        fields = [
            "id",
            "user",
            "full_name",
            "phone",
            "address_line_1",
            "address_line_2",
            "city",
            "state",
            "country",
            "postal_code",
            "is_default",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "created_at",
        ]


# ============================================================
# WISHLIST
# ============================================================

class WishlistSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    product_price = serializers.DecimalField(
        source="product.final_price",
        max_digits=12,
        decimal_places=2,
        read_only=True
    )

    product_image = serializers.ImageField(
        source="product.image",
        read_only=True
    )

    class Meta:
        model = Wishlist
        fields = [
            "id",
            "user",
            "product",
            "product_name",
            "product_price",
            "product_image",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "created_at",
        ]


# ============================================================
# CART ITEM
# ============================================================

class CartItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    product_image = serializers.ImageField(
        source="product.image",
        read_only=True
    )

    product_price = serializers.DecimalField(
        source="product.final_price",
        max_digits=12,
        decimal_places=2,
        read_only=True
    )

    total_price = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = CartItem
        fields = [
            "id",
            "cart",
            "product",
            "product_name",
            "product_image",
            "product_price",
            "quantity",
            "total_price",
        ]

        read_only_fields = [
            "id",
            "cart",
            "product_name",
            "product_image",
            "product_price",
            "total_price",
        ]

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError(
                "Quantity must be at least 1."
            )

        return value


# ============================================================
# CART
# ============================================================

class CartSerializer(serializers.ModelSerializer):

    items = CartItemSerializer(
        many=True,
        read_only=True
    )

    total_price = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = Cart
        fields = [
            "id",
            "user",
            "items",
            "total_price",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "total_price",
            "created_at",
            "updated_at",
        ]


# ============================================================
# COUPON
# ============================================================

class CouponSerializer(serializers.ModelSerializer):

    is_valid = serializers.BooleanField(
        read_only=True
    )

    class Meta:
        model = Coupon
        fields = [
            "id",
            "code",
            "discount_type",
            "discount_value",
            "minimum_order_amount",
            "max_discount",
            "usage_limit",
            "used_count",
            "start_date",
            "expiry_date",
            "is_active",
            "is_valid",
        ]

        read_only_fields = [
            "id",
            "used_count",
            "is_valid",
        ]

    def validate(self, attrs):
        discount_type = attrs.get(
            "discount_type",
            getattr(
                self.instance,
                "discount_type",
                None
            )
        )

        discount_value = attrs.get(
            "discount_value",
            getattr(
                self.instance,
                "discount_value",
                None
            )
        )

        if (
            discount_type == Coupon.DiscountType.PERCENTAGE
            and discount_value is not None
            and discount_value > 100
        ):
            raise serializers.ValidationError({
                "discount_value": (
                    "Percentage discount cannot exceed 100."
                )
            })

        start_date = attrs.get(
            "start_date",
            getattr(self.instance, "start_date", None)
        )

        expiry_date = attrs.get(
            "expiry_date",
            getattr(self.instance, "expiry_date", None)
        )

        if start_date and expiry_date and start_date > expiry_date:
            raise serializers.ValidationError({
                "expiry_date": (
                    "Expiry date must be after start date."
                )
            })

        return attrs


# ============================================================
# ORDER ITEM
# ============================================================

class OrderItemSerializer(serializers.ModelSerializer):

    total_price = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "order",
            "product",
            "product_name",
            "price",
            "quantity",
            "total_price",
        ]

        read_only_fields = [
            "id",
            "product_name",
            "price",
            "total_price",
        ]


# ============================================================
# PAYMENT
# ============================================================

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            "id",
            "order",
            "transaction_id",
            "amount",
            "status",
            "payment_gateway",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


# ============================================================
# ORDER
# ============================================================

class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        read_only=True
    )

    payment = PaymentSerializer(
        read_only=True
    )

    address_details = AddressSerializer(
        source="address",
        read_only=True
    )

    coupon_code = serializers.CharField(
        source="coupon.code",
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "order_number",
            "address",
            "address_details",
            "coupon",
            "coupon_code",
            "subtotal",
            "discount",
            "shipping_charge",
            "total_amount",
            "status",
            "payment_method",
            "payment_status",
            "notes",
            "items",
            "payment",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "order_number",
            "subtotal",
            "discount",
            "total_amount",
            "status",
            "payment_status",
            "items",
            "payment",
            "address_details",
            "coupon_code",
            "created_at",
            "updated_at",
        ]


# ============================================================
# REVIEW
# ============================================================

class ReviewSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(
        source="user.username",
        read_only=True
    )

    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "user_name",
            "product",
            "product_name",
            "rating",
            "title",
            "comment",
            "is_approved",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "user_name",
            "product_name",
            "is_approved",
            "created_at",
            "updated_at",
        ]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 1 and 5."
            )

        return value


# ============================================================
# RETURN REQUEST
# ============================================================

class ReturnRequestSerializer(serializers.ModelSerializer):

    order_number = serializers.CharField(
        source="order.order_number",
        read_only=True
    )

    user_name = serializers.CharField(
        source="user.username",
        read_only=True
    )

    class Meta:
        model = ReturnRequest
        fields = [
            "id",
            "order",
            "order_number",
            "user",
            "user_name",
            "reason",
            "status",
            "refund_amount",
            "admin_note",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "user_name",
            "order_number",
            "status",
            "refund_amount",
            "admin_note",
            "created_at",
            "updated_at",
        ]


# ============================================================
# NOTIFICATION
# ============================================================

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = [
            "id",
            "user",
            "title",
            "message",
            "is_read",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "created_at",
        ]

