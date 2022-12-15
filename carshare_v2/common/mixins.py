from carshare_v2.comments.models import Comment
from carshare_v2.friends.models import Friend, FriendRequest
from carshare_v2.ratings.models import Rating
from carshare_v2.transports.models import Transport


class UserUtilsMixin:
    @staticmethod
    def get_friends_ids(pk):
        ids = [x.requester_id for x in Friend.objects.filter(receiver_id=pk)]
        ids.extend([x.receiver_id for x in Friend.objects.filter(requester_id=pk)])
        return ids

    @staticmethod
    def get_requesters_ids(pk):
        return [x.requester_id for x in FriendRequest.objects.filter(receiver_id=pk)]

    @staticmethod
    def get_current_user_transports(pk):
        current_tranports = [x for x in Transport.objects.filter(driver_id=pk).all().order_by('-date')]
        current_tranports.extend([x for x in Transport.objects.filter(passengers=pk).all().order_by('-date')])
        return current_tranports

    @staticmethod
    def get_commenters_ids(pk):
        return [x.from_profile_id for x in Comment.objects.filter(to_profile_id=pk)]

    @staticmethod
    def get_raters_ids(pk):
        return [x.from_profile_id for x in Rating.objects.filter(to_profile_id=pk)]