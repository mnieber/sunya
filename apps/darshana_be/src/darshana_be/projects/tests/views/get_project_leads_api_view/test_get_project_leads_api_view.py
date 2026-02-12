import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from darshana_be.projects.tests.factories import ProjectFactory
from darshana_be.users.tests.factories import UserFactory


class TestGetProjectLeadsApiView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.mark.django_db
    def test_get_project_leads_success(self, api_client, user):
        api_client.force_authenticate(user=user)
        url = reverse("get-project-leads")

        # Create some test projects
        projects = [ProjectFactory() for _ in range(25)]  # Create 25 projects
        projects.sort(key=lambda x: x.name)  # Sort projects by name

        response = api_client.get(url)

        assert response.status_code == 200
        assert 'results' in response.data
        assert len(response.data['results']) == 20  # Default page size
        assert response.data['count'] == 25
        assert response.data['next'] is not None
        assert response.data['previous'] is None

        # Check the first page of results
        for i, project_data in enumerate(response.data['results']):
            assert project_data['id'] == str(projects[i].id)
            assert project_data['name'] == projects[i].name

    @pytest.mark.django_db
    def test_get_project_leads_pagination(self, api_client, user):
        api_client.force_authenticate(user=user)
        url = reverse("get-project-leads")

        # Create some test projects
        [ProjectFactory() for _ in range(25)]  # Create 25 projects

        # Test custom page size
        response = api_client.get(url + '?page_size=10')
        assert len(response.data['results']) == 10

        # Test second page
        response = api_client.get(url + '?page=2')
        assert response.data['previous'] is not None
        assert len(response.data['results']) == 5  # 25 total, 20 on first page, 5 on second

    @pytest.mark.django_db
    def test_get_project_leads_empty(self, api_client, user):
        api_client.force_authenticate(user=user)
        url = reverse("get-project-leads")

        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data['count'] == 0
        assert len(response.data['results']) == 0
