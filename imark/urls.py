from django.urls import path

from imark import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('add-img/<int:set_id>', views.ImgAddView.as_view(), name='test_form'),
    path('add-note/<int:set_id>/<int:img_id>', views.AddNoteView.as_view(), name='add_note'),
    path('create/set/', views.SetCreateView.as_view(), name='set_create'),
    path('set/list/', views.SetListView.as_view(), name='set_list'),
    path('set/<int:pk>', views.SetDetailView.as_view(), name='set_det'),
    path('create/img/', views.ImgCreatView.as_view(), name='img_create'),
    path('create/note/', views.NoteCreateView.as_view(), name='note_create'),
    path('img-detail/<int:pk>', views.ImgDetailView.as_view(), name='img_det'),
    path('img-update/<int:pk>', views.UpdateImgView.as_view(), name='img_update'),
    path('note-update/<int:pk>', views.UpdateNoteView.as_view(), name='note_update'),
    path('note-delete/<int:pk>', views.NoteDelete.as_view(), name='note_delete'),
    path('set-delete/<int:pk>', views.SetDelete.as_view(), name='set_delete'),
    path('img-delete/<int:pk>', views.ImgDelete.as_view(), name='img_delete'),
]