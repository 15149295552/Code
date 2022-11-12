import json
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from user.models import UserProfile
from .models import Topic
from tools.logging_dec import logging_check


class TopicViews(View):
    # 获取某个用户的文章列表
    def make_topics_res(self,author,author_topics):
        # {code:200,data:{nickname:"abc",topics:[{id:1,title:"xx",content:xxx,introduce,category,created_time,author}]}}
        res = {'code':200,'data':{}}

        # 遍历每一篇文章
        tmp = []
        for topic in author_topics:
            d = {}
            d['id'] = topic.id
            d['title'] = topic.title
            d['category'] = topic.category
            d['created_time'] = topic.created_time.strftime("%Y-%m-%d %H:%M:%S")
            d['introduce'] = topic.introduce
            d['author'] = author.nickname
            tmp.append(d)
        res['data']['nickname'] = author.nickname
        res['data']['topics'] = tmp
        return res

    # 获取某个具体文章信息
    def make_topic_content(self,author,the_topic):
        # {code:200,data:{nickname:"abc",title:"xx",content:xxx,introduce,category,created_time,author,last_id,next_id}]}}
        res = {'code': 200, 'data': {}}

        res['data']['nickname'] = author.nickname
        res['data']['title'] = the_topic.title
        res['data']['category'] = the_topic.category
        res['data']['created_time'] = the_topic.created_time
        res['data']['content'] = the_topic.content
        res['data']['introduce'] = the_topic.introduce
        res['data']['author'] = author.nickname

        return res



    # 显示文章列表 author_id 作者名字
    def get(self,request,author_id):
        try:
            author = UserProfile.objects.get(username=author_id)
        except:
            result = {'code':10301,'error':"The author is not existed"}
            return JsonResponse(result)

        # 具体文章ID 号
        t_id = request.GET.get("t_id")
        if t_id:
            # /v1/topics/Lily?t_id=2
            t_id = int(t_id)
            try:
                the_topic = Topic.objects.get(id=t_id)
            except:
                result = {'code': 10302, 'error': "No Topic"}
                return JsonResponse(result)

            res = self.make_topic_content(author,the_topic)
            return JsonResponse(res)


        try:
            author_topic = Topic.objects.filter(author_id=author.id)
        except:
            result = {'code':10302,'error':"No Topic"}
            return JsonResponse(result)
        res = self.make_topics_res(author,author_topic)
        return JsonResponse(res)



    # 处理上传文章
    @method_decorator(logging_check)
    def post(self,request,author_id):
        author = request.myuser # 登录的用户
        # 取出数据
        json_str = request.body
        json_obj = json.loads(json_str)
        title = json_obj['title']
        content = json_obj['content']
        introduce = json_obj['content_text'][:30] # 截取简介
        limit = json_obj['limit']
        category = json_obj['category']

        # 存储到文章数据库
        Topic.objects.create(title=title,content=content,limit=limit,category=category,introduce=introduce,author=author)
        return JsonResponse({'code':200})

