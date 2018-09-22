from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth

from .twitbot import TweetBot


@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    reply_bot = TweetBot()
    reply_bot.reply_result(user.access_token['screen_name'])
    return render(request, 'user_auth/top.html', {'user': user})
