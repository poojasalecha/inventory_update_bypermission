from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.product_filter, name='list'),
    url(r'^addnewproduct$', views.add_new_product, name='add-new-product'),
    url(r'^(?P<vendor_stock_id>\d+)/updateproduct$', views.update_product, name='update-product'),
    url(r'^needsapproval$', views.needs_approval_list, name='needs-approval-list'),
    url(r'^(?P<approval_id>\d+)/approvedecline$', views.approve_or_decline_request, name='approve-or-decline'),
   ]