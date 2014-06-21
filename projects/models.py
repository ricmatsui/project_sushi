from allauth.socialaccount.models import SocialApp, SocialToken

from django.db import models

from rauth import OAuth1Service
    
# class Milestone(models.Model):
#     name = models.CharField()
#
# class Component(models.Model):
#     name = models.CharField()
#
# class Issue(models.Model):
#     user -
#     kind = models.ChoiceField()
#
# class Repo(models.Model):
#     name = models.CharField()
#     full_name = models.CharField()
    

class Bitbucket(object):
    
    BASE_URL = 'https://bitbucket.org/api/'
    V_1 = '1.0'
    V_2 = '2.0'
    ENDPOINTS = {
        'user_priveleges': V_1 + '/user/privileges/',
        'account_repos': V_2 + '/repositories/{account}/',
        'repo_issues': V_1 + '/repositories/{full_name}/issues/',
    }
    
    def __init__(self, user, social_app=None):
        if not social_app:
            social_app = SocialApp.objects.get(name='Bitbucket')
        self.service = OAuth1Service(name='bitbucket',
            consumer_key=social_app.client_id,
            consumer_secret=social_app.secret)
        social_token = SocialToken.objects.get(app=social_app, account__user=user)
        self.session = self.service.get_session(token=(social_token.token, social_token.token_secret))
    
    def get_endpoint_url(self, endpoint):
        return self.BASE_URL + self.ENDPOINTS[endpoint]
    
    def request_endpoint(self, endpoint, template_params=None, query_params=None):
        template_params = template_params if template_params else {}
        query_params = query_params if query_params else {}
        return self.session.get(self.get_endpoint_url(endpoint).format(**template_params),
                params=query_params).json()
    
    def get_team_names(self):
        response = self.request_endpoint('user_priveleges')
        return response['teams'].keys()
    
    def get_repos_on_page(self, account, page):
        response = self.request_endpoint('account_repos', {'account': account}, {'page': page})
        return response['values']

    def get_repos(self, account):
        page = 1
        response = self.request_endpoint('account_repos', {'account': account}, {'page': page})
        repos = response['values']
        while 'next' in response:
            page += 1
            response = self.request_endpoint('account_repos', {'account': account}, {'page': page})
            repos += response['values']
        return repos
    
    def get_repo_issue_count(self, repo):
        response = self.request_endpoint('repo_issues', {'full_name': repo['full_name']})
        return response['count']
    
    def get_repo_resolved_count(self, repo):
        response = self.request_endpoint('repo_issues', {'full_name': repo['full_name']}, {'status': 'resolved'})
        return response['count']