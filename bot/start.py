#!/usr/bin/env python

import os
import random
import requests
import configparser


class FakeData(object):
    """..."""

    API_URL = 'http://127.0.0.1:8000'

    def __init__(self, config_file):
        """..."""
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def api_call(self, action, params, headers={}, method='post'):
        """..."""
        http = {
            'get': requests.get,
            'post': requests.post
        }
        response = http[method](
            '{url}/{action}/'.format(
                url=self.API_URL,
                action=action
            ),
            params,
            headers=headers
        )
        return response


    def fill(self):
        """..."""
        config = self.config['init']

        for i in range(int(config['number_of_users'])):
            query_params = {
                'email': 'user_{0}@mail.com'.format(i),
                'username': 'user_{0}'.format(i),
                'password': 'test123'
            }
            re = self.api_call('users', query_params)

            num_posts = random.randint(1, int(config['max_posts_per_user']))
            for j in range(num_posts):
                try:
                    auth = self.api_call('auth', query_params)
                    token = auth.json()['token']
                    post_params = {
                        'title': 'Post #{0} from user_{1}'.format(j,i),
                        'text': 'Post text'
                    }
                    headers = {
                        'Authorization': 'JWT {token}'.format(token=token)
                    }
                    post = self.api_call('content/posts', post_params, headers)
                    print('Add post: OK')
                except Exception as e:
                    print('Add post: FAIL')

        for i in range(int(config['number_of_users'])):
            query_params = {
                'username': 'user_{0}'.format(i),
                'password': 'test123'
            }
            auth = self.api_call('auth', query_params)
            token = auth.json()['token']
            headers = {
                'Authorization': 'JWT {token}'.format(token=token)
            }
            num_likes = random.randint(1, int(config['max_likes_per_user']))
            query_params = {'limit': num_likes}
            posts = self.api_call('content/posts', query_params, headers, 'get')
            for r in posts.json().get('results'):
                try:
                    like_params = {
                        'post': r['id'],
                        'value': 'positive'
                    }
                    like = self.api_call('content/likes', like_params, headers)
                    print('Add like: OK')
                except Exception as e:
                    print('Add like: FAIL')


cwd = os.path.dirname(os.path.realpath(__file__))
data = FakeData('{cwd}/config.ini'.format(cwd=cwd))
data.fill()
