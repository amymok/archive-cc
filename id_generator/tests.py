import string

from django.core.cache import cache
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from id_generator.throttling import BurstRateThrottle, SustainedRateThrottle


class IdGeneratorTests(APITestCase):

    def setUp(self):
        self.orig_burst_rate = BurstRateThrottle.rate
        self.orig_sustained_rate = SustainedRateThrottle.rate
        # Setting rates to something really big so it doesn't affect testing
        BurstRateThrottle.rate = '2000/min'
        SustainedRateThrottle.rate = '2000/day'

    def tearDown(self):
        cache.clear()
        BurstRateThrottle.rate = self.orig_burst_rate
        SustainedRateThrottle.rate = self.orig_sustained_rate

    def test_generate_miro_subject_id__valid(self):
        """
        Ensure we can generate a Miro ID
        """
        url = reverse('id_generator:generate')
        data = {
            'study_id': 'interesting-study.prestigious.edu',
            'study_subject_id': '�👍'
        }

        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.data), dict)
        self.assertEqual(len(response.data.keys()), 1)
        self.assertIn("miro_subject_id", response.data)
        self.assertTrue(all(
            c in string.hexdigits
            for c in response.data["miro_subject_id"]
        ))

    def test_generate_miro_subject_id_repeat__valid(self):
        """
        Ensure we can generate a Miro ID repeatedly
        """
        url = reverse('id_generator:generate')
        data = {
            'study_id': 'interesting-study.prestigious.edu',
            'study_subject_id': '�👍'
        }

        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.data), dict)
        self.assertEqual(len(response.data.keys()), 1)
        self.assertIn("miro_subject_id", response.data)
        self.assertTrue(all(
            c in string.hexdigits
            for c in response.data["miro_subject_id"]
        ))

        exp_id = response.data["miro_subject_id"]
        for i in range(10):
            response = self.client.get(url, data)
            self.assertEqual(response.data.get("miro_subject_id"), exp_id)

    def test_generate_miro_subject_id__invalid(self):
        """
        Ensure we will receive errors and 400 if invalid parameters provided
        """
        url = reverse('id_generator:generate')
        data = {
            'study_id': ' ',
            'study_subject_id': ' '
        }

        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.data.keys()), 2)
        self.assertIn("study_id", response.data)
        self.assertEqual(
            ["This field may not be blank."],
            response.data["study_id"]
        )
        self.assertIn("study_subject_id", response.data)
        self.assertEqual(
            ["This field may not be blank."],
            response.data["study_subject_id"]
        )
