---
title: Hexo命令笔记
date: 2017-02-26 21:42:22
tags:
---
hexo建站步骤：http://www.jianshu.com/p/e99ed60390a8

每次部署的步骤，可按以下三步来进行。

```
hexo clean
hexo generate
hexo deploy
```

常用命令：
```
hexo new "postName" #新建文章
hexo new page "pageName" #新建页面
hexo generate #生成静态页面至public目录
hexo server #开启预览访问端口（默认端口4000，'ctrl + c'关闭server）
hexo deploy #将.deploy目录部署到GitHub
hexo help  #查看帮助
hexo version  #查看Hexo的版本
```

文章在 source/_posts，编辑器可以用 Sublime，支持 markdown 语法。如果想修改头像可以直接在主题的 _config.yml 文件里面修改，友情链接，之类的都在这里，修改名字在 public/index.html 里修改



Markdown使用方法：http://www.appinn.com/markdown/#p