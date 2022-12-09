from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

UserModel = get_user_model()


class ProfileDetailsTest(TestCase):
    def test_friend_request_bool__when_sent_request__expect_true(self):
        c = Client()
        profile1 = UserModel.objects.create_user(
            email='abv@abv.bg',
            password='QwertY1!'
        )
        profile2 = UserModel.objects.create_user(
            email='abv2@abv.bg',
            password='QwertY2!'
        )
        c.login(email='abv@abv.bg', password='QwertY1!')

        response = c.post(reverse('friend request send', kwargs={
            'requester_id': profile1.id,
            'receiver_id': profile2.id,
        }), follow=True)

        self.assertTrue(response.context['has_sent_friend_request'])

    def test_friend_request_bool__when_not_sent_request__expect_false(self):
        c = Client()
        profile1 = UserModel.objects.create_user(
            email='abv@abv.bg',
            password='QwertY1!'
        )
        profile2 = UserModel.objects.create_user(
            email='abv2@abv.bg',
            password='QwertY2!'
        )
        c.login(email='abv@abv.bg', password='QwertY1!')

        response = c.get(reverse('profile details', kwargs={
            'pk': profile2.id
        }), follow=True)

        self.assertFalse(response.context['has_sent_friend_request'])

    def test_comment_bool__when_commented__expect_true(self):
        c = Client()
        profile1 = UserModel.objects.create_user(
            email='abv@abv.bg',
            password='QwertY1!'
        )
        profile2 = UserModel.objects.create_user(
            email='abv2@abv.bg',
            password='QwertY2!'
        )
        c.login(email='abv@abv.bg', password='QwertY1!')

        response = c.post(reverse('send comment', kwargs={
            'commenter_id': profile1.id,
            'commented_id': profile2.id,
        }), data={
            'w3review': 'gdsgsd'
        }, follow=True)

        self.assertTrue(response.context['has_commented'])

    def test_commented_bool__when_not_commented__expect_false(self):
        c = Client()
        profile1 = UserModel.objects.create_user(
            email='abv@abv.bg',
            password='QwertY1!'
        )
        profile2 = UserModel.objects.create_user(
            email='abv2@abv.bg',
            password='QwertY2!'
        )
        c.login(email='abv@abv.bg', password='QwertY1!')

        response = c.get(reverse('profile details', kwargs={
            'pk': profile2.id
        }), follow=True)

        self.assertFalse(response.context['has_commented'])

    def test_ratings_bool__when_rated__expect_true(self):
        c = Client()
        profile1 = UserModel.objects.create_user(
            email='abv@abv.bg',
            password='QwertY1!'
        )
        profile2 = UserModel.objects.create_user(
            email='abv2@abv.bg',
            password='QwertY2!'
        )
        c.login(email='abv@abv.bg', password='QwertY1!')

        response = c.post(reverse('give rating', kwargs={
            'giver_id': profile1.id,
            'receiver_id': profile2.id,
        }), data={
            'rating': 5
        }, follow=True)

        self.assertTrue(response.context['has_rated'])

    def test_ratings_bool__when_not_rated__expect_false(self):
        c = Client()
        profile1 = UserModel.objects.create_user(
            email='abv@abv.bg',
            password='QwertY1!'
        )
        profile2 = UserModel.objects.create_user(
            email='abv2@abv.bg',
            password='QwertY2!'
        )
        c.login(email='abv@abv.bg', password='QwertY1!')

        response = c.get(reverse('profile details', kwargs={
            'pk': profile2.id
        }), follow=True)

        self.assertFalse(response.context['has_rated'])

    def test_total_rating__expect_correct_result(self):
        c = Client()
        profile1 = UserModel.objects.create_user(
            email='abv@abv.bg',
            password='QwertY1!'
        )
        profile2 = UserModel.objects.create_user(
            email='abv2@abv.bg',
            password='QwertY2!'
        )
        c.login(email='abv@abv.bg', password='QwertY1!')

        response = c.post(reverse('give rating', kwargs={
            'giver_id': profile1.id,
            'receiver_id': profile2.id,
        }), data={
            'rating': 5
        }, follow=True)

        self.assertEqual(5, response.context['rating'])

    def test_current_comment__expect_correct_result(self):
        c = Client()
        profile1 = UserModel.objects.create_user(
            email='abv@abv.bg',
            password='QwertY1!'
        )
        profile2 = UserModel.objects.create_user(
            email='abv2@abv.bg',
            password='QwertY2!'
        )
        c.login(email='abv@abv.bg', password='QwertY1!')

        response = c.post(reverse('send comment', kwargs={
            'commenter_id': profile1.id,
            'commented_id': profile2.id,
        }), data={
            'w3review': 'gdsgsd'
        }, follow=True)

        self.assertEqual('gdsgsd', response.context['current_comment'].content)

    def test_friend_bool__when_accept_friend_request__expect_true(self):
        c = Client()
        profile1 = UserModel.objects.create_user(
            email='abv@abv.bg',
            password='QwertY1!'
        )
        profile2 = UserModel.objects.create_user(
            email='abv2@abv.bg',
            password='QwertY2!'
        )
        c.login(email='abv@abv.bg', password='QwertY1!')

        c.post(reverse('friend request send', kwargs={
            'requester_id': profile1.id,
            'receiver_id': profile2.id,
        }), follow=True)

        c.post(reverse('friend request accept', kwargs={
            'requester_id': profile1.id,
            'receiver_id': profile2.id,
        }), follow=True)

        response = c.get(reverse('profile details', kwargs={
            'pk': profile2.id
        }))

        self.assertTrue(response.context['is_friend'])

    def test_friend_bool__when_reject_friend_request__expect_false(self):
        c = Client()
        profile1 = UserModel.objects.create_user(
            email='abv@abv.bg',
            password='QwertY1!'
        )
        profile2 = UserModel.objects.create_user(
            email='abv2@abv.bg',
            password='QwertY2!'
        )
        c.login(email='abv@abv.bg', password='QwertY1!')

        c.post(reverse('friend request send', kwargs={
            'requester_id': profile1.id,
            'receiver_id': profile2.id,
        }), follow=True)

        response = c.get(reverse('profile details', kwargs={
            'pk': profile2.id
        }))

        self.assertFalse(response.context['is_friend'])
