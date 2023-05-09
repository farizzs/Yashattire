from django.urls import path
from . import views

urlpatterns = [
      path('',views.admin_login,name="admin_login"),
      path('homepage/',views.Homepage,name="homepage"),
      path('Addcategory/',views.AddCategory,name="AddCategory"),
      path('savecategory/',views.SaveCategory,name="savecategory"),
      path('displaycategoy/',views.DisplayCategory,name="DisplayCategory"),
      path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
      path('update_category/<int:dataid>/',views.update_category,name="update_category"),
      path('delete_category/<int:dataid>/',views.delete_category,name="delete_category"),
      path('adminlogin_fn/',views.adminlogin_fn,name="adminlogin_fn"),
      path('admin_logout/',views.admin_logout,name="admin_logout"),
      path('Add_Product/',views.Add_Product,name="Add_Product"),
      path('save_Product/',views.save_Product,name="save_Product"),
      path('Display_product/',views.Display_product,name="Display_product"),
      path('Edit_product/<int:dataid>/',views.Edit_product,name="Edit_product"),
      path('Update_product/<int:dataid>/',views.Update_product,name="Update_product"),
      path('Delete_product/<int:dataid>/',views.Delete_product,name="Delete_product"),
      path('Add_Carousel/',views.Add_Carousel,name="Add_Carousel"),
      path('SaveCarousel/',views.SaveCarousel,name="SaveCarousel"),
      path('DisplayCarousel/',views.DisplayCarousel,name="DisplayCarousel"),
      path('Edit_Carousel/<int:dataid>/',views.Edit_Carousel,name="Edit_Carousel"),
      path('update_Carousel/<int:dataid>/',views.update_Carousel,name="update_Carousel"),
      path('delete_carousal/<int:dataid>/',views.delete_carousal,name="delete_carousal"),
]

