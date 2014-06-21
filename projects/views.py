from allauth.socialaccount.models import SocialApp, SocialToken

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rauth import OAuth1Service

import urllib

from . import models

@login_required
def index(request):
    context = {}
    bitbucket_app = SocialApp.objects.get(name='Bitbucket')
    bitbucket = OAuth1Service(name='bitbucket',
        consumer_key=bitbucket_app.client_id,
        consumer_secret=bitbucket_app.secret)
    social_token = SocialToken.objects.get(account__user=request.user)
    session = bitbucket.get_session(token=(social_token.token, social_token.token_secret))
    
    bitbucket = models.Bitbucket(request.user)
    
    teams = bitbucket.get_team_names()
    context['repositories'] = []
    for team in teams:
        context['repositories'] += bitbucket.get_repos(account=team)
    from pprint import pprint
    
    for repo in context['repositories']:
        if repo['has_issues']:
            repo['resolved_count'] = bitbucket.get_repo_resolved_count(repo)
            repo['total_count'] = bitbucket.get_repo_issue_count(repo)

    return render(request, 'projects/index.html', context)