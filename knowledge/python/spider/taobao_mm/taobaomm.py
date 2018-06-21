#-*- coding:utf-8 -*-

#---------抓取新版淘女郎“头像，个人信息”，并以文件夹形式存到本地-------

import urllib
import urllib2
import re
import os
import tool
import json

#抓取淘女郎类
class taobaoMM(object):
    def __init__(self):
        #ajax获取淘女郎信息的ajaxURl
        self.ajaxURL='https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
        #淘女郎个人详情页面，再加上女郎的userId即可，如：self.mmBaseURL+str(129361161)
        self.mmBaseURL='https://mm.taobao.com/self/aiShow.htm?spm=0.0.0.0.c86RlF&userId='
        self.tool=tool.Tool() #去除页面标签类
        #设置代理IP地址，防止自己的IP被封
        self.proxyURL='http://120.193.146.97:843'
        #ajax的post数据，其中currentPage为申请的淘女郎页码，现在默认为1
        self.post={
                      'q':'',
                      'viewFlag':'A',
                      'sortType':'default',
                      'searchStyle':'',
                      'searchRegion':'city:',
                      'searchFansNum':'',
                      'currentPage':1,
                      'pageSize':100
                  }
        self.postData=urllib.urlencode(self.post)

        #头部信息
        self.Headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Referer':'https://mm.taobao.com/search_tstar_model.htm?spm=719.1001036.1998606017.2.Ut0v3A',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Connection':'keep-alive',
            'X-Requested-With':'XMLHttpRequest'
        }

        #设置代理
        self.proxy=urllib2.ProxyHandler({'http':self.proxyURL})
        #构建opener,相当于urllib2.urlopen
        self.opener=urllib2.build_opener(self.proxy)

    #传入页码，获取指定页面的淘女郎信息
    def getParsedJson(self,pageIndex=1):
        if not pageIndex==1:
            self.post['currentPage']=int(pageIndex)
            self.postData=urllib.urlencode(self.post)

        request=urllib2.Request(url=self.ajaxURL,data=self.postData,headers=self.Headers)
        response=self.opener.open(request).read().decode('gbk')
        if response:
            print u'获取第',pageIndex,u'页淘女郎信息成功!'
            return json.loads(response)
        else:
            print u'获取淘女郎信息失败'
            return False

    #处理getParsedJson返回的指定页面，淘女郎字典信息
    def operateGirlDict(self,pageIndex):
        resultDict=self.getParsedJson(pageIndex)
        if resultDict:
            print u'成功获取页面信息'
        else:
            print u'失败'
            return False
        taoMMInfoList=resultDict['data']['searchDOList']
        taoMM=[]   #页面所有淘女郎个人信息列表
        for girl in taoMMInfoList:  #循环淘女郎个人信息列表
            taoMMinfos=[]
            taoMMinfos.append(girl['realName'])
            taoMMinfos.append(girl['city'])
            taoMMinfos.append(girl['height'])
            taoMMinfos.append(girl['weight'])
            taoMMinfos.append('https:'+girl['avatarUrl'])
            taoMMinfos.append(girl['userId'])
            taoMM.append(taoMMinfos)  #将淘女郎个人信息列表加入列表
        return taoMM

    #获取mm的个人详情页面
    def getDetailPage(self,mmURL):
        response=self.opener.open(mmURL)
        page=response.read().decode('gbk')
        return page


    #获取个人文字简介
    def getBrief(self,page):
        pattern=re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        result=pattern.search(page)
        return self.tool.replace(result.group(1))

    #获取mm个人页面所有图片
    def getAllImg(self,page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        #个人信息页面所有代码
        content = pattern.search(page)
        #从代码中提取图片
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        images = patternImg.findall(content.group(1))
        return map(lambda url:'https:'+url,images) #返回的是mm页面所有图片的url

    #保存多张写真图片
    def saveImgs(self,images,name):
        number=1
        print u'发现',name,u'共有',len(images),u'张照片'
        for imageURL in images:
            splitPath=imageURL.split('.')
            fTail=splitPath.pop()
            if len(fTail)>3:
                fTail='jpg'
            fileName=name+'/'+str(number)+'.'+fTail
            self.saveImg(imageURL,fileName)
            number+=1

    #保存头像
    def saveIcon(self,iconURL,name):
        splitPath=iconURL.split('.')
        fTail=splitPath.pop()
        fileName=name+'/icon.'+fTail
        self.saveImg(iconURL,fileName)

     #保存个人信息
    def saveBrief(self,content,name):
        fileName=name+'/'+name+'.txt'
        f=open(fileName,'w+')
        print u'正在保存她的个人信息',fileName
        f.write(content.encode('utf-8'))
        f.close()

    #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageURL,imageName):
        try:
            img=urllib2.urlopen(imageURL)
        except (urllib2.URLError,urllib2.HTTPError),e:
            print e
            return
        data=img.read()
        f=open(imageName,'wb')
        f.write(data)

    #创建新目录
    def makeDir(self,path):
        path=path.strip()
        if not os.path.exists(path):
            #如果目录不存在，则创建
            print u'创建了名字叫做',path,u'的文件夹'
            os.makedirs(path)
            return True
        else:
            print u'名为',path,u'的文件夹已经创建成功'
            return False

    #将一页的淘女郎信息保存起来
    def savePageInfo(self,pageIndex):
        #获取一页淘女郎的列表
        contents=self.operateGirlDict(pageIndex)
        for item in contents:
            print u'发现一位淘女郎,名叫',item[0],u'她在',item[1],u'身高',item[2],u'体重',item[3]
            print u'正在保存',item[0],u'的信息'
            print u'并且她的个人信息地址为：',self.mmBaseURL+str(item[5])
            #mm个人信息url
            detailURL=self.mmBaseURL+str(item[5])
            #获取mm个人信息页面html代码
            detailPage=self.getDetailPage(detailURL)
            #根据传入的个人信息代码，获取mm个人简介
            brief=self.getBrief(detailPage)
            #根据传入的个人信息代码，获取页面上mm写真的所有图片url
            images=self.getAllImg(detailPage)
            #创建mm文件夹，以其名字命名
            self.makeDir(item[0])
            #传入个人简介，名字，保存个人简介到txt文档，并以名字命名
            self.saveBrief(brief,item[0])
            #传入头像url，名字，保存头像
            self.saveIcon(item[4],item[0])
            #传入个人页面所有图片url，以及名字，保存所有图片
            self.saveImgs(images,item[0])
    def savePagesInfo(self,start,end):
        for i in range(start,end+1):
            print u'正在获取第',i,u'页的淘女郎信息'
            self.savePageInfo(i)


if __name__=='__main__':
    mm=taobaoMM()
    mm.savePagesInfo(1,1)










