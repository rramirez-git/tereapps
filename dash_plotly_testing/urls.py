from django.contrib.auth.decorators import login_required
from django.urls import path

import dash_plotly_testing.views as views

# base_path => dash-plotly/

urlpatterns = [
    path('', login_required()(
        views.ViewIndex.as_view()),
        name='dpt_test_index'),
    path('test1/', login_required()(
        views.ViewTest1.as_view()),
        name='dpt_test1'),
    path('test2/', login_required()(
        views.ViewTest2.as_view()),
        name='dpt_test2'),
    path('test3/', login_required()(
        views.ViewTest3.as_view()),
        name='dpt_test3'),
    path('test4/', login_required()(
        views.ViewTest4.as_view()),
        name='dpt_test4'),
    path('test5/', login_required()(
        views.ViewTest5.as_view()),
        name='dpt_test5'),
]
