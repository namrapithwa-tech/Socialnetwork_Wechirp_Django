from django.urls import path
from .views import postlistview,postdetailview,posteditview,postdeleteview,commentdelete,profileview,profileeditview,AddFollower,RemoveFollower,AddLike,DisLike,UserSearch,ListFollower,AddCommentLike,AddCommentDisLike,CommentReplayView,PostNotification,FollowNotification,ThreadNotification,RemoveNotification,CreateThread,ListThreads,ThreadView,CreateMessage,SharedPostView,Explore

urlpatterns = [
    path('',postlistview.as_view(),name='post-list'),
    path('explore/',Explore.as_view(),name='explore'),
    path('post/<int:pk>',postdetailview.as_view(),name='post-detail'),
    path('post/edit/<int:pk>',posteditview.as_view(),name='post-edit'),
    path('post/delete/<int:pk>',postdeleteview.as_view(),name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/',commentdelete.as_view(),name='comment-delete'),
    path('post/<int:post_pk>/commnet/<int:pk>/like',AddCommentLike.as_view(),name='comment-like'),
    path('post/<int:post_pk>/commnet/<int:pk>/dislike',AddCommentDisLike.as_view(),name='comment-dislike'),
    path('post/<int:post_pk>/commnet/<int:pk>/repaly',CommentReplayView.as_view(),name='comment-replay'),
    path('post/<int:pk>/like',AddLike.as_view(),name='like'),
    path('post/<int:pk>/dislike',DisLike.as_view(),name='dislike'),
    path('post/<int:pk>/share',SharedPostView.as_view(),name='share-post'),
    path('profile/<int:pk>',profileview.as_view(),name='profile'),
    path('profile/edit/<int:pk>',profileeditview.as_view(),name='profile-edit'),
    path('profile/<int:pk>/followers/',ListFollower.as_view(),name='list-followers'),
    path('profile/<int:pk>/followers/add',AddFollower.as_view(),name='add-follower'),
    path('profile/<int:pk>/followers/remove',RemoveFollower.as_view(),name='remove-follower'),
    path('search/',UserSearch.as_view(),name='profile-search'),
    path('notification/<int:notification_pk>/post/<int:post_pk>',PostNotification.as_view(),name='post-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>',FollowNotification.as_view(),name='follow-notification'),
    path('notification/<int:notification_pk>/thread/<int:object_pk>',ThreadNotification.as_view(),name='thread-notification'),
    path('notification/delete/<int:notification_pk>',RemoveNotification.as_view(),name='delete-notification'),
    path('inbox/',ListThreads.as_view(),name='inbox'),
    path('inbox/create-thread/',CreateThread.as_view(),name='create-thread'),
    path('inbox/<int:pk>/',ThreadView.as_view(),name='thread'),    
    path('inbox/<int:pk>/create-message',CreateMessage.as_view(),name='create-message'),    

]