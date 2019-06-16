from product.models import Product, VendorProduct, VendorStock
from userprofile.models import User
from django.views.decorators.csrf import csrf_exempt
from basecontroller import BaseController


""" List of all Products with name filter"""
@csrf_exempt
def product_filter(request):
	if request.method == 'GET':
		name = request.get('name')
		if name:
			products = Product.objects.filter(name=name)
		else:
			products = Product.objects.all()
		return BaseController.respond_with_paginated_collection(200, products, ProductTransformer)
	return BaseController().respond_with_error(404, 'We will look into it right away.')


""" adding product and makinf is_active true if user is store manager else creating product, vendor product, 
		but making is_active false and sending it to approval list"""
@csrf_exempt
def add_new_product(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		name = data['name']
		mrp = data['mrp'],
		batch_number = data['batchNumber']
		batch_date = data['batch_date']
		quantity = data['quantity']
		vendor = data['vendorId']
		user_id = data['userId']
		product = Product.objects.first(name=name).first()
		user = User.objects.get(id=user_id)
		role = user.roles.filter(name='Store Manager')
		if product:
			return BaseController().respond_with_error(400, "Product already exists")
		product = Product.objects.create(name=name, is_active=True)
		vendor = User.objects.get(id=vendor)
		vendor_product = VendorProduct.objects.create(vendor=vendor, name=name, product=product)
		vendor_stock = VendorStock.objects.create(vendor_product=vendor_product, batch_date=batch_date, 
				batch_number=batch_number, quantity=quantity
				)
		if not role:
			approval = Approval.objects.create(product=product, requested_by_id=user_id, is_approved=False)
			approval.product.is_active = False
			approval.save()
		return BaseController().respond_with_success(200, "Product added successfully")
	return BaseController().respond_with_error(404, 'We will look into it right away.')


""" Allow only store manager to update details"""
@csrf_exempt
def update_product(request, vendor_stock_id):
	if request.method == 'PUT':
		mrp = data['mrp'],
		batch_number = data['batchNumber']
		batch_date = data['batch_date']
		quantity = data['quantity']
		user_id = data['userId']
		user = User.objects.get(id=user_id)
		role = user.roles.filter(name='Store Manager')
		if role:
			VendorStock.objects.filter(id=vendor_stock_id).update(batch_date=batch_date, 
				batch_number=batch_number, quantity=quantity, mrp=mrp)
			return BaseController().respond_with_success(200, "Product updated successfully")
		else:
			return BaseController().respond_with_error(400, 'Permission Denied')
	return BaseController().respond_with_error(404, 'No method found')

	
""" The prducts which are to be merged by store manager"""
@csrf_exempt
def needs_approval_list(request):
	if request.method == 'GET':
		user_id = data['userId']
		user = User.objects.get(id=user_id)
		role = user.roles.filter(name='Store Manager')
		if role:
			approvals = Approval.objects.filter(is_approved=False)
			return BaseController().respond_with_paginated_collection(200, approvals, ApprovalTransformer)
		else:
			return BaseController().respond_with_success(200, "No products")
	return BaseController().respond_with_error(404, 'No method found')


""" If user approves then we make the is_active flag true esle if rejects we delete it from
		product, vendorproduct, approval"""
@csrf_exempt
def approve_or_decline_request(request, approval_id):
	if request.method == 'PUT':
		data = json.loads(request.body)
		is_approved = data['is_approved']
		approval_user_id = data['approvalUserId']
		approval = Approval.objects.filter(id=approval_id).first()
		if approval:
			if is_approved:
				product = approval.product
				product.is_active = True
				product.save()
				approval.approved_by = True
				approval.save()
			else:
				vendor_pro = vendor.vendor_products
				vendor_pro.vendor_stock.delete()
				vendor_pro.delete()
				approval.product.delete()
				approval.delete()




	

