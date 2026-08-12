from django.contrib import admin

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
# CATEGORY
# ============================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


# ============================================================
# PRODUCT IMAGE INLINE
# ============================================================

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


# ============================================================
# PRODUCT
# ============================================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "brand",
        "sku",
        "price",
        "discount_price",
        "stock",
        "is_active",
        "is_featured",
        "created_at",
    )

    list_filter = (
        "category",
        "brand",
        "is_active",
        "is_featured",
    )

    search_fields = (
        "name",
        "sku",
        "brand",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    list_editable = (
        "price",
        "discount_price",
        "stock",
        "is_active",
        "is_featured",
    )

    inlines = [
        ProductImageInline
    ]


# ============================================================
# PRODUCT IMAGE
# ============================================================

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "alt_text",
    )

    search_fields = (
        "product__name",
        "alt_text",
    )


# ============================================================
# ADDRESS
# ============================================================

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "full_name",
        "phone",
        "city",
        "state",
        "postal_code",
        "is_default",
    )

    list_filter = (
        "country",
        "state",
        "city",
        "is_default",
    )

    search_fields = (
        "user__username",
        "user__email",
        "full_name",
        "phone",
        "city",
        "postal_code",
    )


# ============================================================
# WISHLIST
# ============================================================

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "product__name",
    )


# ============================================================
# CART ITEM INLINE
# ============================================================

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


# ============================================================
# CART
# ============================================================

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "user__username",
        "user__email",
    )

    inlines = [
        CartItemInline
    ]


# ============================================================
# CART ITEM
# ============================================================

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "cart",
        "product",
        "quantity",
    )

    search_fields = (
        "cart__user__username",
        "product__name",
    )


# ============================================================
# COUPON
# ============================================================

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "discount_type",
        "discount_value",
        "minimum_order_amount",
        "usage_limit",
        "used_count",
        "start_date",
        "expiry_date",
        "is_active",
    )

    list_filter = (
        "discount_type",
        "is_active",
    )

    search_fields = (
        "code",
    )


# ============================================================
# ORDER ITEM INLINE
# ============================================================

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = (
        "product_name",
        "price",
        "quantity",
    )


# ============================================================
# ORDER
# ============================================================

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_number",
        "user",
        "total_amount",
        "status",
        "payment_method",
        "payment_status",
        "created_at",
    )

    list_filter = (
        "status",
        "payment_method",
        "payment_status",
        "created_at",
    )

    search_fields = (
        "order_number",
        "user__username",
        "user__email",
    )

    list_editable = (
        "status",
        "payment_status",
    )

    readonly_fields = (
        "order_number",
        "created_at",
        "updated_at",
    )

    inlines = [
        OrderItemInline
    ]


# ============================================================
# ORDER ITEM
# ============================================================

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product_name",
        "price",
        "quantity",
    )

    search_fields = (
        "order__order_number",
        "product_name",
    )


# ============================================================
# PAYMENT
# ============================================================

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "transaction_id",
        "amount",
        "status",
        "payment_gateway",
        "created_at",
    )

    list_filter = (
        "status",
        "payment_gateway",
    )

    search_fields = (
        "order__order_number",
        "transaction_id",
    )


# ============================================================
# REVIEW
# ============================================================

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "user",
        "rating",
        "is_approved",
        "created_at",
    )

    list_filter = (
        "rating",
        "is_approved",
    )

    search_fields = (
        "product__name",
        "user__username",
        "user__email",
        "title",
        "comment",
    )

    list_editable = (
        "is_approved",
    )


# ============================================================
# RETURN REQUEST
# ============================================================

@admin.register(ReturnRequest)
class ReturnRequestAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "user",
        "status",
        "refund_amount",
        "created_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "order__order_number",
        "user__username",
        "user__email",
        "reason",
    )

    list_editable = (
        "status",
    )


# ============================================================
# NOTIFICATION
# ============================================================

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "title",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
    )

    search_fields = (
        "user__username",
        "user__email",
        "title",
        "message",
    )

    list_editable = (
        "is_read",
    )