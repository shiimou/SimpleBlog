# SimpleBlog



基于`python3.8`和`Django3.2`的简易博客功能实现。   


## 功能：
- 文章、分类目录、标签的添加、删除、编辑等。集成`Markdown`及代码高亮功能。
- 支持文章全文搜索。
- 侧边栏功能，最新文章、归档分类等。
- Todo：后台图片上传问题；图片及代码块的大小显示；前端页面优化；

## 安装

- 下载依赖项： `pip install -r requirements.txt`
- 创建mysql 数据库
```sql
CREATE DATABASE `simpleblog`;
```

`SimpleBlog/setting.py` 修改数据库配置，如下所示：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'simpleblog',
        'USER': 'root', # your database username
        'PASSWORD': 'root', # your database password
        'HOST': 'host',
        'PORT': 3306,
    }
}
```
### 数据库迁移
在项目根目录终端下执行:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 创建超级用户

 终端下执行:
```bash
python manage.py createsuperuser
```


### 运行
执行： `python manage.py runserver`


浏览器打开 http://127.0.0.1:8000/ 即可访问。  

### 后台管理

 http://127.0.0.1:8000/admin 进入admin页面，添加文章。
 
![image.png](https://s2.loli.net/2022/04/16/ka4URdznYVj8Ewp.png)



