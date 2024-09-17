this is a test repository for cursor ai

Django DB superuser: suadmin/test@111

python manage.py startapp appname   
python manage.py runserver

Django logic:
urls.py: define url patterns and use which view to be called when a url patten matched
    views.py: define how to get data from DB with models defined data structure, and transfer all data into dictionary object: context,  and pass to a specific template(html filename under \templates\appname\filename.html)
        
        models.py: define the structure of the data that our app will manage
        
        x.html: define how to display the data, 
            {% extends "appname/base.html" %}

            {% block blockname %}
                {{ context keyword_name }}

                {% for item in context keyword list object name %}
                    {{ item.attribute [|filter to format the attribute data] }}
                {% endfor %}

            {% endblock blockname %}

https://aigc.unipus.cn/home   13693633778  abc123

https://www.cursor.com/features
https://cursorcasts.com/
https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html

https://www.youtube.com/@AndrejKarpathy
https://www.youtube.com/watch?v=kCc8FmEb1nY
https://github.com/karpathy/llama2.c
https://pytorch.org/docs/stable/generated/torch.multinomial.html#torch-multinomial

https://platform.openai.com/docs/quickstart/adjust-your-settings?context=python


python course:
regular expression:
https://www.bilibili.com/video/BV16b411n7U4/?p=41&spm_id_from=pageDriver&vd_source=f4956936351cafcf49bea22f69352f0d
learning AI following Li mo from bilibili:
https://search.bilibili.com/all?vt=50443064&keyword=%E8%B7%9F%E6%9D%8E%E6%B2%90%E5%AD%A6ai&from_source=webtop_search&spm_id_from=333.1007&search_source=5

FOC control:
https://zhuanlan.zhihu.com/p/147659820
https://www.bilibili.com/video/BV16X4y167XZ/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=f4956936351cafcf49bea22f69352f0d

AI Learning:
https://www.prettypolly.app/signup  #Learning English

trip:
west of sichuan:
https://www.bilibili.com/video/BV1RF411d76n/?spm_id_from=autoNext&vd_source=f4956936351cafcf49bea22f69352f0d

port freeRTOS to STM32F407:
https://www.bilibili.com/video/BV1GN4y157fy/?p=9&vd_source=f4956936351cafcf49bea22f69352f0d



